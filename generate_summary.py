# -*- coding: utf-8 -*-
try:
    from math import log
    from collections import Counter
    from bangla_stemmer import RuleFileParser
    from keras.models import load_model
    from sklearn.preprocessing import StandardScaler
    import operator
    import numpy
except Exception as e:
    print(e)

class Textline():
    def __init__(self,line,value,index):
        self.line =line
        self.value =value
        self.index  =index

chars_to_delete = "!@#$%^&*(){}[]<>?,./+-_|''\\\"\/।"
stopwords =["অতএব","অথচ","অথবা","অনুযায়ী","অনেক","অনেকে","অনেকেই","অন্তত","অন্য","অবধি","অবশ্য","অর্থাত","আই","আগামী","আগে","আগেই","আছে","আজ","আদ্যভাগে","আপনার","আপনি","আবার","আমরা","আমাকে","আমাদের","আমার","আমি","আর","আরও","ই","ইত্যাদি","ইহা","উচিত","উত্তর","উনি","উপর","উপরে","এ","এঁদের","এঁরা","এই","একই","একটি","একবার","একে","এক্","এখন","এখনও","এখানে","এখানেই","এটা","এটাই","এটি","এত","এতটাই","এতে","এদের","এব","এবং","এবার","এমন","এমনকী","এমনি","এর","এরা","এল","এস","এসে","ঐ","ও","ওঁদের","ওঁর","ওঁরা","ওই","ওকে","ওখানে","ওদের","ওর","ওরা","কখনও","কত","কবে","কমনে","কয়েক","কয়েকটি","করছে","করছেন","করতে","করবে","করবেন","করলে","করলেন","করা","করাই","করায়","করার","করি","করিতে","করিয়া","করিয়ে","করে","করেই","করেছিলেন","করেছে","করেছেন","করেন","কাউকে","কাছ","কাছে","কাজ","কাজে","কারও","কারণ","কি","কিংবা","কিছু","কিছুই","কিন্তু","কী","কে","কেউ","কেউই","কেখা","কেন","কোটি","কোন","কোনও","কোনো","ক্ষেত্রে","কয়েক","খুব","গিয়ে","গিয়েছে","গিয়ে","গুলি","গেছে","গেল","গেলে","গোটা","চলে","চান","চায়","চার","চালু","চেয়ে","চেষ্টা","ছাড়া","ছাড়াও","ছিল","ছিলেন","জন","জনকে","জনের","জন্য","জন্যওজে","জানতে","জানা","জানানো","জানায়","জানিয়ে","জানিয়েছে","জে","জ্নজন","টি","ঠিক","তখন","তত","তথা","তবু","তবে","তা","তাঁকে","তাঁদের","তাঁর","তাঁরা","তাঁাহারা","তাই","তাও","তাকে","তাতে","তাদের","তার","তারপর","তারা","তারৈ","তাহলে","তাহা","তাহাতে","তাহার","তিনঐ","তিনি","তিনিও","তুমি","তুলে","তেমন","তো","তোমার","থাকবে","থাকবেন","থাকা","থাকায়","থাকে","থাকেন","থেকে","থেকেই","থেকেও","দিকে","দিতে","দিন","দিয়ে","দিয়েছে","দিয়েছেন","দিলেন","দু","দুই","দুটি","দুটো","দেওয়া","দেওয়ার","দেওয়া","দেখতে","দেখা","দেখে","দেন","দেয়","দ্বারা","ধরা","ধরে","ধামার","নতুন","নয়","না","নাই","নাকি","নাগাদ","নানা","নিজে","নিজেই","নিজেদের","নিজের","নিতে","নিয়ে","নিয়ে","নেই","নেওয়া","নেওয়ার","নেওয়া","নয়","পক্ষে","পর","পরে","পরেই","পরেও","পর্যন্ত","পাওয়া","পাচ","পারি","পারে","পারেন","পি","পেয়ে","পেয়্র্","প্রতি","প্রথম","প্রভৃতি","প্রযন্ত","প্রাথমিক","প্রায়","প্রায়","ফলে","ফিরে","ফের","বক্তব্য","বদলে","বন","বরং","বলতে","বলল","বললেন","বলা","বলে","বলেছেন","বলেন","বসে","বহু","বা","বাদে","বার","বি","বিনা","বিভিন্ন","বিশেষ","বিষয়টি","বেশ","বেশি","ব্যবহার","ব্যাপারে","ভাবে","ভাবেই","মতো","মতোই","মধ্যভাগে","মধ্যে","মধ্যেই","মধ্যেও","মনে","মাত্র","মাধ্যমে","মোট","মোটেই","যখন","যত","যতটা","যথেষ্ট","যদি","যদিও","যা","যাঁর","যাঁরা","যাওয়া","যাওয়ার","যাওয়া","যাকে","যাচ্ছে","যাতে","যাদের","যান","যাবে","যায়","যার","যারা","যিনি","যে","যেখানে","যেতে","যেন","যেমন","র","রকম","রয়েছে","রাখা","রেখে","লক্ষ","শুধু","শুরু","সঙ্গে","সঙ্গেও","সব","সবার","সমস্ত","সম্প্রতি","সহ","সহিত","সাধারণ","সামনে","সি","সুতরাং","সে","সেই","সেখান","সেখানে","সেটা","সেটাই","সেটাও","সেটি","স্পষ্ট","স্বয়ং","হইতে","হইবে","হইয়া","হওয়া","হওয়ায়","হওয়ার","হচ্ছে","হত","হতে","হতেই","হন","হবে","হবেন","হয়","হয়তো","হয়নি","হয়ে","হয়েই","হয়েছিল","হয়েছে","হয়েছেন","হল","হলে","হলেই","হলেও","হলো","হিসাবে","হৈলে","হোক","হয়"]

