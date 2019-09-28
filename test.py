# -*- coding: utf-8 -*-
from bangla_stemmer import *
from math import sqrt
from collections import Counter
from math import log
import os
import numpy
from keras.models import Sequential
from keras.layers import Dense

def common_words(tittle,sentence):
    counter =0
    for word in tittle:
        if word in sentence:
            counter+=1
    return counter


def calculate_degree(sentence,document,index):
    degree =0
    threshold =0.20
    similarities =[0]*len(document)
    for i in range(len(document)):
        similarities[i]=common_words(sentence,document[i])/(log(len(sentence))+log(len(document[i])))
    similarities[index] =0.0
    for i in range(len(document)):
        if similarities[i] >= threshold:
            degree+=1
    return degree

def calculate_sentence_freq(sentence,vocab):
    total_freq =0
    for word in sentence:
        total_freq+=vocab[word]
    return total_freq


doc_path =os.getcwd()+'/Documents'
sum_path =os.getcwd()+'/Summeries_1'

parser =RuleFileParser()

chars_to_delete = "!@#$%^&*(){}[]<>?,./+-_|\'\\\"\/।"
features =[]
target_values =[]

for i in range(1,101):
    doc_lines =open(doc_path+'/Document_'+str(i)+'.txt','r',encoding='utf-8').readlines()
    sum_lines =open(sum_path+'/Document_'+str(i)+'_Summary_1'+'.txt','r',encoding='utf-8').readlines()
    tittle = doc_lines[0]
    doc_lines = doc_lines[1:]

    #PREPROCESSING DOCUMENT

    for i in range(len(doc_lines)):
        for char in chars_to_delete:
            index =doc_lines[i].find(char)
            if index != -1:
                doc_lines[i] =doc_lines[i][:index]+doc_lines[i][index+1:]
        # index =doc_lines[i].find('।')
        # if index != -1:
        #     doc_lines[i] =doc_lines[i][:index]
        #print(i+1,doc_lines[i])


    #PREPROCESSING SUMMARY

    for i in range(len(sum_lines)):
        for char in chars_to_delete:
            index =sum_lines[i].find(char)
            if index != -1:
                sum_lines[i] =sum_lines[i][:index]+sum_lines[i][index+1:]
        #print(i+1,sum_lines[i])

    #PREPROCESSING TITTLE

    for char in chars_to_delete:
        index =tittle.find(char)
        if index != -1:
            tittle =tittle[:index]+tittle[index+1:]


    target_value = [0] * len(doc_lines)
    lengths =[]
    positions =[]
    similar_words =[]
    degrees =[]
    sen_freq =[]
    vocab =[]

    for i in range(len(doc_lines)):
        doc_lines[i] =doc_lines[i].split()
        # for j in range(len(doc_lines[i])):
        #     doc_lines[i][j] =parser.stemOfWord(doc_lines[i][j])
        # vocab.extend(doc_lines[i])


    for i in range(len(sum_lines)):
        sum_lines[i] =sum_lines[i].split()

    for i in range(len(doc_lines)):
        if doc_lines[i] in sum_lines:
            target_value[i] =1
    #print(target_value)
    target_values.extend(target_value)

    for j in range(len(doc_lines[i])):
        doc_lines[i][j] =parser.stemOfWord(doc_lines[i][j])
        vocab.extend(doc_lines[i])

    vocab =Counter(vocab)
    # for key in vocab.keys():
    #     print(key,vocab[key])

    #COLLECTING FEATURES

    for i in range(len(doc_lines)):
        lengths.append(len(doc_lines[i]))
        positions.append((1 / sqrt(i + 1)))
        similar_words.append(common_words(tittle.split(), doc_lines[i]))
        degrees.append(calculate_degree(doc_lines[i],doc_lines,i))
        sen_freq.append(calculate_sentence_freq(doc_lines[i],vocab))

    # print(len(degrees))
    # #PRINTING DEGREES
    # # for i in range(len(degrees)):
    # #     print(i,degrees[i])
    #
    # print()
    #
    # for i in range(len(doc_lines)):
    #     print(lengths[i],positions[i],similar_words[i],degrees[i],sen_freq[i])

    for i in range(len(doc_lines)):
        features.append([lengths[i],positions[i],similar_words[i],degrees[i],sen_freq[i]])
# for f in features:
#     print(f[0],f[1],f[2],f[3],f[4])

seed =7
numpy.random.seed(seed)

#CONVERTING TO NUMPY ARRAY

features =numpy.array(features)
print(features.shape)
target_values =numpy.array(target_values)
print(target_values.shape)

d =Counter(target_values)
for k in d.keys():
    print(k,d[k])

#
#BUILDING THE MODEL

model =Sequential()
model.add(Dense(input_dim=5,units=10,kernel_initializer='normal',activation='relu'))
model.add(Dense(units=10,kernel_initializer='normal',activation='relu'))
model.add(Dense(units=10,kernel_initializer='normal',activation='relu'))
model.add(Dense(units=4,kernel_initializer='normal',activation='relu'))
model.add(Dense(units=1,kernel_initializer='normal',activation='sigmoid'))

model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])
model.fit(features,target_values,batch_size=10,epochs=500)