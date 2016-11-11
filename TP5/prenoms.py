#!/usr/bin/env python3

import re

def double(s) :
    m = re.match(r"(.*)\1$", s)
    return None if m == None else m.group(1)

def contientdouble(s) :
    m = re.search(r"(.{2,})\1", s)
    return None if m == None else m.group(1)

def extraire_ligne(s) :
    motif = r"(\d{4,4}),(\d+),(\d+),(\w+)"
    r = re.match(motif,s.strip())
    if r == None : return None
    return (r.group(1), r.group(2), r.group(3), r.group(4))

'''def extraire_fichier(f) :
    return {(extraire_ligne(x)[3], extraire_ligne(x)[0]) : int(extraire_ligne(x)[1]) for x in (open(f,"r")) if extraire_ligne(x) != None}'''
def extraire_fichier(f) :
    d = {}
    with open(f) as fic :
        for l in fic :
            res = extraire_ligne(l)
            if res :
                if (res[3],res[0]) in d :
                    d[(res[3],res[0])] += int(res[1])
                else : d[(res[3],res[0])] = int(res[1])
    return d

def popularite(d):
    dic = {}
    for (a,b) in d :
        if a in dic : dic[a] += d[(a,b)]
        else : dic[a] = d[(a,b)]
    return dic

'''def liste_prenoms(d) :
    l = []
    for x in d 
    return l'''
    
if __name__ == "__main__":
    print(contientdouble("okokt"))
    print(extraire_ligne("(1995,25,06,Maxime)"))
    #print(extraire_fichier("prenoms.txt"))
    print(popularite(extraire_fichier("prenoms.txt")))
