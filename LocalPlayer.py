from assetloader import *
from playership import IShip

class LocalPlayer:

    def __init__(self, game, x, y, ship: IShip):
        self.x = x
        self.game = game
        self.y = y
        self.ship = ship
        self.health = 100

    def decreaseHealth(self, amount):
        self.health -amount

    def increaseHealth(self, amount):
        self.health +amount

    def switchShip(self, ship: IShip):
        self.ship = ship

    def draw(self):
        self.ship.draw(self)
        self.ship.drawHealthBar(self)

    

    

  
   





    





        