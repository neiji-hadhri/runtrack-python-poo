class Animal:
    def __init__(self) :
        self.age = 0
        self.prenom = ""

    def vieillir(self):
         self.age+=1
    
    def nommer(self):
        self.prenom = "Luna"

Ani = Animal() 
Ani.nommer()
print("L'animal se nomme {} ".format(Ani.prenom))
print("L'age de l'animal {} ans ".format(Ani.age))

Ani.vieillir()

print("L'age de l'animal {} ans".format(Ani.age))

Ani.vieillir()

print("L'age de l'animal {} ans".format(Ani.age))

     