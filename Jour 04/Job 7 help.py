class Carte:
    def __init__(self,valeur,forme):
        self.cout = valeur
        self.valeur = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'][valeur-1]
        self.forme = '♥♦♣♠'[forme]
        
    def show(self):
        print('┌───────┐')
        print(f'| {self.valeur:<2}    |')
        print('|       |')
        print(f'|   {self.forme}   |')
        print('|       |')
        print(f'|    {self.valeur:>2} |')
        print('└───────┘') 

    def price(self):
        if self.cout >= 10:
            return 10
        elif self.cout == 1:
            return 11
        return self.cout
    random.choice

        