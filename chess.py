from shutil import move
import pygame
from sys import exit
import itertools

pygame.init()

screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()

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

# rookW_rect = rookW.get_rect(topleft=(7, 7))
# knightW_rect = knightW.get_rect(topleft=(82, 7))
# bishopW_rect = bishopW.get_rect(topleft=(157, 7))
# kingW_rect = kingW.get_rect(topleft=(232, 7))
# queenW_rect = queenW.get_rect(topleft=(307, 7))
# bishopW_rect = bishopW.get_rect(topleft=(382, 7))
# knightW_rect = knightW.get_rect(topleft=(457, 7))
# rookW_rect = rookW.get_rect(topleft=(532, 7))

# rookB_rect = rookB.get_rect(topleft=(7, 533))
# knightB_rect = knightB.get_rect(topleft=(82, 533)) 
# bishopB_rect = bishopB.get_rect(topleft=(157, 533))
# kingB_rect = kingB.get_rect(topleft=(232, 533))    
# queenB_rect = queenB.get_rect(topleft=(307, 533))
# bishopB_rect = bishopB.get_rect(topleft=(382, 533))
# knightB_rect = knightB.get_rect(topleft=(457, 533))
# rookB_rect = rookB.get_rect(topleft=(532, 533))

piecesA = [rookW, knightW, bishopW, kingW, queenW, bishopW, knightW, rookW]
piecesB = [rookB, knightB, bishopB, kingB, queenB, bishopB, knightB, rookB]
# pieces_rectA = [rookW_rect, knightW_rect, bishopW_rect, kingW_rect, queenW_rect, bishopW_rect, knightW_rect, rookW_rect]
# pieces_rectB = [rookB_rect, knightB_rect, bishopB_rect, kingB_rect, queenB_rect, bishopB_rect, knightB_rect, rookB_rect]

# for x in piecesA:
#     x _rect = x.get_rect(topleft=(str(y), 533))
#     y += 75

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
 
    # for p in pieces: 
    #     if event.type == pygame.MOUSEBUTTONDOWN and p.collidepoint(pygame.mouse.get_pos()):
    #         p.pos = pygame.mouse.get_pos()

    x1 = 7
    for pA in piecesA[0:8:]:
        screen.blit(pA, pA.get_rect(topleft=(x1, 533)))
        x1 += 75

    x1 = 7
    for pB in piecesB:
        screen.blit(pB, pB.get_rect(topleft=(x1, 7)))
        x1 += 75

    pygame.display.update()
    clock.tick(60)