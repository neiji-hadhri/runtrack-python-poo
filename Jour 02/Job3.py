class Livre :
    
    def __init__(self, titre, auteur, nombre_pages) :
        self.__titre = titre
        self.__auteur = auteur
        self.__pages = nombre_pages
        self.__disponible = True
    
    def get_titre(self):
        return self.__titre
    
    def get_auteur(self):
        return self.__auteur

    def get_pages(self): 
        return self.__pages
    
    def vérification(self): 
        if self.__disponible :
            return True
        else :
            return False

    def set_titre(self, nouveau_titre):
        self.__titre = nouveau_titre

    def set_auteur(self, nouveau_auteur):
        self.__auteur = nouveau_auteur
    
    def set_pages(self, nouvelles_pages):
        self.__pages = nouvelles_pages
        if nouvelles_pages > 0 :
            print(nouvelles_pages)
        else :
            print("ERREUR:Vous devez indiquez un nombre positif" )

    def emprunter(self):
        if not self.vérification():
            self.__disponible = True
            print("Le livre a été emprunter ")
        else:
            print("Le livre n'est pas disponible")
    
    def rendre(self):
        if  self.vérification():
            self.__disponible = False
            print("Le livre a été rendu ")
        else:
            print("Le livre est disponible")
            
      
            
Li = Livre("La gloire de mon père", "Marcel Pagnol", 200 )
print("Le livre '{}' écrit par {} contient {} pages".format(Li.get_titre(), Li.get_auteur(), Li.get_pages()))
print("Disponibilité : {}".format(Li.vérification()))
Li.emprunter()
Li.emprunter()
print("Disponibilité : {}".format(Li.vérification()))
Li.rendre()
Li.rendre()





