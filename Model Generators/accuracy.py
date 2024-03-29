# -*- coding: utf-8 -*-
from typing import Optional, Any

from bangla_stemmer import *
from collections import Counter
from math import log,log10,sqrt
import os
import numpy
import operator
from sklearn.preprocessing import StandardScaler,MinMaxScaler
from sklearn import model_selection
from sklearn.metrics import make_scorer
from keras.models import Sequential
from keras.layers import Dense
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score

def create_model():
    model = Sequential()
    model.add(Dense(input_dim=6, units=10, kernel_initializer='normal', activation='relu',use_bias=True))
    model.add(Dense(units=4, kernel_initializer='normal', activation='relu',use_bias=True))
    model.add(Dense(units=10, kernel_initializer='normal', activation='relu',use_bias=True))
    model.add(Dense(units=4, kernel_initializer='normal', activation='relu',use_bias=True))
    model.add(Dense(units=1, kernel_initializer='normal', activation='sigmoid',use_bias=True))
    return model

def pre_process(texts):
    for i in range(len(texts)):
        for char in chars_to_delete:
            while True:
                index =texts[i].find(char)
                if index == -1:
                    break
                texts[i] =texts[i][:index]+texts[i][index+1:]

    for i in range(len(texts)):
        texts[i] =texts[i].split()

    parser =RuleFileParser()

    for i in range(len(texts)):
        text =[]
        for j in range(len(texts[i])):
            if texts[i][j] not in stopwords and len(texts[i][j]) > 1:
                text.append(parser.stemOfWord(texts[i][j]))
        texts[i] =text
    return texts

def list_common_words(doc1, doc2):
    words = []
    for word in doc1:
        if word in doc2:
            words.append(word)
    return words

def common_words(tittle,sentence):
    counter =0
    for word in tittle:
        if word in sentence:
            counter+=1
    return counter

def method(matrix, iterations, tolerance):
    eigen_vector = numpy.zeros(shape=(len(matrix)))
    eigen_vector = (eigen_vector + 1) / len(matrix)
    matrix = numpy.array(matrix)

    for i in range(iterations):
        new_vector = numpy.matmul(eigen_vector, matrix)
        if sum(numpy.absolute(new_vector - eigen_vector)) < tolerance:
            break
        eigen_vector = new_vector

    return eigen_vector

def cosine_value(line0,line1,texts):
    vocabul =[]
    term, inverse = dict(), dict()
    N = len(texts)
    for text in texts:
        for word in text:
            vocabul.append(word)
    for word in vocabul:
        term[word] = vocabul.count(word)
        n = 0
        for text in texts:
            if word in text:
                n += 1
        inverse[word] = log10(float(N / n))

    words =list_common_words(line0,line1)
    numerator =0
    for word in words:
        numerator += term[word] * term[word] * inverse[word] * inverse[word]
    denominator1, denominator2 = 0, 0
    for word in line0:
        denominator1 += term[word] * term[word] * inverse[word] * inverse[word]
    for word in line1:
        denominator2 += term[word] * term[word] * inverse[word] * inverse[word]
    denominator1 = sqrt(denominator1)
    denominator2 = sqrt(denominator2)
    denominator = denominator1 * denominator2
    return float(numerator/denominator)

def calculate_degree(texts):
    #texts = pre_process(texts)
    vocabul = []
    term, inverse = dict(), dict()
    N = len(texts)
    for text in texts:
        for word in text:
            vocabul.append(word)
    for word in vocabul:
        term[word] = vocabul.count(word)
        n = 0
        for text in texts:
            if word in text:
                n += 1
        inverse[word] = log10(float(N / n))

    matrix = []
    for i in range(len(texts)):
        matrix.append([0] * len(texts))

    for i in range(len(texts)):
        for j in range(len(texts)):
            words = list_common_words(texts[i], texts[j])
            numerator = 0
            for word in words:
                numerator += term[word] * term[word] * inverse[word] * inverse[word]
            denominator1, denominator2 = 0, 0
            for word in texts[i]:
                denominator1 += term[word] * term[word] * inverse[word] * inverse[word]
            for word in texts[j]:
                denominator2 += term[word] * term[word] * inverse[word] * inverse[word]
            denominator1 = sqrt(denominator1)
            denominator2 = sqrt(denominator2)
            denominator = denominator1 * denominator2
            matrix[i][j] = float(numerator / denominator)

    threshold = 0.2
    degrees = [0] * len(matrix)

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] >= threshold:
                degrees[i] += 1

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] >= threshold:
                matrix[i][j] = 1
                continue
            matrix[i][j] = 0

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            matrix[i][j] = matrix[i][j] / degrees[i]

    scores = method(matrix, 50, 0.01)
    #scores[0] = 1
    return scores

