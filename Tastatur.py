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
        if self.game.Player.PlayerX <= (self.game.Player.PlayerShip.PlayerShipRectSize[0] / 2):
            # Spieler will außerhalb des Sichtfeldes gehen, Position zurücksetzen
            self.game.Player.PlayerX = (self.game.Player.PlayerShip.PlayerShipRectSize[0] / 2)
        else:
            # Spieler innerhalb des Sichtfeldes, Position mit dem Schiffspeed addieren
            self.game.Player.PlayerX -= self.game.Player.PlayerShip.speed

class PlayerRight(Command):
    def execute(self):
        if self.game.Player.PlayerX >= (self.game.width - self.game.Player.PlayerShip.PlayerShipRectSize[0]):
            # Spieler will außerhalb des Sichtfeldes gehen, Position zurücksetzen
            self.game.Player.PlayerX = (self.game.width - self.game.Player.PlayerShip.PlayerShipRectSize[0])
        else:
            # Spieler innerhalb des Sichtfeldes, Position mit dem Schiffspeed addieren
            self.game.Player.PlayerX += self.game.Player.PlayerShip.speed

class PlayerUp(Command):
    def execute(self):
        if (self.game.Player.PlayerY <= self.game.Player.PlayerShip.PlayerShipRectSize[1] + (self.game.Player.PlayerShip.PlayerShipRectSize[1] / 2)):
            # Spieler will außerhalb des Sichtfeldes gehen, Position zurücksetzen
            self.game.Player.PlayerY = self.game.Player.PlayerShip.PlayerShipRectSize[1] + (
            self.game.Player.PlayerShip.PlayerShipRectSize[1] / 2)
        else:
            # Spieler innerhalb des Sichtfeldes, Position mit dem Schiffspeed addieren
            self.game.Player.PlayerY -= self.game.Player.PlayerShip.speed

class PlayerDown(Command):
    def execute(self):
        # Überprüfung ob Spielerschiff innerhalb des sichtbaren Bereichs ist
            if (self.game.Player.PlayerY >= self.game.height - 0 and self.game.Player.PlayerY <= (self.game.height + self.game.Player.PlayerShip.PlayerShipRectSize[1])):
                # Spieler will außerhalb des Sichtfeldes gehen, Position zurücksetzen
                self.game.Player.PlayerY = self.game.height
            else:
                # Spieler innerhalb des Sichtfeldes, Position mit dem Schiffspeed addieren
                self.game.Player.PlayerY += self.game.Player.PlayerShip.speed

class PlayerSpace(Command):
    def execute(self):
        # Zeitstempel
        time = pygame.time.get_ticks()
        if time - self.game.VorherZeit > 500:
            self.game.VorherZeit = time
            if type(self.game.Player.PlayerShipWeapon).__name__  == "ProjectileWeapon":
                self.game.Player.PlayerShoot(ProjectileWeapon(self, -90, 0, self.game.Player.PlayerShip.PlayerShipRect[0],self.game.Player.PlayerShip.PlayerShipRect[1] ))
            else:
                self.game.Player.PlayerShoot(EnergyWeapon(self, -90, 0 ))
                    



class Invoker():

    def __init__(self):
        self.commands = {}

    def setBefehl(self,key, command: Command):
        self.commands[key] = command

    def PressedKey(self, key):

        for _key in self.commands:
            if (key[_key]):
                self.commands[_key].execute()


       