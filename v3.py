import pygame
import math
from pygame.locals import *
from random import *

board = [[[0, 0, 0, 0] for x in xrange(87)] for y in xrange(162)]
aux = [[[0, 0, 0, 0] for x in xrange(87)] for y in xrange(162)]

pygame.init()

windowSurface = pygame.display.set_mode((1300, 700), 0, 32)

pygame.display.set_caption("Running!")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (67, 18, 174)
YELLOW = (255, 211, 0)
GRAY = (192, 192, 192)

FOOD = (0, 255, 0)

windowSurface.fill(WHITE)
caption = "Running!"
genes = ["", "", ""]
genesi = 0
gen = ""
running = True
paused = False
newlife = False
food = False
status = False


def check(x, y):
    try:
        if board[x][y][0] == 1:
            if board[x][y][2] > 50:
                aux[x][y][0] = 0
                aux[x][y][2] = 0
            else:
                dist = 1000
                for x1 in xrange(len(board)):
                    for y1 in xrange(len(board[0])):
                        if board[x1][y1][0] == "f":
                            dist1 = math.sqrt(pow(x1 - x, 2) + pow(y1 - y, 2))
                            if dist1 <= dist:
                                if dist1 < 2:
                                    dist = dist1
                                    targetx = x1
                                    targety = y1
                                    break
                                else:
                                    dist = dist1
                                    targetx = x1
                                    targety = y1
                board[x][y][2] += 1
                if x > targetx:
                    x1 = x - 1
                    if y > targety:
                        y1 = y - 1
                    elif y < targety:
                        y1 = y + 1
                    else:
                        y1 = y
                elif x < targetx:
                    x1 = x + 1
                    if y > targety:
                        y1 = y - 1
                    elif y < targety:
                        y1 = y + 1
                    else:
                        y1 = y
                elif x == targetx:
                    x1 = x
                    if y > targety:
                        y1 = y - 1
                    elif y < targety:
                        y1 = y + 1
                    else:
                        y1 = y
                if board[x1][y1][0] == "f":
                    aux[x1][y1][0] = 1
                    aux[x1][y1][1] = aux[x][y][1]
                    aux[x1][y1][2] = 1
                    aux[x1][y1][3] = aux[x][y][3] + 1
                    aux[x][y][0] = 0
                    aux[x][y][1] = 0
                    aux[x][y][2] = 0
                    aux[x][y][3] = 0
                    if board[x1][y1][3] >= 50:
                        aux[x][y1 - 15][0] = 1
                        aux[x][y1 - 15][1] = aux[x1][y1][1]
                        aux[x][y1 - 15][2] = 1
                        aux[x][y1 - 15][3] = 0
                        aux[x1][y1][3] = 0
                else:
                    if board[x1][y1][0] != 1:
                        aux[x1][y1][0] = 1
                        aux[x1][y1][1] = aux[x][y][1]
                        aux[x1][y1][2] = aux[x][y][2]
                        aux[x1][y1][3] = aux[x][y][3]
                        aux[x][y][0] = 0
                        aux[x][y][1] = 0
                        aux[x][y][2] = 0
                        aux[x][y][3] = 0
                if aux[x1 - 1][y1 - 1][0] != 1:
                    aux[x1 - 1][y1 - 1][1] = 0
                if aux[x1][y1 - 1][0] != 1:
                    aux[x1][y1 - 1][1] = 0
                if aux[x1 + 1][y1 - 1][0] != 1:
                    aux[x1 + 1][y1 - 1][1] = 0
                if aux[x1 - 1][y1][0] != 1:
                    aux[x1 - 1][y1][1] = 0
                if aux[x1 + 1][y1][0] != 1:
                    aux[x1 + 1][y1][1] = 0
                if aux[x1 - 1][y1 + 1][0] != 1:
                    aux[x1 - 1][y1 + 1][1] = 0
                if aux[x1][y1 + 1][0] != 1:
                    aux[x1][y1 + 1][1] = 0
                if aux[x1 + 1][y1 + 1][0] != 1:
                    aux[x1 + 1][y1 + 1][1] = 0
                for i in range(3):
                    i = randint(1, 9)
                    if i == 1:
                        aux[x1 - 1][y1 - 1][1] = board[x1][y1][1]
                        aux[x1 - 1][y1 - 1][0] = 0
                    elif i == 2:
                        aux[x1][y1 - 1][1] = board[x1][y1][1]
                        aux[x1][y1 - 1][0] = 0
                    elif i == 3:
                        aux[x1 + 1][y1 - 1][1] = board[x1][y1][1]
                        aux[x1 + 1][y1 - 1][0] = 0
                    elif i == 4:
                        aux[x1 - 1][y1][1] = board[x1][y1][1]
                        aux[x1 - 1][y1][0] = 0
                    elif i == 5:
                        aux[x1 + 1][y1][1] = board[x1][y1][1]
                        aux[x1 - 1][y1][0] = 0
                    elif i == 6:
                        aux[x1 - 1][y1 + 1][1] = board[x1][y1][1]
                        aux[x1 - 1][y1 + 1][0] = 0
                    elif i == 7:
                        aux[x1][y1 + 1][1] = board[x1][y1][1]
                        aux[x1][y1 + 1][0] = 0
                    elif i == 8:
                        aux[x1 + 1][y1 + 1][1] = board[x1][y1][1]
                        aux[x1 + 1][y1 + 1][0] = 0
        elif board[x][y][0] == "f":
            if board[x][y][2] == 1:
                board[x][y - 1][0] = "f"
                board[x - 1][y][0] = "f"
                board[x + 1][y][0] = "f"
                board[x][y + 1][0] = "f"
                board[x][y - 1][1] = FOOD
                board[x - 1][y][1] = FOOD
                board[x + 1][y][1] = FOOD
                board[x][y + 1][1] = FOOD
                board[x][y - 1][2] = 2
                board[x - 1][y][2] = 3
                board[x + 1][y][2] = 4
                board[x][y + 1][2] = 5
                board[x][y - 1][3] = randint(5, 10)
                board[x - 1][y][3] = randint(5, 10)
                board[x + 1][y][3] = randint(0, 4)
                board[x][y + 1][3] = randint(0, 4)
                board[x][y][2] = 10
            elif board[x][y][2] == 2:
                i = randint(0, 3)
                if i == 0:
                    if board[x - 1][y - 1][0] == 0 and board[x][y][3] > 0:
                        board[x - 1][y - 1][0] = "f"
                        board[x - 1][y - 1][1] = FOOD
                        board[x - 1][y - 1][2] = 2
                        board[x - 1][y - 1][3] = board[x][y][3] - 3
                    else:
                        board[x][y][2] = 10
                elif i == 1:
                    if board[x][y - 1][0] == 0 and board[x][y][3] > 0:
                        board[x][y - 1][0] = "f"
                        board[x][y - 1][1] = FOOD
                        board[x][y - 1][2] = 2
                        board[x][y - 1][3] = board[x][y][3] - 3
                    else:
                        board[x][y][2] = 10
                elif i == 2:
                    if board[x + 1][y - 1][0] == 0 and board[x][y][3] > 0:
                        board[x + 1][y - 1][0] = "f"
                        board[x + 1][y - 1][1] = FOOD
                        board[x + 1][y - 1][2] = 2
                        board[x + 1][y - 1][3] = board[x][y][3] - 3
                    else:
                        board[x][y][2] = 10
            elif board[x][y][2] == 3:
                i = randint(0, 3)
                if i == 0:
                    if board[x - 1][y - 1][0] == 0 and board[x][y][3] > 0:
                        board[x - 1][y - 1][0] = "f"
                        board[x - 1][y - 1][1] = FOOD
                        board[x - 1][y - 1][2] = 3
                        board[x - 1][y - 1][3] = board[x][y][3] - 3
                    else:
                        board[x][y][2] = 10
                elif i == 1:
                    if board[x][y - 1][0] == 0 and board[x][y][3] > 0:
                        board[x - 1][y][0] = "f"
                        board[x - 1][y][1] = FOOD
                        board[x - 1][y][2] = 3
                        board[x - 1][y][3] = board[x][y][3] - 3
                    else:
                        board[x][y][2] = 10
                elif i == 2:
                    if board[x + 1][y - 1][0] == 0 and board[x][y][3] > 0:
                        board[x - 1][y + 1][0] = "f"
                        board[x - 1][y + 1][1] = FOOD
                        board[x - 1][y + 1][2] = 3
                        board[x - 1][y + 1][3] = board[x][y][3] - 3
                    else:
                        board[x][y][2] = 10
            elif board[x][y][2] == 4:
                board[x + 1][y][0] = "f"
                board[x + 1][y][1] = FOOD
                board[x + 1][y][2] = 8
                board[x + 1][y][3] = randint(0, 4)
                board[x][y][2] = 10
            elif board[x][y][2] == 5:
                board[x][y + 1][0] = "f"
                board[x][y + 1][1] = FOOD
                board[x][y + 1][2] = 9
                board[x][y + 1][3] = randint(0, 2)
                board[x][y][2] = 10
    except:
        pass


