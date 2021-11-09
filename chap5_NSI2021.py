# +-----------------------------+
# | Chapitre 5 : Piles et Files |
# +-----------------------------+

## Piles
class Pile:
    def __init__(self):
        self.valeurs=[]

    def est_vide(self):
        return len(self.valeurs)==0

    def empile(self,x):
        self.valeurs.append(x)

    def depile(self):
        if self.est_vide():
            raise IndexError('depilement d une pile vide')
        else :
            return self.valeurs.pop()

    def __str__(self):
        t1,t2 = "+-","| "
        for x in self.valeurs:
            t=str(x)
            t1+="-"*(len(t)+1)
            t2+=t+" "
        return t1+"\n"+t2+"\n"+t1


def cree_Pile():
    return Pile()

## Activité 2
def retourne(p1: Pile) -> Pile:
    p2=Pile()
    # à compléter
    return p2

#tests
print("=====Activité 2======")
p1=Pile()
p1.empile(1)
p1.empile(2)
p1.empile(3)
print(p1)
p2=retourne(p1)
print(p2)






## Files
class File:
    def __init__(self):
        self.valeurs=[]

    def est_vide(self):
        return len(self.valeurs)==0

    def enfile(self,x):
        self.valeurs.append(x)

    def defile(self):
        if self.est_vide():
            raise IndexError('defilement d une file vide')
        else :
            return L.pop(0)

    def __str__(self):
        t1,t2 = "+-","< "
        for x in self.valeurs:
            t=str(x)
            t1+="-"*(len(t)+1)
            t2+=t+" "
        return t1+"+\n"+t2+"<\n"+t1+"+"



## Activité 4




#tests
print("=====Activité 4======")
f1=File()
f1.enfile(1)
f1.enfile(2)
f1.enfile(3)
print(f1)



## Activité 5

class Cellule :
    def __init__(self,v,s) :
        self.valeur = v
        self.suivante = s

class File :
    def __init__(self) :
        self.tete = None
        self.queue = None

    def est_vide(self) :
        return self.tete is None

    def enfile(self,x) :
        c = Cellule(x,None)
        if self.est_vide() :
            self.tete = c
            self.queue = c
        elif self.queue is self.tete :
            self.queue = c
            self.tete.suivante = self.queue
        else :
            self.queue.suivante = c
            self.queue = c

    def defile(self) :
        if self.est_vide() :
            raise IndexError('defilement d une file vide')
        else :
            v = self.tete.valeur
            if self.queue is self.tete :
                self.tete = None
                self.queue = None
            elif self.tete.suivante is self.queue :
                self.tete = self.queue
            else :
                self.tete = self.tete.suivante
            return v

    def affiche(self) :
        texte = "T"
        a = self.tete
        while a is not None :
            texte = texte + "-(" + str(a.valeur) + ")"
            a = a.suivante
        return texte + "-Q"







