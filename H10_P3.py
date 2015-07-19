# Name: Jeffrey

import random


def createDictionary (fileName) :
    d = {}
    f = open(fileName)
    text = f.read()
    f.close()
    
    LoW = text.split()
    isStart = True
    for i in range(len(LoW)) :
        
        if isStart :
            d.setdefault("$", []).append(LoW[i])
        else :
            d.setdefault(LoW[i-1], []).append(LoW[i])
        last = LoW[i][-1]
        if last == '.' or last == '!' or last == '?' :
            isStart = True
        else :
            isStart = False
    return d 
def generateText (d, n) :
    res = ""
    curr = "$"
    for i in range(n) :
        curr = random.choice(d[curr])
        res += " " + curr
        last = curr[-1]
        if last == '.' or last == '!' or last == '?' :
            curr = "$"
    return res[1:]
#print generateText(createDictionary("text.txt"), 50)