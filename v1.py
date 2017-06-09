import pygame
from pygame.locals import *
from random import randint

board = [[0 for x in xrange(87)] for y in xrange(162)]
aux = [[0 for x in xrange(87)] for y in xrange(162)]
board[87][10] = 1
pygame.init()

windowSurface = pygame.display.set_mode((1300, 700), 0, 32)

pygame.display.set_caption("Runnig!")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (67, 18, 174)
YELLOW = (255, 211, 0)

CHILDY = (255, 255, 0)
TEENY = (159, 238, 0)
ADULTY = (0, 204, 0)
ELDERY = (103, 155, 0)

CHILDB = (105, 151, 211)
TEENB = (66, 130, 211)
ADULTB = (14, 81, 167)
ELDERB = (5, 50, 109)

POISON = (255, 0, 0)
GRAY = (192, 192, 192)

windowSurface.fill(WHITE)

running = True
paused = False
erase = False
wall = False
poison = False
Y = True
B = False


def check(x, y):
    try:
        if board[x][y] == 4:
            i = randint(1, 8)
            if i == 1:
                if aux[x - 1][y - 1] != 10:
                    if aux[x - 1][y - 1] == 100:
                        aux[x][y] = 0
                        aux[x - 1][y - 1] = 0
                        aux[x][y - 1] = 0
                        aux[x + 1][y - 1] = 0
                        aux[x - 1][y] = 0
                        aux[x + 1][y] = 0
                        aux[x - 1][y + 1] = 0
                        aux[x][y + 1] = 0
                        aux[x + 1][y + 1] = 0
                        aux[x - 2][y - 2] = 0
                        aux[x][y - 2] = 0
                        aux[x + 2][y - 2] = 0
                        aux[x - 2][y] = 0
                        aux[x + 2][y] = 0
                        aux[x - 2][y + 2] = 0
                        aux[x][y + 2] = 0
                        aux[x + 2][y + 2] = 0
                    elif aux[x - 1][y - 1] > 11 and aux[x][y] == 1:
                        pass
                    else:
                        aux[x - 1][y - 1] = 1
            elif i == 2:
                if aux[x][y - 1] != 10:
                    if aux[x][y - 1] == 100:
                        aux[x][y] = 0
                        aux[x - 1][y - 1] = 0
                        aux[x][y - 1] = 0
                        aux[x + 1][y - 1] = 0
                        aux[x - 1][y] = 0
                        aux[x + 1][y] = 0
                        aux[x - 1][y + 1] = 0
                        aux[x][y + 1] = 0
                        aux[x + 1][y + 1] = 0
                        aux[x - 2][y - 2] = 0
                        aux[x][y - 2] = 0
                        aux[x + 2][y - 2] = 0
                        aux[x - 2][y] = 0
                        aux[x + 2][y] = 0
                        aux[x - 2][y + 2] = 0
                        aux[x][y + 2] = 0
                        aux[x + 2][y + 2] = 0
                    elif aux[x][y - 1] > 11 and aux[x][y] == 1:
                        pass
                    else:
                        aux[x][y - 1] = 1
            elif i == 3:
                if aux[x + 1][y - 1] != 10:
                    if aux[x + 1][y - 1] == 100:
                        aux[x][y] = 0
                        aux[x - 1][y - 1] = 0
                        aux[x][y - 1] = 0
                        aux[x + 1][y - 1] = 0
                        aux[x - 1][y] = 0
                        aux[x + 1][y] = 0
                        aux[x - 1][y + 1] = 0
                        aux[x][y + 1] = 0
                        aux[x + 1][y + 1] = 0
                        aux[x - 2][y - 2] = 0
                        aux[x][y - 2] = 0
                        aux[x + 2][y - 2] = 0
                        aux[x - 2][y] = 0
                        aux[x + 2][y] = 0
                        aux[x - 2][y + 2] = 0
                        aux[x][y + 2] = 0
                        aux[x + 2][y + 2] = 0
                    elif aux[x + 1][y - 1] > 11 and aux[x][y] == 1:
                        pass
                    else:
                        aux[x + 1][y - 1] = 1
            elif i == 4:
                if aux[x - 1][y] != 10:
                    if aux[x - 1][y] == 100:
                        aux[x][y] = 0
                        aux[x - 1][y - 1] = 0
                        aux[x][y - 1] = 0
                        aux[x + 1][y - 1] = 0
                        aux[x - 1][y] = 0
                        aux[x + 1][y] = 0
                        aux[x - 1][y + 1] = 0
                        aux[x][y + 1] = 0
                        aux[x + 1][y + 1] = 0
                        aux[x - 2][y - 2] = 0
                        aux[x][y - 2] = 0
                        aux[x + 2][y - 2] = 0
                        aux[x - 2][y] = 0
                        aux[x + 2][y] = 0
                        aux[x - 2][y + 2] = 0
                        aux[x][y + 2] = 0
                        aux[x + 2][y + 2] = 0
                    elif aux[x - 1][y] > 11 and aux[x][y] == 1:
                        pass
                    else:
                        aux[x - 1][y] = 1
            elif i == 5:
                if aux[x + 1][y] != 10:
                    if aux[x + 1][y] == 100:
                        aux[x][y] = 0
                        aux[x - 1][y - 1] = 0
                        aux[x][y - 1] = 0
                        aux[x + 1][y - 1] = 0
                        aux[x - 1][y] = 0
                        aux[x + 1][y] = 0
                        aux[x - 1][y + 1] = 0
                        aux[x][y + 1] = 0
                        aux[x + 1][y + 1] = 0
                        aux[x - 2][y - 2] = 0
                        aux[x][y - 2] = 0
                        aux[x + 2][y - 2] = 0
                        aux[x - 2][y] = 0
                        aux[x + 2][y] = 0
                        aux[x - 2][y + 2] = 0
                        aux[x][y + 2] = 0
                        aux[x + 2][y + 2] = 0
                    elif aux[x + 1][y] > 11 and aux[x][y] == 1:
                        pass
                    else:
                        aux[x + 1][y] = 1
            elif i == 6:
                if aux[x - 1][y + 1] != 10:
                    if aux[x - 1][y + 1] == 100:
                        aux[x][y] = 0
                        aux[x - 1][y - 1] = 0
                        aux[x][y - 1] = 0
                        aux[x + 1][y - 1] = 0
                        aux[x - 1][y] = 0
                        aux[x + 1][y] = 0
                        aux[x - 1][y + 1] = 0
                        aux[x][y + 1] = 0
                        aux[x + 1][y + 1] = 0
                        aux[x - 2][y - 2] = 0
                        aux[x][y - 2] = 0
                        aux[x + 2][y - 2] = 0
                        aux[x - 2][y] = 0
                        aux[x + 2][y] = 0
                        aux[x - 2][y + 2] = 0
                        aux[x][y + 2] = 0
                        aux[x + 2][y + 2] = 0
                    elif aux[x - 1][y + 1] > 11 and aux[x][y] == 1:
                        pass
                    else:
                        aux[x - 1][y + 1] = 1
            elif i == 7:
                if aux[x][y + 1] != 10:
                    if aux[x][y + 1] == 100:
                        aux[x][y] = 0
                        aux[x - 1][y - 1] = 0
                        aux[x][y - 1] = 0
                        aux[x + 1][y - 1] = 0
                        aux[x - 1][y] = 0
                        aux[x + 1][y] = 0
                        aux[x - 1][y + 1] = 0
                        aux[x][y + 1] = 0
                        aux[x + 1][y + 1] = 0
                        aux[x - 2][y - 2] = 0
                        aux[x][y - 2] = 0
                        aux[x + 2][y - 2] = 0
                        aux[x - 2][y] = 0
                        aux[x + 2][y] = 0
                        aux[x - 2][y + 2] = 0
                        aux[x][y + 2] = 0
                        aux[x + 2][y + 2] = 0
                    elif aux[x][y + 1] > 11 and aux[x][y] == 1:
                        pass
                    else:
                        aux[x][y + 1] = 1
            else:
                if aux[x + 1][y + 1] != 10:
                    if aux[x + 1][y + 1] == 100:
                        aux[x][y] = 0
                        aux[x - 1][y - 1] = 0
                        aux[x][y - 1] = 0
                        aux[x + 1][y - 1] = 0
                        aux[x - 1][y] = 0
                        aux[x + 1][y] = 0
                        aux[x - 1][y + 1] = 0
                        aux[x][y + 1] = 0
                        aux[x + 1][y + 1] = 0
                        aux[x - 2][y - 2] = 0
                        aux[x][y - 2] = 0
                        aux[x + 2][y - 2] = 0
                        aux[x - 2][y] = 0
                        aux[x + 2][y] = 0
                        aux[x - 2][y + 2] = 0
                        aux[x][y + 2] = 0
                        aux[x + 2][y + 2] = 0
                    elif aux[x + 1][y + 1] > 11 and aux[x][y] == 1:
                        pass
                    else:
                        aux[x + 1][y + 1] = 1
        elif board[x][y] == 14:
            i = randint(1, 8)
            if i == 1:
                if aux[x - 1][y - 1] != 10:
                    if aux[x - 1][y - 1] == 100:
                        aux[x][y] = 0
                        aux[x - 1][y - 1] = 0
                        aux[x][y - 1] = 0
                        aux[x + 1][y - 1] = 0
                        aux[x - 1][y] = 0
                        aux[x + 1][y] = 0
                        aux[x - 1][y + 1] = 0
                        aux[x][y + 1] = 0
                        aux[x + 1][y + 1] = 0
                        aux[x - 2][y - 2] = 0
                        aux[x][y - 2] = 0
                        aux[x + 2][y - 2] = 0
                        aux[x - 2][y] = 0
                        aux[x + 2][y] = 0
                        aux[x - 2][y + 2] = 0
                        aux[x][y + 2] = 0
                        aux[x + 2][y + 2] = 0
                    elif aux[x - 1][y - 1] > 1 and aux[x - 1][y - 1] <= 4 and aux[x][y] == 11:
                        pass
                    else:
                        aux[x - 1][y - 1] = 11
            elif i == 2:
                if aux[x][y - 1] != 10:
                    if aux[x][y - 1] == 100:
                        aux[x][y] = 0
                        aux[x - 1][y - 1] = 0
                        aux[x][y - 1] = 0
                        aux[x + 1][y - 1] = 0
                        aux[x - 1][y] = 0
                        aux[x + 1][y] = 0
                        aux[x - 1][y + 1] = 0
                        aux[x][y + 1] = 0
                        aux[x + 1][y + 1] = 0
                        aux[x - 2][y - 2] = 0
                        aux[x][y - 2] = 0
                        aux[x + 2][y - 2] = 0
                        aux[x - 2][y] = 0
                        aux[x + 2][y] = 0
                        aux[x - 2][y + 2] = 0
                        aux[x][y + 2] = 0
                        aux[x + 2][y + 2] = 0
                    elif aux[x - 1][y - 1] > 1 and aux[x - 1][y - 1] <= 4 and aux[x][y] == 11:
                        pass
                    else:
                        aux[x][y - 1] = 11
            elif i == 3:
                if aux[x + 1][y - 1] != 10:
                    if aux[x + 1][y - 1] == 100:
                        aux[x][y] = 0
                        aux[x - 1][y - 1] = 0
                        aux[x][y - 1] = 0
                        aux[x + 1][y - 1] = 0
                        aux[x - 1][y] = 0
                        aux[x + 1][y] = 0
                        aux[x - 1][y + 1] = 0
                        aux[x][y + 1] = 0
                        aux[x + 1][y + 1] = 0
                        aux[x - 2][y - 2] = 0
                        aux[x][y - 2] = 0
                        aux[x + 2][y - 2] = 0
                        aux[x - 2][y] = 0
                        aux[x + 2][y] = 0
                        aux[x - 2][y + 2] = 0
                        aux[x][y + 2] = 0
                        aux[x + 2][y + 2] = 0
                    elif aux[x - 1][y - 1] > 1 and aux[x - 1][y - 1] <= 4 and aux[x][y] == 11:
                        pass
                    else:
                        aux[x + 1][y - 1] = 11
            elif i == 4:
                if aux[x - 1][y] != 10:
                    if aux[x - 1][y] == 100:
                        aux[x][y] = 0
                        aux[x - 1][y - 1] = 0
                        aux[x][y - 1] = 0
                        aux[x + 1][y - 1] = 0
                        aux[x - 1][y] = 0
                        aux[x + 1][y] = 0
                        aux[x - 1][y + 1] = 0
                        aux[x][y + 1] = 0
                        aux[x + 1][y + 1] = 0
                        aux[x - 2][y - 2] = 0
                        aux[x][y - 2] = 0
                        aux[x + 2][y - 2] = 0
                        aux[x - 2][y] = 0
                        aux[x + 2][y] = 0
                        aux[x - 2][y + 2] = 0
                        aux[x][y + 2] = 0
                        aux[x + 2][y + 2] = 0
                    elif aux[x - 1][y - 1] > 1 and aux[x - 1][y - 1] <= 4 and aux[x][y] == 11:
                        pass
                    else:
                        aux[x - 1][y] = 11
            elif i == 5:
                if aux[x + 1][y] != 10:
                    if aux[x + 1][y] == 100:
                        aux[x][y] = 0
                        aux[x - 1][y - 1] = 0
                        aux[x][y - 1] = 0
                        aux[x + 1][y - 1] = 0
                        aux[x - 1][y] = 0
                        aux[x + 1][y] = 0
                        aux[x - 1][y + 1] = 0
                        aux[x][y + 1] = 0
                        aux[x + 1][y + 1] = 0
                        aux[x - 2][y - 2] = 0
                        aux[x][y - 2] = 0
                        aux[x + 2][y - 2] = 0
                        aux[x - 2][y] = 0
                        aux[x + 2][y] = 0
                        aux[x - 2][y + 2] = 0
                        aux[x][y + 2] = 0
                        aux[x + 2][y + 2] = 0
                    elif aux[x - 1][y - 1] > 1 and aux[x - 1][y - 1] <= 4 and aux[x][y] == 11:
                        pass
                    else:
                        aux[x + 1][y] = 11
            elif i == 6:
                if aux[x - 1][y + 1] != 10:
                    if aux[x - 1][y + 1] == 100:
                        aux[x][y] = 0
                        aux[x - 1][y - 1] = 0
                        aux[x][y - 1] = 0
                        aux[x + 1][y - 1] = 0
                        aux[x - 1][y] = 0
                        aux[x + 1][y] = 0
                        aux[x - 1][y + 1] = 0
                        aux[x][y + 1] = 0
                        aux[x + 1][y + 1] = 0
                        aux[x - 2][y - 2] = 0
                        aux[x][y - 2] = 0
                        aux[x + 2][y - 2] = 0
                        aux[x - 2][y] = 0
                        aux[x + 2][y] = 0
                        aux[x - 2][y + 2] = 0
                        aux[x][y + 2] = 0
                        aux[x + 2][y + 2] = 0
                    elif aux[x - 1][y - 1] > 1 and aux[x - 1][y - 1] <= 4 and aux[x][y] == 11:
                        pass
                    else:
                        aux[x - 1][y + 1] = 11
            elif i == 7:
                if aux[x][y + 1] != 10:
                    if aux[x][y + 1] == 100:
                        aux[x][y] = 0
                        aux[x - 1][y - 1] = 0
                        aux[x][y - 1] = 0
                        aux[x + 1][y - 1] = 0
                        aux[x - 1][y] = 0
                        aux[x + 1][y] = 0
                        aux[x - 1][y + 1] = 0
                        aux[x][y + 1] = 0
                        aux[x + 1][y + 1] = 0
                        aux[x - 2][y - 2] = 0
                        aux[x][y - 2] = 0
                        aux[x + 2][y - 2] = 0
                        aux[x - 2][y] = 0
                        aux[x + 2][y] = 0
                        aux[x - 2][y + 2] = 0
                        aux[x][y + 2] = 0
                        aux[x + 2][y + 2] = 0
                    elif aux[x - 1][y - 1] > 1 and aux[x - 1][y - 1] <= 4 and aux[x][y] == 11:
                        pass
                    else:
                        aux[x][y + 1] = 11
            else:
                if aux[x + 1][y + 1] != 10:
                    if aux[x + 1][y + 1] == 100:
                        aux[x][y] = 0
                        aux[x - 1][y - 1] = 0
                        aux[x][y - 1] = 0
                        aux[x + 1][y - 1] = 0
                        aux[x - 1][y] = 0
                        aux[x + 1][y] = 0
                        aux[x - 1][y + 1] = 0
                        aux[x][y + 1] = 0
                        aux[x + 1][y + 1] = 0
                        aux[x - 2][y - 2] = 0
                        aux[x][y - 2] = 0
                        aux[x + 2][y - 2] = 0
                        aux[x - 2][y] = 0
                        aux[x + 2][y] = 0
                        aux[x - 2][y + 2] = 0
                        aux[x][y + 2] = 0
                        aux[x + 2][y + 2] = 0
                    elif aux[x - 1][y - 1] > 1 and aux[x - 1][y - 1] <= 4 and aux[x][y] == 11:
                        pass
                    else:
                        aux[x + 1][y + 1] = 11
        elif aux[x][y] != 10 and aux[x][y] != 100 and aux[x][y] != 0:
            aux[x][y] += 1
    except:
        pass


