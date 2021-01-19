import pygame
import os
from config import *

pygame.font.init()
pygame.mixer.init()
pygame.display.init()
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Game by Tao")
bg = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'background-darkmatter.jpg')), (WIDTH, HEIGHT))

BORDER = pygame.Rect(WIDTH//2 -15 , 0, 15 , HEIGHT) #( left, top, width, height))

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('assets', 'spaceship_yellow.png'))
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('assets', 'spaceship_red.png'))

PLAYERONE = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)
PLAYERTWO = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join('assets', 'gunfire.wav'))
BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('assets', 'hitmarker.wav'))

P1_HIT = pygame.USEREVENT + 1
P2_HIT = pygame.USEREVENT + 2

HP_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 85)

def handle_p1_movement(keys_pressed, p1):
        if keys_pressed[pygame.K_a] and p1.x - VELOCITY > 0: #LEFT
            p1.x -= VELOCITY
        if keys_pressed[pygame.K_d] and p1.x + VELOCITY + p1.width < BORDER.x: #RIGHT
            p1.x += VELOCITY
        if keys_pressed[pygame.K_w] and p1.y - VELOCITY > 0: #UP
            p1.y -= VELOCITY
        if keys_pressed[pygame.K_s] and p1.y + VELOCITY + MOVEMENT_BUFFER < HEIGHT: #DOWN
            p1.y += VELOCITY

def handle_p2_movement(keys_pressed, p2):
        if keys_pressed[pygame.K_LEFT] and p2.x - VELOCITY > BORDER.x + p2.width: #LEFT
            p2.x -= VELOCITY
        if keys_pressed[pygame.K_RIGHT] and p2.x + VELOCITY + p2.width < WIDTH: #RIGHT
            p2.x += VELOCITY
        if keys_pressed[pygame.K_UP] and p2.y - VELOCITY > 0: #UP
            p2.y -= VELOCITY
        if keys_pressed[pygame.K_DOWN] and p2.y + VELOCITY + MOVEMENT_BUFFER < HEIGHT: #DOWN
            p2.y += VELOCITY


def handle_bullets(p1_bullets, p2_bullets, p1, p2):
    for bullet in p1_bullets:
        bullet.x += BULLET_VELOCITY
        if p2.colliderect(bullet):
            pygame.event.post(pygame.event.Event(P2_HIT))
            p1_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            p1_bullets.remove(bullet)
    for bullet in p2_bullets:
        bullet.x -= BULLET_VELOCITY
        if p1.colliderect(bullet):
            pygame.event.post(pygame.event.Event(P1_HIT))
            p2_bullets.remove(bullet)
        elif bullet.x < 0:
            p2_bullets.remove(bullet)



def draw_window(p1, p2, p1_bullets, p2_bullets, P1_HP, P2_HP):
    WINDOW.blit(bg, (0, 0))
    pygame.draw.rect(WINDOW, BLACK, BORDER)

    P1_HP_TXT = HP_FONT.render("HP: " + str(P1_HP), 1, WHITE)
    P2_HP_TXT = HP_FONT.render("HP: " + str(P2_HP), 1, WHITE)
    WINDOW.blit(P1_HP_TXT, (WIDTH - P1_HP_TXT.get_width() - 10, 10))
    WINDOW.blit(P2_HP_TXT, (10, 10))
    
    WINDOW.blit(PLAYERONE, (p1.x, p1.y))
    WINDOW.blit(PLAYERTWO, (p2.x, p2.y))

    for bullet in p1_bullets:
        pygame.draw.rect(WINDOW, YELLOW, bullet)
    for bullet in p2_bullets:
        pygame.draw.rect(WINDOW, RED, bullet)

    pygame.display.update()


def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WINDOW.blit(draw_text, (WIDTH//2 - draw_text.get_width()//2, HEIGHT//2 - draw_text.get_height()//2))
    pygame.display.update()

def main():
    p1 = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    p2 = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    
    p1_bullets = []
    p2_bullets = []
    P1_HP = BASEHP
    P2_HP = BASEHP
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(p1_bullets) < AMMO:
                    bullet = pygame.Rect(p1.x + p1.width, p1.y + p1.height//2 - 2, 10, 5)
                    p1_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play(0)
                if event.key == pygame.K_RCTRL and len(p2_bullets) < AMMO:
                    bullet = pygame.Rect(p2.x, p2.y + p2.height//2 - 2, 10, 5)
                    p2_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play(0)
            if event.type == P1_HIT:
                P1_HP -= 1
                BULLET_HIT_SOUND.play()
            if event.type == P2_HIT:
                P2_HP -= 1
                BULLET_HIT_SOUND.play()
        winner_text = ""
        if P1_HP <= 0:
            winner_text = "Player Two Wins!"
        if P2_HP <= 0:
            winner_text = "Player One Wins!"
        if winner_text != "":
            draw_winner(winner_text)
            if event.type == pygame.KEYDOWN:
                break

        keys_pressed = pygame.key.get_pressed()
        handle_p1_movement(keys_pressed, p1)
        handle_p2_movement(keys_pressed, p2)
        handle_bullets(p1_bullets, p2_bullets, p1, p2)

        draw_window(p1, p2, p1_bullets, p2_bullets, P2_HP, P1_HP)

    pygame.quit()


if __name__ == "__main__":
    while True:
        main()