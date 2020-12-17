from enemys import *
from objects import * 
from Meteors import *
from LocalEnemys import *


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
        self.bg = Assetloader.getAsset(AssetType.Graphics, "background1.jpg")
        return self.bg

    def load(self):
        self.game.Enemys.addObjectBundle(Enemy_One(self, 3, 0))
        self.game.Enemys.addObjectBundle(Enemy_One(self, 3, 1))
        self.game.Enemys.addObjectBundle(Enemy_One(self, 3,  2))

        self.game.Enemys.addObjectBundle(Enemy_One(self, 4, 0))
        self.game.Enemys.addObjectBundle(Enemy_One(self, 4, 1))
        self.game.Enemys.addObjectBundle(Enemy_One(self, 4,  2))

        self.game.Enemys.addObjectBundle(Enemy_One(self, 5, 0))
        self.game.Enemys.addObjectBundle(Enemy_One(self, 5, 1))
        self.game.Enemys.addObjectBundle(Enemy_One(self, 5,  2))

        self.game.Enemys.addObjectBundle(Enemy_One(self, 6, 0))
        self.game.Enemys.addObjectBundle(Enemy_One(self, 6, 1))
        self.game.Enemys.addObjectBundle(Enemy_One(self, 6,  2))

        self.game.Enemys.addObjectBundle(Enemy_One(self, 7, 0))
        self.game.Enemys.addObjectBundle(Enemy_One(self, 7, 1))
        self.game.Enemys.addObjectBundle(Enemy_One(self, 7,  2))
        
        self.game.Enemys.addObjectBundle(Enemy_One(self, 8, 0))
        self.game.Enemys.addObjectBundle(Enemy_One(self, 8, 1))
        self.game.Enemys.addObjectBundle(Enemy_One(self, 8,  2))
        
        
        self.game.Enemys.addObjectBundle(Enemy_One(self, 9, 0))
        self.game.Enemys.addObjectBundle(Enemy_One(self, 9, 1))
        self.game.Enemys.addObjectBundle(Enemy_One(self, 9,  2))
        
        
        self.game.Enemys.addObjectBundle(Enemy_One(self, 10 , 0))
        self.game.Enemys.addObjectBundle(Enemy_One(self, 10 , 1))
        self.game.Enemys.addObjectBundle(Enemy_One(self, 10,  2))

        self.game.Enemys.addObjectBundle(Enemy_One(self, 11 , 0))
        self.game.Enemys.addObjectBundle(Enemy_One(self, 11 , 1))
        self.game.Enemys.addObjectBundle(Enemy_One(self, 11 , 2))

        self.game.Enemys.addObjectBundle(Enemy_One(self, 12 , 0))
        self.game.Enemys.addObjectBundle(Enemy_One(self, 12 , 1))
        self.game.Enemys.addObjectBundle(Enemy_One(self, 12 , 2))

        #self.game.Object.addObject(ArmorItemObject(self))
        #self.game.Object.addObject(ArmorItemObject(self))
        #self.game.Object.addObject(ArmorItemObject(self))
        #self.game.Object.addObject(SwitchWeaponItemObject(self))
        self.game.Object.addObject(HealthItemObject(self))

        for i in range(1):
            self.game.Object.addObject(MeteorItemObject(self))

        

class Level2(ILevel):

    def __init__(self, game):
        self.game = game

    def background(self):
        bg = Assetloader.getAsset(AssetType.Graphics, "level2.jpg")
        return bg

    def load(self):
        #Enemys adden
        self.game.Enemys.addObjectBundle(Enemy_One(self, 3, 0))
        self.game.Enemys.addObjectBundle(Enemy_One(self, 3, 1))
        self.game.Enemys.addObjectBundle(Enemy_One(self, 3,  2))

        self.game.Enemys.addObjectBundle(Enemy_One(self, 4, 0))
        self.game.Enemys.addObjectBundle(Enemy_One(self, 4, 1))
        self.game.Enemys.addObjectBundle(Enemy_One(self, 4,  2))

        self.game.Enemys.addObjectBundle(Enemy_One(self, 5, 0))
        self.game.Enemys.addObjectBundle(Enemy_One(self, 5, 1))
        self.game.Enemys.addObjectBundle(Enemy_One(self, 5,  2))

        self.game.Enemys.addObjectBundle(Enemy_One(self, 6, 0))
        self.game.Enemys.addObjectBundle(Enemy_One(self, 6, 1))
        self.game.Enemys.addObjectBundle(Enemy_One(self, 6,  2))

        self.game.Enemys.addObjectBundle(Enemy_One(self, 7, 0))
        self.game.Enemys.addObjectBundle(Enemy_One(self, 7, 1))
        self.game.Enemys.addObjectBundle(Enemy_One(self, 7,  2))
        
        self.game.Enemys.addObjectBundle(Enemy_One(self, 8, 0))
        self.game.Enemys.addObjectBundle(Enemy_One(self, 8, 1))
        self.game.Enemys.addObjectBundle(Enemy_One(self, 8,  2))
        
        
        self.game.Enemys.addObjectBundle(Enemy_One(self, 9, 0))
        self.game.Enemys.addObjectBundle(Enemy_One(self, 9, 1))
        self.game.Enemys.addObjectBundle(Enemy_One(self, 9,  2))
        
        
        self.game.Enemys.addObjectBundle(Enemy_One(self, 10 , 0))
        self.game.Enemys.addObjectBundle(Enemy_One(self, 10 , 1))
        self.game.Enemys.addObjectBundle(Enemy_One(self, 10,  2))

        self.game.Enemys.addObjectBundle(Enemy_One(self, 11 , 0))
        self.game.Enemys.addObjectBundle(Enemy_One(self, 11 , 1))
        self.game.Enemys.addObjectBundle(Enemy_One(self, 11 , 2))

        self.game.Enemys.addObjectBundle(Enemy_One(self, 12 , 0))
        self.game.Enemys.addObjectBundle(Enemy_One(self, 12 , 1))
        self.game.Enemys.addObjectBundle(Enemy_One(self, 12 , 2))

       