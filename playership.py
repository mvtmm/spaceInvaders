from Weapons import IWeapon
from colors import ColorType
from assettype import AssetType
from assetloader import Assetloader
import pygame

# Interface Klasse Ship
class IShip:
    # Init
    def __init__(self, game):
        # Zugriffsvariable 
        self.game = game
        # Schiffspeed
        self.speed = 2
        # Spieler Schiff Rect
        self.PlayerShipRect = None
        # Spielershiff
        self.playership = None
        # Schild Item
        self.Schild = None

    # Zeichen Methode
    def draw(self):
        pass
  
    # Lebensbalken Methode
    def drawHealthBar(self):
        # Füllstand berechnen unterhalb des Spielerschiffes 
        innerrect       = pygame.Rect(self.game.PlayerX, self.game.PlayerY - 20, self.game.PlayerHealth / 100 * self.PlayerShipRectSize[1]  , 5)
        # Rand um den Füllstand berechnen unterhalb des Spielerschiffes 
        border_rect     = pygame.Rect(self.game.PlayerX, self.game.PlayerY - 20, self.PlayerShipRectSize[1] , 5)
        # Zeichnen des Lebensbalkens
        pygame.draw.rect(self.game.game.screen, ColorType.Red.value, innerrect)
        # Zeichnen des Lebensbalkens Rand
        pygame.draw.rect(self.game.game.screen, ColorType.White.value, border_rect, 2)

    # Rüstungsbilder Methode
    def drawArmorBar(self):
        # Für jedes Schild ein Schild zeichnen
        for x in range(self.game.PlayerShield): 
            # Schild Bild laden
            Schild = Assetloader.getAsset(AssetType.Items, "Armor_Bonus.png")
            # Schild Bild skalieren
            Schild = pygame.transform.scale(Schild, (19,19))
            # Schild positionieren und das Rect zeichnen
            SchildRect = pygame.Rect(self.game.PlayerX + (x * 20), self.game.PlayerY - 30, 19, 5)
            # Schild zeichnen
            self.game.game.screen.blit(Schild, SchildRect)
   

    def moveRect(self):
        # Spielerschiff Größe bestimmen
        self.PlayerShipRectSize = self.playership.get_rect().size
        # Spielerschiff Rect erzeugen
        self.PlayerShipRect = pygame.Rect(self.game.PlayerX, self.game.PlayerY - 80, 64, 64)
        # Spielerschiff zeichnen
        self.game.game.screen.blit(self.playership, self.PlayerShipRect)


# Schiff 1
class Ship_One(IShip):
    
    # Spielerschiff zeichnen Methode
    def draw(self):
        # Überschreiben der Schiffsgeschwindigkeit
        self.speed = 2
        # Spielerschiff Grafik laden
        if self.playership is None:
            self.playership = Assetloader.getAsset(AssetType.Graphics, "Ship1.png")
            # Spielerschiff um 90 ° drehen
            self.playership = pygame.transform.rotate(self.playership, 90)
            # Spielerschiff skalieren
            self.playership = pygame.transform.scale(self.playership, (64, 64))
        # Spielerschiff bewegen & zeichnen
        self.moveRect(self)
    
# Schiff 2
class Ship_Two(IShip):
   
   # Spielerschiff zeichnen Methode
    def draw(self):
        # Überschreiben der Schiffsgeschwindigkeit
        self.speed = 3
        # Spielerschiff Grafik laden
        if self.playership is None:
            self.playership = Assetloader.getAsset(AssetType.Graphics, "Ship2.png")
             # Spielerschiff um 90 ° drehen
            self.playership = pygame.transform.rotate(self.playership, 90)
            # Spielerschiff skalieren
            self.playership = pygame.transform.scale(self.playership, (64, 64))
        # Spielerschiff bewegen & zeichnen
        self.moveRect()
        

# Schiff 3
class Ship_Three(IShip):
    # Spielerschiff zeichnen Methode
    def draw(self):
        # Überschreiben der Schiffsgeschwindigkeit
        self.speed = 4
        # Spielerschiff Grafik laden
        if self.playership is None:
            self.playership = Assetloader.getAsset(AssetType.Graphics, "Ship3.png")
            # Spielerschiff um 90 ° drehen
            self.playership = pygame.transform.rotate(self.playership, 90)
            # Spielerschiff skalieren
            self.playership = pygame.transform.scale(self.playership, (64, 64))
        # Spielerschiff bewegen & zeichnen
        self.moveRect()

# Schiff 4  
class Ship_Four(IShip):
    # Spielerschiff zeichnen Methode
    def draw(self):
        # Überschreiben der Schiffsgeschwindigkeit
        self.speed = 5
        # Spielerschiff Grafik laden
        if self.playership is None:
            self.playership = Assetloader.getAsset(AssetType.Graphics, "Ship4.png")
            # Spielerschiff um 90 ° drehen
            self.playership = pygame.transform.rotate(self.playership, 90)
            # Spielerschiff skalieren
            self.playership = pygame.transform.scale(self.playership, (64, 64))
        # Spielerschiff bewegen & zeichnen
        self.moveRect()

# Schiff 5     
class Ship_Five(IShip):
    # Spielerschiff zeichnen Methode
    def draw(self):
        # Überschreiben der Schiffsgeschwindigkeit
        self.speed = 6
        # Spielerschiff Grafik laden
        if self.playership is None:
            self.playership = Assetloader.getAsset(AssetType.Graphics, "Ship5.png")
            # Spielerschiff um 90 ° drehen
            self.playership = pygame.transform.rotate(self.playership, 90)
            # Spielerschiff skalieren
            self.playership = pygame.transform.scale(self.playership, (64, 64))
        # Spielerschiff bewegen & zeichnen
        self.moveRect()

# Schiff 6    
class Ship_Six(IShip):
    # Spielerschiff zeichnen Methode
    def draw(self):
        # Überschreiben der Schiffsgeschwindigkeit
        self.speed = 7
        # Spielerschiff Grafik laden
        if self.playership is None:
            self.playership = Assetloader.getAsset(AssetType.Graphics, "Ship6.png")
            # Spielerschiff um 90 ° drehen
            self.playership = pygame.transform.rotate(self.playership, 90)
            # Spielerschiff skalieren
            self.playership = pygame.transform.scale(self.playership, (64, 64))
        # Spielerschiff bewegen & zeichnen
        self.moveRect()

