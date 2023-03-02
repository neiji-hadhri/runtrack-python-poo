class Tache : 
    def __init__(self, titre, description, statut) -> None:
        self.titre = titre
        self.description = description
        self.statut = statut 

class ListeDeTaches:
    def __init__(self, taches) -> None:
        self.taches = taches

    def ajouterTache(self):
        ajout_tache = input("Ajouter une taches : ")

        
               