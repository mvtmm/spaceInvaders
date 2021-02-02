from Scenes import GameScene
from SceneBase import SceneBase
import pygame
from Textboxes import *
from Konstanten import *
from Buttons import *
from Level import *
from Colors import ColorType


class ScoreScreen(SceneBase):
    def __init__(self, level, score):
        SceneBase.__init__(self)
        self.level = level
        self.score = score

    def start_game(self):
        self.SwitchToScene(GameScene.GameScene(self.level, self.score))

    def quit_game(self):
        quit()

    def ProcessInput(self, events, pressed_keys):
        pass

    def Update(self):
        pass

    def Render(self, screen):

        screen.fill((0, 0, 0))

        button("Continue", 500, 200, 200, 50, ColorType.Red,
               ColorType.Green, screen, self.start_game)
        button("Quits", 500, 600, 200, 50, ColorType.Red,
               ColorType.Green, screen, self.quit_game)
