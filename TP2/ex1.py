#!/usr/bin/env python3

def inversion() :
    s = input("Entrer une phrase :\n")
    l = s.split(" ")
    l.reverse()
    return (" ".join(l))

#print(inversion())

def inclus(l1, l2) :
    if len(l1) == 0 : return True
    if len(l1) > len(l2) : return False
    for i in l1 :
        for j in range(0, len(l2)) :
            if i == l2[j] :
                return inclus(l1[1:], l2[(j+1):])
        return False

l1 = [1, 2, 4]
l2 = range(0,10)
l3 = [2, 4, 1]
#print(inclus(l1, l2))

l5 = [i for i in range(0, 200) if (i%5==0 or i%7==0)]
#print(l5)

lpaire = [c for (i, c) in enumerate(l2) if i%2==0]
#print(lpaire)

l7 = [i for i in  zip(l1, l3)]
#print(l7)

def diviseurs(n) :
    return [i for i in range(2, n) if (n%i == 0)]

def premiers(n):
    return [i for i in range(1, n) if diviseurs(i) == []]

#print(premiers(100))

def sans_e(l):
    return [i for i in l if not("e" in i)]

#print(sans_e(["banane","banan","baba","bebe"]))

def anti_begue(l):
    res = [x for x,y in list(zip(l, l[1:])) if x!=y]
    res.append(l[-1])
    return res
           
#print(anti_begue(["ceci", "est", "un", "un", "test"]))

def prefixes(mot, taille) :
    return [mot[:m] for m in range(1, taille)]
#print(prefixes("banane", 4))
def est_sans_prefixe_cube(mot): 
    return ([i for i in prefixes(mot, len(mot)) if (3*i) in mot] == [])
#print(est_sans_prefixe_cube("baaa"))
def est_sans_cube(mot):
    for i in range(0, len(mot)) :
        if not(est_sans_prefixe_cube(mot[i:])) : return False
    return True
#print(est_sans_cube("aaaa"))
#print(est_sans_cube("aabaabba"))
