class Noeud :
    def __init__(self,g,v,d):
        self.gauche = g
        self.valeur = v
        self.droit = d

    def assigne_gauche(self,n):
        self.gauche = n

    def assigne_droit(self,n):
        self.droit = n

    def assigne_valeur(self,v):
        self.valeur = v

G = Noeud(None,'G',None)
H = Noeud(None,'H',None)
I = Noeud(None,'I',None)
D = Noeud(None,'D',None)
E = Noeud(G,'E',None)
F = Noeud(H,'F',I)
B = Noeud(D,'B',E)
C = Noeud(F,'C',None)
A = Noeud(B,'A',C)

A = Noeud(None,'A',None)
B = Noeud(None,'B',None)
C = Noeud(None,'C',None)
D = Noeud(None,'D',None)
E = Noeud(None,'E',None)
F = Noeud(None,'F',None)
G = Noeud(None,'G',None)
H = Noeud(None,'H',None)
I = Noeud(None,'I',None)
A.assigne_gauche(B)
A.assigne_droit(C)
B.assigne_gauche(D)
B.assigne_droit(E)
C.assigne_gauche(F)
E.assigne_gauche(G)
F.assigne_gauche(H)
F.assigne_droit(I)
