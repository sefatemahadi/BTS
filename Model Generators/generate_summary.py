# -*- coding: utf-8 -*-
try:
    from math import log,ceil,sqrt,log10
    from collections import Counter
    from bangla_stemmer import RuleFileParser
    from keras.models import load_model
    from sklearn.preprocessing import StandardScaler,MinMaxScaler
    import operator
    import numpy
    import gensim.models.doc2vec
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

def list_common_words(doc1, doc2):
    words = []
    for word in doc1:
        if word in doc2:
            words.append(word)
    return words
    
def get_embedding(sentence):
	model =doc2vec.load('doc2vec.model')
	return model.infer_vector(sentence)

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

def list_common_words(doc1, doc2):
    words = []
    for word in doc1:
        if word in doc2:
            words.append(word)
    return words

def calculate_degree(sentence,document,index):
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

def generate_degree(texts):
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

def generate(file_name):
    try:
        fp = open(file_name, 'r', encoding='utf-8')
    except Exception as e:
        print(e)
    texts = fp.readlines()
    fp.close()
    tittle = texts[0]

    vocab = []
    copy_texts = texts[:]
    texts = pre_process(texts)

    for char in chars_to_delete:
        while True:
            index = tittle.find(char)
            if index == -1:
                break
            tittle = tittle[:index] + tittle[index + 1:]
    tittle = tittle.split()
    for i in range(len(tittle)):
        tittle[i] = parser.stemOfWord(tittle[i])

    for text in texts:
        vocab.extend(text)

    vocab = Counter(vocab)
    top_words = []
    sorted_x = sorted(vocab.items(), key=operator.itemgetter(1), reverse=True)
    for i in range(20):
        top_words.append(sorted_x[i][0])

    scores =generate_degree(texts)

    features = []

    print(texts)

    for i in range(len(texts)):
        features.append([len(texts[i]) / len(texts), 1 - (i + 1) / len(texts), scores[i],
                cosine_value(texts[0],texts[i],texts), calculate_sentence_freq(texts[i], vocab),
                calculate_top_words(top_words, texts[i])])

    features = numpy.array(features)

    scalar = MinMaxScaler()
    features = scalar.fit_transform(features)
    try:
        model = load_model('model5.h5')
    except Exception as e:
        print(e)
    y = model.predict(features)

    print(y)
    textlines = []
    for i in range(len(y)):
        textlines.append(Textline(copy_texts[i], y[i], i))

    copy_textlines =textlines[:]
    copy_textlines.sort(key=lambda x:x.value,reverse=True)

    #copy_textlines =copy_textlines[:int(len(copy_textlines)/3)+1]
    copy_textlines =copy_textlines[:ceil(len(copy_textlines)/3)]
    copy_textlines.sort(key=lambda x:x.index,reverse=False)

    flag =False

    for line in copy_textlines:
        if not line.index:
            flag =True
    if flag == False:
        copy_textlines.insert(0,textlines[0])
        copy_textlines =copy_textlines[:len(copy_textlines)-1]

    file =open('trad_summary.txt','w')

    for i in range(len(copy_textlines)):
        file.write(str(copy_textlines[i].index))
        file.write('\n')
    file.close()

    page_size = 3
    write_output = open('page_summary.txt', 'w', encoding='utf-8')

    def get_line(page, flag):
        if flag:
            #write_output.write(page[0].line)
            write_output.write(str(page[0].index))
            write_output.write('\n')
            return
        max_value = -100
        max_index = 0
        for i in range(len(page)):
            if page[i].value > max_value:
                max_value = page[i].value
                max_index = i
        write_output.write(str(page[max_index].index))
        write_output.write('\n')

    index = 0
    if_first = True
    while True:
        flag = False
        page = []
        for i in range(page_size):
            if index >= len(texts):
                flag = True
                break
            page.append(textlines[index])
            index += 1
        if len(page):
            get_line(page, if_first)
        if if_first:
            if_first = False
        if flag:
            break
    write_output.close()
#generate('/home/sefat/Desktop/Test/test1.txt')
