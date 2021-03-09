import pygame
import sys
from pygame.locals import *

pygame.init()

RED = pygame.Color(255,0,0)
BLUE = pygame.Color(0,0,255)
GREEN = pygame.Color(0,255,0)
WHITE = pygame.Color(255,255,255)
BLACK = pygame.Color(0,0,0)

#Display window
display = pygame.display.set_mode((500,500))
pygame.display.set_caption("Poggers")

#FPS
FPS = pygame.time.Clock()
FPS.tick(30)

#First enemy
class Sparx(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("spark.png")
        self.surf = pygame.Surface((5,5))
        self.rect = self.surf.get_rect(center=(50,50))

    def move(self):
        x = self.rect.centerx
        y = self.rect.centery
        print(x,y)
        if y == 50:
            if x < 450:
                self.rect.move_ip(5,0)
            else:
                self.rect.move_ip(0,5)
        if x == 450:
            if y < 450:
                self.rect.move_ip(0,5)
            else:
                self.rect.move_ip(-5,0)
        if y == 450:
            if x > 50:
                self.rect.move_ip(-5,0)
            else:
                self.rect.move_ip(0,-5)
        if x == 50:
            if y > 50:
                self.rect.move_ip(0,-5)
            else:
                self.rect.move_ip(5,0)


    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("player.png")
        self.surf = pygame.Surface((10,10))
        self.rect = self.surf.get_rect()

    def update(self):
        key = pygame.key.get_pressed()
        if self.rect.centerx < 400:
            if key[K_RIGHT]:
                self.rect.move_ip(5,0)
        if self.rect.centerx > 50:
            if key[K_LEFT]:
                self.rect.move_ip(-5,0)
        if self.rect.centerx == 50 or self.rect.centerx == 450:
            if self.rect.centery > 50:
                if key[K_UP]:
                    self.rect.move_ip(0, -5)
            if self.rect.centery < 450:
                if key[K_DOWN]:
                    self.rect.move_ip(0,5)
    def draw(self, surface):
        surface.blit(self.image, self.rect)


P1 = Player()
E1 = Sparx()

while True:
    pygame.display.update()
    P1.update()
    E1.move()
    display.fill(BLACK)
    pygame.draw.rect(display, WHITE, (50, 50, 400, 400), 1)
    P1.draw(display)
    E1.draw(display)
    pygame.display.update()
    FPS.tick(50)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


