from assetloader import *
from enemys import IEnemyShip

class LocalEnemys:

    # Initialisieren
    def __init__(self, game):
        self.game               = game
        self.game.EnemyObjects   = []

    # Fügt dem Array ein neues Objekt hinzu
    def addObject(self, object: IEnemyShip):
        self.game.EnemyObjects.append(object)

    # Entfernt aus dem Array ein Objekt
    def removeObject(self, object: IEnemyShip):
        self.game.EnemyObjects.remove(object)
    
    # Liefert alle Objekte zurück
    def getObjects(self):
        return self.game.EnemyObjects
    
    # Zeichnet alle Objekte aus dem Array 
    def draw(self):
        for _object in self.game.EnemyObjects:
            _object.draw()

    # Update alle Objekte aus dem Array 
    def update(self):
        for _object in self.game.EnemyObjects:
            _object.update()