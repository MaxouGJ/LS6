#!/usr/bin/env python3

class Individu:

    def __init__(self, csv):
        s = csv.split(',')
        self.nom = s[0]
        self.prenom = s[1]
        self.profession = s[2]
        self.adresse = s[3]
        self.numero = s[4]

    def __str__(self):
        return (self.nom+" "+self.prenom+"\n"+self.profession+"\n"+self.adresse+"\n"+self.numero)

    

if __name__ == "__main__":
    i = Individu("Haddock,Archibald,Capitaine,Chateau de Moulinsart,421")
    print(i)
