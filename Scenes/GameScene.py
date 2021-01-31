from CollisionHandler import CollisionHandler
from Explosion import Explosion
from Weapons import *
from Objects import *
from Playership import *
from Enemys import *
from Assettype import AssetType
from Assetloader import Assetloader
import pygame
import pygame.display

from Tastatur import *
from Levelmanager import *
from Level import *
from LocalPlayer import LocalPlayer
from LocalEnemys import LocalEnemys
from LocalObjects import LocalObjects

from Konstanten import *
from SceneBase import SceneBase
from Textboxes import *


class GameScene(SceneBase):

    def __init__(self, level, score):
        SceneBase.__init__(self)
        pygame.display.set_caption('Daniel ist schon ein bisschen komisch')
        # Spielbreite festlegen
        self.width = width
        # Spielhöhe festlegen
        self.height = height
        # Spielzeit anlegen
        self.clock = pygame.time.Clock()
        # LocalPlayer mit Anfangsschiff hinzufügen
        self.player = LocalPlayer(self, width / 2, height - 20, Ship_Five, ProjectileWeapon)
        # Spielobjekte anlegen
        self.object = LocalObjects(self)
        # Gegner anlegen
        self.enemys = LocalEnemys(self)
        # Bedingung für die Schleife, Spielabbruch
        self.quitgame = False
        # Zeitstempel fürs Schießen
        self.vorherZeit = pygame.time.get_ticks()
        # Animationsgruppe
        self.animations_Explosions = pygame.sprite.Group()
        # Tastatur Invoker
        self.tastatur = Invoker()
        # Level 
        self.level = level
        # Levelmanager
        self.levelmanager = Levelmanager(self)
        # Kollisionhandler
        self.collisionhandler = CollisionHandler(self)
        # Scorelabel
        self.scorelabel = TextBox((0, 0, 200, 32), "Score")
        # levellabel
        self.levellabel = TextBox((1000, 0, 200, 32), "Level")

        # Tastatur EInstellungen festlegen
        command_Down = PlayerDown(self)
        command_Up = PlayerUp(self)
        command_Right = PlayerRight(self)
        command_Left = PlayerLeft(self)
        command_Space = PlayerSpace(self)

        self.tastatur.setBefehl(pygame.K_DOWN,      command_Down)
        self.tastatur.setBefehl(pygame.K_UP,        command_Up)
        self.tastatur.setBefehl(pygame.K_RIGHT,     command_Right)
        self.tastatur.setBefehl(pygame.K_LEFT,      command_Left)
        self.tastatur.setBefehl(pygame.K_SPACE,     command_Space)

        self.levelmanager.level = self.level
        self.player.setScore(score)
 

    def Render(self, screen):
        # Bildschirm
        self.screen = screen
        self.levelmanager.setScreen(screen)

        if (self.levelmanager.level is None):
            self.levelmanager.level = Level1
        
        self.levelmanager.loadLevel()

        # Spielschleife
        while not self.quitgame:

            # Levelmanager updaten
            self.levelmanager.update()
            # Tastatur Klasse die gedrückten Tasten übermitteln
            self.tastatur.PressedKey(pygame.key.get_pressed())

            for pyevents in pygame.event.get():
                if pyevents.type == pygame.QUIT:
                    self.quitgame = True
           

            pygame.display.flip()
            # FPS einstellen/ Ticks per Sek
            self.clock.tick(60)
            # Schwarzer Hintergrund
            self.screen.blit(self.levelmanager.getBackground(), (0, 0))
            # Items updaten
            self.object.update()
            # Enemys updaten
            self.enemys.update()
            # Spieler updaten
            self.player.update()
            # Spieler zeichnen
            self.player.draw()
            # Gegner zeichnen
            self.enemys.draw()
            # Objekte zeichnen
            self.object.draw()

            # Explosionen zeichnen
            self.animations_Explosions.draw(self.screen)
            # Explosionen updaten
            self.animations_Explosions.update()

            # Kollisionshandler updaten
            self.collisionhandler.update()
            # Score update
            self.scorelabel.update(self.screen, "Score", self.player.getPlayerScore())

            # Score zeichnen
            self.scorelabel.draw(self.screen)

            # level update
            self.levellabel.update(self.screen, "Level", "1")

            # level zeichnen
            self.levellabel.draw(self.screen)
