import pygame

# Loads image as a surface and converts it to blit it faster, "alpha" also preserves alpha / transparent particles
sky_surface = pygame.image.load("assets/img/sky.png").convert_alpha()
ground_surface = pygame.image.load("assets/img/ground.png").convert_alpha()
snail_surface = pygame.image.load("assets/img/snail/snail1.png").convert_alpha()
player_surface = pygame.image.load("assets/img/player/player_walk_1.png").convert_alpha()
# Loads the font
pixel_font = pygame.font.Font("assets/font/Pixeltype.ttf", 50)