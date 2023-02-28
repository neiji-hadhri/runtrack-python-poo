class Personnage :
    def __init__(self) :
        self.x = 0
        self.y = 0
    
    def gauche(self):
        self.x= self.x - 1
    
    def droite(self):
        self.x= self.x + 1

    def haut(self):
        self.y= self.y + 1

    def bas(self):
        self.y= self.y - 1


    def position(self):
        print("(x={} , y={})".format(per.x, per.y))


per = Personnage()
per.gauche()
per.gauche()
per.gauche()
per.droite()
per.bas()
per.bas()
per.bas()
per.bas()
per.bas()
per.bas()
per.haut()
per.position()
