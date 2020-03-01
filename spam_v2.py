import numpy as np
import pandas as pd
from process_data import process
from tfidf import TFIDF_model
from metrics import metric

# Load the spam data file
data = pd.read_csv('spam.csv', encoding='cp437')
data_counts = data['v1'].value_counts().tolist()
data['v1'] = data['v1'].map({'ham': 0, 'spam': 1})
print("Data set: \nNumber of spam: ", data_counts[0],"\nNumber of ham: ", data_counts[1])

# Split data set into training and testing sets
# 80% for training, 20% for testing
trainIndex = list()
testIndex = list()
for i in range(data.shape[0]):
    if np.random.uniform(0,100) <= 80:
        trainIndex += [i]
    else:
        testIndex += [i]
trainData = data.loc[trainIndex]
testData = data.loc[testIndex]
# Reset index in training data set
trainData.reset_index(inplace = True)
training_counts = trainData['v1'].value_counts().tolist()
print("\nTraining data set: 80% of data set\nNumber of spam: ", training_counts[0],"\nNumber of ham: ", training_counts[1])
# Reset index in testing data set
testData.reset_index(inplace = True)
testing_counts = testData['v1'].value_counts().tolist()
print("\nTesting data set: 20% of data set\nNumber of spam: ", testing_counts[0],"\nNumber of ham: ", testing_counts[1])

# Training the TF-IDF model
tfidf = TFIDF_model(trainData)
tfidf.TF_and_IDF()
tfidf.TFIDF()

metric(testData['v1'], tfidf.test(testData['v2']))

# Running examples
message1 = 'OMW. I will call you later.'
process1 = process(message1)
print("\nMessage 1: ", message1, "\nSpam = 1, Ham = 0: ", tfidf.classify(process1))

message2 = 'I will text you when I finish work'
process2 = process(message2)
print("\nMessage 2: ", message2, "\nSpam = 1, Ham = 0: ", tfidf.classify(process2))

message3 = 'You win a trip to Europe! Call now to redeem'
process3 = process(message3)
print("\nMessage 3: ", message3, "\nSpam = 1, Ham = 0: ", tfidf.classify(process3))

message4 = 'Text or call now for a week of FREE membership.'
process4 = process(message4)
print("\nMessage 4: ", message4, "\nSpam = 1, Ham = 0: ", tfidf.classify(process4))