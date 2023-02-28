class Personne :
    def __init__(self, nom, prenom) :
        self.nom = nom
        self.prenom = prenom
    def SePresenter(self):
        print("je suis {} {}".format(self.nom, self.prenom))

per = Personne("John","Doe")
per.SePresenter()       
per = Personne("Jean","Dupond")
per.SePresenter()