#%%
class Ruban:
    def __init__(self,L,position=0,blanc="•"):
        """Crée un ruban donc les valeurs de départ
        sont dans L et la position initiale de la tête
        paut être spécifiée.
        """
        self.gauche = []
        self.droite = L[:]
        self.position = position
        self.index_min = 0
        self.index_max = len(L)-1
        self.blanc = blanc

    def lire(self):
        """Donne la valeur en face de la tête."""
        return self.valeur(self.position)

    def ecrire(self,valeur):
        """Ecrit la valeur en face de la tête."""
        i=self.position
        if i<self.index_min:
            for _ in range(self.index_min-1,i,-1):
                self.gauche.append(self.blanc)
            self.gauche.append(valeur)
            self.index_min=i
        elif i<0:
            self.gauche[-i-1]=valeur
        elif i<=self.index_max:
            self.droite[i]=valeur
        else:
            for _ in range(self.index_max+1,i):
                self.droite.append(self.blanc)
            self.droite.append(valeur)
            self.index_max=i

    def avancer(self):
        """Déplace la tête d'une case vers la droite."""
        self.position+=1

    def reculer(self):
        """Déplace la tête d'une case vers la gauche."""
        self.position-=1

    def valeur(self,i):
        """Donne la valeur à la position i."""
        if i<self.index_min:
            return self.blanc
        elif i<0:
            return self.gauche[-i-1]
        elif i<=self.index_max:
            return self.droite[i]
        else:
            return self.blanc

    def afficher(self):
        """affiche le ruban et la position de sa tête."""
        txt=self.blanc
        for i in range(self.index_min,self.position):
            txt+=str(self.valeur(i))
        txt+="["+str(self.valeur(self.position))+"]"
        for i in range(self.position+1,self.index_max+1):
            txt+=str(self.valeur(i))
        txt+=self.blanc
        print(txt)


class Turing:
    
