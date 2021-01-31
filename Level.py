from Enemys import *
from Objects import * 
from Meteors import *
from LocalEnemys import *
from Konstanten import *



#Interface Klasse für einzelne Level
class ILevel:

    def __init__(self, game):
        # Zugriffsvariable 
        self.game = game
        self.bg = None

    #Methode zum laden des Levels
    def load(self):
        pass
    #Methode zum zurücksetzen des Levels
    def reset(self):
        pass
    #Methode um den Hintergrund festzulegen
    def background(self):
        pass




class Level1(ILevel):
    def __init__(self, game):
        self.game = game

    #Override der background Methode
    def background(self):
        #Hintergrundgrafik laden
        self.bg = Assetloader.getAsset(AssetType.Graphics, "background3.jpg")
        pygame.transform.scale(self.bg, (width, height))
        return self.bg

    #Gegnerstruktur laden
    def load(self):
        txt = "1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0"
        addEnemy(self, txt)

    #Checkt ob das Level bestanden wurde
    def state(self):
        bestanden = False
        if self.game.enemys.getObjects() == []:
            bestanden = True
        return bestanden 


        

class Level2(ILevel):

    def __init__(self, game):
        self.game = game

    #Hintergrundgrafik laden
    def background(self):
        self.bg = Assetloader.getAsset(AssetType.Graphics, "background3.jpg")
        return self.bg

    #Gegnerstruktur laden
    def load(self):
        txt = "1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0"
        addEnemy(self, txt)
    
    #Checkt ob das Level bestanden wurde
    def state(self):
        bestanden = False
        if self.game.enemys.getObjects() == []:
            bestanden = True
        return bestanden 


class Level3(ILevel):

    def __init__(self, game):
        self.game = game

    #Hintergrundgrafik laden
    def background(self):
        bg = Assetloader.getAsset(AssetType.Graphics, "background3.jpg")
        return bg
    
    #Gegnerstruktur laden
    def load(self):
        txt = "0,1,0,1,0,1,0,1,0,0,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,0,1,0,1,0,1,0,1,0"
        addEnemy(self, txt)

    #Checkt ob das Level bestanden wurde
    def state(self):
        bestanden = False
        if self.game.enemys.getObjects() == []:
            bestanden = True
        return bestanden 


class Level4(ILevel):

    def __init__(self, game):
        self.game = game

    #Hintergrundgrafik laden
    def background(self):
        bg = Assetloader.getAsset(AssetType.Graphics, "background3.jpg")
        return bg
    
    #Gegnerstruktur laden
    def load(self):
        txt = "1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0"
        addEnemy(self, txt)

        #Checkt ob das Level bestanden wurde
    def state(self):
        bestanden = False
        if self.game.enemys.getObjects() == []:
            bestanden = True
        return bestanden 
    
class Level5(ILevel):

    def __init__(self, game):
        self.game = game

    #Hintergrundgrafik laden
    def background(self):
        bg = Assetloader.getAsset(AssetType.Graphics, "background3.jpg")
        return bg
    
    #Gegnerstruktur laden
    def load(self):
        txt = "1,0,1,0,0,0,1,0,1,0,0,0,1,0,1,0,1,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,1,0,1,0,0,0,1,0,1,0,0,0,1,0,1,0,1,0,1,0"
        addEnemy(self, txt)

        #Checkt ob das Level bestanden wurde
    def state(self):
        bestanden = False
        if self.game.enemys.getObjects() == []:
            bestanden = True
        return bestanden 


#Gegner adden an den Stellen wo eine 1 im übergebenen String vorhanden ist
def addEnemy(self, txt):
    i = [int(x) for x in txt.split(",")]
    y = 0
    #Schleife für mögliche Gegner auf dem Screen (60)
    for x in range(60):

        if i[x] == 1:
            #Oberste Reihe
            if x < 20: 
                self.game.enemys.addObjectBundle(Enemy_One(self, x, y))
            #Mittlere Reihe
            if 20 <= x < 40:
                y = 1
                z = x-20
                self.game.enemys.addObjectBundle(Enemy_One(self, z, y))
            #Untere Reihe
            if 40 <= x < 60:
                y = 2
                q = x - 40
                self.game.enemys.addObjectBundle(Enemy_One(self, q, y))       