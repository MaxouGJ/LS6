#!/usr/bin/env python3

from ctypes import *

class Image(Structure):
    _fields_ = [("img", POINTER(c_char_p)),("nb_lign", c_int), ("nb_col", c_int)]
