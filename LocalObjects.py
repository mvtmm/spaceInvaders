from assetloader import *
from objects import IObjects

class LocalObjects:

    # Initialisieren
    def __init__(self, game):
        self.game               = game
        self.game.GameObjects   = []

    # Fügt dem Array ein neues Objekt hinzu
    def addObject(self, object: IObjects):
        self.game.GameObjects.append(object)

    # Entfernt aus dem Array ein Objekt
    def removeObject(self, object: IObjects):
        self.game.GameObjects.remove(object)
    
    # Liefert alle Objekte zurück
    def getObjects(self):
        return self.game.GameObjects
    
    # Zeichnet alle Objekte aus dem Array 
    def draw(self):
        for _object in self.game.GameObjects:
            _object.draw()

    # Update alle Objekte aus dem Array 
    def update(self):
        for _object in self.game.GameObjects:
            _object.update()