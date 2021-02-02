from Level import *
from LocalEnemys import *
from Enemys import *
from SceneBase import SceneBase
from Scenes import ScoreScreen
from Scenes import EndScreen


class Levelmanager:

    # Initialisieren
    def __init__(self, game):
        # Zugriffsvariablen
        self.game = game
        self.level = None
        self.lvl = 1

    # Screen erzeugen
    def setScreen(self, screen):
        self.SceneBase = screen

    # aktuelles Level zurückgeben
    def getLevel(self):
        return self.level

    # Level laden
    def loadLevel(self):
        self.level.load(self)
        # Schwarzer Hintergrund
        self.game.screen.blit(self.getBackground(), (0, 0))

    # aktuellen Hintergrund zurückgeben
    def getBackground(self):
        return self.level.background(self)

    # Methode um Objekte hinzuzuladen
    def loadObjects(self, lvl):
        if self.game.enemys.getObjects() > []:
            # Meteore kommen öfter, je höher das Level wird
            meteor_drop = random.randint(1, int(200))
            # health + armor kommen seltener je höher das Level wird
            health_drop = random.randint(1, int(lvl*550))
            armor_drop = random.randint(1, int(lvl*650))
            # Das Waffenupgrade kommt häufiger, je höher das Level ist
            weapon_drop = random.randint(1, int(3500))
            if meteor_drop == 13:
                print("METEOR")
                self.game.object.addObject(MeteorItemObject(self))
            if health_drop == 25:
                print("HEALTH")
                self.game.object.addObject(HealthItemObject(self))
            if armor_drop == 153:
                print("ARMOR")
                self.game.object.addObject(ArmorItemObject(self))
            if weapon_drop == 1000:
                print("WEAPON")
                self.game.object.addObject(SwitchWeaponItemObject(self))

    # Level wechseln, sobald keine Enemys mehr da sind
    def update(self):

        # Variable für die Berchnung der Dropchancen
        if self.getLevel() == Level1:
            self.lvl = 1
        if self.getLevel() == Level2:
            self.lvl = 2
        if self.getLevel() == Level3:
            self.lvl = 3
        if self.getLevel() == Level4:
            self.lvl = 4
        if self.getLevel() == Level5:
            self.lvl = 5

        # Level wechseln
        if self.getLevel() == Level4 and self.level.state(self) == True:
            self.game.quitgame = True
        self.game.next.SwitchToScene(
            EndScreen.EndScreen(" Sie haben Gewonnen"))
        # Level wechseln
        if self.getLevel() == Level3 and self.level.state(self) == True:
            self.game.quitgame = True
            self.level = Level4
            self.lvl = 4
            self.game.next.SwitchToScene(ScoreScreen.ScoreScreen(
                self.level, self.game.player.getPlayerScore()))
        # Level wechseln
        if self.getLevel() == Level2 and self.level.state(self) == True:
            self.game.quitgame = True
            self.level = Level3
            self.lvl = 3
            self.game.next.SwitchToScene(ScoreScreen.ScoreScreen(
                self.level, self.game.player.getPlayerScore()))
        # Level wechseln
        if self.getLevel() == Level1 and self.level.state(self) == True:
            self.game.quitgame = True
            self.level = Level2
            self.lvl = 2
            self.game.next.SwitchToScene(ScoreScreen.ScoreScreen(
                self.level, self.game.player.getPlayerScore()))

        self.loadObjects(self.lvl)
