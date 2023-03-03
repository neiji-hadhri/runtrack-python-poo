class Véhicule :
    def __init__(self, marque, modele, annee, prix) -> None:
        self._marque = marque
        self._modele = modele
        self._annee = annee
        self._prix = prix
        

    def informationsVehicule (self):
        print("Marque du Véhicule : {}".format(self._marque))
        print("Modèle du Véhicule : {}".format(self._modele))
        print("Année : {}".format(self._annee))
        print("Prix : {} €".format(self._prix))

    def demarrer(self):
        print("Attention, je roule ")

class Voiture(Véhicule):
    def __init__(self, marque, modele, annee, prix) -> None:
        Véhicule.__init__(self, marque, modele, annee, prix)
        self.__portes = 4

    def informationsVehicule(self):
        print("Marque du Véhicule : {}".format(self._marque))
        print("Modèle du Véhicule : {}".format(self._modele))
        print("Année : {}".format(self._annee))
        print("Prix : {} €".format(self._prix))
        print("Nombre de porte dans le véhicule : {} portes".format(self.__portes))

    def demarrer(self):
        print("Attention, je roule en voiture {} : {}".format(self._marque, self._modele))

class Moto(Véhicule):
    def __init__(self, marque, modele, annee, prix) -> None:
        Véhicule.__init__(self, marque, modele, annee, prix)
        self.__roue = 2

    def informationsVehicule(self):
        print("Marque du Véhicule : {}".format(self._marque))
        print("Modèle du Véhicule : {}".format(self._modele))
        print("Année : {}".format(self._annee))
        print("Prix : {} €".format(self._prix))
        print("Nombre de roue : {}".format(self.__roue))

    def demarrer(self):
        print("Attention, je roule en moto {} : {}".format(self._marque, self._modele))
voiture = Véhicule("Renault","Clio" ,1989, 17300)
voiture.informationsVehicule()
# voiture = Voiture("Renault", 1989, 17300)
# voiture.informationsVehicule()
moto = Moto("Yamaha", "1200 Vmax", 1987, 4500)
moto.informationsVehicule()
moto.demarrer()