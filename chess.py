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

piece_touched = False
WhiteTurn = True

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

# Return to original position:
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

# How the knights move:
def horsies(nox, noy):
    ss = [1, -1]
    for s in ss:
        for sss in ss:
            if destX == originX + hop*nox*s*sss and destY == originY + hop*noy*s:
                return True

# Makes next section more readable:
def is_rook(zing, zist):
    if zist.index(zing) == 0 or zist.index(zing) == 7:
        return True
def is_knight(zing, zist):
    if zist.index(zing) == 1 or zist.index(zing) == 6:
        return True
def is_bishop(zing, zist):
    if zist.index(zing) == 2 or zist.index(zing) == 5:
        return True
def is_king(zing, zist):
    if zist.index(zing) == 3:
        return True
def is_queen(zing, zist):
    if zist.index(zing) == 4:
        return True
def is_white_pawn(zing, zist):
    if zist == p_rectA and 8 <= zist.index(zing) <= 15:
        return True
def is_black_pawn(zing, zist):
    if zist == p_rectB and 8 <= zist.index(zing) <= 15:
        return True

# What piece was moved and where can it go:
def checkinWho(zing, zist):
    if is_rook(zing, zist):
        if originX == destX or originY == destY:
            pass
        else:
            print("that's not how rooks move")
            zing.x = originX
            zing.y = originY
            return True
    elif is_knight(zing, zist):
        if horsies(2, 1) or horsies(1, 2):
            pass
        else:
            print("that's not how knights move")
            zing.x = originX
            zing.y = originY
            return True

    elif is_bishop(zing, zist):
        biV = pygame.math.Vector2(abs(destX - originX), abs(destY - originY))
        biV0 = pygame.math.Vector2(hop, hop)
        if biV.normalize() == biV0.normalize():
            pass
        else:
            print("that's not how bishops move")
            zing.x = originX
            zing.y = originY
            return True

    elif is_king(zing, zist):
        if (destX == originX or destX == originX + hop or destX == originX - hop) and (destY == originY or destY == originY + hop or destY == originY - hop):
            pass
        else:
            print("that's not how the king moves")
            zing.x = originX
            zing.y = originY
            return True

    elif is_queen(zing, zist):
        biV = pygame.math.Vector2(abs(destX - originX), abs(destY - originY))
        biV0 = pygame.math.Vector2(hop, hop)
        if biV.normalize() == biV0.normalize() or originX == destX or originY == destY:
            pass
        else:
            print("that's not how the queen moves")
            zing.x = originX
            zing.y = originY
            return True

    elif is_white_pawn(zing, zist):
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
        
    elif is_black_pawn(zing, zist):
        if destY == originY + hop and destX == originX:
            pass
        elif originY == 82 and destY == originY + hop*2 and destX == originX:
            pass
        elif destY == originY + hop and (destX == originX - hop or destX == originX + hop) and checkinKilled(p_rectA):
            pass
        else:
            print("that's not how pawns move")
            zing.x = originX
            zing.y = originY
            return True

class Pieces:
    def setting_board(rect_pieces, img_pieces):
        for pA, p_A in itertools.zip_longest(img_pieces, rect_pieces):
            if pA:
                screen.blit(pA, p_A)
    def moving(rect_pieces, enemy_pieces_rect, enemy_pieces_img):
        for sltd in rect_pieces:
            global piece_touched
            if sltd and event.type == pygame.MOUSEBUTTONDOWN and sltd.collidepoint(pygame.mouse.get_pos()) and piece_touched is False:
                global Selected
                global originX
                global originY
                Selected = sltd
                originX = Selected.x
                originY = Selected.y
                piece_touched = True
            if piece_touched:
                Selected.center = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONUP:
                    checkinXY(Selected)
                    if checkinCollide(Selected, rect_pieces) or checkinWho(Selected, rect_pieces):
                        piece_touched = False
                        return False
                    else:
                        if checkinKilled(enemy_pieces_rect):
                            enemy_pieces_rect[i] = None
                            enemy_pieces_img[i] = None
                        Selected.x = destX
                        Selected.y = destY
                        return True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(chess_surf, (0, 0))

    Pieces.setting_board(p_rectA, piecesA)
    Pieces.setting_board(p_rectB, piecesB)

    if WhiteTurn:
        if Pieces.moving(p_rectA, p_rectB, piecesB) is True:
            WhiteTurn = False
            piece_touched = False
            print("Black's Turn")

    else:
        if Pieces.moving(p_rectB, p_rectA, piecesA) is True:
            WhiteTurn = True
            piece_touched = False
            print("White's Turn")

    pygame.display.update()
    clock.tick(60)
    