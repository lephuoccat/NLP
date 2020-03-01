from math import log, sqrt
from process_data import process

class TFIDF_model(object):
    def __init__(self, train):
        self.label = train['v1']
        self.sms = train['v2']
        self.tf_spam = dict()
        self.tf_ham = dict()
        self.idf_spam = dict()
        self.idf_ham = dict()
        self.P_spam = dict()
        self.P_ham = dict()

        
    def TF_and_IDF(self):
        self.spam_num = self.label.value_counts()[1]
        self.ham_num = self.label.value_counts()[0]

        for i in range(self.sms.shape[0]):
            message = process(self.sms[i])
            word_list = list()

            # Calculate TF
            for word in message:
                if word not in word_list:
                    word_list += [word]
                if self.label[i]:
                    self.tf_spam[word] = self.tf_spam.get(word,0) + 1
                else:
                    self.tf_ham[word] = self.tf_ham.get(word,0) + 1
                    
            # Calculate IDF
            for word in word_list:
                if self.label[i]:
                    self.idf_spam[word] = self.idf_spam.get(word,0) + 1
                else:
                    self.idf_ham[word] = self.idf_ham.get(word,0) + 1


    def TFIDF(self):
        self.tfidf_spam = 0
        self.tfidf_ham = 0
        
        # Calculate TF-IDF for spam
        for word in self.tf_spam:
            self.P_spam[word] = (self.tf_spam[word]) * log((self.spam_num + self.ham_num) / (self.idf_spam[word] + self.idf_ham.get(word, 0)))
            self.tfidf_spam += self.P_spam[word]
        for word in self.tf_spam:
            self.P_spam[word] = (self.P_spam[word] + 1) / (self.tfidf_spam + 1)
        # Calculate TF-IDF for ham
        for word in self.tf_ham:
            self.P_ham[word] = (self.tf_ham[word]) * log((self.spam_num + self.ham_num) / (self.idf_spam.get(word, 0) + self.idf_ham[word]))
            self.tfidf_ham += self.P_ham[word]
        for word in self.tf_ham:
            self.P_ham[word] = (self.P_ham[word] + 1) / (self.tfidf_ham + 1)
    

    def classify(self, message):
        # Making decision: spam vs non-spam
        decision = 0
        P_spam_sms = 0
        P_ham_sms = 0
        # Use log to convert multiplication to addition
        # To reduce the complexity of the algorithm
        for word in message:                
            if word in self.P_spam:
                P_spam_sms += log(self.P_spam[word])
            else:
                P_spam_sms -= log(self.tfidf_spam + 1)
            
            if word in self.P_ham:
                P_ham_sms += log(self.P_ham[word])
            else:
                P_ham_sms -= log(self.tfidf_ham + 1)

            P_spam_sms += log(self.spam_num / (self.spam_num + self.ham_num))
            P_ham_sms += log(self.ham_num / (self.spam_num + self.ham_num))
        
        if P_spam_sms >= P_ham_sms:
            # decide spam
            decision = 1
        else:
            #decide ham
            decision = 0
        return decision
    

    def test(self, test):
        # Run the prediction model on the testing dataset
        prediction = dict()
        for (i, sms) in enumerate(test):
            message = process(sms)
            prediction[i] = self.classify(message)
        return prediction