def calculate_top_words(top_words,sentence):
    count =0
    for word in sentence:
        if word in top_words:
            count+=1
    return count

def generate_degree(sentence,document,index):
    degree =0
    threshold =0.010
    similarities =[0]*len(document)
    for i in range(len(document)):
        try:
            similarities[i] = common_words(sentence, document[i]) / (log(len(sentence)) + log(len(document[i])))
        except:
            similarities[i] =0.0
    similarities[index] =0.0
    for i in range(len(document)):
        if similarities[i] >= threshold:
            degree+=1
    return degree

def calculate_sentence_freq(sentence,vocab):
    total_freq =0
    for word in sentence:
        total_freq+=vocab[word]
    return total_freq-len(sentence)

doc_path =os.getcwd()+'/Dataset/Train/Documents'
sum_path =os.getcwd()+'/Dataset/Train/Summaries'

parser =RuleFileParser()

chars_to_delete = "!@#$%^&*(){}[]<>?,./+-_|''\\\"\/।"
features =[]
target_values =[]
stopwords =["অতএব","অথচ","অথবা","অনুযায়ী","অনেক","অনেকে","অনেকেই","অন্তত","অন্য","অবধি","অবশ্য","অর্থাত","আই","আগামী","আগে","আগেই","আছে","আজ","আদ্যভাগে","আপনার","আপনি","আবার","আমরা","আমাকে","আমাদের","আমার","আমি","আর","আরও","ই","ইত্যাদি","ইহা","উচিত","উত্তর","উনি","উপর","উপরে","এ","এঁদের","এঁরা","এই","একই","একটি","একবার","একে","এক্","এখন","এখনও","এখানে","এখানেই","এটা","এটাই","এটি","এত","এতটাই","এতে","এদের","এব","এবং","এবার","এমন","এমনকী","এমনি","এর","এরা","এল","এস","এসে","ঐ","ও","ওঁদের","ওঁর","ওঁরা","ওই","ওকে","ওখানে","ওদের","ওর","ওরা","কখনও","কত","কবে","কমনে","কয়েক","কয়েকটি","করছে","করছেন","করতে","করবে","করবেন","করলে","করলেন","করা","করাই","করায়","করার","করি","করিতে","করিয়া","করিয়ে","করে","করেই","করেছিলেন","করেছে","করেছেন","করেন","কাউকে","কাছ","কাছে","কাজ","কাজে","কারও","কারণ","কি","কিংবা","কিছু","কিছুই","কিন্তু","কী","কে","কেউ","কেউই","কেখা","কেন","কোটি","কোন","কোনও","কোনো","ক্ষেত্রে","কয়েক","খুব","গিয়ে","গিয়েছে","গিয়ে","গুলি","গেছে","গেল","গেলে","গোটা","চলে","চান","চায়","চার","চালু","চেয়ে","চেষ্টা","ছাড়া","ছাড়াও","ছিল","ছিলেন","জন","জনকে","জনের","জন্য","জন্যওজে","জানতে","জানা","জানানো","জানায়","জানিয়ে","জানিয়েছে","জে","জ্নজন","টি","ঠিক","তখন","তত","তথা","তবু","তবে","তা","তাঁকে","তাঁদের","তাঁর","তাঁরা","তাঁাহারা","তাই","তাও","তাকে","তাতে","তাদের","তার","তারপর","তারা","তারৈ","তাহলে","তাহা","তাহাতে","তাহার","তিনঐ","তিনি","তিনিও","তুমি","তুলে","তেমন","তো","তোমার","থাকবে","থাকবেন","থাকা","থাকায়","থাকে","থাকেন","থেকে","থেকেই","থেকেও","দিকে","দিতে","দিন","দিয়ে","দিয়েছে","দিয়েছেন","দিলেন","দু","দুই","দুটি","দুটো","দেওয়া","দেওয়ার","দেওয়া","দেখতে","দেখা","দেখে","দেন","দেয়","দ্বারা","ধরা","ধরে","ধামার","নতুন","নয়","না","নাই","নাকি","নাগাদ","নানা","নিজে","নিজেই","নিজেদের","নিজের","নিতে","নিয়ে","নিয়ে","নেই","নেওয়া","নেওয়ার","নেওয়া","নয়","পক্ষে","পর","পরে","পরেই","পরেও","পর্যন্ত","পাওয়া","পাচ","পারি","পারে","পারেন","পি","পেয়ে","পেয়্র্","প্রতি","প্রথম","প্রভৃতি","প্রযন্ত","প্রাথমিক","প্রায়","প্রায়","ফলে","ফিরে","ফের","বক্তব্য","বদলে","বন","বরং","বলতে","বলল","বললেন","বলা","বলে","বলেছেন","বলেন","বসে","বহু","বা","বাদে","বার","বি","বিনা","বিভিন্ন","বিশেষ","বিষয়টি","বেশ","বেশি","ব্যবহার","ব্যাপারে","ভাবে","ভাবেই","মতো","মতোই","মধ্যভাগে","মধ্যে","মধ্যেই","মধ্যেও","মনে","মাত্র","মাধ্যমে","মোট","মোটেই","যখন","যত","যতটা","যথেষ্ট","যদি","যদিও","যা","যাঁর","যাঁরা","যাওয়া","যাওয়ার","যাওয়া","যাকে","যাচ্ছে","যাতে","যাদের","যান","যাবে","যায়","যার","যারা","যিনি","যে","যেখানে","যেতে","যেন","যেমন","র","রকম","রয়েছে","রাখা","রেখে","লক্ষ","শুধু","শুরু","সঙ্গে","সঙ্গেও","সব","সবার","সমস্ত","সম্প্রতি","সহ","সহিত","সাধারণ","সামনে","সি","সুতরাং","সে","সেই","সেখান","সেখানে","সেটা","সেটাই","সেটাও","সেটি","স্পষ্ট","স্বয়ং","হইতে","হইবে","হইয়া","হওয়া","হওয়ায়","হওয়ার","হচ্ছে","হত","হতে","হতেই","হন","হবে","হবেন","হয়","হয়তো","হয়নি","হয়ে","হয়েই","হয়েছিল","হয়েছে","হয়েছেন","হল","হলে","হলেই","হলেও","হলো","হিসাবে","হৈলে","হোক","হয়"]

