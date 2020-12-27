from Weapons import *
from Assetloader import *
from Playership import IShip

class LocalPlayer:
    # Init
    def __init__(self, game, x, y, ship: IShip, weapon: IWeapon):
        # Spieler X Koordinate
        self.playerX = x
        # Zugriffsvariable
        self.game = game
        # Spieler Y Koordinate
        self.playerY = y
        # Spielerschiff Objekt
        self.playerShip = ship(self)
        # Spielerschiff Waffe
        self.playerShipWeapon = weapon(self, -90, 0, 0, 0)
        # Spieler Leben
        self.playerHealth = 100
        # Spieler Schilde
        self.playerShield = 0
        # Array der Schüsse des Spielers 
        self.projectileObjects   = []

    # Leben verringern Methode
    def decreaseHealth(self, amount):
        if self.playerShield > 0:
            self.decreaseArmor()
        else:
            self.playerHealth -= amount
        
    # Leben erhöhen Methode
    def increaseHealth(self, amount):
        # Neues Leben addieren
        # Überprüfen ob mit dem neuem Wert das Leben über 100 kommt
        if (self.playerHealth + amount) >= 100:
            # Über 100 Leben gleichsetzen mit Leben 100
            self.playerHealth = 100
        else:
            self.playerHealth += amount

    # Schild verringern Methode
    def decreaseArmor(self):
        # Schild entfernen
        # Maximal 3 Schilde
        if self.playerShield != 0:
            self.playerShield -= 1
        
    # Schild erhöhen Methode
    def increaseArmor(self):
        # Neues Schild hinzufügen
        # Maximal 3 Schilde
        if self.playerShield != 3:
            self.playerShield += 1
     
    # Schiff wechseln Methode
    def switchShip(self, ship: IShip):
        # Schiff wechseln
        self.ship = ship

    # Waffe wechseln Methode
    def switchWeapon(self, weapon: IWeapon):
        # Waffe wechseln
        self.playerShipWeapon = weapon

    # Zeichnen Methode
    def draw(self):
        # Spielerschiff zeichnen
        self.playerShip.draw()
        # Spielerlebensbalken zeichnen
        self.playerShip.drawHealthBar()
        # Spieler Rüstung zeichnen
        self.playerShip.drawArmorBar()

        for _object in self.projectileObjects:
            _object.draw()
    
    # Gibt alle Projectile zurück
    def getProjectileObjects(self):
        return self.projectileObjects

    # Spieler schießt
    def PlayerShoot(self, object: IWeapon):
        self.projectileObjects.append(object)

    # Spieler Projectile entfernen
    def RemovePlayerShoot(self, object: IWeapon):
        if object in self.projectileObjects:
            self.projectileObjects.remove(object)

    # Update Methode
    def update(self):
        for _object in self.projectileObjects:
            _object.update()

   


    

  
   





    





        