from assets import *
from settings import SCREEN_WIDTH
import pygame


class Snail(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surface = snail_surface
        # Rectangles allow for more efficient surface positioning, movement, and checking for collisions
        # get_rect draws a rectangle around the surface
        # if no kwaargs are given, (0, 0) is used
        # Can use points topleft, midtop, topright, midleft, center, etc like topleft=()
        # or place sides like left, right etc
        # Can also use width and height
        # These keywords can also be used to access points on the rect
        self.rect = self.surface.get_rect(
            bottom=sky_surface.get_height(),
            right=SCREEN_WIDTH-50
        )

    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right <= 0:
            self.rect.left = SCREEN_WIDTH


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surface = player_surface
        self.rect = self.surface.get_rect(
            bottom=sky_surface.get_height(),
            left=50
        )
    
    def update(self):
        pass