def gerate(x, y):
    if aux[x][y] == 1:
        board[x][y] = 1
    elif aux[x][y] == 2:
        board[x][y] = 2
    elif aux[x][y] == 3:
        board[x][y] = 3
    elif aux[x][y] == 4:
        board[x][y] = 4
    elif aux[x][y] == 10:
        board[x][y] = 10
    elif aux[x][y] == 11:
        board[x][y] = 11
    elif aux[x][y] == 12:
        board[x][y] = 12
    elif aux[x][y] == 13:
        board[x][y] = 13
    elif aux[x][y] == 14:
        board[x][y] = 14
    elif aux[x][y] == 100:
        board[x][y] = 100
    else:
        board[x][y] = 0


def print_pygame():
    for x in xrange(len(board)):
        for y in xrange(len(board[0])):
            if board[x][y] >= 1 and board[x][y] <= 4:
                draw_y(x * 8, y * 8)
            elif board[x][y] >= 11 and board[x][y] <= 14:
                draw_b(x * 8, y * 8)
            elif board[x][y] == 10:
                draw_wall(x * 8, y * 8)
            elif board[x][y] == 100:
                draw_poison(x * 8, y * 8)
            else:
                draw_board(x * 8, y * 8)


def draw_y(x, y):
    if board[x / 8][y / 8] == 1:
        x += 6
        y += 6
        pygame.draw.polygon(windowSurface, CHILDY, ((x - 3, y - 3), (x + 3, y - 3), (x + 3, y + 3), (x - 3, y + 3)))
    elif board[x / 8][y / 8] == 2:
        x += 6
        y += 6
        pygame.draw.polygon(windowSurface, TEENY, ((x - 3, y - 3), (x + 3, y - 3), (x + 3, y + 3), (x - 3, y + 3)))
    elif board[x / 8][y / 8] == 3:
        x += 6
        y += 6
        pygame.draw.polygon(windowSurface, ADULTY, ((x - 3, y - 3), (x + 3, y - 3), (x + 3, y + 3), (x - 3, y + 3)))
    else:
        x += 6
        y += 6
        pygame.draw.polygon(windowSurface, ELDERY, ((x - 3, y - 3), (x + 3, y - 3), (x + 3, y + 3), (x - 3, y + 3)))


