from Enemys import *
from Objects import * 
from Meteors import *
from LocalEnemys import *
from Konstanten import *


class ILevel:

    def __init__(self, game):
        # Zugriffsvariable 
        self.game = game
        self.bg = None

    def load(self):
        pass

    def reset(self):
        pass
    
    def background(self):
        pass


class Level1(ILevel):
    def __init__(self, game):
        self.game = game

    def background(self):
        self.bg = Assetloader.getAsset(AssetType.Graphics, "background3.jpg")
        pygame.transform.scale(self.bg, (width, height))
        return self.bg

    def load(self):

        self.game.enemys.addObjectBundle(Enemy_One(self, 1, 0))
        self.game.enemys.addObjectBundle(Enemy_One(self, 0, 1))
        self.game.enemys.addObjectBundle(Enemy_One(self, 1,  2))

        self.game.enemys.addObjectBundle(Enemy_One(self, 3, 0))
        self.game.enemys.addObjectBundle(Enemy_One(self, 2, 1))
        self.game.enemys.addObjectBundle(Enemy_One(self, 3,  2))


        self.game.enemys.addObjectBundle(Enemy_One(self, 5, 0))
        self.game.enemys.addObjectBundle(Enemy_One(self, 4, 1))
        self.game.enemys.addObjectBundle(Enemy_One(self, 5,  2))

        self.game.enemys.addObjectBundle(Enemy_One(self, 7, 0))
        self.game.enemys.addObjectBundle(Enemy_One(self, 6, 1))
        self.game.enemys.addObjectBundle(Enemy_One(self, 7,  2))

        self.game.enemys.addObjectBundle(Enemy_One(self, 9, 0))
        self.game.enemys.addObjectBundle(Enemy_One(self, 8, 1))
        self.game.enemys.addObjectBundle(Enemy_One(self, 9,  2))

        self.game.enemys.addObjectBundle(Enemy_One(self, 11, 0))
        self.game.enemys.addObjectBundle(Enemy_One(self, 10, 1))
        self.game.enemys.addObjectBundle(Enemy_One(self, 11,  2))

        self.game.enemys.addObjectBundle(Enemy_One(self, 13, 0))
        self.game.enemys.addObjectBundle(Enemy_One(self, 12, 1))
        self.game.enemys.addObjectBundle(Enemy_One(self, 13,  2))
        
        self.game.enemys.addObjectBundle(Enemy_One(self, 15, 0))
        self.game.enemys.addObjectBundle(Enemy_One(self, 14, 1))
        self.game.enemys.addObjectBundle(Enemy_One(self, 15,  2))

        self.game.enemys.addObjectBundle(Enemy_One(self, 17, 0))
        self.game.enemys.addObjectBundle(Enemy_One(self, 16, 1))
        self.game.enemys.addObjectBundle(Enemy_One(self, 17,  2))

        self.game.enemys.addObjectBundle(Enemy_One(self, 19, 0))
        self.game.enemys.addObjectBundle(Enemy_One(self, 18, 1))
        self.game.enemys.addObjectBundle(Enemy_One(self, 19,  2))

        self.game.enemys.addObjectBundle(Enemy_One(self, 20, 1))

    def loadObjects(self):    
        for i in range(1):
            self.game.object.addObject(MeteorItemObject(self))
            self.game.tick(40)
            self.game.object.addObject(ArmorItemObject(self))
            self.game.object.addObject(ArmorItemObject(self))
            self.game.object.addObject(ArmorItemObject(self))
            self.game.object.addObject(SwitchWeaponItemObject(self))
            self.game.object.addObject(HealthItemObject(self))
        

class Level2(ILevel):

    def __init__(self, game):
        self.game = game

    def background(self):
        bg = Assetloader.getAsset(AssetType.Graphics, "background3.jpg")
        return bg

    def load(self):
        #Enemys adden
        self.game.enemys.addObjectBundle(Enemy_One(self, 3, 0))
        self.game.enemys.addObjectBundle(Enemy_One(self, 3, 1))
        self.game.enemys.addObjectBundle(Enemy_One(self, 3,  2))

        self.game.enemys.addObjectBundle(Enemy_One(self, 4, 0))
        self.game.enemys.addObjectBundle(Enemy_One(self, 4, 1))
        self.game.enemys.addObjectBundle(Enemy_One(self, 4,  2))

        self.game.enemys.addObjectBundle(Enemy_One(self, 5, 0))
        self.game.enemys.addObjectBundle(Enemy_One(self, 5, 1))
        self.game.enemys.addObjectBundle(Enemy_One(self, 5,  2))

        self.game.enemys.addObjectBundle(Enemy_One(self, 6, 0))
        self.game.enemys.addObjectBundle(Enemy_One(self, 6, 1))
        self.game.enemys.addObjectBundle(Enemy_One(self, 6,  2))

       

        self.game.enemys.addObjectBundle(Enemy_One(self, 11 , 0))
        self.game.enemys.addObjectBundle(Enemy_One(self, 11 , 1))
        self.game.enemys.addObjectBundle(Enemy_One(self, 11 , 2))

        self.game.enemys.addObjectBundle(Enemy_One(self, 12 , 0))
        self.game.enemys.addObjectBundle(Enemy_One(self, 12 , 1))
        self.game.enemys.addObjectBundle(Enemy_One(self, 12 , 2))

class Level3(ILevel):

    def __init__(self, game):
        self.game = game

    def background(self):
        bg = Assetloader.getAsset(AssetType.Graphics, "background3.jpg")
        return bg

    def load(self):
        #Enemys adden
        

        self.game.enemys.addObjectBundle(Enemy_One(self, 5, 0))
        self.game.enemys.addObjectBundle(Enemy_One(self, 5, 1))
        self.game.enemys.addObjectBundle(Enemy_One(self, 5,  2))

        self.game.enemys.addObjectBundle(Enemy_One(self, 6, 0))
        self.game.enemys.addObjectBundle(Enemy_One(self, 6, 1))
        self.game.enemys.addObjectBundle(Enemy_One(self, 6,  2))

        self.game.enemys.addObjectBundle(Enemy_One(self, 7, 0))
        self.game.enemys.addObjectBundle(Enemy_One(self, 7, 1))
        self.game.enemys.addObjectBundle(Enemy_One(self, 7,  2))
        
        self.game.enemys.addObjectBundle(Enemy_One(self, 8, 0))
        self.game.enemys.addObjectBundle(Enemy_One(self, 8, 1))
        self.game.enemys.addObjectBundle(Enemy_One(self, 8,  2))
        
        
        self.game.enemys.addObjectBundle(Enemy_One(self, 9, 0))
        self.game.enemys.addObjectBundle(Enemy_One(self, 9, 1))
        self.game.enemys.addObjectBundle(Enemy_One(self, 9,  2))
       