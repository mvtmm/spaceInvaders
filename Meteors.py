from Explosion import Explosion
from random import randint
from Objects import IObjects
from Assettype import AssetType
from Assetloader import Assetloader
import random
import pygame
# Meteor1


class MeteorItemObject(IObjects):

    def __init__(self, game):
        # X Koordinate des Items
        self.item_X = 0
        # Y Koordinate des Items
        self.item_Y = 0
        # Das Item als Bild
        self.item = None
        # Das Item als Rect
        self.itemRect = None
        # Zufällige Geschwindigkeiten
        self.item_Speed = random.randint(1, 4)
        # Zugriffsvariable
        self.game = game
        # RandomMeteorImg
        self.randomMeteorImg = randint(1, 10)

    # Override der Draw Methode
    def draw(self):
        # Item bewegen
        self.moveItemRect()

    # Override der Update Methode
    def update(self):
        # Item Rect erzeugen
        if self.item is None:
            self.item = Assetloader.getAsset(
                AssetType.Items, "Meteor_" + str(self.randomMeteorImg) + ".png")
            self.item = pygame.transform.scale(self.item, (80, 80))
        self.itemRect = self.getItemRect()

    # Override der Item eingesammelt Methode
    def trigger(self):
        self.game.game.player.decreaseHealth(15)
        self.game.game.object.removeObject(self)
        self.createExplosion()
        self.game.game.player.increaseScore(15)

    def projectileTrigger(self):
        self.game.game.object.removeObject(self)
        self.createExplosion()

    def createExplosion(self):
        explosion = Explosion(self.itemRect[0] + 40, self.item_Y + 40)
        self.game.game.animations_Explosions.add(explosion)
