class ArbreComplet:
    def __init__(self):
        self.L=[]

    def ajouter(self,valeur):
        self.L.append(valeur)

    def est_vide(self):
        self.L==[]

    def fils_droit(self,k):
        return 2*k+2

    def fils_gauche(self,k):
        return 2*k+1

    def pere(self,k):
        return (k-1)//2

    def valeur(self,k):
        return self.L[k]

class Tas:
    def __init__(self):
        self.L=[]

    def ajouter(self,valeur):
        self.L.append(valeur)
        k=len(self.L)-1 #position de la valeur ajoutée.
        while k>0 and self.valeur(self.pere(k))<valeur :
            p=self.pere(k)
            self.L[k],self.L[p]=self.L[p],self.L[k]
            k=p

    def est_vide(self):
        self.L==[]

    def fils_droit(self,k):
        return 2*k+2

    def fils_gauche(self,k):
        return 2*k+1

    def pere(self,k):
        return (k-1)//2

    def valeur(self,k):
        return self.L[k]

    def retirer_max(self):
        if len(self.L)==1 :
            return self.L.pop()
        M=self.L[0] # on mémorise
        valeur=self.L.pop() # on retire le dernier.
        self.L[0]=valeur # on écrase la racine avec.
        k=0 #position de départ.
        n=len(self.L)
        pas_fini=True
        while pas_fini :
            d=self.fils_droit(k)
            g=self.fils_gauche(k)
            k1=k #destination de l'échange avec k
            # on cherche le plus grand entre fils droit et gauche et notre valeur.
            if g<n and self.valeur(g)>self.valeur(k):
                k1=g
            if d<n and self.valeur(d)>self.valeur(k1):
                k1=d
            if k1!=k :
                self.L[k],self.L[k1]=self.L[k1],self.L[k]
                k=k1
            else:
                pas_fini=False
        return M

def heapsort(liste):
    T=Tas()
    n=len(liste)
    for k in range(n):
        T.ajouter(liste.pop())
    for k in range(n):
        L.append(T.retirer_max())

L=[7,4,2,1,9,5,8,3,4,6]
heapsort(L)
print(L)

# pour heapsort2 il faut utiliser un curseur qui marque la fin de l'arbre et le début du reste de la liste. Du coup, il faut adapter le code ajouter et de retirer_max : il y a du boulot.
