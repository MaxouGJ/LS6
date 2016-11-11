#!/usr/bin/env python3

from random import randint
from time import process_time

def inittable(n):
    return n*[None]

def ajoutertable(x, n, t):
    if(t[x%n] == None):
        t[x%n] = x
    elif(t[x%n] != x):
        for i in range(1, len(t)):
            if t[(x+i)%n] == None :
                t[(x+i)%n] = x
                break

def ajoutertablequadra(x, n, t):
    if(t[x%n] == None):
        t[x%n] = x
    elif(t[x%n] != x):
        for i in range(1, len(t)):
            if t[(x+(i**2))%n] == None :
                t[(x+(i**2))%n] = x
                break
            
def danstable(x, n, t):
    return x in t

def testhachage(n, l):
    t = inittable(n)
    for i in l :
        if not(danstable(i, n, t)):
            ajoutertable(i, n, t)
    for i in l :
        if not(danstable(i, n, t)):
            return False
    return True

def testhachagequadra(n, l):
    t = inittable(n)
    for i in l :
        if not(danstable(i, n, t)):
            ajoutertablequadra(i, n, t)
    for i in l :
        if not(danstable(i, n, t)):
            return False
    return True

def testset(l):
    s = {i for i in l if i != None}
    for i in s :
        if not(i in s):
            return False
    return True

def testmethodes(k, m, n):
    l = [randint(0, m) for i in range(0,k)]
    t1 = process_time()
    testhachage(n, l)
    t2 = process_time()
    testset(l)
    t3 = process_time()
    testhachagequadra(n, l)
    t4 = process_time() 
    print("List lineaire: ", t2-t1, "List quadra: ", t4-t3, " Set : ", t3-t2)

def enlever(x, n, t):
    if(not(danstable(x,n,t))) : return
    i=x
    while(t[i%n] != x) :
        i+=1
    t[i%n] = None
    j = i+1
    while(t[j%n] != None):
        a = t[j%n]
        t[j%n] = None
        ajoutertable(a, n, t)
        j+=1

def hash(s, n):
    res = 0
    for i in range(0, len(s)) :
        res += (ord(s[i])*(128**i))
    print(res)
    return (res%n)
        
if __name__ == "__main__":
    #(testmethodes(350, 1000, 400))
    '''m = 100
    k = 30
    n = 20
    l = [randint(0, m) for i in range(0,k)]
    t = inittable(n)
    ajoutertable(12, n, t)
    ajoutertable(13, n, t)
    ajoutertable(32, n, t)
    print(t)
    enlever(12,n,t)
    print(t)'''
    #print(hash("machin", 10))#
