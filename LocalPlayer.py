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

    # Leben verringern Methode
    def decreaseHealth(self, amount):
        # Neues Leben abziehen
        self.health -amount
        
    # Leben erhöhen Methode
    def increaseHealth(self, amount):
        # Neues Leben addieren
        self.health +amount

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

    

    

  
   





    





        