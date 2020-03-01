import numpy as numpy
from random import choices

# theta = document, topic matrix
# phi = topic, word matrix
# N = num words per document we are generating


def lda(vocabulary, phi, theta, N):
    topics = []
    for i in range(len(theta[0])):
        topics.append(i)
    full_list = []
    for document in theta:
        # draw randomly from theta to get list of topics
        word_list = []
        for i in range(N):
            word_list.append(
                choices(vocabulary, phi[choices(topics, document)[0]])[0])
        full_list.append(word_list)
    print(full_list)
    return full_list
