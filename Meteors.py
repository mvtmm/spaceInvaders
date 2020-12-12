from random import randint
from objects import IObjects
from assettype import AssetType
from assetloader import Assetloader
import random
# Meteor1
class MeteorItemObject(IObjects):

    
    def __init__(self, game):
        # X Koordinate des Items
        self.Item_X = 0
        # Y Koordinate des Items
        self.Item_Y = 0
        # Das Item als Bild
        self.Item = None
        # Das Item als Rect
        self.ItemRect = None
        # Item Ausrichtung
        self.Item_Angle = 0
        # Zufällige Geschwindigkeiten
        self.Item_Speed = random.randint(1, 4)
        # Zugriffsvariable 
        self.game = game
        # RandomMeteorImg
        self.RandomMeteorImg = randint(1,10)

    # Override der Draw Methode
    def draw(self):
        # Item bewegen
        self.moveItemRect()

    # Override der Update Methode
    def update(self):
        # Item Rect erzeugen
        
        self.Item = Assetloader.getAsset(AssetType.Items, "Meteor_" + str(self.RandomMeteorImg) + ".png")
        self.ItemRect = self.getItemRect()   
 
    # Override der Item eingesammelt Methode
    def trigger(self):
        self.game.Player.decreaseHealth(15)
