from assettype import AssetType
from assetloader import Assetloader
import pygame

class IShip():

    speed = 2
    def draw(self):
        pass
    def shoot(self):
        pass

    def drawHealthBar(self):
        if self.health < 0:
            health = 0

        # Füllstand berechnen
        innerrect       = pygame.Rect(self.x - 20, self.y -5, (self.health / 100) * 100, 5)
        border_rect     = pygame.Rect(self.x - 20, self.y -5, 100, 5)
            
        pygame.draw.rect(self.game.screen, (255,   0,   0), innerrect)
        pygame.draw.rect(self.game.screen, (255, 255, 255), border_rect, 2)


class Ship_One(IShip):
    speed = 2
    def draw(self):
        playership = Assetloader.getAsset(AssetType.Graphics, "Ship1.png")
        playership = pygame.transform.rotate(playership, 90)
        self.game.screen.blit(playership, (self.x, self.y -80))
    def shoot(self):
        pass
    

class Ship_Two(IShip):
    speed = 4
    def draw(self):
        playership = Assetloader.getAsset(AssetType.Graphics, "Ship2.png")
        playership = pygame.transform.rotate(playership, 90)
        self.screen.blit(playership, (self.x, self.y -80))
    def shoot(self):
        pass

class Ship_Three(IShip):
    speed = 6
    def draw(self):
        playership = Assetloader.getAsset(AssetType.Graphics, "Ship3.png")
        playership = pygame.transform.rotate(playership, 90)
        self.screen.blit(playership, (self.x, self.y -80))
    def shoot(self):
        pass
class Ship_Four(IShip):
    speed = 8
    def draw(self):
        playership = Assetloader.getAsset(AssetType.Graphics, "Ship4.png")
        playership = pygame.transform.rotate(playership, 90)
        self.screen.blit(playership, (self.x, self.y -80))
    def shoot(self):
        pass
class Ship_Five(IShip):
    speed = 10
    def draw(self):
        playership = Assetloader.getAsset(AssetType.Graphics, "Ship5.png")
        playership = pygame.transform.rotate(playership, 90)
        self.screen.blit(playership, (self.x, self.y -80))
    def shoot(self):
        pass
class Ship_Six(IShip):
    speed = 12
    def draw(self):
        playership = Assetloader.getAsset(AssetType.Graphics, "Ship6.png")
        playership = pygame.transform.rotate(playership, 90)
        self.screen.blit(playership, (self.x, self.y -80))
    def shoot(self):
        pass