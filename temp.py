import pygame
import sys
from pygame.locals import *
import time

TOPLEFT = (50,50)
TOPRIGHT = (450,50)
BOTTOMLEFT = (50,450)
BOTTOMRIGHT = (450,450)
PLAYER_LIVES = 3

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
        self.surf = pygame.Surface((9,9))
        self.rect = self.surf.get_rect(center=(50,50))

    def move(self):
        x = self.rect.centerx
        y = self.rect.centery
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
        self.rect = self.surf.get_rect(center=(BOTTOMRIGHT))

    def update(self):
        key = pygame.key.get_pressed()
        if self.rect.centerx < 450:
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
enemies = pygame.sprite.Group()
enemies.add(E1)
sprites = pygame.sprite.Group()
sprites.add(P1)
sprites.add(E1)
font = pygame.font.SysFont("Times New Roman",16)
temp = "Lives:",str(PLAYER_LIVES)
lives = font.render(("Lives: "+str(PLAYER_LIVES)),True,RED)
livesRect = lives.get_rect()
livesRect.topright = (500,0)
lose = font.render('You lost!',True,RED,BLACK)
loseRect = lose.get_rect()
loseRect.center = (250,250)

while True:
    pygame.display.update()
    P1.update()
    E1.move()
    display.fill(BLACK)
    pygame.draw.rect(display, WHITE, (50, 50, 400, 400), 1)
    P1.draw(display)
    E1.draw(display)
    lives = font.render(("Lives: "+str(PLAYER_LIVES)), True, RED)
    display.blit(lives,livesRect)
    pygame.display.update()
    FPS.tick(50)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    if pygame.sprite.spritecollideany(P1, enemies):
        if PLAYER_LIVES <= 1:
            display.blit(lose,loseRect)
            pygame.display.update()
            time.sleep(4)
            pygame.quit()
            sys.exit()
        else:
            PLAYER_LIVES -= 1
            # TODO:Move sparx, keep player in initial spot.
