#!/usr/bin/env python3

from sys import *

def recherche(fichier, mot) :
    return "".join([str((i+1))+"\t"+l+"\n" for i,l in enumerate(open(fichier).readlines()) if mot in l])

def sans_e(fichier):
    return "".join([])
if __name__ == "__main__":
    print(recherche(argv[1], argv[2]))
    
