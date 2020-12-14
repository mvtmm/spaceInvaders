from Level import *
class Levelmanager:

    # Initialisieren
    def __init__(self, game):
        self.game                       = game
        self.Level                      = None

    def loadLevel(self, _level: ILevel):
        self.Level = _level
        self.Level.load()

    def update(self):
        pass