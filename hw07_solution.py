import numpy as np
from sklearn.preprocessing import normalize

def transition_matrix(dictionary):
    array = np.zeros((27, 27))
    for word in dictionary:
        prev = None
        for index in range(0, len(word)):
            if (index == 0):
                letter = word[index]
                array[26][ord(letter)-97] += 1
            else:
                letter = word[index]
                array[ord(prev)-97][ord(letter)-97] += 1
            prev = word[index]
        array[ord(prev)-97][26] += 1
    
    for i in range(26):
        for j in range(26):
            if (array[i][j] == 0):
                array[i][j] = 1
    
    array = normalize(array, axis=1, norm='l1')
    return array

def most_likely_word(dictionary, matrix, n):
    likelyword = ""
    max_prob = -100
    matrix = np.log(matrix)
    
    for word in dictionary:
        if (len(word) == n):  
            prob = 0          
            for i in range(0,len(word)):
                if (i == 0):
                    prob += matrix[26][ord(word[i])-97]
                else:
                    prob += matrix[ord(word[i-1])-97][ord(word[i])-97]
            prob += matrix[ord(word[len(word)-1])-97][26]

            if (prob > max_prob):
                max_prob = prob
                likelyword = word
    return likelyword