import pygame, sys
from pygame.locals import *

# set up pygame
pygame.init()

# set up the window
window_surface = pygame.display.set_mode( (500, 400), 0, 32 )
pygame.display.set_caption("Hello world!")

# set up the colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

# set up the fonts
basic_font = pygame.font.SysFont(None, 48)

# set up the text
text = basic_font.render("Hello world!", True, WHITE, BLUE)
text_rect = text.get_rect()
text_rect.centerx = window_surface.get_rect().centerx
text_rect.centery = window_surface.get_rect().centery

# draw the white background onto the surface
window_surface.fill(WHITE)

# draw a green polygon onto the surface
pygame.draw.polygon(window_surface, GREEN, ((146,0), (291, 106), (236, 277), (56, 277), (0, 106)))

# draw some blue lines ontot the surface
pygame.draw.line(window_surface, BLUE, (60, 60), (120, 60), 4)
pygame.draw.line(window_surface, BLUE, (120, 60), (60, 120))
pygame.draw.line(window_surface, BLUE, (60, 120), (120, 120), 4)

# draw a blue circle onto the surface
pygame.draw.circle(window_surface, BLUE, (300, 50), 20, 0)


# ==============================================================================

# draw the window onto the screen
pygame.display.update()

# run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
