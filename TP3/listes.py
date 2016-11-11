#!/usr/bin/env python3

def couples(i, j):
    return[(x, y) for x in range(0,i+1) for y in range(0,j+1)]

def transposee(m):
    return [[i[j] for i in m] for j in range(0, len(m[0]))]

def produit(l):
    res = [[]]
    for l1 in l:
        res = [[i]+j for j in res for i in l1]
    return res
    
if __name__ == "__main__":
    print(couples(3, 4))
    print(transposee([[1,2,3],[4,5,6]]))
    print(produit([[4,5], ['cd'], [1,2,3]]))
