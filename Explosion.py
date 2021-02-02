import pygame
from Assettype import AssetType
from Assetloader import Assetloader

class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        # Bilder die nach einander angezeigt werden um eine Animation zu erzeugen
        self.images = []
        # Alle Bilder laden
        for num in range(1,12):
            img = Assetloader.getAsset(AssetType.Shoot, "Explosion1_" + str(num) + ".png")
            # Bilder skalieren
            img = pygame.transform.scale(img, (100,100))
            self.images.append(img)
        self.index = 0
        self.image = self.images[self.index]
        self.rect  = self.image.get_rect()
        self.rect.center = [x,y]
        self.counter = 0

    def update(self):
        # Schnelligkeit der Bilder Wechsel Methode
        explosion_speed = 2
        self.counter += 1
        if self.counter >= explosion_speed and self.index < len(self.images) -1:
            # Animation abspielen
            self.counter = 0
            self.index += 1
            self.image = self.images[self.index]
        if self.index >= len(self.images) -1 and self.counter >= explosion_speed:
            # Animation abgelaufen deshalb Objekt zerstören
            self.kill()
