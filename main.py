from settings import * 
import sys
import pygame  
# Module containing constants for keyboard input
from pygame.locals import KEYDOWN, K_SPACE

# Initializes the library
pygame.init()
# Helps in tracking time
clock = pygame.time.Clock()
# Makes a display surface that is displayed as the base
# A regular surface is an object that is on the display surface
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# Sets a title for the window
pygame.display.set_caption("Dino but in Pygame")

from assets import *
from sprites import *

# Returns a surface
# Anti-Alias means to smooth the edges of the text (shouldnt be used with pixel art)
# The pygame.draw module is used to display shapes and lines
score = 0
score_surface = pixel_font.render(f"Score: {score}", False, (64, 64, 64))
score_rect = score_surface.get_rect(
    center=(SCREEN_WIDTH / 2, 50)
)

snail = Snail()
player = Player()

# Game loop that draws each frame till the game window is closed
while True:
    # Event loop that iterates through all events that were triggered
    for event in pygame.event.get():
        # If the "X" button is pressed
        if event.type == pygame.QUIT:
            # Exits the python interpreter completely and is better than pygame.quit since it instantly closes everything
            sys.exit()
        # if event.type == pygame.MOUSEMOTION:
        #     if player.rect.collidepoint(event.pos):
        #         print("collision of mouse with player")
        # Checks if a key is pressed and whether or not that key is the space bar
        elif event.type == KEYDOWN and event.key == K_SPACE:
            player.gravity = -20

    snail.update()
    # .colliderect() Returns a 0 or 1 depending on whether or not the two rects are colliding
    # .collidepoint() checks collision between point and rect
    # Two ways to get mouse position: 1. In the event handler 2. Using pygame.mouse.get_pos()
    # if player.rect.colliderect(snail.rect):
    #     print("collision of snail with player")

    # Used to transfer a surface to the display surface
    # A surface is drawn in the position of its rectangle
    # Note: surfaces previously blitted to the screen get drawn over
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (
        0, 
        sky_surface.get_height()
    ))
    screen.blit(score_surface, score_rect)
    screen.blit(snail.surface, snail.rect)

    player.gravity += 1
    player.rect.move_ip((0, player.gravity))

    screen.blit(player.surface, player.rect)
    # Updates the screen
    pygame.display.flip()
    # Sets maximum frame rate limit
    clock.tick(FPS)
