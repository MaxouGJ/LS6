#!/usr/bin/env python3

from Individu import Individu

class Annuaire:

    def __init__(self, fichier):
        f = open(fichier)
        l = f.readlines()
        f.close()
        self.individus = []
        for i in l :
            self.individus.append(Individu(i))

    def __str__(self):
        s = ""
        for i in self.individus :
            s += str(i)+"\n"
        return s

    def copie(self, fichier):
        f = open(fichier, "w")
        for i in self.individus:
            f.write(i.nom+","+i.prenom+","+i.profession+","+i.adresse+","+i.numero)
        f.close()

    def liste_pages_jaunes(self, profession):
        return [str(i) for i in self.individus if i.profession == profession]

    def cherche_pages_jaune(self, profession):
        l = self.liste_pages_jaunes(profession)
        print(str(len(l))+" résultats trouvés\n")
        for i in l :
            print(i)

    def liste_pages_blanches(self, nom):
        return [str(i) for i in self.individus if nom in i.nom or nom in i.prenom]

    def cherche_pages_blanches(self, nom):
        l = self.liste_pages_blanches(nom)
        print(str(len(l))+" résultats trouvés\n")
        for i in l :
            print(i)

    def selectionne(self, nom):
        l = [i for i in self.individus if nom == i.nom]
        if len(l) == 0 : return None
        if len(l) == 1 : return l[0]
        for n,i in enumerate(l):
            print(str(n)+" : "+str(i))
        return l[int(input("Entrez le numéro correspondant à votre choix\n"))]

    def modifier(self, nom):
        ind = self.selectionne(nom)
        if ind != None :
            ind.numero = input("Entrez le nouveau numéro de téléphone : ")


if __name__ == "__main__":
    a = Annuaire("annuaire")
    print(a)
    #a.copie("copie")
    #a.cherche_pages_jaune("Marin")
    #a.cherche_pages_blanches("Mi")
    a.modifier("Haddock")
    a.modifier("Odema")
    a.copie("copie")
