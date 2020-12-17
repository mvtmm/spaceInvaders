from assetloader import *
from enemys import IEnemyShip
from Weapons import *

class LocalEnemys:

    # Initialisieren
    def __init__(self, game):
        self.game               = game
        self.game.EnemyBundleObjects = []
        # Array der Schüsse der Gegner
        self.ProjectileObjects   = []

    # Fügt dem Array ein neues Objekt hinzu
    def addObjectBundle(self, object: IEnemyShip):
        self.game.EnemyBundleObjects.append(object)

    # Entfernt aus dem Array ein Objekt
    def removeObject(self, object: IEnemyShip):
        self.game.EnemyBundleObjects.remove(object)
    
    # Liefert alle Objekte zurück
    def getObjects(self):
        return self.game.EnemyBundleObjects
    
    def createShoots(self):
        if len(self.getProjectileObjects()) < 5:
            for _object in self.game.EnemyBundleObjects:
                if len(self.getProjectileObjects()) < 5:
                    self.game.Enemys.EnemyShoot(ProjectileWeapon(self.game, 90, 1, _object.Ship_X,_object.Ship_Y))

    # Zeichnet alle Objekte aus dem Array 
    def draw(self):
       
        for _object in self.ProjectileObjects:
            _object.draw()
    
        for _object in self.game.EnemyBundleObjects:
            _object.draw()

        self.createShoots()


    # Gibt alle Projectile zurück
    def getProjectileObjects(self):
        return self.ProjectileObjects

    # Gegner schießt
    def EnemyShoot(self, object: IWeapon):
        self.ProjectileObjects.append(object)

    # Gegner Projectile entfernen
    def RemoveEnemyShoot(self, object: IWeapon):
        if object in self.ProjectileObjects:
            self.ProjectileObjects.remove(object)

    # Update alle Objekte aus dem Array 
    def update(self):
        for _object in self.ProjectileObjects:
            _object.update()

        for _object in self.game.EnemyBundleObjects:
            _object.update()
