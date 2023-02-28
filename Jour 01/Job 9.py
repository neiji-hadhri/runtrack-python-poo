class Produit : 
    def __init__(self, nom, prixHT, TVA) :
        self.nom = nom
        self.HT = prixHT
        self.TVA = TVA
    
    def CalculerPrixTTC(self,) : 
        self.TVA = self.HT * (self.TVA / 100)
        self.TCC = self.HT + self.TVA 
        print("Le prix TTC du produit suivant : {} est de {} €".format(self.nom, self.TCC))

    def changer_Nom(self,nouveau_nom):
        ancien_nom = self.nom
        self.nom = nouveau_nom
        print("Vous avez changer le produit: {},  par:{} ".format(ancien_nom, self.nom))

    def changer_Prix(self,nouveau_prix):
        ancien_prix = self.HT
        self.HT = nouveau_prix
        print("Le prix de : {} est de : {} €".format(self.nom, ancien_prix))

pro = Produit("stylo", 3, 20)
pro.CalculerPrixTTC()
pro.changer_Nom("crayon")
pro.changer_Prix(1)
pro = Produit("ordinateur", 400, 30)
pro.CalculerPrixTTC()
pro.changer_Nom("téléphone")
pro.changer_Prix(600)
pro = Produit("canapé", 1200, 10)
pro.CalculerPrixTTC()
pro.changer_Nom("lit")
pro.changer_Prix(900)
pro = Produit("voiture", 2100, 5)
pro.CalculerPrixTTC()
pro.changer_Nom("moto")
pro.changer_Prix(1500)