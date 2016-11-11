#!/usr/bin/env python3

import re


if __name__ == "__main__":
    print(re.match(r"A.C", "abc"))#None
    print(re.match(r"A.C", "AZZC"))#None
    print(re.match(r"A.C", "AC"))#None
    print(re.match(r"A.C", "ABC").group(0))#ABC

    print(re.match(r"[ABC]", "A").group(0))#A
    print(re.match(r"[ABC]", "B").group(0))#B
    print(re.match(r"[ABC]", "C").group(0))#C
    print(re.match(r"[ABC]", "ABC").group(0))#A

    print(re.match(r"[a-k1-5]", "A2"))#None
    print(re.match(r"[a-k1-5]", "a-3").group(0))#a
    print(re.match(r"[a-k1-15]", "e").group(0))#e
    print(re.match(r"[a-k1-15]", "1").group(0))#1

    print(re.match(r"[^A]", "A"))#None
    print(re.match(r"[^A]", "B").group(0))#B
    print(re.match(r"[^A]", ".").group(0))#.
    print(re.match(r"[^A]", "BCD").group(0))#B

    print(re.match(r"[^ABC]", "AZZ"))#None
    print(re.match(r"[^ABC]", "A"))#None
    print(re.match(r"[^ABC]", "B"))#None
    print(re.match(r"[^ABC]", "XY").group(0))#X

    print(re.match(r"AB.|A.C|.BC", "AB"))#None
    print(re.match(r"AB.|A.C|.BC", "ADC").group(0))#ADC
    print(re.match(r"AB.|A.C|.BC", "AZZC"))#None
    print(re.match(r"AB.|A.C|.BC", "AB.").group(0))#AB.

    print(re.match(r"[A|B]", "A").group(0))#A
    print(re.match(r"[A|B]", "B").group(0))#B
    print(re.match(r"[A|B]", "AB").group(0))#AB
    print(re.match(r"[A|B]", "|").group(0))#|
