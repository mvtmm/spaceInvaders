from Level import *
from LocalEnemys import *
from Enemys import *


class Levelmanager:


    # Initialisieren
    def __init__(self, game):
        self.game                       = game
        self.level                      = None
        

    def loadLevel(self, _level: ILevel):
        self.level = _level
        self.level.load()
        # Schwarzer Hintergrund
        self.game.screen.blit(self.getBackground(),(0,0))

    def getBackground(self):
        return self.level.background()

    # Level wechseln, sobald keine Enemys mehr da sind
    def update(self):
        if self.game.enemys.getObjects() == []:
            self.loadLevel(Level2(self.game))
            