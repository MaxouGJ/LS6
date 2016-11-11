#!/usr/bin/env python3

import os
import re

def list_jpeg(ref = ".") :
    exp = r"\.jpe?g$"
    for f in os.listdir(ref) :
        if re.search(exp, f.lower()):
            print(f)

def list_jpeg_r(ref = ".") :
    for root, dirs, files in os.walk(ref):
        exp = r"\.jpe?g$"
        for f in files :
            if re.search(exp, f.lower()):
                #print(os.path.join(root, f),f)
                print(os.path.abspath(root), f)

def range_jpeg(rep, ref = "."):
    try :
        os.mkdir(rep, 0o755)
    except FileExistsError :
        pass
    for root, dirs, files in os.walk(ref):
        exp = r"\.jpe?g$"
        for f in files :
            if re.search(exp, f.lower()):
                try :
                    os.link(os.path.join(root, f), os.path.join(rep, f.lower()))
                except FileExistsError:
                    pass

if __name__ == "__main__":
    list_jpeg("Arbo/Photos")
    list_jpeg_r("Arbo")
    range_jpeg("copie", "Arbo")
