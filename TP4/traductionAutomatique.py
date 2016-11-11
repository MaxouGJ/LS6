#!/usr/bin/env python3

from sys import *

def read_lexic(fichier):
    f = open(fichier, "r")
    l = f.readlines()
    d = {c:v for [c,v] in [x[:len(x)-1].split(":") for x in l[:(len(l)-1)]]}
    f.close()
    return d

if __name__ == "__main__":
    print(read_lexic(argv[1]))
