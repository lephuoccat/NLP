import nltk
import itertools
from nltk import word_tokenize, pos_tag
from nltk.corpus import brown, treebank, conll2000

## Initialize Input Text and Corpus
text = "My friend and I often enjoy working in the coffee house"
#text = "I usually hang out with cute friends and watch national football league every Saturday night"
corpus1 = brown.tagged_sents(tagset='universal')
corpus2 = conll2000.tagged_sents(tagset='universal')
corpus3 = treebank.tagged_sents(tagset='universal')
corpus4 = brown.tagged_sents(categories=['news'], tagset='universal')
corpus5 = brown.tagged_sents(categories=['reviews'], tagset='universal')
corpus6 = brown.tagged_sents(categories=['romance'], tagset='universal')
corpus = list(itertools.chain(corpus1))

## Calculate state transition prob and word prob
word_list = []
for sentence in corpus:
    word_list.append(("_BEGIN_", "_begin_"))
    word_list.extend([(tag, word) for (word, tag) in sentence])
    word_list.append(("_END_", "_end_"))
tags = [tag for (tag, word) in word_list]
tag_list = []
for i in range(len(tags)-1):
    tag_list.append([tags[i], tags[i+1]])

# words prob
word_freq = nltk.ConditionalFreqDist(word_list)
B = nltk.ConditionalProbDist(word_freq, nltk.MLEProbDist)
# state transition prob
tag_freq= nltk.ConditionalFreqDist(tag_list)
A = nltk.ConditionalProbDist(tag_freq, nltk.MLEProbDist)


## Hidden Markov Model
# Viterbi Algorithm
words = word_tokenize(text)
tag_set = set(tags)
smooth = 1e-100
alpha = []
beta = []

## Step 1: Initialization
# BEGIN tag
alpha1 = {}
beta1 = {}
for tag in tag_set:
    if tag == "_BEGIN_": 
        continue
    pi = A["_BEGIN_"].prob(tag)
    alpha1[tag] = pi * (B[tag].prob(words[0])+ smooth)
    beta1[tag] = "_BEGIN_"
alpha.append(alpha1)
beta.append(beta1)

## Step 2: Recursion
# Text tags
for index in range(1, len(words)):
    curr_alpha = {}
    curr_beta = {}
    prev_alpha = alpha[-1]
    for tag in tag_set:
        if tag == "_BEGIN_": 
            continue
        prev_max = max(prev_alpha.keys(), key=lambda prev_t: prev_alpha[prev_t] * A[prev_t].prob(tag) * (B[tag].prob(words[index]) + smooth))
        curr_alpha[tag] = prev_alpha[prev_max] * A[prev_max].prob(tag) * (B[tag].prob(words[index]) + smooth)
        curr_beta[tag] = prev_max
    alpha.append(curr_alpha)
    beta.append(curr_beta)

## Step 3: Termination
# END tag
prev_alpha = alpha[-1]
prev_max = max(prev_alpha.keys(), key=lambda prev_t: prev_alpha[prev_t] * A[prev_t].prob("_END_"))
P = prev_alpha[prev_max] * A[prev_max].prob("_END_")
Q = [prev_max]

## Step 4: Path  backtracking
beta.reverse()
curr_q = Q[0]
for b in beta:
    curr_q = b[curr_q]
    if curr_q == "_BEGIN_":
        break
    Q.insert(0, curr_q)

## Step5: Print POS tagging and correct tagging
print('The input text: ', words)
print('The tag sequence: ' + f'{Q} with p = {P}')
# correct tagging
correct_tag_sent = pos_tag(words, tagset='universal')
correct_tag = [tag for word, tag in correct_tag_sent]
print('The correct tag: ', correct_tag)
# error rate
error = 0
for i in range(len(words)):
    if Q[i] != correct_tag[i]:
        error+=1
rate = (1 - error/len(words)) * 100
print('The success rate: {:0.2f}%'.format(rate))