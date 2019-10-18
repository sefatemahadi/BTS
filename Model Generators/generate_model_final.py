# -*- coding: utf-8 -*-
from bangla_stemmer import *
from collections import Counter
from math import log
import os
import numpy as np
import operator
from sklearn.preprocessing import StandardScaler
from keras.models import Sequential
from keras.layers import Dense,GRU
from keras import *
from keras.layers.embeddings import Embedding
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

def create_sentence_embedding_model(sentences,num_words):
    maxlen = 20
    tokenizer = Tokenizer(num_words=num_words, split=' ')
    tokenizer.fit_on_texts(sentences)
    seqs = tokenizer.texts_to_sequences(sentences)
    pad_seqs = pad_sequences(seqs, maxlen)
    sentence_skip = []
    sentence_befor = []
    sentence_after = []
    for i in range(range(1, len(pad_seqs) - 1)):
        if len(seqs[i]) > 4:
            sentence_skip.append(pad_seqs[i].tolist())
            sentence_befor.append(pad_seqs[i - 1].tolist())
            sentence_after.append(pad_seqs[i + 1].tolist())
    sentence_befor = np.matrix([[0] + i[:-1] for i in sentence_befor])
    sentence_befor = np.matrix([[0] + i[:-1] for i in sentence_after])
    sentence_skip = np.matrix(sentence_after)
    sentence_befor = np.matrix(sentence_befor)
    sentence_skip = np.matrix(sentence_skip)

    embedding_length =100
    latent_dimension =128
    batch_size =64

    encoder_inputs =Input(shape=(embedding_length,),name='Encoder-Input')
    embedding_layer =Embedding(num_words,embedding_length,input_length=maxlen,mask_zero=False)
    embedding_model =embedding_layer(encoder_inputs)

    _,state_h =GRU(latent_dimension,return_state=True,name ="Encoder-GRU")(embedding_model)
    encoder_model =Model(inputs =encoder_inputs,outputs =state_h,name ='Encoder-model')
    encoder_out =encoder_model(encoder_inputs)

    decoder_inputs_before =Input(shape=(None,),name='Decoder-input-before')
    decoder_embedding_before =embedding_layer(decoder_inputs_before)
    decoder_gru_before =GRU(latent_dimension,return_state=True,return_sequences=True,name ='Decoder-GRU-before')
    decoder_gru_output_before,_=decoder_gru_before(decoder_embedding_before,initial_state=encoder_out)
    decoder_dense_before =Dense(num_words,activation='softmax')
    decoder_outputs_before =decoder_dense_before(decoder_gru_output_before)

    decoder_inputs_after =Input(shape=(None,))
    decoder_embedding_after =embedding_layer(decoder_inputs_after)
    decoder_gru_after =GRU(latent_dimension,return_state=True,return_sequences=True)
    decoder_gru_output_after,_ =decoder_gru_after(decoder_embedding_after,initial_state=encoder_out)
    decoder_dense_after =Dense(num_words,activation='softmax')
    decoder_output_after =decoder_dense_after(decoder_gru_output_after)

    model =Model([encoder_inputs,decoder_inputs_before,decoder_inputs_after],[decoder_outputs_before,decoder_output_after])
    model.compile(optimizer=optimizers.Adam(lr=.001))

    print(model.summary())

    model.fit([sentence_skip,sentence_befor,sentence_after],[np.expand_dims(sentence_befor,-1),np.expand_dims(sentence_after,-1)],\
              batch_size=batch_size,epochs=1000,validation_split=.12)
	model.save('encoder.h5)


def create_model():
    model = Sequential()
    model.add(Dense(input_dim=5, units=10, kernel_initializer='normal', activation='relu'))
    model.add(Dense(units=32, kernel_initializer='normal', activation='relu'))
    model.add(Dense(units=10, kernel_initializer='normal', activation='relu'))
    model.add(Dense(units=4, kernel_initializer='normal', activation='relu'))
    model.add(Dense(units=1, kernel_initializer='normal', activation='sigmoid'))
    return model

def common_words(tittle,sentence):
    counter =0
    for word in tittle:
        if word in sentence:
            counter+=1
    return counter/len(sentence)

def calculate_top_words(top_words,sentence):
    count =0
    for word in sentence:
        if word in top_words:
            count+=1
    return count/len(sentence)

def calculate_degree(sentence,document,index):
    degree =0
    threshold =0.015
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
    return degree/len(sentence)

def calculate_sentence_freq(sentence,vocab):
    total_freq =0
    for word in sentence:
        total_freq+=vocab[word]
    return (total_freq-len(sentence))/len(sentence)

doc_path =os.getcwd()+'/Final_Dataset/Documents'
sum_path =os.getcwd()+'/Final_Dataset/Summaries'

parser =RuleFileParser()

chars_to_delete = "!@#$%^&*(){}[]<>?,./+-_|''\\\"\/।"
features =[]
target_values =[]
stopwords =["অতএব","অথচ","অথবা","অনুযায়ী","অনেক","অনেকে","অনেকেই","অন্তত","অন্য","অবধি","অবশ্য","অর্থাত","আই","আগামী","আগে","আগেই","আছে","আজ","আদ্যভাগে","আপনার","আপনি","আবার","আমরা","আমাকে","আমাদের","আমার","আমি","আর","আরও","ই","ইত্যাদি","ইহা","উচিত","উত্তর","উনি","উপর","উপরে","এ","এঁদের","এঁরা","এই","একই","একটি","একবার","একে","এক্","এখন","এখনও","এখানে","এখানেই","এটা","এটাই","এটি","এত","এতটাই","এতে","এদের","এব","এবং","এবার","এমন","এমনকী","এমনি","এর","এরা","এল","এস","এসে","ঐ","ও","ওঁদের","ওঁর","ওঁরা","ওই","ওকে","ওখানে","ওদের","ওর","ওরা","কখনও","কত","কবে","কমনে","কয়েক","কয়েকটি","করছে","করছেন","করতে","করবে","করবেন","করলে","করলেন","করা","করাই","করায়","করার","করি","করিতে","করিয়া","করিয়ে","করে","করেই","করেছিলেন","করেছে","করেছেন","করেন","কাউকে","কাছ","কাছে","কাজ","কাজে","কারও","কারণ","কি","কিংবা","কিছু","কিছুই","কিন্তু","কী","কে","কেউ","কেউই","কেখা","কেন","কোটি","কোন","কোনও","কোনো","ক্ষেত্রে","কয়েক","খুব","গিয়ে","গিয়েছে","গিয়ে","গুলি","গেছে","গেল","গেলে","গোটা","চলে","চান","চায়","চার","চালু","চেয়ে","চেষ্টা","ছাড়া","ছাড়াও","ছিল","ছিলেন","জন","জনকে","জনের","জন্য","জন্যওজে","জানতে","জানা","জানানো","জানায়","জানিয়ে","জানিয়েছে","জে","জ্নজন","টি","ঠিক","তখন","তত","তথা","তবু","তবে","তা","তাঁকে","তাঁদের","তাঁর","তাঁরা","তাঁাহারা","তাই","তাও","তাকে","তাতে","তাদের","তার","তারপর","তারা","তারৈ","তাহলে","তাহা","তাহাতে","তাহার","তিনঐ","তিনি","তিনিও","তুমি","তুলে","তেমন","তো","তোমার","থাকবে","থাকবেন","থাকা","থাকায়","থাকে","থাকেন","থেকে","থেকেই","থেকেও","দিকে","দিতে","দিন","দিয়ে","দিয়েছে","দিয়েছেন","দিলেন","দু","দুই","দুটি","দুটো","দেওয়া","দেওয়ার","দেওয়া","দেখতে","দেখা","দেখে","দেন","দেয়","দ্বারা","ধরা","ধরে","ধামার","নতুন","নয়","না","নাই","নাকি","নাগাদ","নানা","নিজে","নিজেই","নিজেদের","নিজের","নিতে","নিয়ে","নিয়ে","নেই","নেওয়া","নেওয়ার","নেওয়া","নয়","পক্ষে","পর","পরে","পরেই","পরেও","পর্যন্ত","পাওয়া","পাচ","পারি","পারে","পারেন","পি","পেয়ে","পেয়্র্","প্রতি","প্রথম","প্রভৃতি","প্রযন্ত","প্রাথমিক","প্রায়","প্রায়","ফলে","ফিরে","ফের","বক্তব্য","বদলে","বন","বরং","বলতে","বলল","বললেন","বলা","বলে","বলেছেন","বলেন","বসে","বহু","বা","বাদে","বার","বি","বিনা","বিভিন্ন","বিশেষ","বিষয়টি","বেশ","বেশি","ব্যবহার","ব্যাপারে","ভাবে","ভাবেই","মতো","মতোই","মধ্যভাগে","মধ্যে","মধ্যেই","মধ্যেও","মনে","মাত্র","মাধ্যমে","মোট","মোটেই","যখন","যত","যতটা","যথেষ্ট","যদি","যদিও","যা","যাঁর","যাঁরা","যাওয়া","যাওয়ার","যাওয়া","যাকে","যাচ্ছে","যাতে","যাদের","যান","যাবে","যায়","যার","যারা","যিনি","যে","যেখানে","যেতে","যেন","যেমন","র","রকম","রয়েছে","রাখা","রেখে","লক্ষ","শুধু","শুরু","সঙ্গে","সঙ্গেও","সব","সবার","সমস্ত","সম্প্রতি","সহ","সহিত","সাধারণ","সামনে","সি","সুতরাং","সে","সেই","সেখান","সেখানে","সেটা","সেটাই","সেটাও","সেটি","স্পষ্ট","স্বয়ং","হইতে","হইবে","হইয়া","হওয়া","হওয়ায়","হওয়ার","হচ্ছে","হত","হতে","হতেই","হন","হবে","হবেন","হয়","হয়তো","হয়নি","হয়ে","হয়েই","হয়েছিল","হয়েছে","হয়েছেন","হল","হলে","হলেই","হলেও","হলো","হিসাবে","হৈলে","হোক","হয়"]

for file_index in range(1,201):
    doc_lines =open(doc_path+'/Document_'+str(file_index)+'.txt','r',encoding='utf-8').readlines()
    sum_lines =open(sum_path+'/Document_'+str(file_index)+'_Summary_1'+'.txt','r',encoding='utf-8').readlines()

    for i in range(len(doc_lines)):
        for char in chars_to_delete:
            while True:
                index =doc_lines[i].find(char)
                if index == -1:
                    break
                doc_lines[i] = doc_lines[i][:index]+doc_lines[i][index+1:]

    for i in range(len(sum_lines)):
        for char in chars_to_delete:
            while True:
                index =sum_lines[i].find(char)
                if index == -1:
                    break
                sum_lines[i] =sum_lines[i][:index]+sum_lines[i][index+1:]

    for i in range(len(doc_lines)):
        doc_lines[i] =doc_lines[i].split()

    for i in range(len(sum_lines)):
        sum_lines[i] =sum_lines[i].split()

    for i in range(len(doc_lines)):
        new_doc_line =[]
        for j in range(len(doc_lines[i])):
            if doc_lines[i][j] not in stopwords and len(doc_lines[i][j]) > 1:
                new_doc_line.append(doc_lines[i][j])
        doc_lines[i] =new_doc_line

        for j in range(len(doc_lines[i])):
            doc_lines[i][j] =parser.stemOfWord(doc_lines[i][j])

    for i in range(len(sum_lines)):
        new_sum_line =[]
        for j in range(len(sum_lines[i])):
            if sum_lines[i][j] not in stopwords and len(sum_lines[i][j]) > 1:
                new_sum_line.append(sum_lines[i][j])
        sum_lines[i] =new_sum_line

        for j in range(len(sum_lines[i])):
            sum_lines[i][j] =parser.stemOfWord(sum_lines[i][j])

    tittle =doc_lines[0]
    doc_lines =doc_lines[1:]

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

    lengths =[]
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

    for i in range(15):
        top_words.append(sorted_x[i][0])

    # print(top_words)

    #COLLECTING FEATURES

    for i in range(len(doc_lines)):
        lengths.append(len(doc_lines[i])/len(doc_lines))
        similar_words.append(common_words(tittle, doc_lines[i]))
        degrees.append(calculate_degree(doc_lines[i],doc_lines,i))
        sen_freq.append(calculate_sentence_freq(doc_lines[i],vocab))
        keywords.append(calculate_top_words(top_words,doc_lines[i]))

    for i in range(len(doc_lines)):
        features.append([lengths[i],similar_words[i],degrees[i],sen_freq[i],keywords[i]])

# CONVERTING TO NUMPY ARRAY

features =np.array(features)
print(features.shape)
target_values =np.array(target_values)
print(target_values.shape)

scalar =StandardScaler()
features =scalar.fit_transform(features)

print("Crossed")

model =create_model()
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(features,target_values, batch_size=10, epochs=1000)
model.save('model3.h5')