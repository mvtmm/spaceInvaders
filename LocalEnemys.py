from assetloader import *
from enemys import IEnemyShip

class LocalEnemys:

    # Initialisieren
    def __init__(self, game):
        self.game               = game
        self.game.EnemyBundleObjects = []

    # Fügt dem Array ein neues Objekt hinzu
    def addObjectBundle(self, object: IEnemyShip):
        self.game.EnemyBundleObjects.append(object)

    # Entfernt aus dem Array ein Objekt
    def removeObject(self, object: IEnemyShip):
        self.game.EnemyBundleObjects.remove(object)
    
    # Liefert alle Objekte zurück
    def getObjects(self):
        return self.game.EnemyBundleObjects
    
    # Zeichnet alle Objekte aus dem Array 
    def draw(self):
        for _object in self.game.EnemyBundleObjects:
            _object.draw()

    # Update alle Objekte aus dem Array 
    def update(self):
        for _object in self.game.EnemyBundleObjects:
            _object.update()
#basti_stinkt