import heapq
import nltk
from nltk.corpus import brown
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize
import math
import numpy as np


def related_words(word):
    n = 10
    news_words = brown.sents(categories=['news', 'editorial'])
    words_two = list()
    for i in range(len(news_words)-4):
        if(i % 5 == 1):
            words_two.append(news_words[i]+news_words[i+1]+news_words[i+2] +
                             news_words[i+3]+news_words[i+4])

    corpus_freq = [count_freq(corpus) for corpus in words_two]
    tf_dicts = calc_tf(corpus_freq)
    idf_dict = calc_idf(corpus_freq)
    matrix, word_matrix, word_list = calc_matrix(tf_dicts, idf_dict, word)
    return cos_distance(matrix, word_matrix, word_list, word)


def count_freq(corpus):
    freq = dict()
    ps = PorterStemmer()
    for word in corpus:
        stemmed = ps.stem(word)
        if not stemmed in freq:
            freq[stemmed] = 0
        freq[stemmed] += 1
    return freq


def calc_total_freq(corpus_freqs):
    dictionary = dict()
    for corpus in corpus_freqs:
        for word in corpus.keys():
            if not word in dictionary:
                dictionary[word] = 0
            dictionary[word] += 1
    return dictionary


def calc_tf(corpus_freqs):
    tf_freq = list()
    for corpus in corpus_freqs:
        dictionary = dict()
        for word in corpus.keys():
            if not word in dictionary:
                dictionary[word] = 0
            dictionary[word] += 1
        summation = sum(dictionary.values())
        for key in dictionary.keys():
            dictionary[key] = dictionary[key]/summation
        tf_freq.append(dictionary)
    return tf_freq


def calc_idf(corpuses_freqs):
    idf_dict = calc_total_freq(corpuses_freqs)
    for word in idf_dict.keys():
        idf_dict[word] = math.log10(len(corpuses_freqs)/idf_dict[word])
    print(idf_dict['play'])
    return idf_dict


def calc_matrix(tf_dicts, idf_dict, word):
    ps = PorterStemmer()
    matrix = np.zeros((len(idf_dict), len(tf_dicts)))
    word_matrix = np.zeros(len(tf_dicts))
    word_list = []
    row = 0
    for i in idf_dict.keys():
        if i == 'play':
            print(i)
        word_list.append(i)
        col = 0
        for j in tf_dicts:
            num = tf_dicts[col].get(i)
            if(num) == None:
                num = 0
            matrix[row][col] = idf_dict.get(i) * num
            if i == ps.stem(word):
                word_matrix[col] = (matrix[row][col])
            col += 1
        row += 1
    return matrix, word_matrix, word_list


def cos_distance(matrix, word_matrix, word_list, word):
    ps = PorterStemmer()
    distance = dict()
    for i in range(len(matrix)):
        if word_list[i] != ps.stem(word):
            dot = np.dot(word_matrix, matrix[i])
            distance[word_list[i]] = dot /\
                (np.sqrt(word_matrix.dot(word_matrix))
                 * np.sqrt(matrix[i].dot(matrix[i])))
    h = heapq.nlargest(10, distance, key=distance.get)
    top = list()
    for item in h:
        top.append(item)
    return top
