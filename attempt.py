from gettext import dgettext
import math
from os import truncate
import random
from random import randint, randrange
from sqlite3 import Cursor
from tkinter import Y
import pygame
from sys import exit

# initiate pygame
pygame.init()
game_active = False
# screen size
screen = pygame.display.set_mode((800, 600))
# game title
pygame.display.set_caption("The Isles")

clock = pygame.time.Clock()

SPAWN_TIMER = pygame.USEREVENT
pygame.time.set_timer(SPAWN_TIMER, 1000)

test_font = pygame.font.SysFont('sitkaheading', 50)

space_surface = pygame.image.load('graphics/space.png').convert()
spaceA_rect = space_surface.get_rect(bottom = 600)
spaceB_rect = space_surface.get_rect(bottom = spaceA_rect.top)

# text stuff
game_over_text = test_font.render("GAME OVER", False, 'White')
start_text = test_font.render("Start Game", False, 'White')
quit_text = test_font.render("Quit", False, 'White')

start_text_rect = start_text.get_rect(topleft=(250, 300))

# player stuff
player_surf = pygame.image.load('graphics/ship.png').convert_alpha()
player_rect = player_surf.get_rect(center=(400, 520))

bullet_surf = pygame.image.load('graphics/bullet1.png').convert_alpha()

bullet_list = []

def fire_bullet(bullet_list):                                           # We add the bullet_rect here
    for bullet_rect in bullet_list:                                     # But we assign it a name here
        bullet_rect.y -= 12                                              # Each loop a new bullet is added and given the same name
        screen.blit(bullet_surf, bullet_rect)                           # Which works since lists allow duplicates
    bullet_list = [bullet for bullet in bullet_list if bullet.y > -50]
    return bullet_list

# enemy stuff
enemy_list = []

enemy_surf = pygame.image.load('graphics/enemy.png').convert_alpha()

class Enemies:
    def __init__(self):
        self.x = random.randrange(50, 750, 50)
        self.y = random.randint(-300, 0)
        self.speed = 5
    def add_enemy(self):
        # if enemy_list:
        #     for enemy in enemy_list:
        #         if new_enemy.x == enemy.x:
        #             enemy_list.remove(enemy)
        #         else: enemy_list.append(enemy_surf.get_rect(center=(self.x, self.y)))
        # else: 
        enemy_list.append(enemy_surf.get_rect(center=(self.x, self.y)))
    def enemy_move(self):
        global enemy_rect
        enemy_rect.y += 5
        if enemy_rect.y < player_rect.y:
            dx = player_rect.x - enemy_rect.x
            dy = player_rect.y - enemy_rect.y
            dz = math.hypot(dx, dy)
            dx = dx / dz
            enemy_rect.x += dx * self.speed
        screen.blit(enemy_surf, enemy_rect)
    def enemy_clear(self):
        global enemy_list
        # for enemy in enemy_list:                                          # My Idea
        #     if enemy.y > 400:
        #         enemy_list.remove(enemy)
        enemy_list = [enemy for enemy in enemy_list if enemy.y < 700]       # Better Idea from Internet
        for bullet_rect in bullet_list:
                if bullet_rect.colliderect(enemy_rect):
                    print("HIT ENEMY")
                enemy_list = [enemy for enemy in enemy_list if not enemy.colliderect(bullet_rect)]
        return enemy_list
    def colision(self):
        for enemy_rect in enemy_list:
            if enemy_rect.colliderect(player_rect):
                enemy_list.clear()
                bullet_list.clear()
                return False
            else: return True

# THE GAME LOOP #

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == SPAWN_TIMER:
            new_enemy = Enemies()
            new_enemy.add_enemy()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet_list.append(bullet_surf.get_rect(center=player_rect.center))
        if event.type == pygame.KEYDOWN and pygame.K_SPACE and not game_active:
            game_active = True
    
# graphics stuff
    if game_active:
        screen.blit(space_surface, spaceA_rect)
        screen.blit(space_surface, spaceB_rect)
        spaceA_rect.y += 4
        if spaceA_rect.top > 600:
            spaceA_rect.bottom = spaceB_rect.top
        spaceB_rect.y += 4
        if spaceB_rect.top > 600:
            spaceB_rect.bottom = spaceA_rect.top
        
        screen.blit(player_surf, player_rect)

    # controls
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and player_rect.right < 790:
            player_rect.x += 6
        if keys[pygame.K_LEFT] and player_rect.left > 10:
                player_rect.x -= 6
        if keys[pygame.K_UP] and player_rect.top > 0:
            player_rect.y -= 2
        if keys[pygame.K_DOWN] and player_rect.bottom < 600:
            player_rect.y += 6
        # if keys[pygame.K_SPACE]:
        #     Bullet.add_bullet(bullet_list)

    # enemy related
        if bullet_list:
            fire_bullet(bullet_list)
        else:
            pass

        if enemy_list:
            for enemy_rect in enemy_list:
                Enemies.enemy_move(new_enemy)
            Enemies.enemy_clear(enemy_list) # cleaning
            Enemies.colision(enemy_list)
            game_active = Enemies.colision(enemy_list)
        else:
            pass
        
    else:
        screen.blit(space_surface, spaceA_rect)
        screen.blit(space_surface, spaceB_rect)
        screen.blit(start_text, start_text_rect)
        screen.blit(game_over_text, (250, 200))
        screen.blit(quit_text, (250, 400))
        spaceA_rect.y += 1
        if spaceA_rect.top > 600:
            spaceA_rect.bottom = spaceB_rect.top
        spaceB_rect.y += 1
        if spaceB_rect.top > 600:
            spaceB_rect.bottom = spaceA_rect.top

        if start_text_rect.collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN:
            game_active = True

    pygame.display.update()
    clock.tick(60)
