from Level import *
from LocalEnemys import *
from enemys import *


class Levelmanager:


    # Initialisieren
    def __init__(self, game):
        self.game                       = game
        self.Level                      = None
        

    def loadLevel(self, _level: ILevel):
        self.Level = _level
        self.Level.load()

    # Level wechseln, sobald keine Enemys mehr da sind
    def update(self):
        if self.game.Enemys.getObjects() == []:
            self.loadLevel(Level2(self.game))