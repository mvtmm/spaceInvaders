from Level import *
from LocalEnemys import *
from Enemys import *


class Levelmanager:

    # Initialisieren
    def __init__(self, game):
        self.game                       = game
        self.level                      = Level1
        
    
    def getLevel(self):
        if self.level == Level1:
            return self.level
        if self.level == Level2:
            return self.level
        #if Level3: 
        #    return 3
        
        

    def loadLevel(self):
        self.level.load(self)
        # Schwarzer Hintergrund
        self.game.screen.blit(self.getBackground(),(0,0))

    def getBackground(self):
        return self.level.background(self)

    def loadObjects(self, lvl):
        if self.game.enemys.getObjects() > []:
            meteor_drop =       random.randint(1,250/lvl) #Meteore kommen öfter, je höher das Level wird
            health_drop =       random.randint(1,lvl*2*250) #health + armor kommen seltener je höher das Level wird
            armor_drop =        random.randint(1,lvl*2*350)
            weapon_drop =       random.randint(1, 1500/lvl) #Das Waffenupgrade kommt häufiger, je höher das Level ist
            if meteor_drop == 13:
                print("METEOR")
                self.game.object.addObject(MeteorItemObject(self))
            if health_drop == 25:
                print("HEALTH")
                self.game.object.addObject(HealthItemObject(self))
            if armor_drop == 153:
                print("ARMOR")
                self.game.object.addObject(ArmorItemObject(self))


    # Level wechseln, sobald keine Enemys mehr da sind
    # lvl darf nicht am anfang der Methode stehen, sonst wird es immer überschrieben!!!!111!!
    def update(self):
        lvl = 1
        self.loadObjects(lvl)

        if self.game.enemys.getObjects() == [] and self.getLevel() == Level1:
            self.level = Level2
            lvl = 2
            self.loadLevel()
        
        if self.game.enemys.getObjects() == [] and self.getLevel() == Level2:
            self.level = Level3
            lvl = 3
            self.loadLevel()
            