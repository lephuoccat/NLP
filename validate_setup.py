import nltk
import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score

def count_nouns(pos_list):
    return len([pos for pos in pos_list if pos[1].startswith('NN')])

def count_prepositions(pos_list):
    return len([pos for pos in pos_list if pos[1] == 'IN'])

corpora = [
    nltk.corpus.gutenberg.sents('carroll-alice.txt'),
    nltk.corpus.gutenberg.sents('bible-kjv.txt')
]
corpora = [list(c)[10:111] for c in corpora]

sentence = corpora[0][0]
print(sentence)
pos = nltk.pos_tag(sentence)
print(pos)
print(f"{count_nouns(pos)} nouns and {count_prepositions(pos)} prepositions")

features = []
labels = []
for class_idx, corpus in enumerate(corpora):
    for sentence in corpus:
        pos = nltk.pos_tag(sentence)
        num_nn = count_nouns(pos)
        num_in = count_prepositions(pos)
        features.append([num_nn, num_in])
        labels.append(class_idx)
features = np.array(features)
labels = np.array(labels)

clf = SVC()
scores = cross_val_score(clf, features, labels, cv=5)
print(f"{sum(scores) / len(scores) * 100:0.0f} percent correct!")
