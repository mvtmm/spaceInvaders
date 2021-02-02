from enum import Enum

# Farben
class ColorType(Enum):
    Black           = (  0,   0,   0)
    White           = (255, 255, 255)
    Red             = (255,   0,   0)
    Blue            = (  0,   0, 255)
    Green           = (  0, 255,   0)
    Yellow          = (255, 255,   0)
    active_color    = (255, 0, 0)

