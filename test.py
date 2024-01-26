import pygame
import sys
import time
import random
from pygame.locals import *

pygame.init()
pygame.display.set_caption("Test Morgane !")
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

WIDTH, HEIGHT = screen.get_width(), screen.get_height()

clock = pygame.time.Clock()

#############

### Font

font = pygame.font.SysFont("sherif", 40)

### Colors

RED = (255, 0, 0)
DARK_RED = (180, 0, 0)
YELLOW = (255,235,42)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
GRAYISH = (150, 150, 150)
DARK_GRAY = (100, 100, 100)
GREEN = (0, 128, 0)
BROWN = (83, 61, 50)

#############

player = pygame.Rect(500, 400, 50, 50)

pickup = pygame.Rect(300, 500, 30, 30)

floor = pygame.Rect(0, HEIGHT - 80, WIDTH, 50)

chrono = time.time()

class game:
    velocity = 0
    game_max_time = 5
    score = 0

#############


def game_draw_window():
    screen.fill(GRAY)

    pygame.draw.rect(screen, DARK_RED, player)
    
    pygame.draw.rect(screen, GREEN, pickup)

    pygame.draw.rect(screen, BLACK, floor)

    score_text = font.render(f"Score : {game.score}", 1, BLACK)
    screen.blit(score_text, (10, 10))

    chrono_text = font.render(f"{game.game_max_time - (time.time() - chrono):.2f} s", 1, BLACK)
    screen.blit(chrono_text, (10, 40))

    pygame.display.update()


def main_game():
    run = True
    left = False
    right = False
    while run:
        clock.tick(60)

        game.velocity += 1
        player.y += game.velocity

        if player.bottom >= floor.y:
            game.velocity = -35
            player.bottom = floor.y

        if left:
            player.x -= 20
        if right:
            player.x += 20

        if player.colliderect(pickup):
            new_x = random.random() * WIDTH
            pickup.x = new_x
            game.score += 1

        if game.game_max_time - (time.time() - chrono) <= 0:
            game_over()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False
                    pygame.quit()
                    sys.exit()
                if event.key == K_q:
                    left = True
                if event.key == K_d:
                    right = True
            if event.type == KEYUP:
                if event.key == K_q:
                    left = False
                if event.key == K_d:
                    right = False
        
        game_draw_window()


#####################


def game_over_draw_window():
    screen.fill(GRAY)

    score_text = font.render(f"Score : {game.score}", 1, BLACK)
    screen.blit(score_text, (WIDTH//2, HEIGHT//2))

    pygame.display.update()


def game_over():
    run = True
    while run:
        clock.tick(60)



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False
                    pygame.quit()
                    sys.exit()
        
        game_over_draw_window()


main_game()