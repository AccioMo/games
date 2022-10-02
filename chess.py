from cmath import pi
from shutil import move
from threading import local
from tkinter import W, Y
from urllib.parse import parse_qsl
from xml.sax import parseString
import pygame
from sys import exit
import itertools
import math

pygame.init()

screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()

yies = [7, 82, 157, 232, 307, 382, 457, 532]
xies = [7, 82, 157, 232, 307, 382, 457, 532]

hop = 75

White_touched = False
Black_touched = False

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
y1 = 532
for rectA in piecesA:
    p_rectA.append(rectA.get_rect(topleft=(x1, y1)))
    x1 += hop
    if x1 == 607:
        x1 = 7
        y1 -= hop

x1 = 7
y1 = 7
for rectB in piecesB:
    p_rectB.append(rectB.get_rect(topleft=(x1, y1)))
    x1 += hop
    if x1 == 607:
        x1 = 7
        y1 += hop

def fuckoff(shit):
    shit.x = originX
    shit.y = originY
    return True

# Positioning piece in center of square:
def checkinXY(zing):
    dx = 600
    dy = 600
    for x in xies:
        if abs(zing.x - x) <= abs(dx):
            dx = zing.x - x
    global destX
    destX = zing.x - dx
    for y in yies:
        if abs(zing.y - y) <= abs(dy):
            dy = zing.y - y
    global destY
    destY = zing.y - dy

# Checking for pieces on square:
def checkinCollide(zing, zist):
    for piece in zist:
        if piece and (piece.x == destX and piece.y == destY) or (destX == originX and destY == originY):
            zing.x = originX
            zing.y = originY
            return True
        else:
            pass

# Gobbling:
def checkinKilled(zist):
    for piece in zist:
        if piece and piece.x == destX and piece.y == destY:
            global i
            i = zist.index(piece)
            return True
        else:
            pass
def horsies(nox, noy):
    ss = [1, -1]
    for s in ss:
        for sss in ss:
            if destX == originX + hop*nox*s*sss and destY == originY + hop*noy*s:
                return True

def checkinWho(zing, zist):
    if zist.index(zing) == 0 or zist.index(zing) == 7:
        if originX == destX or originY == destY:
            pass
        else:
            print("that's not how rooks move")
            zing.x = originX
            zing.y = originY
            return True
    elif zist.index(zing) == 1 or zist.index(zing) == 6:
        if horsies(2, 1) or horsies(1, 2):
            pass
        else:
            print("that's not how knights move")
            zing.x = originX
            zing.y = originY
            return True

    elif zist.index(zing) == 2 or zist.index(zing) == 5:
        biV = pygame.math.Vector2(abs(destX - originX), abs(destY - originY))
        biV0 = pygame.math.Vector2(hop, hop)
        if biV.normalize() == biV0.normalize():
            pass
        else:
            print("that's not how bishops move")
            zing.x = originX
            zing.y = originY
            return True

    elif zist.index(zing) == 3:
        if destX == originX + hop or destX == originX - hop or destY == originY + hop or destY == originY - hop:
            pass
        else:
            print("that's not how the king moves")
            zing.x = originX
            zing.y = originY
            return True

    elif zist.index(zing) == 4:
        biV = pygame.math.Vector2(abs(destX - originX), abs(destY - originY))
        biV0 = pygame.math.Vector2(hop, hop)
        if biV.normalize() == biV0.normalize() or originX == destX or originY == destY:
            pass
        else:
            print("that's not how the queen moves")
            zing.x = originX
            zing.y = originY
            return True

    elif zist == p_rectA and 8 <= zist.index(zing) <= 15:
        if destY == originY - hop and destX == originX:
            pass
        elif originY == 457 and destY == originY - hop*2 and destX == originX:
            pass
        elif destY == originY - hop and (destX == originX - hop or destX == originX + hop) and checkinKilled(p_rectB):
            pass
        else:
            print("that's not how pawns move")
            zing.x = originX
            zing.y = originY
            return True
        
    elif zist == p_rectB and 8 <= zist.index(zing) <= 15:
        if destY == originY + hop and destX == originX:
            pass
        elif originY == 82 and destY == originY + hop*2 and destX == originX:
            pass
        elif destY == originY + hop and destX == originX + hop and checkinKilled(p_rectA):
            pass
        else:
            print("that's not how pawns move")
            zing.x = originX
            zing.y = originY
            return True

class PiecesA:
    def loc(self):
        for pA, p_A in itertools.zip_longest(piecesA, p_rectA):
            if pA:
                screen.blit(pA, p_A)
    def move(self):
        for sltd_A in p_rectA:
            global White_touched
            if sltd_A and event.type == pygame.MOUSEBUTTONDOWN and sltd_A.collidepoint(pygame.mouse.get_pos()) and White_touched is False:
                global Selected_A
                global originX
                global originY
                Selected_A = sltd_A
                originX = Selected_A.x
                originY = Selected_A.y
                White_touched = True
            if White_touched:
                Selected_A.center = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONUP:
                    checkinXY(Selected_A)
                    if checkinCollide(Selected_A, p_rectA) or checkinWho(Selected_A, p_rectA):
                        White_touched = False
                        return False
                    else:
                        if checkinKilled(p_rectB): 
                            p_rectB[i] = None
                            piecesB[i] = None
                        print("what")
                        Selected_A.x = destX
                        Selected_A.y = destY
                        return True
    # def clean_up():
    #     for pA in p_rectA:
    #         if p_rectA.index(pA) == 0 or p_rectA.index(pA) == 7:
    #             pA.x
                

class PiecesB:
    def loc(self):
        for pB, p_B in itertools.zip_longest(piecesB, p_rectB):
            if pB:
                screen.blit(pB, p_B)
    def move(self):
        for sltd_B in p_rectB:
            global Black_touched
            if sltd_B and event.type == pygame.MOUSEBUTTONDOWN and sltd_B.collidepoint(pygame.mouse.get_pos()) and Black_touched is False:
                global Selected_B
                global originX
                global originY
                Selected_B = sltd_B
                originX = Selected_B.x
                originY = Selected_B.y
                Black_touched = True
            if Black_touched:
                Selected_B.center = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONUP:
                    checkinXY(Selected_B)
                    if checkinCollide(Selected_B, p_rectB) or checkinWho(Selected_B, p_rectB):
                        Black_touched = False
                        return False
                    else:
                        if checkinKilled(p_rectA): 
                            p_rectA[i] = None
                            piecesA[i] = None
                        Selected_B.x = destX
                        Selected_B.y = destY
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
        if PiecesA.move(x1) is True:
            WhiteTurn = False
            White_touched = False
            print("black")

    else:
        if PiecesB.move(x1) is True:
            WhiteTurn = True
            Black_touched = False
            print("white")

    pygame.display.update()
    clock.tick(60)
    