from assetloader import *
from objects import IObjects

class LocalObjects:

    def __init__(self, game):
        self.game               = game
        self.game.GameObjects   = []
    
    def addObject(self, object: IObjects):
        self.game.GameObjects.append(object)

    def removeObject(self, object: IObjects):
        self.game.GameObjects.remove(object)

    def draw(self):
        for _object in self.game.GameObjects:
            _object.draw()