class Personne:
    def __init__(self, age = 14 ) -> None:
        self._age = int(age)
    
    def get_age(self):
        return self._age
    
    def afficherAge(self):
        print(self._age, "ans")
    
    def bonjour(self):
        print("Hello")
        
    def ModifierAge(self,nouvelle_age):
        print("L'âge de {} ans a été modifié par {} ans".format(self._age, nouvelle_age))

class Eleve(Personne) :
    def allerEnCours (self):
        print("Je vais en cours")

    def affichageAge(self,age):
        print("J'ai {} ans".format(age))

class Professeur(Personne):
    def __init__(self, matiereEnseignée, age ) -> None:
        Personne.__init__(self, age)
        self.__matiere = matiereEnseignée


    def enseigner(self): 
        print("Le cours va commencer")
        
    def pasimportant(self):
        print("le professeur de {} a {} ans".format(self.__matiere, self._age))
Per = Personne(12)
Per.bonjour()
Per.afficherAge()
Per.ModifierAge(17)
Per = Eleve(13)
Per.allerEnCours()
Per.affichageAge(12)
Per = Professeur("mathematique" , 37)
Per.enseigner()
Per.pasimportant()