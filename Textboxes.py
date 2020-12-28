from Konstanten import *
import pygame


class TextBox:

    FONT = pygame.font.Font(None, 32)

    def __init__(self, rect, text=''):
        self.rect = pygame.Rect(rect)
        self.color = pygame.Color(20, 200, 20)
        self.text = text
        self.txt_surface = pygame.font.Font(
            None, 32).render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = pygame.Color(200, 200, 20)

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)
