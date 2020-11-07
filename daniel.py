from assettype import AssetType
from assetloader import Assetloader
import pygame

class IEnemyShip():

    speed = 2
    def draw(self, x, y):
        pass
    def shoot(self, x, y):
        pass

class Enemy_One(IEnemyShip):
    speed = 2
    def draw(self, game, x, y):
        ship = Assetloader.getAsset(AssetType.Graphics, "Ship2.png")
        ship = pygame.transform.rotate(ship, -90)

        game.screen.blit(ship, (x,y))

    def shoot(self, x, y):
        pass    