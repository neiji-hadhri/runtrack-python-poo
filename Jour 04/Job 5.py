class Forme : 
    def __init__(self) -> None:
        pass
    def aire(self):
        return 0
    

class Rectangle(Forme):
    def __init__(self, largeur, longueur) -> None:
        Forme.__init__(self)
        self.__largeur = largeur
        self.__longueur = longueur

    def aire(self): 
        self.aire = self.__longueur * self.__largeur
        print("L'air du rectangle est de {} cm²".format(self.aire))


        
class Cercle(Forme):
    def __init__(self, radius) -> None:
        Forme.__init__(self)
        self.__radius = radius

    def aire(self): 
        self.aire = 3.14 * (self.__radius * self.__radius)
        print("L'air du Cercle est de {} cm²".format(self.aire))


Cal = Forme()

Cal = Rectangle(4, 7)
Cal.aire()

Cal = Cercle(3)
Cal.aire()