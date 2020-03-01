from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Process the dataset
def process(data):
    data = data.lower()
    words = word_tokenize(data)
    
    # stemming
    ps = PorterStemmer()
    words = [ps.stem(word) for word in words] 
    
    # remove stopword
    words = [word for word in words if word not in stopwords.words('english')] 

    # n-gram
    w = []
    gram = 2
    for i in range(len(words) - gram + 1):
        w += [' '.join(words[i:i + gram])]
    return w
