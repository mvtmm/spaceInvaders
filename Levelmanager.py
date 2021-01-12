from Level import *
from LocalEnemys import *
from Enemys import *


class Levelmanager:


    # Initialisieren
    def __init__(self, game):
        self.game                       = game
        self.level                      = Level1
    
    def getLevel(self):
        if self.level == Level1:
            return 1
        if self.level == Level2:
            return 2
        #if Level3: 
        #    return 3
        
        

    def loadLevel(self):
        self.level.load(self)
        # Schwarzer Hintergrund
        self.game.screen.blit(self.getBackground(),(0,0))

    def getBackground(self):
        return self.level.background(self)

    # Level wechseln, sobald keine Enemys mehr da sind
    def update(self):
        if self.game.enemys.getObjects() == [] and self.getLevel() == 1:
            self.level = Level2
            self.loadLevel()
        if self.game.enemys.getObjects() == [] and self.getLevel() == 2:
            self.level = Level3
            self.loadLevel()
            