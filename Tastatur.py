from Weapons import *
import abc

class Command(metaclass=abc.ABCMeta): 
    def __init__(self, game):
        self.game = game

    def execute(self):
        pass
    def undo(self):
        pass

class PlayerLeft(Command):
    def execute(self):
        if self.game.player.playerX <= (self.game.player.playerShip.playerShipRectSize[0] / 2):
            # Spieler will außerhalb des Sichtfeldes gehen, Position zurücksetzen
            self.game.player.playerX = (self.game.player.playerShip.playerShipRectSize[0] / 2)
        else:
            # Spieler innerhalb des Sichtfeldes, Position mit dem Schiffspeed addieren
            self.game.player.playerX -= self.game.player.playerShip.speed

class PlayerRight(Command):
    def execute(self):
        if self.game.player.playerX >= (self.game.width - self.game.player.playerShip.playerShipRectSize[0]):
            # Spieler will außerhalb des Sichtfeldes gehen, Position zurücksetzen
            self.game.player.playerX = (self.game.width - self.game.player.playerShip.playerShipRectSize[0])
        else:
            # Spieler innerhalb des Sichtfeldes, Position mit dem Schiffspeed addieren
            self.game.player.playerX += self.game.player.playerShip.speed

class PlayerUp(Command):
    def execute(self):
        #if (self.game.player.PlayerY <= self.game.player.PlayerShip.PlayerShipRectSize[1] + (self.game.player.PlayerShip.PlayerShipRectSize[1] / 2)):
            # Spieler will außerhalb des Sichtfeldes gehen, Position zurücksetzen
            #self.game.player.PlayerY = self.game.player.PlayerShip.PlayerShipRectSize[1] + (
            #self.game.player.PlayerShip.PlayerShipRectSize[1] / 2)
        #else:
            # Spieler innerhalb des Sichtfeldes, Position mit dem Schiffspeed addieren
            #self.game.player.PlayerY -= self.game.player.PlayerShip.speed
        pass

class PlayerDown(Command):
    def execute(self):
        # Überprüfung ob Spielerschiff innerhalb des sichtbaren Bereichs ist
            #if (self.game.player.PlayerY >= self.game.height - 0 and self.game.player.PlayerY <= (self.game.height + self.game.player.PlayerShip.PlayerShipRectSize[1])):
                # Spieler will außerhalb des Sichtfeldes gehen, Position zurücksetzen
                #self.game.player.PlayerY = self.game.height
           # else:
                # Spieler innerhalb des Sichtfeldes, Position mit dem Schiffspeed addieren
                #self.game.player.PlayerY += self.game.player.PlayerShip.speed
        pass

class PlayerSpace(Command):
    def execute(self):
        # Zeitstempel
        time = pygame.time.get_ticks()
        if time - self.game.vorherZeit > 500:
            self.game.vorherZeit = time
            if type(self.game.player.playerShipWeapon).__name__  == "ProjectileWeapon":
                self.game.player.PlayerShoot(ProjectileWeapon(self, -90, 0, self.game.player.playerShip.playerShipRect[0],self.game.player.playerShip.playerShipRect[1] ))
            else:
                self.game.player.PlayerShoot(EnergyWeapon(self, -90, 0, 0, 0))
                    



class Invoker():

    def __init__(self):
        self.commands = {}

    def setBefehl(self,key, command: Command):
        self.commands[key] = command

    def PressedKey(self, key):

        for _key in self.commands:
            if (key[_key]):
                self.commands[_key].execute()


       