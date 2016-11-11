import re

def question1c(l) :
    return l[4]+l[len(l)-1]
#

def question2e(l):
    return [i for i in l if i >= 8]
#

def question3c(l):
    res = []
    for i in l :
        if len(i)>=3:
            res.append([2*j for j in i])
    return res
#

def question4a(fichier):
    f = open(fichier)
    res = re.findall(r"\w*[Aa]\w*", f.read())
    f.close()
    return res;
#

def question5f(t):
    d = {}
    for i in t :
        if i in d :
            d[i] += 1
        else : d[i] = 1
    return d
#

def question6a(s):
    return re.findall(r"\d{4,}", s)
#

def question7a(fichier):
    f = open(fichier)
    exp = re.compile(r"<([a-z]*?)> (.*?) </\1>")
    m = exp.findall(f.read())
    f.close()
    return {i:j for (i,j) in m}
#

def question8a(fichier):
    f = open(fichier)
    s = f.read()
    exp = re.compile(r"(\d+\.\d+),(-{0,1}\d+\.\d+),(\d{1,2}:\d{2,2}:\d{2,2}[NS]),(\d{1,2}:\d{2,2}:\d{2,2}[WE]),(\S+)")
    m = exp.findall(s)
    f.close()
    d = {}
    for (a,b,c,x,e) in m :
        d[e] = (a,b)
    return d
#

def question9b(d, lat_ref):
    return [i for i in d if (float(d[i][0])>lat_ref and float(d[i][0])<lat_ref+1) ]
#

def question10a(d, pref):
    res = []
    for i in d :
        if re.match(pref, i) : res.append(i)
        res = sorted(res)
        s = ""
    for j in res :
        s += j+"\t"
    return s
#

def question11a(d):
    d2 = {}
    for i in d :
        if d[i][0] in d2 :
            d2[d[i][0]] = d2[d[i][0]]+"\t"+i
        else :
            d2[d[i][0]] = i
    return d2
#

def question12b(d):
    return (min(d),d[min(d)])
#
