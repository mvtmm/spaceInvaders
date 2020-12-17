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
        # Schwarzer Hintergrund
        self.game.screen.blit(self.getBackground(),(0,0))

    def getBackground(self):
        return self.Level.background()

    # Level wechseln, sobald keine Enemys mehr da sind
    def update(self):
        if self.game.Enemys.getObjects() == []:
            self.loadLevel(Level2(self.game))
            