from Scenes import GameScene
from SceneBase import SceneBase
import pygame
from Textboxes import *
from Konstanten import *
from Buttons import *
from Level import *
from Colors import *

class SplashScreen(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)

    def start_game(self):
        self.SwitchToScene(GameScene.GameScene(None, 0))

    def quit_game(self):
        quit()

    def ProcessInput(self, events, pressed_keys):
        pass

    def Render(self, screen):
        screen.fill((255, 250, 250))
        button("Start Game", 500, 200, 200, 50, ColorType.Red,
               ColorType.Green, screen, self.start_game)
        button("Quit", 500, 600, 200, 50, ColorType.Red,
               ColorType.Green, screen, self.quit_game)
