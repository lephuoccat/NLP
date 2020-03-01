import re
import nltk
from nltk import word_tokenize

def last_words(word, n):
    last_words = []
    for i in range (len(word)-n, len(word)):
        last_words.append(word[i])
    return last_words

def prob(word, n, corpus):
    model = {}
    for i in range(0, len(corpus)):
        if corpus[i] == word[0]:
            for count in range (0, n):
                if corpus[i+count] != word[count]:
                    break
                if count == (n-1):
                    if corpus[i+n] in model.keys():
                        model[corpus[i+n]] += 1
                    else:
                        model[corpus[i+n]] = 1
    next_word = max(model.keys(), key=model.get)
    return next_word


def finish_sentence(words, n, corpus):
    extended = []
    extended.extend(words)
    if n > len(words):
        print("error")
    else:
        while extended[len(extended)-1] != "." and extended[len(extended)-1] != "?" and extended[len(extended)-1] != "!":
            last_w = last_words(extended, n)
            next_w = prob(last_w, n, corpus)
            extended.append(next_w)
    return extended
