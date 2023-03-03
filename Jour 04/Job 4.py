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

Cal = Forme()
Cal.aire()
Cal = Rectangle(4, 7)
Cal.aire()
        