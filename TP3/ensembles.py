#!/usr/bin/env python3

def ens_(w):
    s = set()
    for i in w :
        if not(i in s) : s.add(i)
    return s

def ens(w):
    return {i for i in w}

def afficher(s):
    for i in s : print(i)

def minimum(s) :
    min = s.pop()
    for i in s :
        if i < min : min = i
    return min

def memeslistes(l1, l2):
    return {i for i in l1}=={j for j in l2}

def multiples(p, n):
    return {i for i in range(p+1, n+1) if i%p==0}

def premiers(n):
    s = {i for i in range(2, n+1)}
    for p in s :
        s = s-multiples(p, n)
    return s

if __name__ == "__main__":
    print(ens("caracteres"))
    afficher({'s', 'w', 1, 6, 'G', 'test'})
    print(minimum({i for i in range(0, 57)}))
    print(memeslistes(range(1,6), [3, 2, 5, 1, 4]))
    print(multiples(7, 100))
    print(premiers(25))
