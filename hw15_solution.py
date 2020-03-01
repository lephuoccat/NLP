import numpy as np


class Rule:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return f'{self.left} -> {self.right}'


def print_parse_trees(sentence, rule_list):
    intermediateRules = list()
    terminalRules = list()
    for i in rule_list:
        if type(i.right) == tuple:
            intermediateRules.append(i)
        else:
            terminalRules.append(i)

    sentence_pos = list()
    sentence = sentence.split(" ")
    for i in sentence:
        for rule in terminalRules:
            if i in rule.right:
                sentence_pos.append(rule.left)
                break

    table = []
    new = []
    for i in range(len(sentence_pos)):
        for j in range(len(sentence_pos)):
            new.append([""])
        table.append(new)
        new = []

    for j in range(0, len(sentence_pos)):
        for i in range(0, j+1):
            if i == 0:
                table[j][j] = [sentence_pos[j]]
            else:
                for k in range(len(table[j-i][j-i])):
                    for l in range(len(table[j-i+1][j])):
                        rule_tuple = (table[j-i][j-i][k], table[j-i+1][j][l])
                        for rule in intermediateRules:
                            if rule.right == rule_tuple:
                                if table[j-i][j] == [""]:
                                    table[j-i][j] = [rule.left]
                                else:
                                    table[j-i][j].append(rule.left)

    for i in range(len(table)):
        print(table[i])

    max_val = 0
    for i in range(len(table)):
        for j in range(len(table[i])):
            max_val = max(len(table[i][j]), max_val)

    # build the trees

    j = len(sentence_pos)-1
    for k in range(max_val):
        for i in range(len(sentence_pos)):
            print("\nRow #"+str(i))
            for m in range(0, i-1):
                print("\t", end="")
            if i == 0:
                if len(table[i][j]) > 1:
                    table[i][j].remove(table[i][j][0])
            else:
                print("(" + table[i-1][i-1][0]+")   ("+table[i][j][0]+")")
                if len(table[i-1][i-1]) > 1:
                    table[i][j].remove(table[i-1][i-1][0])
                if len(table[i][j]) > 1:
                    table[i][j].remove(table[i][j][0])
