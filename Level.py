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
        txt = "1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0"
        addEnemy(self, txt)


        

class Level2(ILevel):

    def __init__(self, game):
        self.game = game

    def background(self):
        bg = Assetloader.getAsset(AssetType.Graphics, "background3.jpg")
        return bg

    def load(self):
        txt = "1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0"
        addEnemy(self, txt)
              


class Level3(ILevel):

    def __init__(self, game):
        self.game = game

    def background(self):
        bg = Assetloader.getAsset(AssetType.Graphics, "background3.jpg")
        return bg

    def load(self):
        txt = "0,1,0,1,0,1,0,1,0,0,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,0,1,0,1,0,1,0,1,0"
        addEnemy(self, txt)


class Level4(ILevel):

    def __init__(self, game):
        self.game = game

    def background(self):
        bg = Assetloader.getAsset(AssetType.Graphics, "background3.jpg")
        return bg

    def load(self):
        txt = "1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0"
        addEnemy(self, txt)
    
class Level5(ILevel):

    def __init__(self, game):
        self.game = game

    def background(self):
        bg = Assetloader.getAsset(AssetType.Graphics, "background3.jpg")
        return bg

    def load(self):
        txt = "1,0,1,0,0,0,1,0,1,0,0,0,1,0,1,0,1,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,1,0,1,0,0,0,1,0,1,0,0,0,1,0,1,0,1,0,1,0"
        addEnemy(self, txt)



def addEnemy(self, txt):
    i = [int(x) for x in txt.split(",")]
    y = 0

    for x in range(60):

        if i[x] == 1:
            if x < 20: 
                self.game.enemys.addObjectBundle(Enemy_One(self, x, y))
            if 20 <= x < 40:
                y = 1
                z = x-20
                self.game.enemys.addObjectBundle(Enemy_One(self, z, y))
            if 40 <= x < 60:
                y = 2
                q = x - 40
                self.game.enemys.addObjectBundle(Enemy_One(self, q, y))       