def draw_b(x, y):
    if board[x / 8][y / 8] == 11:
        x += 6
        y += 6
        pygame.draw.polygon(windowSurface, CHILDB, ((x - 3, y - 3), (x + 3, y - 3), (x + 3, y + 3), (x - 3, y + 3)))
    elif board[x / 8][y / 8] == 12:
        x += 6
        y += 6
        pygame.draw.polygon(windowSurface, TEENB, ((x - 3, y - 3), (x + 3, y - 3), (x + 3, y + 3), (x - 3, y + 3)))
    elif board[x / 8][y / 8] == 13:
        x += 6
        y += 6
        pygame.draw.polygon(windowSurface, ADULTB, ((x - 3, y - 3), (x + 3, y - 3), (x + 3, y + 3), (x - 3, y + 3)))
    else:
        x += 6
        y += 6
        pygame.draw.polygon(windowSurface, ELDERB, ((x - 3, y - 3), (x + 3, y - 3), (x + 3, y + 3), (x - 3, y + 3)))


def draw_cell(x, y):
    x += 6
    y += 6
    pygame.draw.polygon(windowSurface, YELLOW, ((x - 3, y - 3), (x + 3, y - 3), (x + 3, y + 3), (x - 3, y + 3)))


def draw_board(x, y):
    x += 6
    y += 6
    pygame.draw.polygon(windowSurface, GRAY, ((x - 3, y - 3), (x + 3, y - 3), (x + 3, y + 3), (x - 3, y + 3)))


