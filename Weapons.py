import pygame
from Assettype import AssetType
from Assetloader import Assetloader

class IWeapon:

    def __init__(self, game, rotation, direction, start_x, start_y):

        # Das Projektil als Bild
        self.projectile_Item = None
        # Das Item als Rect
        self.projectile_Rect = None
        # Zufällige Geschwindigkeiten
        self.projectile_Rect_Speed = 6
        # Zugriffsvariable
        self.game = game
        
        # X Koordinate des Projektil
        self.projectile_X = 0
        # Y Koordinate des Projektil
        self.projectile_Y = 0

        # Rotation für das Projektil
        self.rotation = rotation
        # Richtung für das Projektil
        self.direction = direction
        
        # Startwerte X
        self.startProjectil_X = start_x
        # Startwert Y
        self.startProjectil_Y = start_y

    # Methode zum Zeichnen des Projektiles
    def draw(self):
        pass

    # Methode zum Updaten des Projektiles
    def update(self):
        pass

    # Methode zum zufälligen Startpunkt (X) für ein Objekt
    def getItemRect(self):
        if self.direction == 0:
            if (self.projectile_X == 0 and self.projectile_Y == 0):
                 # Projektil über dem Schiff positionieren #17.12 X-Position +10 gesetzt, damit der shot aus der Mitte des Schiffes kommt
                self.projectile_Rect = pygame.Rect(self.game.game.player.playerShip.playerShipRect[0]+12, self.game.game.player.playerShip.playerShipRect[1], 5, 50)
                self.projectile_X = self.game.game.player.playerShip.playerShipRect[0]
                self.projectile_Y = self.game.game.player.playerShip.playerShipRect[1]
            else:
                # Bewegen
                self.projectile_Rect = pygame.Rect(self.projectile_X +12, self.projectile_Y, 5, 50)
        else:
            if (self.projectile_X == 0 and self.projectile_Y == 0):
                # Projectil über dem Schiff positionieren
                self.projectile_Rect = pygame.Rect(100, 100, 50, 50)
                self.projectile_X = self.startProjectil_X
                self.projectile_Y = self.startProjectil_Y
            else:
               # Bewegen (X+10 gesetzt, damit der Schuss aus der Mitte des Schiffes abgefeuert wird)
                self.projectile_Rect = pygame.Rect(self.projectile_X+12, self.projectile_Y, 5, 50)

        # ItemRect zurückgeben
        return self.projectile_Rect

    # Methode zum Bewegen eines Objektes
    def moveItemRect(self):
        if self.direction == 0: # von unten nach oben
            # Überprüfung ob das Item Y innerhalb des Bildschirms ist
            if (self.projectile_Y >= 15):
                # Item mit den zufälligen Item Speed von unten nach oben bewegen lassen
                self.projectile_Y  = self.projectile_Y - self.projectile_Rect_Speed
            else:
                self.game.game.player.RemovePlayerShoot(self)
            # Item zeichnen
            self.game.game.screen.blit(self.projectile_Item, self.projectile_Rect)
        else: ## Gegnerische Schüsse
            # Überprüfung ob das Item Y innerhalb des Bildschirms ist
            if (self.projectile_Y <= 1000):
                # Item mit den zufälligen Item Speed von oben nach unten bewegen lassen
                self.projectile_Y  = self.projectile_Y + self.projectile_Rect_Speed
            else:
                self.game.enemys.RemoveEnemyShoot(self)
            # Item zeichnen
            self.game.screen.blit(self.projectile_Item, self.projectile_Rect)


class ProjectileWeapon(IWeapon):

    # Override der Draw Methode
    def draw(self):
        # Item bewegen
        self.moveItemRect()

    # Override der Update Methode
    def update(self):
        # Image laden für das Projektil
        if self.projectile_Item is None:
            self.projectile_Item = Assetloader.getAsset(AssetType.Shoot, "shot2small.png")
            self.projectile_Item = pygame.transform.scale(self.projectile_Item, (32, 8))
            self.projectile_Item = pygame.transform.rotate(self.projectile_Item, -90)
        # Item Rect erzeugen
        if self.projectile_Item is None:
            self.projectile_Item = Assetloader.getAsset(AssetType.Shoot, "shot2.png")
            # Item runterskalieren
            self.projectile_Item = pygame.transform.scale(self.projectile_Item, (50, 50))
            self.projectile_Item = pygame.transform.rotate(self.projectile_Item, self.rotation)
        self.projectile_Rect = self.getItemRect()   

class EnergyWeapon(IWeapon):
    # Override der Draw Methode
    def draw(self):
        self.projectile_Rect_Speed = 9
        # Item bewegen
        self.moveItemRect()

    # Override der Update Methode
    def update(self):
        # Item Rect erzeugen
        if self.projectile_Item is None:
            self.projectile_Item = Assetloader.getAsset(AssetType.Shoot, "shot1.png")
            # Item runterskalieren
            self.projectile_Item = pygame.transform.scale(self.projectile_Item, (50, 50))
            self.projectile_Item = pygame.transform.rotate(self.projectile_Item, 90)
        self.projectile_Rect = self.getItemRect()        

