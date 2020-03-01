def metric(actual, predict):
    true_positive = 0
    true_negative = 0
    false_positive = 0
    false_negative = 0
    
    for i in range(len(actual)):
        if actual[i] == 1 and predict[i] == 1:
            true_positive += 1
        elif actual[i] == 1 and predict[i] == 0:
            false_negative += 1
        elif actual[i] == 0 and predict[i] == 1:
            false_positive += 1
        else:
            true_negative += 1

    print("\nTF-IDF Model Metrics:")
    print("True Positive:\t {:d}".format(true_positive))
    print("True Negative:\t {:d}".format(true_negative))
    print("False Positive:\t {:d}".format(false_positive))
    print("False Negative:\t {:d}".format(false_negative))

    total = true_positive + true_negative + false_positive + false_negative
    accuracy = (true_positive + true_negative) / total
    precision = true_positive / (true_positive + false_positive)
    recall = true_positive / (true_positive + false_negative)
    F1score = 2 * (precision * recall) / (precision + recall)
    print("\nAccuracy:\t {:0.5f}".format(accuracy))
    print("Precision:\t {:0.5f}".format(precision))
    print("Recall:\t\t {:0.5f}".format(recall))
    print("F1 score:\t {:0.5f}".format(F1score))