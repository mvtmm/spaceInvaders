from Assetloader import *
from Objects import IObjects

class LocalObjects:

    # Initialisieren
    def __init__(self, game):
        self.game               = game
        self.game.gameObjects   = []

    # Fügt dem Array ein neues Objekt hinzu
    def addObject(self, object: IObjects):
        self.game.gameObjects.append(object)

    # Entfernt aus dem Array ein Objekt
    def removeObject(self, object: IObjects):
        self.game.gameObjects.remove(object)
    
    # Liefert alle Objekte zurück
    def getObjects(self):
        return self.game.gameObjects
    
    # Zeichnet alle Objekte aus dem Array 
    def draw(self):
        for _object in self.game.gameObjects:
            _object.draw()

    # Update alle Objekte aus dem Array 
    def update(self):
        for _object in self.game.gameObjects:
            _object.update()