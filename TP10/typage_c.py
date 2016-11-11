#!/usr/bin/env python3

import ctypes
import sys

if __name__ == "__main__":
    lib = ctypes.CDLL("./libaffichage.so")
    print(lib.multiplier(ctypes.c_int(5), 9))
    lib.aff_chaine(ctypes.c_char_p("Bonjour ensoleillé".encode()))
    lib.jakadi(ctypes.pointer(ctypes.c_char_p("mets les mains sur ta tête".encode())))