def draw_wall(x, y):
    x += 6
    y += 6
    pygame.draw.polygon(windowSurface, WHITE, ((x - 3, y - 3), (x + 3, y - 3), (x + 3, y + 3), (x - 3, y + 3)))


def draw_poison(x, y):
    x += 6
    y += 6
    pygame.draw.polygon(windowSurface, POISON, ((x - 3, y - 3), (x + 3, y - 3), (x + 3, y + 3), (x - 3, y + 3)))


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            (mouseX, mouseY) = pygame.mouse.get_pos()
            mouseX -= 3
            mouseY -= 3
            if erase:
                erase = (True, False)[erase]
                for x in range(5):
                    for y in range(5):
                        aux[mouseX / 8 - x][mouseY / 8 - y] = 0
                        aux[mouseX / 8 - x][mouseY / 8 + y] = 0
                        aux[mouseX / 8 + x][mouseY / 8 - y] = 0
                        aux[mouseX / 8 + x][mouseY / 8 + y] = 0
                        gerate(mouseX / 8 - x, mouseY / 8 - y)
                        gerate(mouseX / 8 - x, mouseY / 8 + y)
                        gerate(mouseX / 8 + x, mouseY / 8 - y)
                        gerate(mouseX / 8 + x, mouseY / 8 + y)
            elif wall:
                aux[mouseX / 8][mouseY / 8] = 10
                gerate(mouseX / 8, mouseY / 8)
            elif poison:
                aux[mouseX / 8][mouseY / 8] = 100
                gerate(mouseX / 8, mouseY / 8)
            elif B:
                aux[mouseX / 8][mouseY / 8] = 11
                gerate(mouseX / 8, mouseY / 8)
            elif Y:
                aux[mouseX / 8][mouseY / 8] = 1
                gerate(mouseX / 8, mouseY / 8)
            else:
                aux[mouseX / 8][mouseY / 8] = 0
                gerate(mouseX / 8, mouseY / 8)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = (True, False)[paused]
                if paused == True:
                    pygame.display.set_caption("Paused...")
                else:
                    pygame.display.set_caption("Running!")
            elif event.key == pygame.K_c:
                for x in xrange(len(board)):
                    for y in xrange(len(board[0])):
                        aux[x][y] = 0
                for x in xrange(len(board)):
                    for y in xrange(len(board[0])):
                        gerate(x, y)
            elif event.key == pygame.K_DELETE:
                erase = (True, False)[erase]
                wall = False
                poison = False
                B = False
                Y = False
            elif event.key == pygame.K_F1:
                wall = (True, False)[wall]
                erase = False
                poison = False
                B = False
                Y = False
            elif event.key == pygame.K_F2:
                poison = (True, False)[poison]
                erase = False
                wall = False
                B = False
                Y = False
            elif event.key == pygame.K_b:
                B = (True, False)[B]
                erase = False
                wall = False
                poison = False
                Y = False
            elif event.key == pygame.K_y:
                Y = (True, False)[Y]
                erase = False
                wall = False
                poison = False
                B = False
    if paused == False:
        for x in xrange(len(aux)):
            for y in xrange(len(aux[0])):
                check(x, y)
        for x in xrange(len(aux)):
            for y in xrange(len(aux[0])):
                gerate(x, y)
    print_pygame()
    pygame.display.update()
pygame.quit()
