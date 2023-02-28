class Point : 
    def __init__(self, x, y) :
        self.horizental = x 
        self.vertical = y 

    def afficherLesPoints(self):
        print("coordonnées horizental(x) =  {}".format(self.horizental))
        print("coordonnées vertical(y) =  {}".format(self.vertical))
    
    def afficherX(self):
        print("Valeur de X = {}".format(self.horizental))
    def afficherY(self):
        print("Valeur de Y = {}".format(self.vertical))

    def changerX(self, nouveauX):
        ancienX = self.horizental
        self.horizental = nouveauX
        print("Vous avez modifié {} par la valeur {} ".format(ancienX, self.horizental))

    def changerY(self, nouveauY):
        ancienY = self.vertical
        self.horizental = nouveauY
        print("Vous avez modifié {} par la valeur {} ".format(ancienY, self.horizental))
Po = Point(400, 100)
Po.afficherLesPoints()
Po.afficherX()
Po.afficherY()
Po.changerX(200)
Po.changerY(50)