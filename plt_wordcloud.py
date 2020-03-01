import matplotlib.pyplot as plt
from wordcloud import WordCloud

def wordcloud(data):
    # Plot the spam wordcloud
    spam = ' '.join(list(data[data['label'] == 1]['sms']))
    spam_wordcloud = WordCloud(width = 1000,height = 1000).generate(spam)
    plt.figure(1)
    plt.imshow(spam_wordcloud)
    # Plot the ham wordcloud
    ham = ' '.join(list(data[data['label'] == 0]['sms']))
    ham_wordcloud = WordCloud(width = 1000,height = 1000).generate(ham)
    plt.figure(2)
    plt.imshow(ham_wordcloud)
    plt.show()