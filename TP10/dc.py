#!/usr/bin/env python3

import subprocess
import sys
import time

def mon_dc():
    p = subprocess.Popen(["dc"])
    time.sleep(20)
    p.send_signal(9)

def dc_fics(fichier):
    f = open(fichier)
    out = open(fichier+".out", "w")
    err = open(fichier+".err", "w")
    p = subprocess.Popen("dc", stdin=f, stdout=out, stderr=err)
    p = subprocess.Popen(["cat", fichier+".out"])
    p = subprocess.Popen(["cat", fichier+".err"])

def dc_tubes(calcul):
    p = subprocess.Popen("dc", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    outs, errs = p.communicate(calcul)
    print("out : ",outs)
    print("err : ",errs)

def tube(cmd1, entree, cmd2):
    f = open(entree)
    p1 = subprocess.Popen(cmd1, stdin=f, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    outs1, errs2 = p1.communicate(entree)
    p2 = subprocess.Popen(cmd2, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    outs2, errs2 = p2.communicate(outs1)
    print(outs2)

if __name__ == "__main__":
    #mon_dc()
    #dc_fics(sys.argv[1])
    #dc_tubes(sys.argv[1])
    #tube("less", "calcul", "dc")