for file_index in range(1,201):
    #print(file_index)
    doc_file =open(doc_path+'/Document_'+str(file_index)+'.txt','r',encoding='utf-8')
    sum_file =open(sum_path+'/Document_'+str(file_index)+'_Summary_1'+'.txt','r',encoding='utf-8')
    # doc_lines =open(doc_path+'/Document_'+str(file_index)+'.txt','r',encoding='utf-8').readlines()
    # sum_lines =open(sum_path+'/Document_'+str(file_index)+'_Summary_1'+'.txt','r',encoding='utf-8').readlines()
    doc_lines =doc_file.readlines()
    sum_lines =sum_file.readlines()

    #Remove unnecessary characters from document

    for i in range(len(doc_lines)):
        for char in chars_to_delete:
            while True:
                index =doc_lines[i].find(char)
                if index == -1:
                    break
                doc_lines[i] = doc_lines[i][:index]+doc_lines[i][index+1:]

    #Remove unnecessary characters from summary

    for i in range(len(sum_lines)):
        for char in chars_to_delete:
            while True:
                index =sum_lines[i].find(char)
                if index == -1:
                    break
                sum_lines[i] =sum_lines[i][:index]+sum_lines[i][index+1:]

    #Split the document

    for i in range(len(doc_lines)):
        doc_lines[i] =doc_lines[i].split()

    #Split the summary

    for i in range(len(sum_lines)):
        sum_lines[i] =sum_lines[i].split()

    #Remove stop words from summary

    for i in range(len(doc_lines)):
        new_doc_line =[]
        for j in range(len(doc_lines[i])):
            if doc_lines[i][j] not in stopwords and len(doc_lines[i][j]) > 1:
                new_doc_line.append(doc_lines[i][j])
        doc_lines[i] =new_doc_line

        #Stem each word of the document

        for j in range(len(doc_lines[i])):
            doc_lines[i][j] =parser.stemOfWord(doc_lines[i][j])

    #Remove stop words from summary

    for i in range(len(sum_lines)):
        new_sum_line =[]
        for j in range(len(sum_lines[i])):
            if sum_lines[i][j] not in stopwords and len(sum_lines[i][j]) > 1:
                new_sum_line.append(sum_lines[i][j])
        sum_lines[i] =new_sum_line

    #Parse each word of summary

        for j in range(len(sum_lines[i])):
            sum_lines[i][j] =parser.stemOfWord(sum_lines[i][j])

    #Calculate similarity of the first sentence

    tittle =doc_lines[0]

    #Generate target values

    targets =[0]*len(doc_lines)

    for i in range(len(doc_lines)):
        for j in range(len(sum_lines)):
            flag =True
            for k in range(len(doc_lines[i])):
                if doc_lines[i][k] not in sum_lines[j]:
                    flag =False
                    break
            if flag:
                targets[i] =1
                break
    target_values.extend(targets)

    #Calculate Other features

    lengths =[]
    positions =[]
    similar_words =[]
    degrees =[]
    sen_freq =[]
    keywords =[]
    vocab =[]

    for line in doc_lines:
        vocab.extend(line)

    vocab =Counter(vocab)

    sorted_x = sorted(vocab.items(), key=operator.itemgetter(1), reverse=True)

    top_words =[]

    for i in range(20):
        top_words.append(sorted_x[i][0])

    #doc_texts =pre_process(doc_file.readlines())
    #print(doc_lines)
    cosine_scores =calculate_degree(doc_lines)

    for i in range(len(doc_lines)):
        lengths.append(len(doc_lines[i])/len(doc_lines))
        positions.append(1-(i+1)/len(doc_lines))
        #similar_words.append(common_words(tittle, doc_lines[i]))
        #degrees.append(calculate_degree(doc_lines[i],doc_lines,i))
        degrees.append(cosine_scores[i])
        similar_words.append(cosine_value(doc_lines[0],doc_lines[i],doc_lines))
        sen_freq.append(calculate_sentence_freq(doc_lines[i],vocab))
        keywords.append(calculate_top_words(top_words,doc_lines[i]))

    for i in range(len(doc_lines)):
        features.append([lengths[i],positions[i],similar_words[i],degrees[i],sen_freq[i],keywords[i]])

