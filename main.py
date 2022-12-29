from settings import * 
import sys
import pygame  

# Initializes the library
pygame.init()
# Helps in tracking time
clock = pygame.time.Clock()
# Makes a display surface that is displayed as the base
# A regular surface is an object that is on the display surface
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# Sets a title for the window
pygame.display.set_caption("Dino but in Pygame")

import assets
import sprites

# Returns a surface
# Anti-Alias means to smooth the edges of the text (shouldnt be used with pixel art)
score = assets.pixel_font.render("Heyo", False, (255, 0, 0))
x = 600
# Game loop that draws each frame till the game window is closed
while True:
    x -= 5
    # Event loop that iterates through all events that were triggered
    for event in pygame.event.get():
        # If the "X" button is pressed
        if event.type == pygame.QUIT:
            # Exits the python interpreter completely and is better than pygame.quit since it instantly closes everything
            sys.exit()

    # Used to transfer a surface to the display surface
    # Note: surfaces previously blitted to the screen get drawn over
    screen.blit(assets.sky, (0, 0))
    screen.blit(assets.ground, (
        0, 
        assets.sky.get_height()
    ))
    screen.blit(score, ((SCREEN_WIDTH-score.get_width())/2, 50))
    if x <= 0:
        x = 600
    screen.blit(assets.snail, (x, 250))

    # Updates the screen
    pygame.display.flip()
    # Sets maximum frame rate limit
    clock.tick(FPS)
