import numpy as np

'''
obs = int list of observations
pi = initial state probabilities [list of floats]
A = state transition probability matrix [2D numpy array]
B = observation probability matrix [2D numpy array]

Returns:
states = inferred state sequence
p_star = probability of state sequence given obs
'''


def infer_states(obs, pi, A, B):

    alpha = np.zeros((len(obs), len(pi)))

    for i in range(len(pi)):
        alpha[0][i] = pi[i]*B[i][obs[0]]

    for t in range(1, len(obs)):
        for j in range(len(pi)):
            a = np.zeros(len(pi))
            for i in range(len(pi)):
                a[i] = alpha[t-1][i]*A[i][j]
            alpha[t][j] = np.max(a)*B[j][obs[t]]

    beta = np.zeros((len(obs), len(pi)))

    for t in range(1, len(obs)):
        for j in range(len(pi)):
            m = -9999
            index = 0
            for i in range(len(pi)):
                if alpha[t-1][i]*A[i][j] > m:
                    index = i
                    m = alpha[t-1][i]*A[i][j]
            beta[t][j] = int(index)

    P = np.max(alpha[len(obs)-1])
    Q = np.zeros(len(obs))
    for i in range(len(pi)):
        if np.max(alpha[-1][i]) == P:
            Q[-1] = i
            break

    for t in range(len(obs)-2, -1, -1):
        Q[t] = beta[t+1][int(Q[t+1])]

    list_out = [i for i in Q]
    return list_out, P