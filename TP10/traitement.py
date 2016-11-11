#!/usr/bin/env python3

import ctypes
import sys
import subprocess
from Image import Image

if __name__ == "__main__":

    lib = ctypes.CDLL("./libimage.so")

    lib.lire_image.restype = Image
    lib.melange.restype = Image
    lib.zoom.restype = Image
    lib.negatif.restype = Image

    i = lib.lire_image(sys.argv[1].encode())
    #If mauvais
    if(sys.argv[2] == "ecrire_image"):
        lib.ecrire_image(i, ctypes.c_char_p(sys.argv[3].encode()))
    elif(sys.argv[2] == "melange") :
        i = lib.melange(i)
    elif(sys.argv[2] == "zoom") :
        i = lib.zoom(i, int(sys.argv[3]))
    elif(sys.argv[2] == "negatif") :
        i = lib.negatif(i)
    else :
        print("Commande non reconnue")