features =numpy.array(features)
target_values =numpy.array(target_values)

scalar =MinMaxScaler()
features =scalar.fit_transform(features)

# model =create_model()
# model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
# model.fit(features,target_values, batch_size=10, epochs=1000)
# model.save('model5.h5')
# seed =7
kfold = model_selection.KFold(n_splits=3, shuffle=True, random_state=42)
# cvscores = []


# evaluate the model
	# scores = model.evaluate(features[test], target_values[test], verbose=2)
	# print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
	# cvscores.append(scores[1] * 100)

# create model
# model = create_model()
# # Compile model
# model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# # Fit the model
# model.fit(features[train], target_values[train], epochs=500, batch_size=10, verbose=0)
#
# y_predict = model.predict_classes(features[test])
# y_predict = y_predict[:, 0]
# print(y_predict)

#print(type(target_values[test]))
    # y_actual =numpy.array(target_values[test])
    # # print('printing shape:')
    # print(y_predict.shape)
    # print(y_actual.shape)
    # # print(y_actual)
    # # print()
    # # print(y_predict)
    # # print(len(y_predict),len(y_actual))
    # from collections import Counter
    # d =Counter(y_predict)
    # print(d)
    # d =Counter(y_actual)
    # print(d)
    # #print(y_actual)
    # #print(type(y_actual))
    # acc =accuracy_score(y_actual,y_predict)
    # print(acc)
    # precision = precision_score(y_actual, y_predict)
    # print('Precision: %f' % precision)
    # # recall: tp / (tp + fn)
    # recall = recall_score(y_actual,y_predict)
    # print('Recall: %f' % recall)
    # # f1: 2 tp / (2 tp + fp + fn)
    # f1 = f1_score(y_actual,y_predict)
    # print('F1 score: %f' % f1)
print(len(features),len(target_values))
for train, test in kfold.split(features, target_values):
    model =create_model()
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.fit(features[train], target_values[train], epochs=500, batch_size=10, verbose=0)
    y_predict =model.predict(features[test])
    y_predict =numpy.array(y_predict)
    y_predict =y_predict[:,0]
    for y in y_predict:
        print(y)
    print('Iteration done')
    # print(len(numpy.array(features[train])),len(numpy.array(features[test])))
    # print(len(numpy.array(target_values[test])),len(numpy.array(target_values[test])))
    # print()
    # print()