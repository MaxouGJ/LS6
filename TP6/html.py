#!/usr/bin/env python3

import re
import sys

def imprimeHTML(fichier) : 
    exp = re.compile(r"</?(.*?)>")
    with open(fichier) as f :
        for l in f :
            for c in (exp.finditer(l)):
               print(c.group(1))

def printlien(fichier):
    exp = re.compile(r"<a href=\"(.*?)\".*>")
    with open(fichier) as f:
        for l in f:
            for c in (exp.finditer(l)):
                print(c.group(1))

def printdomaine(fichier):
    exp = re.compile(r"<a href=\"(.*?)(\.[^.]*?)/*\".*>")
    with open(fichier) as f:
        for l in f:
            for c in (exp.finditer(l)):
                print(c.group(2))

def printnocomment(fichier) :
    f = open(fichier)
    contenu = f.read()
    exp = re.compile(r"<!--(.*?)-->", re.DOTALL)
    print(exp.sub("", contenu))
    f.close()
                
if __name__ == "__main__":
    #imprimeHTML(sys.argv[1])
    #printlien(sys.argv[1])
    #printdomaine(sys.argv[1])
    #printnocomment(sys.argv[1])
