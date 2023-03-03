class Rectangle:
    def __init__(self, longueur, largeur) -> None:
        self._longueur = longueur
        self._largeur = largeur 

    def get_longueur(self):
        return self._longueur
    
    def get_largeur(self):
        return self._largeur
    
    def set_longueur(self, longueur):
        self._longueur = longueur

    def set_largeur(self, largeur):
        self._longueur = largeur
    
    def périmètre(self):
        self.périmètre = self._largeur + self._longueur + self._largeur + self._longueur
        print("Le périmètre du rectangle est de {} cm".format(self.périmètre))

    def surface(self):
        self.surface = self._longueur * self._largeur
        print("La surface du rectangle est de {} cm".format(self.surface))


class Parallélépipède(Rectangle):
    def __init__(self, hauteur, longueur, largeur) -> None:
        Rectangle.__init__(self, longueur, largeur)
        self.__hauteur = hauteur

    def volume(self):
        self.volume = self._largeur * self._longueur * self.__hauteur
        print("Volume du parallélépipède : {} cm3".format(self.volume))

Rect = Rectangle(12, 15)
Rect.périmètre()
Rect.surface()
Rect = Parallélépipède(14, 7, 5)
Rect.volume()