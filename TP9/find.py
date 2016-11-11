#!/usr/bin/env python3

import recherche_fichier
import sys
from argparse import ArgumentParser

if __name__ == "__main__":
    f = sys.argv[1]
    parser = ArgumentParser()
    parser.add_argument(action="store", dest="f", help="find.py <file>")
    parser.add_argument("-n", "--name", action="store", dest="n", help="-n <expr> ou --name <expr> : liste les références absolues des fichiers de l'arborescence.")
    parser.add_argument("-s", "--size", action="store", dest="s", help="-s <taille> ou --size <taille> : liste les références absolues des fichiers de l'arborescence.")
    parser.add_argument("-c", "--clean", action="store_true", dest="c", help="Supprime les fichiers de l'arborescence")
    args = parser.parse_args()
    if args.n:
        if args.c :
            recherche_fichier.find_nom(args.n, args.f, args.c)
        else :
            recherche_fichier.find_nom(args.n, args.f)
    elif args.s :
        if args.c :
            recherche_fichier.find_taille(args.s, args.f, args.c)
        else :
            recherche_fichier.find_taille(args.s, args.f)
    else :
        print(args.f)
