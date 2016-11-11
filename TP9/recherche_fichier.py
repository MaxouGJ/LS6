#!/usr/bin/env python3

import os
import re

def find_nom(exp,rep, rm=False):
    for root, dirs, files in os.walk(rep):
        for f in files :
            if re.search(exp, f):
                print(os.path.join(os.path.abspath(root), f))
                if rm :
                    os.remove(os.path.join(root, f))

def find_taille(tail, rep, rm=False):
    for root, dirs, files in os.walk(rep):
        for f in files :
            if os.stat(os.path.join(root,f)).st_size == tail:
                print(os.path.join(os.path.abspath(root), f))
                if rm :
                    os.remove(os.path.join(root, f))

if __name__ == "__main__":
    find_nom('.gif', 'Arbo')
    find_taille(510, '.')
