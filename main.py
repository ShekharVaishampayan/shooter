import sys
import pygame
import player
import enemy


class Cursor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/cursor.png").convert_alpha()
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.center = pygame.mouse.get_pos()


# initiate pygame
pygame.init()
pygame.mixer.init()

# constants
WIDTH = 1100
HEIGHT = 550

# basic setup
display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("shooter")
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)

# background and score
background = pygame.image.load("images/blue.png").convert()
font_thin = pygame.font.Font("fonts/font_thin.ttf", 24)
font = pygame.font.Font("fonts/font.ttf", 60)

# cursor
cursor = Cursor()
cursors = pygame.sprite.Group()
cursors.add(cursor)

# player
player_obj = player.Player()
player_group = pygame.sprite.Group()
player_group.add(player_obj)

# Bullet initial setup
bullets = pygame.sprite.Group()

enemy_ticks_add = 1500
start_time = 0

# game loop
while True:
    # event loop

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.add(player_obj.shoot())

    if enemy.game_state == "game_on":
        enemy_ticks_add = 1500 - player.score

        # add enemies
        current_time = pygame.time.get_ticks()
        if start_time + enemy_ticks_add < current_time:
            enemy.add_enemy()
            start_time = current_time

        display.blit(background, (0, 0))
        score_text = font_thin.render(f"score: {player.score}", False, (255, 255, 255))
        display.blit(score_text, (20, 20))

        cursors.update()
        cursors.draw(display)

        player_group.update()
        player_group.draw(display)

        enemy.enemies.update()
        enemy.enemies.draw(display)

        bullets.update()
        bullets.draw(display)

    if enemy.game_state == "lose":
        # black out screen
        display.fill((0, 0, 0))

        # game over!
        game_over_text = font.render("GAME OVER!", True, (198, 57, 57))
        game_over_rect = game_over_text.get_rect(center=(550, 275))

        # score
        score_text = font_thin.render(f"score: {player.score}", True, (128, 0, 0))
        score_rect = score_text.get_rect(center=(550, 335))

        display.blit(game_over_text, game_over_rect)
        display.blit(score_text, score_rect)

    pygame.display.update()
    clock.tick(60)
