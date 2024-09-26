from random import randint

class Die():
    """Uma classe que representa um único dado"""

    def __init__(self, num_sides = 6):
        """Supõe que um dado seja de 6 lados"""
        self.num_sides = num_sides

    def roll(self):
        """Devolve um valor aleatório entre 1 e o número de lados"""
        return(randint(1, self.num_sides))
    
