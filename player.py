import pygame
import random
from enemy import enemies

# initial setup
BULLET_SPEED = 10
BULLET_OFFSET = [-50, 50]
score = 0


# player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/playerShip.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = [550, 500]
        self.laser_sounds = [pygame.mixer.Sound("sounds/sfx_laser1.ogg"),
                             pygame.mixer.Sound("sounds/sfx_laser2.ogg")]

    def update(self):
        self.rect.centerx = pygame.mouse.get_pos()[0]

    def shoot(self):
        random.choice(self.laser_sounds).play()
        return Bullet(self.rect.center)


# bullet class
class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("images/laser.png")
        self.offset = random.choice(BULLET_OFFSET)
        self.rect = self.image.get_rect(center=(pos[0] + self.offset, pos[1]))

    def update(self):
        global score

        self.rect.y -= BULLET_SPEED
        if self.rect.bottom < 0:
            self.kill()
        collided = pygame.sprite.spritecollide(self, enemies, True)
        if collided:
            score += 1
