import pygame
from pygame.locals import *


# Initializes pygame
pygame.init()

# Initializes Pygame Audio Mixer
pygame.mixer.init()

# loading images


screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("Qix")

main_background = pygame.image.load('img/main_background.png')
main_background = pygame.transform.scale(main_background, (800,800))


game_state = 0 # Main Screen

running = True
while running:
    if game_state == 0:
        screen.blit(main_background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()