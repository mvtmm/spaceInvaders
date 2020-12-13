from assettype import AssetType
from assetloader import Assetloader
import pygame
import random


class IEnemyShip:

    
    def __init__(self, game):
        # X Koordinate des Enemy
        self.Ship_X = 0
        # Y Koordinate des Enemy
        self.Ship_Y = 0
        # Enemy als Bild
        self.Ship = None
        # Enemy als Rect
        self.ShipRect = None
        # Zugriffsvariable 
        self.game = game
        # Zählervariable
        self.move_counter = 0
        # Enemybewegung auf x-Achse bei positivem Wert nach rechts, bei negativem Wert nach links
        self.move_direction_x = 1
        # Enemybewegung auf y-Achse 
        self.move_direction_y = 25
        

    # Methode zum Zeichnen der Enemys
    def draw(self):
        self.moveShipRect()

    # Methode zum Updaten der Enemys
    def update(self):
        pass

    # Enemys als Rect
    def getShipRect(self):
        self.ShipRect = pygame.Rect(self.Ship_X, self.Ship_Y, 30, 30)
        return self.ShipRect

    # Methode zum Bewegen der Enemys
    def moveShipRect(self):
        # Asset um 90 Grad drehen
        self.Ship = pygame.transform.rotate(self.Ship, -90)
        # Asset runterskalieren auf 100x100 Pixel
        self.Ship = pygame.transform.scale(self.Ship, (100, 100))
        
        # Ship von links nach rechts bewegen & nach unten 
        self.Ship_X  += self.move_direction_x
        self.move_counter += 1
        if abs(self.move_counter) > 500:
            self.move_direction_x *= -1
            self.Ship_Y += self.move_direction_y
            self.move_counter = 0
            #self.move_counter = self.move_direction_x * self.move_direction_x
        
        # Enemys auf Bildschirm zeichnen
        self.game.screen.blit(self.Ship, self.ShipRect)

        


class Enemy_One(IEnemyShip):
    def __init__(self, game, row, cell):
        self.Ship_X = (40 * row)
        self.Ship_Y = (70 * cell)
        self.Ship_Row = row
        self.Ship_Cell = cell
        self.Ship = None
        self.ShipRect = None 
        self.game = game
        self.move_counter = 0
        self.move_direction_x = 1
        self.move_direction_y = 25
        
    # Override der Update Methode
    def update(self):
        # Ship Rect erzeugen
        self.Ship = Assetloader.getAsset(AssetType.Graphics, "Ship2.png")
        self.ShipRect = self.getShipRect()