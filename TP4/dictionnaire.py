#!/usr/bin/env python3

from time import process_time

def listeversdico(l):
    #return {x:y for x,y in enumerate(l)}
    return dict(enumerate(l))

def merge(d1, d2):
    d = d1.copy()
    for x in d2.items() : d[x[0]] = x[1] #<=>d.update(d2)
    return d

def chars(w) :
    return {c:w.count(c) for c in w}

def chars2(w):
    d = {}
    for c in w :
        if c in d :
            d[c] = d[c]+1
        else :
            d[c] = 1
    return d

def affichedico(d) :
    for x in d : print(x[0]," -> ", d[x])

def mergeval(d1, d2):
    d = {}
    for x in d1 : 
        if x in d2 :
            d[x] = (d1[x], d2[x])
    return d

if __name__ == "__main__":
    print(listeversdico(["petit", "klein", "small"]))
    d1 = {1:2, 2:3}
    d2 = {1:4, 4:4}
    print(d1)
    print(d2)
    print(merge(d1, d2))
    affichedico(chars("bonjour"))
    print(mergeval(d1, d2))
    t1 = process_time()
    chars(10000*"ab")
    t2 = process_time()
    chars2(10000*"ab")
    t3 = process_time()
    print(t2-t1," / ", t3-t2) 
