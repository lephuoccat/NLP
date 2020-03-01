from nltk.corpus import wordnet


def score_document(document, positive_seeds, negative_seeds):
    positive_words = get_synonyms(positive_seeds)
    negative_words = get_synonyms(negative_seeds)
    positive_words = get_synonyms(positive_words)
    negative_words = get_synonyms(negative_words)
    pos_score = 0
    neg_score = 0
    for word in document:
        if word in positive_words:
            pos_score += 1
        if word in negative_words:
            neg_score += 1
    return pos_score - neg_score


def get_synonyms(seeds):
    synonyms = list()
    for i in seeds:
        for words in wordnet.synsets(i):
            for w in words.lemmas():
                synonyms.append(w.name())
    return synonyms
