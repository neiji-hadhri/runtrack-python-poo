class Rectangle :
    def __init__(self, longueur, largeur) :
        self.__longueur = longueur
        self.__largeur = largeur
    
    def get_longueur(self):
        return self.__longueur

    def set_longueur(self, nouvelle_longueur):
        self.__longueur = nouvelle_longueur

    def get_largeur(self):
        return self.__largeur
    
    def set_largeur(self, nouvelle_largeur):
        self.__largeur = nouvelle_largeur

Rec = Rectangle(10, 5)
print("Longueur = {} , Largeur = {}".format(Rec.get_longueur(), Rec.get_largeur()))
Rec.set_longueur(5)
Rec.set_largeur(2)
print("Nouvelle longueur = {} , Nouvelle largeur = {}".format(Rec.get_longueur(), Rec.get_largeur()))
