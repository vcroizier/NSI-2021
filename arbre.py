class Noeud :
    def __init__(self,v,e):
        self.valeur = v
        self.enfants = e

    def ajoute_enfant(self,n):
        self.enfants.append(n)

rep1=Noeud('rep1',[])
rep4=Noeud('rep4',[])
f3=Noeud('f3',[])
rep6=Noeud('rep6',[])
rep1.ajoute_enfant(rep4)
rep1.ajoute_enfant(f3)
rep1.ajoute_enfant(rep6)
rep7=Noeud('rep7',[])
rep4.ajoute_enfant(rep7)
f1=Noeud('f1',[])
f2=Noeud('f2',[])
rep7.ajoute_enfant(f1)
rep7.ajoute_enfant(f2)
f4=Noeud('f4',[])
rep6.ajoute_enfant(f4)