def gerate(x, y):
    board[x][y] = aux[x][y]


def printPygame():
    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[x][y][1] == 0:
                drawBoard(x * 8, y * 8)
            else:
                drawCell(x * 8, y * 8)


def drawCell(x, y):
    x += 6
    y += 6
    pygame.draw.polygon(windowSurface, board[(x - 6) / 8][(y - 6) / 8][1],
                        ((x - 3, y - 3), (x + 3, y - 3), (x + 3, y + 3), (x - 3, y + 3)))


def drawBoard(x, y):
    x += 6
    y += 6
    pygame.draw.polygon(windowSurface, GRAY, ((x - 3, y - 3), (x + 3, y - 3), (x + 3, y + 3), (x - 3, y + 3)))


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            (mouseX, mouseY) = pygame.mouse.get_pos()
            mouseX -= 3
            mouseY -= 3
            if newlife:
                try:
                    board[mouseX / 8][mouseY / 8][1] = [int(genes[i]) for i in range(len(genes))]
                    board[mouseX / 8][mouseY / 8][0] = 1
                    board[mouseX / 8][mouseY / 8][2] = 1
                except:
                    pass
            elif food:
                board[mouseX / 8][mouseY / 8][0] = "f"
                board[mouseX / 8][mouseY / 8][1] = FOOD
                board[mouseX / 8][mouseY / 8][2] = 1
            elif status:
                print board[mouseX / 8][mouseY / 8]
            else:
                board[mouseX / 8][mouseY / 8][1] = 0
                board[mouseX / 8][mouseY / 8][0] = 0
                board[mouseX / 8][mouseY / 8][2] = 0
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = (True, False)[paused]
                if paused:
                    caption = "Paused..."
                    pygame.display.set_caption(caption + gen + ",".join(genes))
                else:
                    caption = "Running!"
                    pygame.display.set_caption(caption + gen + ",".join(genes))
            elif event.key == pygame.K_c:
                for x in xrange(len(board)):
                    for y in xrange(len(board[0])):
                        aux[x][y][0] = 0
                        aux[x][y][1] = 0
                for x in xrange(len(board)):
                    for y in xrange(len(board[0])):
                        gerate(x, y)
            elif event.key == pygame.K_F1:
                newlife = (True, False)[newlife]
                food = False
                status = False
                if newlife:
                    gen = "       genes:"
                    genes = ["", "", ""]
                    genesi = 0
                else:
                    genes = ""
                    genesi = 0
                    gen = ""
                    pygame.display.set_caption(caption + gen + ",".join(genes))
            elif event.key == pygame.K_F2:
                newlife = (True, False)[newlife]
                food = False
                status = False
                if newlife:
                    gen = "       genes:"
                    genes = [str(randint(0, 255)), str(randint(0, 255)), str(randint(0, 255))]
                    pygame.display.set_caption(caption + gen + ",".join(genes))
                else:
                    genes = ""
                    genesi = 0
                    gen = ""
                    pygame.display.set_caption(caption + gen + ",".join(genes))
            elif event.key == pygame.K_i:
                status = (True, False)[status]
                newlife = False
                newlife = food
            elif event.key == pygame.K_f:
                food = (True, False)[food]
                newlife = False
                status = False
            elif newlife:
                if len(genes[genesi]) >= 3:
                    genesi += 1
                    if genesi > 2:
                        genesi = 0
                else:
                    if event.key == pygame.K_0:
                        genes[genesi] += "0"
                    elif event.key == pygame.K_1:
                        genes[genesi] += "1"
                    elif event.key == pygame.K_2:
                        genes[genesi] += "2"
                    elif event.key == pygame.K_3:
                        genes[genesi] += "3"
                    elif event.key == pygame.K_4:
                        genes[genesi] += "4"
                    elif event.key == pygame.K_5:
                        genes[genesi] += "5"
                    elif event.key == pygame.K_6:
                        genes[genesi] += "6"
                    elif event.key == pygame.K_7:
                        genes[genesi] += "7"
                    elif event.key == pygame.K_8:
                        genes[genesi] += "8"
                    elif event.key == pygame.K_9:
                        genes[genesi] += "9"
                    elif event.key == pygame.K_BACKSPACE:
                        if len(genes[genesi]) == 0 and genesi - 1 > -1:
                            genesi -= 1
                            try:
                                genes[genesi] = genes[genesi][:-1:]
                            except:
                                pass
                        else:
                            try:
                                genes[genesi] = genes[genesi][:-1:]
                            except:
                                pass
                            if len(genes[genesi]) == 0 and genesi - 1 > -1:
                                genesi -= 1
                    if len(genes[genesi]) >= 3:
                        genesi += 1
                        if genesi > 2:
                            genesi = 0
                pygame.display.set_caption(caption + gen + ",".join(genes))
    if not paused:
        for i in xrange(1):
            seed()
            x = randint(0, len(board) - 1)
            y = randint(0, len(board[0]) - 1)
            if aux[x][y][0] == 0 or (aux[x][y][0] != 0 and aux[x][y][1] != FOOD and aux[x][y][2] == 0):
                aux[x][y][0] = "f"
                aux[x][y][1] = FOOD
                aux[x][y][2] = 1
        for x in xrange(len(board)):
            for y in xrange(len(board[0])):
                if aux[x][y][0] == 0 or (aux[x][y][0] != 0 and aux[x][y][1] != FOOD and aux[x][y][2] == 0):
                    board[x][y][1] = 0
        for x in xrange(len(aux)):
            for y in xrange(len(aux[0])):
                check(x, y)
        for x in xrange(len(aux)):
            for y in xrange(len(aux[0])):
                gerate(x, y)
    printPygame()
    pygame.display.update()
pygame.quit()
