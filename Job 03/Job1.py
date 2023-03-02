class Ville : 
    def __init__(self, nom, nombre_habitant) -> None:
        self.__nom = nom 
        self.__habitant = nombre_habitant

    def get_nom(self):
        return self.__nom

    def get_habitant(self):
        return self.__habitant

class Personne : 
    def __init__(self, nomP, age, objet_ville) -> None:
        self.__nomP = nomP
        self.__age = age
        self.__ville = objet_ville

    def get_nomP(self):
        return self.__nomP
    
    def get_age(self):
        return self.__age
    
    def get_ville(self):
        return self.__ville
    
    
    def ajouter_Population(self) :
        self.__ville._Ville__habitant += 1
    

Vil = Ville("Paris", 1000000)
print("Population de la ville de {} : {} habitants".format(Vil.get_nom(), Vil.get_habitant()))

Vil2 = Ville("Marseille", 861635)
print("Population de la ville de {} : {} habitants".format(Vil2.get_nom(), Vil2.get_habitant()))

Per = Personne("John", 45, Vil)
Per.ajouter_Population()

Per1 = Personne("Myrtille", 4, Vil)
Per.ajouter_Population()
print("Mise à jour de la population de la ville de {} : {} habitants".format(Vil.get_nom(), Vil.get_habitant() ))

Per2 = Personne("Chloé", 18 , Vil2)

Per2.ajouter_Population()

print("Mise à jour de la population de la ville de {} : {} habitants".format(Vil2.get_nom(), Vil2.get_habitant() ))
print("Population de la ville de {} après mise à jour : {} habitants".format(Vil.get_nom(), Vil.get_habitant()))
print("Population de la ville de {} après mise à jour : {} habitants".format(Vil2.get_nom(), Vil2.get_habitant()))