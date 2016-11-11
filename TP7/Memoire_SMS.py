#!/usr/bin/env python3

class Memoire_SMS :

    def __init__(self):
        self.listsms = []
        self.currentpos = 0

    def ajouter(self, numero, heure, texte):
        self.listsms.append((False, numero, heure, texte))

    def __getitem__(self, i):
        if i >= len(self.listsms) : return None
        sms = self.listsms[i]
        self.listsms[i] = (True, sms[1], sms[2], sms[3])
        return (sms[1], sms[2], sms[3])

    def __delitem__(self, i):
        if i<len(self.listsms):
            self.listsms.pop(i)

    def __str__(self):
        return "\n".join([str(m) for m in self.listsms])

    def __len__(self):
        return len(self.listsms)

    def __iter__(self):
        self.currentpos = 0
        return self

    def __next__(self):
        if(len(self) == self.currentpos) : raise StopIteration
        self.currentpos += 1
        return self.listsms[self.currentpos-1]

    def clone(self):
        m = Memoire_SMS()
        m.listsms = self.listsms[:]
        return m

    def non_lu(self):
        return [i for i,s in enumerate(self.listsms) if not(self.listsms[i][0])]

    def nombre_non_lu(self):
        return len(non_lu(self))

    def message_non_lus(self):
        for i in range(0, len(self.listsms)) :
            print(self[i])

    def recherche_mot(self, mot):
        return [i for i,s in enumerate(self.listsms) if mot in s[3]]

    def recherche_num(self, num):
        return [s for s in self.listsms if s[1] == num]

    def efface_num(self, num):
        for i,s in enumerate(self.listsms) :
            if s[1] == num : del(self[i])

    def remettreazero(self):
        self.listsms = []

    def copier(self, mem, eff=False):
        if eff :
            remettreazero(m)
        mem.listsms = self.listsms[:]


if __name__ == "__main__":
    m = Memoire_SMS()
    m.ajouter("0636712011", "12:00", "Hello")
    m.ajouter("0636754311", "12:00", "Hello")
    m.ajouter("0636712011", "12:00", "Ca va?")
    m.ajouter("0636754311", "12:00", "Oui et toi?")
    #print(m[0])
    #print(m[1])
    del(m[0])
    #print(m)
    #print(len(m))
    #for s in m:
    #    print(s)
    c = m.clone()
    c.ajouter("0636712011", "12:00", "Hello")
    #print(c)
    #print(m.non_lu())
    #print(m.message_non_lus())
    #print(c.recherche_mot("Hel"))
    #print(c.recherche_num("0636712011"))
    #c.efface_num("0636712011")
    #print(c.recherche_num("0636712011"))
    #m.remettreazero()
    m.copier(c)
    print(c)
