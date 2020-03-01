import numpy as np
from random import choices
from sklearn.decomposition import LatentDirichletAllocation

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
    return full_list

def lda_solve(documents):
    k = 3
    N = len(documents)
    for sentense in documents:
        words = [word for word in sentense] 
    word_set = set(words)
    vocab = list(word_set)
    V = len(vocab)
    print(vocab)
    
    X = np.zeros((N,V))
    i = 0
    for sentense in documents:
        for word in sentense:
            X[i, vocab.index(word)] += 1
        i += 1
    
    model = LatentDirichletAllocation(n_components=k, learning_method='online', random_state=0)
    model.fit(X)
    print(model.components_)
    return model.components_, vocab