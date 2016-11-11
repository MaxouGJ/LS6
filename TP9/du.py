#!/usr/bin/env python3

import os
import sys

def du_bs(ref = "."):
    somme = os.stat(ref).st_size
    inode = set()
    for root, dirs, files in os.walk(ref, False):
        for d in dirs :
            somme += os.stat(os.path.join(root,d)).st_size
        for f in files :
            stat = os.stat(os.path.join(root,f))
            if(not(stat.st_ino in inode)):
                somme += stat.st_size
                inode.add(stat.st_ino)
    return somme

if __name__ == "__main__":
    print(du_bs())
