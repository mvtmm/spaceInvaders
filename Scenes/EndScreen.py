from Scenes import SplashScreen
from SceneBase import SceneBase
import pygame
from Textboxes import *
from Konstanten import *
from Buttons import *
from Level import *
from Colors import ColorType


class EndScreen(SceneBase):
    def __init__(self, txt):
        self.txt = txt
        SceneBase.__init__(self)
        # Scorelabel
        self.endscreenlabel = TextBox((480, 200, 240, 30), self.txt)

    def menu(self):
        self.SwitchToScene(SplashScreen.SplashScreen())

    def quit_game(self):
        quit()

    def ProcessInput(self, events, pressed_keys):
        pass

    def Update(self):
        pass

    def Render(self, screen):

        screen.fill((0, 0, 0))

        button("Menu", 500, 400, 200, 50, ColorType.Red,
               ColorType.Green, screen, self.menu)
        button("Quits", 500, 600, 200, 50, ColorType.Red,
               ColorType.Green, screen, self.quit_game)

        # Score zeichnen
        self.endscreenlabel.draw(screen)
