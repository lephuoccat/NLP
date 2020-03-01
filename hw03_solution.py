# Group Member: Ashley Meuser, Liuyi Zhu, Cat Le

import re

def modernize(corpus):
    words = re.compile("[\\s+]").split(corpus)
    print(words)
    returnString = ""
    for word in words:
        temp = word
        temp = re.sub(r'yes([:,?.\)]?)$', r'ys\1', temp)
        temp = re.sub(r'wes([:,?.\)]?)$', r'ws\1', temp)
        temp = re.sub(r'esse([:,?.\)]?)$', r'ess\1', temp)
        if re.match(r'.*[aeiou][aeiou][^(aeiou)]e[:,?.\)]?$', temp):
            temp = re.sub(r'e([:,?.\)])?$', r'\1', temp)
        if re.match(r'.*[aeiou].*\'st[:,?.\)]?$', temp):
            temp = re.sub(r'\'st([:,?.\)])?$', r'\1', temp)
        if re.match(r'.*[aeiou].*\'d[:,?.\)]?$', temp):
            temp = re.sub(r'\'d([:,?.\)])?$', r'ed\1', temp)
        returnString += temp + " "
    print(returnString)
    return returnString