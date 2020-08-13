from math import sqrt
import re
import numpy as np
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
from time import *

def delete_stopwords(word_lst):
    lst_add = ['could','will','can','would','also']
    text_collection = []
    wordnet_lematizer = WordNetLemmatizer()   # 统一单词的形式，比如将三单原型化
    new_word_lst = []
    for j in range(len(word_lst)):
        lst1 = []
        token_words = pos_tag(word_lst[j])
        for word,tag in token_words:
            if word not in stopwords.words('english'):  # 提取所有形容词，并且将他们统一单词的形式，比如将三单原型化
                new_word = wordnet_lematizer.lemmatize(word)
                lst1.append(new_word)
                if new_word not in text_collection and new_word not in lst_add:
                    text_collection.append(new_word)
        if lst1 != []:
            new_word_lst.append(lst1)
    return new_word_lst,text_collection

# 将文本向量化
def text_CountVectorizer(new_word_lst,text_collection):
    num_collection = len(text_collection)
    num_text = len(new_word_lst)
    array_text = np.zeros((num_text,num_collection), dtype=int)
    for i in range(num_text):
        for j in range(len(new_word_lst[i])):
            if new_word_lst[i][j] in text_collection:
                place = text_collection.index(new_word_lst[i][j])
                array_text[i][place] += 1
    return array_text

# 皮尔森相关系数法
def Person(array_text,text_collection, len_negative, len_positive):
    yuzhi = 0.06
    delete_lst = []
    array_negative = np.zeros(len_negative)
    array_positive = np.ones(len_positive)
    vb = np.hstack((array_negative, array_positive))
    num = array_text.shape[1]
    for i in range(num):
        vc = array_text[:,i]
        co = np.mean(np.multiply((vc - np.mean(vc)), (vb - np.mean(vb)))) / (np.std(vb) * np.std(vc))
        if abs(co) < yuzhi:
            delete_lst.append(i)
    array_text = np.delete(array_text, delete_lst, axis=1)
    lst_word = [text_collection[i] for i in range(len(text_collection)) if i not in delete_lst]
    return array_text,lst_word

# 方差选择法
def feature_Var_selection(array_text,text_collection):
    array_text_new = array_text.T
    yuzhi = 0.0595
    delete_lst = []
    for i in range(array_text_new.shape[0]):
        var_line = np.var(array_text_new[i])
        if var_line < yuzhi:
            delete_lst.append(i)
    array_text = np.delete(array_text, delete_lst, axis=1)
    lst_word = [text_collection[i] for i in range(len(text_collection)) if i not in delete_lst]
    return array_text,lst_word


# 将文本文件以数组的形式输出
def input_test(where_from,num):
    s1 = open(where_from, 'r')
    X = s1.readlines()
    lst = []
    for i in range(num):
        lst1 = re.compile(r'\b[a-zA-Z\-]+\b', re.I).findall(X[i])
        lst.append(lst1)
    return lst

def KNN(array_train, array_text,k):
    negative_correct = 0 ; positive_correct =0
    train_len = len(array_train)
    text_len = len(array_text)
    for i in range(text_len):     # 计算每一组数的距离
        dis = []
        for j in range(train_len):
            temp_dis = sqrt(np.sum((array_train[j] - array_text[i])**2))  # 计算距离
            dis.append(temp_dis)
        dis = np.array(dis)
        sort_id = dis.argsort()        #返回原数组的下标
        dic = {'negative' : 0, 'positive' : 0}
        # 对于前排在前面k个元素进行统计，从而判断是negative还是positive。
        for w in range(k):
            num = sort_id[w]  # 为对应的标签记数
            if num <= train_len/2:
                dic['negative'] += 1
            else:
                dic['positive'] += 1
        if dic['negative'] > dic['positive'] and i < text_len/2 :
            negative_correct += 1
        if dic['negative'] < dic['positive'] and i >= text_len/2:
            positive_correct += 1
    print(negative_correct,positive_correct)
    return negative_correct/(text_len/2), positive_correct/(text_len/2)


def main():
    begin_time = time()
    tr_negative = input_test('venv/train_negative.txt',2995)
    tr_positive  = input_test('venv/train_positive.txt',2995)
    te_negative = input_test('venv/test_negative.txt',2000)
    te_positive = input_test('venv/test_positive.txt',2000)
    train_lst = tr_negative + tr_positive
    text_lst = te_negative + te_positive
    # 输出训练集的向量组
    lst1, word_lst_train = delete_stopwords(train_lst)
    array_train = text_CountVectorizer(lst1, word_lst_train)
    array_train, word_train = Person(array_train, word_lst_train, 2995, 2995)
    print('训练集的特征数目是：', len(word_train))
    end_time_train = time()
    run_time_train = end_time_train - begin_time
    print('训练的时间是：', str(run_time_train)+'s')
    # 输出测试集的向量组
    lst2, word_lst_text = delete_stopwords(text_lst)
    array_text = text_CountVectorizer(lst2, word_train)    # 这里的向量化是根据训练集的词库生成的
    k = 25
    negative_correct, positive_correct = KNN(array_train, array_text,k)
    print('此时的k值是',k)
    end_time_text = time()
    run_time_text = end_time_text - end_time_train
    print('测试的时间是：', str(run_time_text)+'s')
    run_time = end_time_text - begin_time
    print('总运行的时间是', str(run_time)+'s')
    print('消极和积极文本分析的正确率分别是：',negative_correct, positive_correct)
    print('总正确率是',end = '')
    return (negative_correct+positive_correct)/2

if __name__ == '__main__':
    print(main())