from shutil import move
from threading import local
from tkinter import W
import pygame
from sys import exit
import itertools

pygame.init()

screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()

piece_selected = False
piece_selectedB = False

chess_surf = pygame.image.load('graphics/chess.png').convert_alpha()
kingW = pygame.image.load('graphics/kingW.png').convert_alpha()
kingB = pygame.image.load('graphics/kingB.png').convert_alpha() 
queenW = pygame.image.load('graphics/queenW.png').convert_alpha()
queenB = pygame.image.load('graphics/queenB.png').convert_alpha()
bishopW = pygame.image.load('graphics/bishopW.png').convert_alpha()
bishopB = pygame.image.load('graphics/bishopB.png').convert_alpha()
knightW = pygame.image.load('graphics/knightW.png').convert_alpha()
knightB = pygame.image.load('graphics/knightB.png').convert_alpha()
rookW = pygame.image.load('graphics/rookW.png').convert_alpha()
rookB = pygame.image.load('graphics/rookB.png').convert_alpha()
pawnW = pygame.image.load('graphics/pawnW.png').convert_alpha()
pawnB = pygame.image.load('graphics/pawnB.png').convert_alpha()

piecesA = [rookW, knightW, bishopW, kingW, queenW, bishopW, knightW, rookW, pawnW, pawnW, pawnW, pawnW, pawnW, pawnW, pawnW, pawnW]
piecesB = [rookB, knightB, bishopB, kingB, queenB, bishopB, knightB, rookB, pawnB, pawnB, pawnB, pawnB, pawnB, pawnB, pawnB, pawnB]

p_rectA = []
p_rectB = []

x1 = 7
for rectA in piecesA[0:8:]:
    p_rectA.append(rectA.get_rect(topleft=(x1, 533)))
    x1 += 75
x1 = 7
for rectA in piecesA[8:16:]:
    p_rectA.append(rectA.get_rect(topleft=(x1, 458)))
    x1 += 75

x1 = 7
for rectB in piecesB[0:8:]:
    p_rectB.append(rectB.get_rect(topleft=(x1, 7)))
    x1 += 75
x1 = 7
for rectB in piecesB[8:16:]:
    p_rectB.append(rectB.get_rect(topleft=(x1, 82)))
    x1 += 75

class PiecesA:
    def loc(self):
        for pA, p_A in itertools.zip_longest(piecesA, p_rectA):
            screen.blit(pA, p_A)
    def move(self):
        for sltd_A in p_rectA:
            if event.type == pygame.MOUSEBUTTONDOWN and sltd_A.collidepoint(pygame.mouse.get_pos()):
                global piece_selected
                global piecd
                piecd = sltd_A
                piece_selected = True
            if piece_selected:
                piecd.center = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONUP:
                    return True
                    

class PiecesB:
    def loc(self):
        for pB, p_B in itertools.zip_longest(piecesB, p_rectB):
            screen.blit(pB, p_B)
    def move(self):
        for sltd_B in p_rectB:
            if event.type == pygame.MOUSEBUTTONDOWN and sltd_B.collidepoint(pygame.mouse.get_pos()):
                global piece_selectedB
                global piecd
                piecd = sltd_B
                piece_selectedB = True
            if piece_selectedB:
                piecd.center = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONUP:
                    return True

WhiteTurn = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(chess_surf, (0, 0))

    PiecesA.loc(x1)
    PiecesB.loc(x1)

    if WhiteTurn:
        PiecesA.move(x1)
        if PiecesA.move(x1) is True:
            WhiteTurn = False
            piece_selected = False
            print("black")

    else:
        PiecesB.move(x1)
        if PiecesB.move(x1) is True:
            WhiteTurn = True
            piece_selectedB = False
            print("white")

    pygame.display.update()
    clock.tick(60)
    