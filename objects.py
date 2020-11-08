from assettype import AssetType
from assetloader import Assetloader
import pygame
import random


class IObjects:

    def __init__(self, game):
        self.item_x = 0
        self.item_y = 0
        self.item = None
        self.positionrandom = random.randint(0, 2)
        self.item_angle = 0
        self.item_speed = random.randint(1, 4)
        self.game = game

    def draw(self):
        pass

    def getItemRect(self):
        if (self.item_x == 0 and self.item_y == 0):

            if(self.positionrandom == 0):
                self.itemrect = self.game.screen.get_rect()
                self.itemrect = self.itemrect.topleft
            elif (self.positionrandom == 1):
                self.itemrect = self.game.screen.get_rect()
                self.itemrect = self.itemrect.midtop
            elif (self.positionrandom == 2):
                self.itemrect = (self.game.width - 50, self.item_y)
        else:
            self.itemrect = (self.itemrect[0], self.item_y)

        return self.itemrect

    def moveItemRect(self):
        self.item_angle = self.item_angle + 1
        self.item_y     = self.item_y + self.item_speed

class ArmorItemObject(IObjects):

    def draw(self):

        self.item = Assetloader.getAsset(AssetType.Items, "Armor_Bonus.png")
        self.item = pygame.transform.rotate(self.item, self.item_angle)
        self.item = pygame.transform.scale(self.item, (50, 50))

        self.itemrect = self.getItemRect()

        self.game.screen.blit(self.item, self.itemrect)
        self.moveItemRect()
   

class HealthItemObject(IObjects):

    def draw(self):

        self.item = Assetloader.getAsset(AssetType.Items, "HP_Bonus.png")
        self.item = pygame.transform.rotate(self.item, self.item_angle)
        self.item = pygame.transform.scale(self.item, (50, 50))

        self.itemrect = self.getItemRect()
        self.game.screen.blit(self.item, self.itemrect)
        self.moveItemRect()


class DamageBoostItemObject(IObjects):

    def draw(self):

        self.item = Assetloader.getAsset(AssetType.Items, "Damage_Bonus.png")
        self.item = pygame.transform.rotate(self.item, self.item_angle)
        self.item = pygame.transform.scale(self.item, (50, 50))

        self.itemrect = self.getItemRect()
        
        self.game.screen.blit(self.item, self.itemrect)
        self.moveItemRect()
