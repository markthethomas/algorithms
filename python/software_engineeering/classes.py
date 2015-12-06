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

Bulbasaur = Pokemon('bulbasaur', 100, 20)

Pikachu = Pokemon('Pikachu', 100, 20)

Bulbasaur.attack(, 'floober')