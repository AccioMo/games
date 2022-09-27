from shutil import move
import pygame
from sys import exit

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

pieces = [kingW, kingB, queenW, queenB, bishopW, bishopB, knightW, knightB, rookW, rookB, pawnW, pawnB]

# class Piece:
#     def move(self):
#         for p in pieces:
            
screen.blit(chess_surf, (0, 0))
screen.blit(rookW, (7, 7))
screen.blit(knightW, (82, 7)) 
screen.blit(bishopW, (157, 7))
screen.blit(kingW, (232, 7))  
screen.blit(queenW, (307, 7))
screen.blit(bishopW, (382, 7))
screen.blit(knightW, (457, 7))
screen.blit(rookW, (532, 7))
screen.blit(pawnW, (7, 82))
screen.blit(pawnW, (82, 82)) 
screen.blit(pawnW, (157, 82))
screen.blit(pawnW, (232, 82))
screen.blit(pawnW, (307, 82))
screen.blit(pawnW, (382, 82))
screen.blit(pawnW, (457, 82))
screen.blit(pawnW, (532, 82))

screen.blit(rookB, (7, 533))
screen.blit(knightB, (82, 533)) 
screen.blit(bishopB, (157, 533))
screen.blit(kingB, (232, 533))  
screen.blit(queenB, (307, 533))
screen.blit(bishopB, (382, 533))
screen.blit(knightB, (457, 533))
screen.blit(rookB, (532, 533))
screen.blit(pawnB, (7, 458))
screen.blit(pawnB, (82, 458)) 
screen.blit(pawnB, (157, 458))
screen.blit(pawnB, (232, 458))
screen.blit(pawnB, (307, 458))
screen.blit(pawnB, (382, 458))
screen.blit(pawnB, (457, 458))
screen.blit(pawnB, (532, 458))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()



    
    for p in pieces: 
        if event.type == pygame.MOUSEBUTTONDOWN and p.collidepoint(pygame.mouse.get_pos()):
            p.pos = pygame.mouse.get_pos()


    pygame.display.update()
    clock.tick(60)