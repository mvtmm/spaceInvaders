from assetloader import *
from playership import IShip

class LocalPlayer:
    # Init
    def __init__(self, game, x, y, ship: IShip):
        # Spieler X Koordinate
        self.PlayerX = x
        # Zugriffsvariable
        self.game = game
        # Spieler Y Koordinate
        self.PlayerY = y
        # Spielerschiff Objekt
        self.PlayerShip = ship(self)
        # Spieler Leben
        self.PlayerHealth = 100
        # Spieler Schilde
        self.PlayerShield = 0
        

    # Leben verringern Methode
    def decreaseHealth(self, amount):
        if self.PlayerShield >= 0:
            self.decreaseArmor()
        else:
            self.PlayerHealth -= amount
        
    # Leben erhöhen Methode
    def increaseHealth(self, amount):
        # Neues Leben addieren
        # Überprüfen ob mit dem neuem Wert das Leben über 100 kommt
        if (self.PlayerHealth + amount) >= 100:
            # Über 100 Leben gleichsetzen mit Leben 100
            self.PlayerHealth = 100
        else:
            self.PlayerHealth += amount

    # Schild verringern Methode
    def decreaseArmor(self):
        # Schild entfernen
        # Maximal 3 Schilde
        if self.PlayerShield != 0:
            self.PlayerShield -= 1
        
    # Schild erhöhen Methode
    def increaseArmor(self):
        # Neues Schild hinzufügen
        # Maximal 3 Schilde
        if self.PlayerShield != 3:
            self.PlayerShield += 1
     
    # Schiff wechseln Methode
    def switchShip(self, ship: IShip):
        # Schiff wechseln
        self.ship = ship

    # Zeichnen Methode
    def draw(self):
        # Spielerschiff zeichnen
        self.PlayerShip.draw()
        # Spielerlebensbalken zeichnen
        self.PlayerShip.drawHealthBar()
        # Spieler Rüstung zeichnen
        self.PlayerShip.drawArmorBar()
    

    

  
   





    





        