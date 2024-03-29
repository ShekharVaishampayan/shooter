import pygame
import random


# enemies initial setup
enemies = pygame.sprite.Group()
game_state = "game_on"


# add enemy function
def add_enemy():
    enemies.add(Enemy())


# enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/enemy.png")
        self.rect = self.image.get_rect()
        self.speed = 5
        self.lose_sound = pygame.mixer.Sound("sounds/sfx_lose.ogg")

        # get center
        self.rect.centerx = random.randint(10, 1090)
        self.rect.bottom = 0

    def update(self):
        global game_state
        self.rect.y += self.speed

        if self.rect.top > 550:
            self.kill()
            self.lose_sound.play()
            game_state = "lose"
            pygame.mouse.set_visible(True)
