import pygame
from Konstanten import *

# Textobjekt erstellen mit Farbe und Schriftart


def text_objects(text, font):
    text_surface = font.render(text, True, (255, 255, 255))
    return text_surface


def button(text, x, y, width_btn, height_btn, active_color, inactive_color, screen, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # Hovereffekt Farbwechsel
    if x < mouse[0] < x + width_btn and y < mouse[1] < y + height_btn:
        pygame.draw.rect(screen, active_color.value,
                         (x, y, width_btn, height_btn))
        if click[0] == 1 and action != None:
            action()

    else:
        pygame.draw.rect(screen, inactive_color.value,
                         (x, y, width_btn, height_btn))
    # Schriftgröße festlegen
    text_font_small = pygame.font.Font(None, 32)
    text_surface = text_objects(text, text_font_small)
    # Schrift zentrieren im Rect
    text_rect = text_surface.get_rect(
        center=((x + (width_btn / 2)), (y + (height_btn / 2))))
    # Button erzeugen
    screen.blit(text_surface, text_rect)