parser =RuleFileParser()

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

    for i in range(len(texts)):
        text =[]
        for j in range(len(texts[i])):
            if texts[i][j] not in stopwords and len(texts[i][j]) > 1:
                text.append(parser.stemOfWord(texts[i][j]))
        texts[i] =text
    return texts

def common_words(tittle,sentence):
    counter =0
    for word in tittle:
        if word in sentence:
            counter+=1
    return counter

def calculate_degree(sentence,document,index):
    #print(sentence)
    degree =0
    threshold =0.020
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

def calculate_top_words(top_words,sentence):
    count =0
    for word in sentence:
        if word in top_words:
            count+=1
    return count

#model =load_model('model3.h5')
# print('model is loaded')
print('Place the input file in same directory and enter the file name with extension:')
file_name =input()
# fp =open('input.txt','r',encoding='utf-8')
try:
    fp = open(file_name, 'r', encoding='utf-8')
except Exception as e:
    print(e)
texts =fp.readlines()
fp.close()
tittle =texts[0]
# texts =texts[1:]

vocab =[]
copy_texts =texts[:]
texts =pre_process(texts)

for char in chars_to_delete:
    while True:
        index =tittle.find(char)
        if index == -1:
            break
        tittle =tittle[:index]+tittle[index+1:]
tittle =tittle.split()
for i in range(len(tittle)):
    tittle[i] =parser.stemOfWord(tittle[i])

for text in texts:
    vocab.extend(text)

vocab =Counter(vocab)

# for text in texts:
#     print(text)

top_words =[]
sorted_x = sorted(vocab.items(), key=operator.itemgetter(1), reverse=True)
for i in range(20):
    top_words.append(sorted_x[i][0])

features =[]

for i in range(len(texts)):
    features.append([len(texts[i])/len(texts),1-(i+1)/len(texts),common_words(tittle,texts[i]),calculate_degree(texts[i],texts,i),calculate_sentence_freq(texts[i],vocab),calculate_top_words(top_words,texts[i])])

for f in features:
    print(f[0],f[1],f[2],f[3],f[4],f[5])

features =numpy.array(features)
#print(features)
scalar =StandardScaler()
features =scalar.fit_transform(features)
try:
    model = load_model('model4.h5')
except Exception as e:
    print(e)
y =model.predict(features)
#print(y)

textlines =[]
for i in range(len(y)):
   textlines.append(Textline(copy_texts[i],y[i],i))
#
# #WITHOUT PAGING
#
# textlines.sort(key=lambda ob:ob.value,reverse=True)
# print(len(texts))
# textlines =textlines[:int(len(texts)/3)]
# textlines.sort(key=lambda ob:ob.index,reverse=False)
#
# print(copy_texts[0])
# for t in textlines:
#     print(t.value,t.line)

#WITH PAGING
# print(y)
page_size =3
import os
print(os.getcwd())
write_output =open('summary.txt','w',encoding='utf-8')

def get_line(page,flag):
    if flag:
        #print(page[0].line)
        write_output.write(page[0].line)
        write_output.write('\n')
        return
    max_value =-100
    max_index =0
    for i in range(len(page)):
        if page[i].value > max_value:
            max_value =page[i].value
            max_index =i
    #print(page[max_index].line)
    write_output.write(page[max_index].line)
    write_output.write('\n')
index =0
if_first =True
while True:
    flag =False
    page =[]
    for i in range(page_size):
        if index >= len(texts):
            flag =True
            break
        page.append(textlines[index])
        index+=1
    if len(page):
        get_line(page,if_first)
    if if_first:
        if_first =False
    if flag:
        break
write_output.close()
print('Check inside the directory.A text file named as summary.txt contains generated summary')
while True:
    continue