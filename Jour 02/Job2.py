class Livre :
    def __init__(self, titre, auteur, nombre_pages) :
        self.__titre = titre
        self.__auteur = auteur
        self.__pages = nombre_pages

    def get_titre(self):
        return self.__titre
    
    def get_auteur(self):
        return self.__auteur

    def get_pages(self): 
        return self.__pages
    
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
            
            
Li = Livre("La gloire de mon père", "Marcel Pagnol", 200 )
if Li.get_pages() > 0:
    print("Le livre '{}' écrit par {} contient {} pages".format(Li.get_titre(), Li.get_auteur(), Li.get_pages()))
Li.set_pages(-56)
if Li.get_pages() > 0:
    print("Le livre '{}' écrit par {} contient {} pages".format(Li.get_titre(), Li.get_auteur(), Li.get_pages()))