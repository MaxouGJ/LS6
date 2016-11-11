#!/usr/bin/env python3

import re
import sys

def listekw(f) :
    #return re.findall(r"(\w*[wk]\w*)", f.read())
    return re.findall(r"(\w*[wk]\w*)\W*$", f.read(), re.MULTILINE)
    
def liste19(f):
    return re.findall(r"(18\d\d)\W*$", f.read(), flags=re.MULTILINE)

def listeaimer(f):
    #return re.findall(r"\s(aim\w*)", f.read())
    return re.findall(r"\W(aim\w*)\W*$", f.read(), re.MULTILINE)

def enum19(f):
    exp = re.compile(r"(18\d\d)")
    for (l, w) in enumerate(f.readlines()) :
        if exp.findall(w) != [] : print(l, exp.findall(w)[0])

def doublon(f):
    return re.findall(r"(\w*?(\w\w\w)\w*\2\w*)", f.read())

def doublonphrase(f):
    return re.findall(r".*(\s[\d\w]+\s).*\1.*[\.\?\!]", f.read())

if __name__ == "__main__":
    f = open(sys.argv[1])
    #print(listekw(f))
    #print(liste19(f))
    #print(listeaimer(f))
    #print(enum19(f))
    #print(doublon(f))
    print(doublonphrase(f))
    f.close()
