class Cercle : 
    def __init__(self, rayon) :
        self.rayon = rayon 

    def changerRayon(self, nouveau_rayon) : 
        ancien_rayon = self.rayon
        self.rayon = nouveau_rayon
        print("Vous avez modifié le rayon {} par {} ".format(ancien_rayon, self.rayon))
        
    def afficherInfos(self, couleur_infos):
        self.infos = couleur_infos
        print("Information à savoir : Couleur : {}".format(self.infos))
        print("Rayon du cercle : {}".format(self.rayon))

    def circonférence(self) : 
        self.circonférence = self.rayon * 2
        self.circonférence = self.circonférence * 3.14
        print("la circonférence du cercle est de {}".format(self.circonférence))

    def aire(self):
        self.aire = self.rayon * self.rayon
        self.aire = self.aire * 3.14 
        print("L'air du cercle est de : {} cm²".format(self.aire))

    def diametre(self):
        self.diametre = self.rayon * 2
        print("Le diamtètre du cercle est de {} cm".format(self.diametre))





cer = Cercle(10)
cer.changerRayon(4)
cer.afficherInfos("rouge")
cer.circonférence()
cer.aire()
cer.diametre()
print("--------------------------------------------------------------------")
print("Cercle 2")
print("^", "^", "^")
print("|", "|", "|")
print("--------------------------------------------------------------------")
cer = Cercle(4)
cer.changerRayon(7)
cer.afficherInfos("vert")
cer.circonférence()
cer.aire()
cer.diametre()