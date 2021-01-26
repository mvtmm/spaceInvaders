from Level import *
from LocalEnemys import *
from Enemys import *
from SceneBase import SceneBase
from Scenes import ScoreScreen


class Levelmanager:

    # Initialisieren
    def __init__(self, game):
        self.game = game
        self.level = Level1

    def setScreen(self, screen):
        self.SceneBase = screen

    def getLevel(self):
        return self.level

    def loadLevel(self):
        self.level.load(self)
        # Schwarzer Hintergrund
        self.game.screen.blit(self.getBackground(), (0, 0))

    def getBackground(self):
        return self.level.background(self)

    def loadObjects(self, lvl):
        if self.game.enemys.getObjects() > []:
            # Meteore kommen öfter, je höher das Level wird
            meteor_drop = random.randint(1, 198/lvl)
            # health + armor kommen seltener je höher das Level wird
            health_drop = random.randint(1, lvl*450)
            armor_drop = random.randint(1, lvl*550)
            # Das Waffenupgrade kommt häufiger, je höher das Level ist
            weapon_drop = random.randint(1, 3000/lvl)
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
        lvl = 0

        if self.getLevel() == Level1 and self.game.enemys.getObjects() != []:
            lvl = 1
        if self.getLevel() == Level2 and self.game.enemys.getObjects() != []:
            lvl = 2
        if self.getLevel() == Level3 and self.game.enemys.getObjects() != []:
            lvl = 3

        if self.game.enemys.getObjects() == [] and self.getLevel() == Level1:
            #self.level = Level2
            self.game.quitgame = True
            self.game.next.SwitchToScene(ScoreScreen.ScoreScreen())

            # Hier ScoreScreen mit weiter Button

            #vl = 2
            # self.loadLevel()

        if self.game.enemys.getObjects() == [] and self.getLevel() == Level2:
            self.level = Level3
            lvl = 3
            self.loadLevel()

        self.loadObjects(lvl)
