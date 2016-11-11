#!/usr/bin/env python3

from sys import *

def compterLettres(fichier):
    return len({i for i in open(fichier).read()})

if __name__ == "__main__":
    print(compterLettres(argv[1]))
