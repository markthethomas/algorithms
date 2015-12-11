"""
Practicing with classes and inheritance in Python, using Pokemon.
"""
class Pokemon(object):
    """docstring for Pokemon"""
    def __init__(self, name, hp, level):
        super(Pokemon, self).__init__()
        self.name = name
        self.hp = hp
        self.level = level
    def attack(self, target, move):
        print('{name} is attacking {target} with {move}!'.format(name=self.name, target=target, move=move))

class Water(Pokemon):
    """docstring for Water"""
    # def __init__(self):
    #     super(Water, self).__init__()


Bulbasaur = Pokemon('bulbasaur', 100, 20)

Pikachu = Pokemon('Pikachu', 100, 20)

Bulbasaur.attack('Mark', 'floober')