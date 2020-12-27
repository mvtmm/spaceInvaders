from Assetloader import *
from Enemys import IEnemyShip
from Weapons import *
import random

class LocalEnemys:

    # Initialisieren
    def __init__(self, game):
        self.game               = game
        self.game.enemyBundleObjects = []
        # Array der Schüsse der Gegner
        self.projectileObjects   = []

    # Fügt dem Array ein neues Objekt hinzu
    def addObjectBundle(self, object: IEnemyShip):
        self.game.enemyBundleObjects.append(object)

    # Entfernt aus dem Array ein Objekt
    def removeObject(self, object: IEnemyShip):
        self.game.enemyBundleObjects.remove(object)
    
    # Liefert alle Objekte zurück
    def getObjects(self):
        return self.game.enemyBundleObjects
    
    def createShoots(self):
        if len(self.getProjectileObjects()) < 10:
            for _object in self.game.enemyBundleObjects:
                #if len(self.getProjectileObjects()) < 5:
                    if random.randrange(0, 120) == 1:
                        self.game.enemys.EnemyShoot(ProjectileWeapon(self.game, 90, 1, _object.ship_X,_object.ship_Y))

    # Zeichnet alle Objekte aus dem Array 
    def draw(self):
       
        for _object in self.projectileObjects:
            _object.draw()
    
        for _object in self.game.enemyBundleObjects:
            _object.draw()

        self.createShoots()


    # Gibt alle Projectile zurück
    def getProjectileObjects(self):
        return self.projectileObjects

    # Gegner schießt
    def EnemyShoot(self, object: IWeapon):
        self.projectileObjects.append(object)

    # Gegner Projectile entfernen
    def RemoveEnemyShoot(self, object: IWeapon):
        if object in self.projectileObjects:
            self.projectileObjects.remove(object)

    # Update alle Objekte aus dem Array 
    def update(self):
        for _object in self.projectileObjects:
            _object.update()

        for _object in self.game.enemyBundleObjects:
            _object.update()
