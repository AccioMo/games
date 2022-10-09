from cmath import pi
from shutil import move
from threading import local
from tkinter import W, Y
from unicodedata import name
from urllib.parse import parse_qsl
from xml.sax import parseString
import pygame
from sys import exit
import itertools
import math

pygame.init()

BOARD = 600
PIECE_SIZE = 60
SQUARE = 75
A1 = 7
A2 = A1+SQUARE
A3 = A2+SQUARE
A4 = A3+SQUARE
A5 = A4+SQUARE
A6 = A5+SQUARE
A7 = A6+SQUARE
A8 = A7+SQUARE

screen = pygame.display.set_mode((BOARD, BOARD))
clock = pygame.time.Clock()

yies = [A1, A2, A3, A4, A5, A6, A7, A8]
xies = yies

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

x1 = A1
y1 = A8
for rectA in piecesA:
    p_rectA.append(rectA.get_rect(topleft=(x1, y1)))
    x1 += SQUARE
    if x1 == BOARD + A1:
        x1 = A1
        y1 -= SQUARE

x1 = A1
y1 = A1
for rectB in piecesB:
    p_rectB.append(rectB.get_rect(topleft=(x1, y1)))
    x1 += SQUARE
    if x1 == BOARD + A1:
        x1 = A1
        y1 += SQUARE

allpieces = p_rectA + p_rectB
# AllPieces = ["White Rook", "White Knight", "White Bishop", "White King", "White Queen", "White Bishop", "White Knight", "White Rook", "White Pawn", "White Pawn", "White Pawn", "White Pawn", "White Pawn", "White Pawn", "White Pawn", "White Pawn", "Black Rook", "Black Knight", "Black Bishop", "Black King", "Black Queen", "Black Bishop", "Black Knight", "Black Rook", "Black Pawn", "Black Pawn", "Black Pawn", "Black Pawn", "Black Pawn", "Black Pawn", "Black Pawn", "Black Pawn"]
# Return to original position:
# def fuckoff(shit):
#     shit.x = originX
#     shit.y = originY
#     return True

# Positioning piece in center of SQUARE:

def setting_board(rect_pieces, img_pieces):
    for pA, p_A in itertools.zip_longest(img_pieces, rect_pieces):
        if pA:
            screen.blit(pA, p_A)

def checkinXY(zing):
    dx = BOARD
    dy = BOARD
    for x in xies:
        if abs(zing.x - x) <= abs(dx):
            dx = zing.x - x
    global destX
    global distanceX
    destX = zing.x - dx
    distanceX = destX - originX
    for y in yies:
        if abs(zing.y - y) <= abs(dy):
            dy = zing.y - y
    global destY
    global distanceY
    destY = zing.y - dy
    distanceY = destY - originY

# Checking for pieces on SQUARE:
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

def checkinWay(zing):
    if distanceX:
        xway = int(distanceX / abs(distanceX))
    else:
        xway = 1
    if distanceY:
        yway = int(distanceY / abs(distanceY))
    else:
        yway = 1
    for pointX, pointY in itertools.zip_longest(range(originX, destX, SQUARE*xway), range(originY, destY, SQUARE*yway)):
        global piece
        if not pointX:
            pointX = originX
        if not pointY:
            pointY = originY
        for piece in allpieces:
            if piece and allpieces.index(zing) is not allpieces.index(piece) and (piece.x == pointX and piece.y == pointY):
                return True
            else:
                pass

# How the knights move:
def horsies(nox, noy):
    ss = [1, -1]
    for s in ss:
        for sss in ss:
            if destX == originX + SQUARE*nox*s*sss and destY == originY + SQUARE*noy*s:
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
        if (originX == destX or originY == destY) and not checkinWay(zing):
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
        biV = pygame.math.Vector2(abs(distanceX), abs(distanceY))
        biV0 = pygame.math.Vector2(SQUARE, SQUARE)
        if biV.normalize() == biV0.normalize() and not checkinWay(zing):
            pass
        else:
            print("that's not how bishops move")
            zing.x = originX
            zing.y = originY
            return True

    elif is_king(zing, zist):
        if (destX == originX or destX == originX + SQUARE or destX == originX - SQUARE) and (destY == originY or destY == originY +SQUARE or destY == originY -SQUARE):
            pass
        else:
            print("that's not how the king moves")
            zing.x = originX
            zing.y = originY
            return True

    elif is_queen(zing, zist):
        biV = pygame.math.Vector2(abs(destX - originX), abs(destY - originY))
        biV0 = pygame.math.Vector2(SQUARE, SQUARE)
        if (biV.normalize() == biV0.normalize() or originX == destX or originY == destY) and not checkinWay(zing):
            pass
        else:
            print("that's not how the queen moves")
            zing.x = originX
            zing.y = originY
            return True

    elif is_white_pawn(zing, zist):
        if destY == originY - SQUARE and destX == originX and not checkinKilled(p_rectB):
            pass
        elif originY == A7 and destY == originY - SQUARE*2 and destX == originX and not checkinWay(zing) and not checkinKilled(p_rectB):
            pass
        elif destY == originY - SQUARE and (destX == originX -SQUARE or destX == originX +SQUARE) and checkinKilled(p_rectB):
            pass
        else:
            print("that's not how pawns move")
            zing.x = originX
            zing.y = originY
            return True
        
    elif is_black_pawn(zing, zist):
        if destY == originY + SQUARE and destX == originX and not checkinKilled(p_rectA):
            pass
        elif originY == A2 and destY == originY + SQUARE*2 and destX == originX and not checkinWay(zing) and not checkinKilled(p_rectA):
            pass
        elif destY == originY + SQUARE and (destX == originX - SQUARE or destX == originX + SQUARE) and checkinKilled(p_rectA):
            pass
        else:
            print("that's not how pawns move")
            zing.x = originX
            zing.y = originY
            return True

class Pieces:
    # def __init__(self):
    #     self.name = AllPieces[allpieces.index(piece)]
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

    setting_board(p_rectA, piecesA)
    setting_board(p_rectB, piecesB)

    if WhiteTurn:
        if Pieces.moving(p_rectA, p_rectB, piecesB):
            WhiteTurn = False
            piece_touched = False
            print("Black's Turn")

    else:
        if Pieces.moving(p_rectB, p_rectA, piecesA):
            WhiteTurn = True
            piece_touched = False
            print("White's Turn")

    pygame.display.update()
    clock.tick(60)
    