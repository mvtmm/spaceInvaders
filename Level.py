from enemys import *
from objects import * 
from Meteors import *
from LocalEnemys import *

class ILevel:

    def __init__(self, game):
        # Zugriffsvariable 
        self.game = game


class Level1(ILevel):
    def __init__(self, game):
        self.game = game

    def load(self):

        self.game.Enemys.addObjectBundle(Enemy_One(self, 3, 0))
        self.game.Enemys.addObjectBundle(Enemy_One(self, 3, 1))

        

class Level2(ILevel):

    def __init__(self, game):
        self.game = game

    def load(self):
        self.game.Enemys.addObjectBundle(Enemy_One(self, 3, 0))
        self.game.Enemys.addObjectBundle(Enemy_One(self, 3, 1))
        self.game.Enemys.addObjectBundle(Enemy_One(self, 3,  2))

       