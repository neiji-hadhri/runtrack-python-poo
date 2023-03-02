class CompteBancaire :
    def __init__(self, numero_de_compte, nom, prenom, solde) -> None:
        self.__num = numero_de_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__découvert = False
    def get_num (self) :
        return self.__num 

    def get_nom (self) :
        return self.__nom 

    def get_prenom (self) :
        return self.__prenom 
    
    def get_solde (self):
        return self.__solde     

        
    def afficher(self) :


        print("Détail du compte")
        print("Numéro du compte : {}".format(self.__num))
        print("Nom : {}".format(self.__nom))
        print("Prénom : {}".format(self.__prenom))
        if self.__découvert:
            print("Vous avez le droit à un découvert ".format(self.__solde))
        else :
            print("Vous n'avez pas le droit à un découvert")
        

    def afficherSolde(self):
        print("Solde du compte : {} €".format(self.__solde))

    def versement(self, versement):
        self.__solde += versement
        print("Après versement votre compte contient : {} €".format(self.__solde))
    
    def retrait(self,retrait):


        if self.__découvert:
            self.__solde = self.__solde - retrait
            print("Vous avez retiré {} €".format(retrait))
            print("Votre compte contient : {} €".format(self.__solde))

        else :
            print("vous ne pouvez pas faire de retrait tant que votre compte est à découvert")
    


    def agios(self):
        if self.__découvert :
            print("Vous n'avez pas de frais à payer" )

        else:
            
            print("Vous avez 1 mois pour rembouser votre pret fait à la banque,si vous le faites pas, la banque vous prélèvera 35 € " )
            self.__solde = self.__solde - 35

            print("Votre compte contient {} €".format(self.__solde))
            print("Vous avez  2 semaines pour rembouser votre pret fait à la banque,si vous le faites pas, la banque vous prélèvera 40 €" )
            self.__solde = self.__solde - 40

            print("Votre compte contient {} €".format(self.__solde))
            print("Vous avez  1 semaine et 2 jours pour rembouser votre pret fait à la banque,si vous le faites pas, la banque vous prélèvera 60 €" )
            self.__solde = self.__solde - 60

            print("Votre compte contient {} €".format(self.__solde))



    def virement(self,compte_recevant_le_virement, montant):
        self.__solde = self.__solde - montant 
        
        if montant > self.__solde :
            print("Vous n'avez pas assez d'argent sur votre compte pour envoyer cette somme")
        else:
            print("Le compte numéro° {} au nom de {} a envoyé {} € à {}".format(self.__num, self.__nom, montant, compte_recevant_le_virement))
            print("Votre compte bancaire contient désormais {} €".format(self.__solde) )
            


CB = CompteBancaire(1232, "HADHRI", "Neiji", 3000)
CB.afficher()
CB.afficherSolde()
CB.versement(12)
CB.retrait(14)
CB.agios()
CB.virement(1345, 1000)
"""supprimer les "#" pour voir le CB1 """
#CB1 = CompteBancaire(1345 , "Alisson", "Joe", -300)
#CB1.afficher()
#CB1.afficherSolde()
#CB1.versement(512)
#CB1.retrait(14)
#CB1.agios()

