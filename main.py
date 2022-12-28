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

# Loads image as a surface and converts it to blit it faster
sky_surface = pygame.image.load("assets/img/sky.png").convert()
ground_surface = pygame.image.load("assets/img/ground.png").convert()
# Loads the font
font = pygame.font.Font("assets/font/Pixeltype.ttf", 50)
# Returns a surface
# Anti-Alias means to smooth the edges of the text (shouldnt be used with pixel art)
score = font.render("Heyo", False, (255, 0, 0))

# Game loop that draws each frame till the game window is closed
while True:
    # Event loop that iterates through all events that were triggered
    for event in pygame.event.get():
        # If the "X" button is pressed
        if event.type == pygame.QUIT:
            # Exits the python interpreter completely and is better than pygame.quit since it instantly closes everything
            sys.exit()

    # Used to transfer a surface to the display surface
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (
        0, 
        sky_surface.get_height()
    ))
    screen.blit(score, ((SCREEN_WIDTH-score.get_width())/2, 50))

    # Updates the screen
    pygame.display.flip()
    # Sets maximum frame rate limit
    clock.tick(FPS)
