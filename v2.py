import pygame
from pygame.locals import *
from random import randint

board = [[[0, 0] for x in xrange(87)] for y in xrange(162)]
aux = [[[0, 0] for x in xrange(87)] for y in xrange(162)]

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

ii = 0
POISON = (255, 0, 0)
GRAY = (192, 192, 192)
VIRUS = (255, 0, 0)
MARKER = (255, 116, ii)

windowSurface.fill(WHITE)

running = True
paused = False
erase = False
wall = False
poison = False
Y = True
B = False
virus = False
marker = False
black = False
cure = False


def check(x, y):
    try:
        if aux[x][y][1] == 4:
            if aux[x - 1][y - 1][1] == 3:
                aux[x - 1][y - 1][1] = 4
                if aux[x][y - 2][1] == 3:
                    aux[x][y - 2][1] = 4
            if aux[x][y - 1][1] == 3:
                aux[x][y - 1][1] = 4
                if aux[x + 2][y - 2][1] == 3:
                    aux[x + 2][y - 2][1] = 4
            if aux[x + 1][y - 1][1] == 3:
                aux[x + 1][y - 1][1] = 4
                if aux[x - 2][y][1] == 3:
                    aux[x - 2][y][1] = 4
            if aux[x - 1][y][1] == 3:
                aux[x - 1][y][1] = 4
                if aux[x + 2][y][1] == 3:
                    aux[x + 2][y][1] = 4
            if aux[x + 1][y][1] == 3:
                aux[x + 1][y][1] = 4
                if aux[x - 2][y + 2][1] == 3:
                    aux[x - 2][y + 2][1] = 4
            if aux[x - 1][y + 1][1] == 3:
                aux[x - 1][y + 1][1] = 4
                if aux[x][y - 2][1] == 3:
                    aux[x][y - 2][1] = 4
            if aux[x][y - 1][1] == 3:
                aux[x][y - 1][1] = 4
                if aux[x + 2][y + 2][1] == 3:
                    aux[x + 2][y + 2][1] = 4
            if aux[x + 1][y + 1][1] == 3:
                aux[x + 1][y + 1][1] = 4
                if aux[x - 2][y - 2][1] == 3:
                    aux[x - 2][y - 2][1] = 4
        if aux[x][y][0] != 0 and aux[x][y][1] == 3 and aux[x][y][0] != 10:
            if aux[x][y][1] == 3:
                if aux[x][y][0] != 0 and aux[x - 1][y - 1][0] != 10:
                    aux[x - 1][y - 1][1] = 3
                    if aux[x][y][0] != 0 and aux[x - 1][y - 1][0] != 10:
                        aux[x - 2][y - 2][1] = 3
                if aux[x][y][0] != 0 and aux[x][y - 1][0] != 10:
                    aux[x][y - 1][1] = 3
                    if aux[x][y][0] != 0 and aux[x][y - 1][0] != 10:
                        aux[x][y - 2][1] = 3
                if aux[x][y][0] != 0 and aux[x + 1][y - 1][0] != 10:
                    aux[x + 1][y - 1][1] = 3
                    if aux[x][y][0] != 0 and aux[x + 1][y - 1][0] != 10:
                        aux[x + 2][y - 2][1] = 3
                if aux[x][y][0] != 0 and aux[x - 1][y][0] != 10:
                    aux[x - 1][y][1] = 3
                    if aux[x][y][0] != 0 and aux[x - 1][y][0] != 10:
                        aux[x - 2][y][1] = 3
                if aux[x][y][0] != 0 and aux[x + 1][y][0] != 10:
                    aux[x + 1][y][1] = 3
                    if aux[x][y][0] != 0 and aux[x + 1][y][0] != 10:
                        aux[x + 2][y][1] = 3
                if aux[x][y][0] != 0 and aux[x - 1][y + 1][0] != 10:
                    aux[x - 1][y + 1][1] = 3
                    if aux[x][y][0] != 0 and aux[x - 1][y + 1][0] != 10:
                        aux[x - 2][y + 2][1] = 3
                if aux[x][y][0] != 0 and aux[x][y - 1][0] != 10:
                    aux[x][y - 1][1] = 3
                    if aux[x][y][0] != 0 and aux[x][y - 1][0] != 10:
                        aux[x][y - 2][1] = 3
                if aux[x][y][0] != 0 and aux[x + 1][y + 1][0] != 10:
                    aux[x + 1][y + 1][1] = 3
                    if aux[x][y][0] != 0 and aux[x + 1][y + 1][0] != 10:
                        aux[x + 2][y + 2][1] = 3
        elif board[x][y][0] == 4 or board[x][y][0] == 3:
            i = randint(1, 8)
            if i == 1:
                if aux[x - 1][y - 1][0] != 10:
                    if aux[x - 1][y - 1][0] == 100:
                        for x1 in range(x - 10, x + 10):
                            for y1 in range(y - 10, y + 10):
                                aux[x1][y1][0] = 0
                                board[x1][y1][0] = 0
                    elif (aux[x - 1][y - 1][0] > 11 and aux[x][y][0] == 1) or aux[x - 1][y - 1][0] != 0:
                        aux[x][y][0] = 0
                        if aux[x][y][1] == 1:
                            for x1 in range(x - randint(0, 2), x + randint(0, 2)):
                                for y1 in range(y - randint(0, 2), y + randint(0, 2)):
                                    aux[x1][y1][1] = 1
                        pass
                    else:
                        aux[x][y][0] += 1
                        if aux[x][y][1] == 1:
                            k = randint(0, 10)
                            if k < 5:
                                aux[x - 1][y - 1][0] = 1
                                aux[x - 1][y - 1][1] = 1
                            else:
                                aux[x - 1][y - 1][0] = 1
                                aux[x - 1][y - 1][1] = 0
                        elif aux[x][y][1] == 2:
                            aux[x - 1][y - 1][0] = 2
                            aux[x - 1][y - 1][1] = 2
                        elif aux[x - 1][y - 1][1] == 3:
                            pass
                        elif aux[x][y][1] == 4:
                            i = randint(0, 10)
                            if i < 5:
                                aux[x - 1][y - 1][0] = 1
                                aux[x - 1][y - 1][1] = 4
                            else:
                                aux[x - 1][y - 1][0] = 1
                                aux[x - 1][y - 1][1] = 0
                        else:
                            aux[x - 1][y - 1][0] = 1
                            aux[x - 1][y - 1][1] = 4
            elif i == 2:
                if aux[x][y - 1][0] != 10:
                    if aux[x][y - 1][0] == 100:
                        for x1 in xrange(x - 10, x + 10):
                            for y1 in xrange(y - 10, y + 10):
                                aux[x1][y1][0] = 0
                                board[x1][y1][0] = 0
                    elif (aux[x][y - 1][0] > 11 and aux[x][y][0] == 1) or aux[x][y - 1][0] != 0:
                        aux[x][y][0] = 0
                        if aux[x][y][1] == 1:
                            for x1 in xrange(x - randint(0, 2), x + randint(0, 2)):
                                for y1 in xrange(y - randint(0, 2), y + randint(0, 2)):
                                    aux[x1][y1][1] = 1
                        pass
                    else:
                        aux[x][y][0] += 1
                        if aux[x][y][1] == 1:
                            k = randint(0, 10)
                            if k < 5:
                                aux[x][y - 1][0] = 1
                                aux[x][y - 1][1] = 1
                            else:
                                aux[x][y - 1][0] = 1
                                aux[x][y - 1][1] = 0
                        elif aux[x][y][1] == 2:
                            aux[x][y - 1][0] = 2
                            aux[x][y - 1][1] = 2
                        elif aux[x][y - 1][1] == 3:
                            pass
                        elif aux[x][y][1] == 4:
                            k = randint(0, 10)
                            if k < 5:
                                aux[x][y - 1][0] = 1
                                aux[x][y - 1][1] = 4
                            else:
                                aux[x][y - 1][0] = 1
                                aux[x][y - 1][1] = 0
                        else:
                            aux[x][y - 1][0] = 1
                            aux[x][y - 1][1] = 4
            elif i == 3:
                if aux[x + 1][y - 1][0] != 10:
                    if aux[x + 1][y - 1][0] == 100:
                        for x1 in xrange(x - 10, x + 10):
                            for y1 in xrange(y - 10, y + 10):
                                aux[x1][y1][0] = 0
                                board[x1][y1][0] = 0
                    elif (aux[x + 1][y - 1][0] > 11 and aux[x][y][0] == 1) or aux[x + 1][y - 1][0] != 0:
                        aux[x][y][0] = 0
                        if aux[x][y][1] == 1:
                            for x1 in xrange(x - randint(0, 2), x + randint(0, 2)):
                                for y1 in xrange(y - randint(0, 2), y + randint(0, 2)):
                                    aux[x1][y1][1] = 1
                        pass
                    else:
                        aux[x][y][0] += 1
                        if aux[x][y][1] == 1:
                            k = randint(0, 10)
                            if k < 5:
                                aux[x + 1][y - 1][0] = 1
                                aux[x + 1][y - 1][1] = 1
                            else:
                                aux[x + 1][y - 1][0] = 1
                                aux[x + 1][y - 1][1] = 0
                        elif aux[x][y][1] == 2:
                            aux[x + 1][y - 1][0] = 2
                            aux[x + 1][y - 1][1] = 2
                        elif aux[x + 1][y - 1][1] == 3:
                            pass
                        elif aux[x][y][1] == 4:
                            k = randint(0, 10)
                            if k < 5:
                                aux[x + 1][y - 1][0] = 1
                                aux[x + 1][y - 1][1] = 4
                            else:
                                aux[x + 1][y - 1][0] = 1
                                aux[x + 1][y - 1][1] = 0
                        else:
                            aux[x + 1][y - 1][0] = 1
                            aux[x + 1][y - 1][1] = 0
            elif i == 4:
                if aux[x - 1][y][0] != 10:
                    if aux[x - 1][y][0] == 100:
                        for x1 in xrange(x - 10, x + 10):
                            for y1 in xrange(y - 10, y + 10):
                                aux[x1][y1][0] = 0
                                board[x1][y1][0] = 0
                    elif (aux[x - 1][y][0] > 11 and aux[x][y][0] == 1) or aux[x - 1][y][0] != 0:
                        aux[x][y][0] = 0
                        if aux[x][y][1] == 1:
                            for x1 in xrange(x - randint(0, 2), x + randint(0, 2)):
                                for y1 in xrange(y - randint(0, 2), y + randint(0, 2)):
                                    aux[x1][y1][1] = 1
                        pass
                    else:
                        aux[x][y][0] += 1
                        if aux[x][y][1] == 1:
                            k = randint(0, 10)
                            if k < 5:
                                aux[x - 1][y][0] = 1
                                aux[x - 1][y][1] = 1
                            else:
                                aux[x - 1][y][0] = 1
                                aux[x - 1][y][1] = 0
                        elif aux[x][y][1] == 2:
                            aux[x - 1][y][0] = 2
                            aux[x - 1][y][1] = 2
                        elif aux[x - 1][y][1] == 3:
                            pass
                        elif aux[x][y][1] == 4:
                            k = randint(0, 10)
                            if k < 5:
                                aux[x - 1][y][0] = 1
                                aux[x - 1][y][1] = 4
                            else:
                                aux[x - 1][y][0] = 1
                                aux[x - 1][y][1] = 0
                        else:
                            aux[x - 1][y][0] = 1
                            aux[x - 1][y][1] = 0
            elif i == 5:
                if aux[x + 1][y][0] != 10:
                    if aux[x + 1][y][0] == 100:
                        for x1 in xrange(x - 10, x + 10):
                            for y1 in xrange(y - 10, y + 10):
                                aux[x1][y1][0] = 0
                                board[x1][y1][0] = 0
                    elif (aux[x + 1][y][0] > 11 and aux[x][y][0] == 1) or aux[x + 1][y][0] != 0:
                        aux[x][y][0] = 0
                        if aux[x][y][1] == 1:
                            for x1 in xrange(x - randint(0, 2), x + randint(0, 2)):
                                for y1 in xrange(y - randint(0, 2), y + randint(0, 2)):
                                    aux[x1][y1][1] = 1
                        pass
                    else:
                        aux[x][y][0] += 1
                        if aux[x][y][1] == 1:
                            k = randint(0, 10)
                            if k < 5:
                                aux[x + 1][y][0] = 1
                                aux[x + 1][y][1] = 1
                            else:
                                aux[x + 1][y][0] = 1
                                aux[x + 1][y][1] = 0
                        elif aux[x][y][1] == 2:
                            aux[x + 1][y][0] = 2
                            aux[x + 1][y][1] = 2
                        elif aux[x + 1][y][1] == 3:
                            pass
                        elif aux[x][y][1] == 4:
                            k = randint(0, 10)
                            if k < 5:
                                aux[x + 1][y][0] = 1
                                aux[x + 1][y][1] = 4
                            else:
                                aux[x + 1][y][0] = 1
                                aux[x + 1][y][1] = 0
                        else:
                            aux[x + 1][y][0] = 1
                            aux[x + 1][y][1] = 0
            elif i == 6:
                if aux[x - 1][y + 1][0] != 10:
                    if aux[x - 1][y + 1][0] == 100:
                        for x1 in xrange(x - 10, x + 10):
                            for y1 in xrange(y - 10, y + 10):
                                aux[x1][y1][0] = 0
                                board[x1][y1][0] = 0
                    elif (aux[x - 1][y + 1][0] > 11 and aux[x][y][0] == 1) or aux[x - 1][y + 1][0] != 0:
                        aux[x][y][0] = 0
                        if aux[x][y][1] == 1:
                            for x1 in xrange(x - randint(0, 2), x + randint(0, 2)):
                                for y1 in xrange(y - randint(0, 2), y + randint(0, 2)):
                                    aux[x1][y1][1] = 1
                        pass
                    else:
                        aux[x][y][0] += 1
                        if aux[x][y][1] == 1:
                            k = randint(0, 10)
                            if k < 5:
                                aux[x - 1][y + 1][0] = 1
                                aux[x - 1][y + 1][1] = 1
                            else:
                                aux[x - 1][y + 1][0] = 1
                                aux[x - 1][y + 1][1] = 0
                        elif aux[x][y][1] == 2:
                            aux[x - 1][y + 1][0] = 2
                            aux[x - 1][y + 1][1] = 2
                        elif aux[x - 1][y + 1][1] == 3:
                            pass
                        elif aux[x][y][1] == 4:
                            k = randint(0, 10)
                            if k < 5:
                                aux[x - 1][y + 1][0] = 1
                                aux[x - 1][y + 1][1] = 4
                            else:
                                aux[x - 1][y + 1][0] = 1
                                aux[x - 1][y + 1][1] = 0
                        else:
                            aux[x - 1][y + 1][0] = 1
                            aux[x - 1][y + 1][1] = 0
            elif i == 7:
                if aux[x][y + 1][0] != 10:
                    if aux[x][y + 1][0] == 100:
                        for x1 in xrange(x - 10, x + 10):
                            for y1 in xrange(y - 10, y + 10):
                                aux[x1][y1][0] = 0
                                board[x1][y1][0] = 0
                    elif (aux[x][y + 1][0] > 11 and aux[x][y][0] == 1) or aux[x][y + 1][0] != 0:
                        aux[x][y][0] = 0
                        if aux[x][y][1] == 1:
                            for x1 in xrange(x - randint(0, 2), x + randint(0, 2)):
                                for y1 in xrange(y - randint(0, 2), y + randint(0, 2)):
                                    aux[x1][y1][1] = 1
                        pass
                    else:
                        aux[x][y][0] += 1
                        if aux[x][y][1] == 1:
                            k = randint(0, 10)
                            if k < 5:
                                aux[x][y + 1][0] = 1
                                aux[x][y + 1][1] = 1
                            else:
                                aux[x][y + 1][0] = 1
                                aux[x][y + 1][1] = 0
                        elif aux[x][y][1] == 2:
                            aux[x][y + 1][0] = 2
                            aux[x][y + 1][1] = 2
                        elif aux[x][y + 1][1] == 3:
                            pass
                        elif aux[x][y][1] == 4:
                            k = randint(0, 10)
                            if k < 5:
                                aux[x][y + 1][0] = 1
                                aux[x][y + 1][1] = 4
                            else:
                                aux[x][y + 1][0] = 1
                                aux[x][y + 1][1] = 0
                        else:
                            aux[x][y + 1][0] = 1
                            aux[x][y + 1][1] = 0
            else:
                if aux[x + 1][y + 1][0] != 10:
                    if aux[x + 1][y + 1][0] == 100:
                        for x1 in xrange(x - 10, x + 10):
                            for y1 in xrange(y - 10, y + 10):
                                aux[x1][y1][0] = 0
                                board[x1][y1][0] = 0
                    elif (aux[x + 1][y + 1][0] > 11 and aux[x][y][0] == 1) or aux[x + 1][y + 1][0] != 0:
                        aux[x][y][0] = 0
                        if aux[x][y][1] == 1:
                            for x1 in xrange(x - randint(0, 2), x + randint(0, 2)):
                                for y1 in xrange(y - randint(0, 2), y + randint(0, 2)):
                                    aux[x1][y1][1] = 1
                        pass
                    else:
                        aux[x][y][0] += 1
                        if aux[x][y][1] == 1:
                            k = randint(0, 10)
                            if k < 5:
                                aux[x + 1][y + 1][0] = 1
                                aux[x + 1][y + 1][1] = 1
                            else:
                                aux[x + 1][y + 1][0] = 1
                                aux[x + 1][y + 1][1] = 0
                        elif aux[x][y][1] == 2:
                            aux[x + 1][y + 1][0] = 2
                            aux[x + 1][y + 1][1] = 2
                        elif aux[x + 1][y + 1][1] == 3:
                            pass
                        elif aux[x][y][1] == 4:
                            k = randint(0, 10)
                            if k < 5:
                                aux[x + 1][y + 1][0] = 1
                                aux[x + 1][y + 1][1] = 4
                            else:
                                aux[x + 1][y + 1][0] = 1
                                aux[x + 1][y + 1][1] = 0
                        else:
                            aux[x + 1][y + 1][0] = 1
                            aux[x + 1][y + 1][1] = 4
        elif board[x][y][0] == 14 or board[x][y][0] == 13:
            i = randint(1, 8)
            if i == 1:
                if aux[x - 1][y - 1][0] != 10:
                    if aux[x - 1][y - 1][0] == 100:
                        for x1 in xrange(x - 10, x + 10):
                            for y1 in xrange(y - 10, y + 10):
                                aux[x1][y1][0] = 0
                                board[x1][y1][0] = 0
                    elif (aux[x - 1][y - 1][0] > 11 and aux[x][y][0] == 1) or aux[x - 1][y - 1][0] != 0:
                        aux[x][y][0] = 0
                        if aux[x][y][1] == 1:
                            for x1 in xrange(x - randint(0, 2), x + randint(0, 2)):
                                for y1 in xrange(y - randint(0, 2), y + randint(0, 2)):
                                    aux[x1][y1][1] = 1
                        pass
                    else:
                        aux[x][y][0] += 1
                        if aux[x][y][1] == 1:
                            k = randint(0, 10)
                            if k < 5:
                                aux[x - 1][y - 1][0] = 11
                                aux[x - 1][y - 1][1] = 1
                            else:
                                aux[x - 1][y - 1][0] = 11
                                aux[x - 1][y - 1][1] = 0
                        elif aux[x][y][1] == 2:
                            aux[x - 1][y - 1][0] = 11
                            aux[x - 1][y - 1][1] = 2
                        else:
                            aux[x - 1][y - 1][0] = 11
                            aux[x - 1][y - 1][1] = 0
            elif i == 2:
                if aux[x][y - 1][0] != 10:
                    if aux[x][y - 1][0] == 100:
                        for x1 in xrange(x - 10, x + 10):
                            for y1 in xrange(y - 10, y + 10):
                                aux[x1][y1][0] = 0
                                board[x1][y1][0] = 0
                    elif (aux[x][y - 1][0] > 11 and aux[x][y][0] == 1) or aux[x][y - 1][0] != 0:
                        aux[x][y][0] = 0
                        if aux[x][y][1] == 1:
                            for x1 in xrange(x - randint(0, 2), x + randint(0, 2)):
                                for y1 in xrange(y - randint(0, 2), y + randint(0, 2)):
                                    aux[x1][y1][1] = 1
                        pass
                    else:
                        aux[x][y][0] += 1
                        if aux[x][y][1] == 1:
                            k = randint(0, 10)
                            if k < 5:
                                aux[x][y - 1][0] = 11
                                aux[x][y - 1][1] = 1
                            else:
                                aux[x][y - 1][0] = 11
                                aux[x][y - 1][1] = 0
                        elif aux[x][y][1] == 2:
                            aux[x][y - 1][0] = 11
                            aux[x][y - 1][1] = 2
                        else:
                            aux[x][y - 1][0] = 11
                            aux[x][y - 1][1] = 0
            elif i == 3:
                if aux[x + 1][y - 1][0] != 10:
                    if aux[x + 1][y - 1][0] == 100:
                        for x1 in xrange(x - 10, x + 10):
                            for y1 in xrange(y - 10, y + 10):
                                aux[x1][y1][0] = 0
                                board[x1][y1][0] = 0
                    elif (aux[x + 1][y - 1][0] > 11 and aux[x][y][0] == 1) or aux[x + 1][y - 1][0] != 0:
                        aux[x][y][0] = 0
                        if aux[x][y][1] == 1:
                            for x1 in xrange(x - randint(0, 2), x + randint(0, 2)):
                                for y1 in xrange(y - randint(0, 2), y + randint(0, 2)):
                                    aux[x1][y1][1] = 1
                        pass
                    else:
                        aux[x][y][0] += 1
                        if aux[x][y][1] == 1:
                            k = randint(0, 10)
                            if k < 5:
                                aux[x + 1][y - 1][0] = 11
                                aux[x + 1][y - 1][1] = 1
                            else:
                                aux[x + 1][y - 1][0] = 11
                                aux[x + 1][y - 1][1] = 0
                        elif aux[x][y][1] == 2:
                            aux[x + 1][y - 1][0] = 11
                            aux[x + 1][y - 1][1] = 2
                        else:
                            aux[x + 1][y - 1][0] = 11
                            aux[x + 1][y - 1][1] = 0
            elif i == 4:
                if aux[x - 1][y][0] != 10:
                    if aux[x - 1][y][0] == 100:
                        for x1 in xrange(x - 10, x + 10):
                            for y1 in xrange(y - 10, y + 10):
                                aux[x1][y1][0] = 0
                                board[x1][y1][0] = 0
                    elif (aux[x - 1][y][0] > 11 and aux[x][y][0] == 1) or aux[x - 1][y][0] != 0:
                        aux[x][y][0] = 0
                        if aux[x][y][1] == 1:
                            for x1 in xrange(x - randint(0, 2), x + randint(0, 2)):
                                for y1 in xrange(y - randint(0, 2), y + randint(0, 2)):
                                    aux[x1][y1][1] = 1
                        pass
                    else:
                        aux[x][y][0] += 1
                        if aux[x][y][1] == 1:
                            k = randint(0, 10)
                            if k < 5:
                                aux[x - 1][y][0] = 11
                                aux[x - 1][y][1] = 1
                            else:
                                aux[x - 1][y][0] = 11
                                aux[x - 1][y][1] = 0
                        elif aux[x][y][1] == 2:
                            aux[x - 1][y][0] = 11
                            aux[x - 1][y][1] = 2
                        else:
                            aux[x - 1][y][0] = 11
                            aux[x - 1][y][1] = 0
            elif i == 5:
                if aux[x + 1][y][0] != 10:
                    if aux[x + 1][y][0] == 100:
                        for x1 in xrange(x - 10, x + 10):
                            for y1 in xrange(y - 10, y + 10):
                                aux[x1][y1][0] = 0
                                board[x1][y1][0] = 0
                    elif (aux[x + 1][y][0] > 11 and aux[x][y][0] == 1) or aux[x + 1][y][0] != 0:
                        aux[x][y][0] = 0
                        if aux[x][y][1] == 1:
                            for x1 in xrange(x - randint(0, 2), x + randint(0, 2)):
                                for y1 in xrange(y - randint(0, 2), y + randint(0, 2)):
                                    aux[x1][y1][1] = 1
                        pass
                    else:
                        aux[x][y][0] += 1
                        if aux[x][y][1] == 1:
                            k = randint(0, 10)
                            if k < 5:
                                aux[x + 1][y][0] = 11
                                aux[x + 1][y][1] = 1
                            else:
                                aux[x + 1][y][0] = 11
                                aux[x + 1][y][1] = 0
                        elif aux[x][y][1] == 2:
                            aux[x + 1][y][0] = 11
                            aux[x + 1][y][1] = 2
                        else:
                            aux[x + 1][y][0] = 11
                            aux[x + 1][y][1] = 0
            elif i == 6:
                if aux[x - 1][y + 1][0] != 10:
                    if aux[x - 1][y + 1][0] == 100:
                        for x1 in xrange(x - 10, x + 10):
                            for y1 in xrange(y - 10, y + 10):
                                aux[x1][y1][0] = 0
                                board[x1][y1][0] = 0
                    elif (aux[x - 1][y + 1][0] > 11 and aux[x][y][0] == 1) or aux[x - 1][y + 1][0] != 0:
                        aux[x][y][0] = 0
                        if aux[x][y][1] == 1:
                            for x1 in xrange(x - randint(0, 2), x + randint(0, 2)):
                                for y1 in xrange(y - randint(0, 2), y + randint(0, 2)):
                                    aux[x1][y1][1] = 1
                        pass
                    else:
                        aux[x][y][0] += 1
                        if aux[x][y][1] == 1:
                            k = randint(0, 10)
                            if k < 5:
                                aux[x - 1][y + 1][0] = 11
                                aux[x - 1][y + 1][1] = 1
                            else:
                                aux[x - 1][y + 1][0] = 11
                                aux[x - 1][y + 1][1] = 0
                        elif aux[x][y][1] == 2:
                            aux[x - 1][y + 1][0] = 11
                            aux[x - 1][y + 1][1] = 2
                        else:
                            aux[x - 1][y + 1][0] = 11
                            aux[x - 1][y + 1][1] = 0
            elif i == 7:
                if aux[x][y + 1][0] != 10:
                    if aux[x][y + 1][0] == 100:
                        for x1 in xrange(x - 10, x + 10):
                            for y1 in xrange(y - 10, y + 10):
                                aux[x1][y1][0] = 0
                                board[x1][y1][0] = 0
                    elif (aux[x][y + 1][0] > 11 and aux[x][y][0] == 1) or aux[x][y + 1][0] != 0:
                        aux[x][y][0] = 0
                        if aux[x][y][1] == 1:
                            for x1 in xrange(x - randint(0, 2), x + randint(0, 2)):
                                for y1 in xrange(y - randint(0, 2), y + randint(0, 2)):
                                    aux[x1][y1][1] = 1
                        pass
                    else:
                        aux[x][y][0] += 1
                        if aux[x][y][1] == 1:
                            k = randint(0, 10)
                            if k < 5:
                                aux[x][y + 1][0] = 11
                                aux[x][y + 1][1] = 1
                            else:
                                aux[x][y + 1][0] = 11
                                aux[x][y + 1][1] = 0
                        elif aux[x][y][1] == 2:
                            aux[x][y + 1][0] = 11
                            aux[x][y + 1][1] = 2
                        else:
                            aux[x][y + 1][0] = 11
                            aux[x][y + 1][1] = 0
            else:
                if aux[x + 1][y + 1][0] != 10:
                    if aux[x + 1][y + 1][0] == 100:
                        for x1 in xrange(x - 10, x + 10):
                            for y1 in xrange(y - 10, y + 10):
                                aux[x1][y1][0] = 0
                                board[x1][y1][0] = 0
                    elif (aux[x + 1][y + 1][0] > 11 and aux[x][y][0] == 1) or aux[x + 1][y + 1][0] != 0:
                        aux[x][y][0] = 0
                        if aux[x][y][1] == 1:
                            for x1 in xrange(x - randint(0, 2), x + randint(0, 2)):
                                for y1 in xrange(y - randint(0, 2), y + randint(0, 2)):
                                    aux[x1][y1][1] = 1
                        pass
                    else:
                        aux[x][y][0] += 1
                        if aux[x][y][1] == 1:
                            k = randint(0, 10)
                            if k < 5:
                                aux[x + 1][y + 1][0] = 11
                                aux[x + 1][y + 1][1] = 1
                            else:
                                aux[x + 1][y + 1][0] = 11
                                aux[x + 1][y + 1][1] = 0
                        elif aux[x][y][1] == 2:
                            aux[x + 1][y + 1][0] = 11
                            aux[x + 1][y + 1][1] = 2
                        else:
                            aux[x + 1][y + 1][0] = 11
                            aux[x + 1][y + 1][1] = 0
        elif aux[x][y][0] != 10 and aux[x][y][0] != 100 and aux[x][y][0] != 0:
            aux[x][y][0] += 1

    except:
        pass


def gerate(x, y):
    if aux[x][y][0] == 1:
        board[x][y][0] = 1
    elif aux[x][y][0] == 2:
        board[x][y][0] = 2
    elif aux[x][y][0] == 3:
        board[x][y][0] = 3
    elif aux[x][y][0] == 4:
        board[x][y][0] = 4
    elif aux[x][y][0] == 10:
        board[x][y][0] = 10
    elif aux[x][y][0] == 11:
        board[x][y][0] = 11
    elif aux[x][y][0] == 12:
        board[x][y][0] = 12
    elif aux[x][y][0] == 13:
        board[x][y][0] = 13
    elif aux[x][y][0] == 14:
        board[x][y][0] = 14
    elif aux[x][y][0] == 100:
        board[x][y][0] = 100
    else:
        board[x][y][0] = 0
        board[x][y][1] = 0
        aux[x][y][0] = 0
        aux[x][y][1] = 0
    if aux[x][y][1] == 1 and aux[x][y][0] != 0:
        board[x][y][1] = 1
    elif aux[x][y][1] == 2 and aux[x][y][0] != 0:
        board[x][y][1] = 2
    elif aux[x][y][1] == 3 and aux[x][y][0] != 0:
        board[x][y][1] = 3
    elif aux[x][y][1] == 4 and aux[x][y][0] != 0:
        board[x][y][1] = 4
    else:
        board[x][y][1] = 0


def print_pygame():
    for x in xrange(len(board)):
        for y in xrange(len(board[0])):
            if board[x][y][0] >= 1 and board[x][y][0] <= 4:
                draw_y(x * 8, y * 8)
            elif board[x][y][0] >= 11 and board[x][y][0] <= 14:
                draw_b(x * 8, y * 8)
            elif board[x][y][0] == 10:
                draw_wall(x * 8, y * 8)
            elif board[x][y][0] == 100:
                draw_poison(x * 8, y * 8)
            else:
                draw_board(x * 8, y * 8)
            if board[x][y][1] == 1:
                draw_virus(x * 8, y * 8)
            elif board[x][y][1] == 2:
                draw_marker(x * 8, y * 8)
            elif board[x][y][1] == 3:
                draw_black(x * 8, y * 8)
            elif board[x][y][1] == 4:
                draw_cure(x * 8, y * 8)


def draw_y(x, y):
    if board[x / 8][y / 8][0] == 1:
        x += 6
        y += 6
        pygame.draw.polygon(windowSurface, CHILDY, ((x - 3, y - 3), (x + 3, y - 3), (x + 3, y + 3), (x - 3, y + 3)))
    elif board[x / 8][y / 8][0] == 2:
        x += 6
        y += 6
        pygame.draw.polygon(windowSurface, TEENY, ((x - 3, y - 3), (x + 3, y - 3), (x + 3, y + 3), (x - 3, y + 3)))
    elif board[x / 8][y / 8][0] == 3:
        x += 6
        y += 6
        pygame.draw.polygon(windowSurface, ADULTY, ((x - 3, y - 3), (x + 3, y - 3), (x + 3, y + 3), (x - 3, y + 3)))
    else:
        x += 6
        y += 6
        pygame.draw.polygon(windowSurface, ELDERY, ((x - 3, y - 3), (x + 3, y - 3), (x + 3, y + 3), (x - 3, y + 3)))


def draw_b(x, y):
    if board[x / 8][y / 8][0] == 11:
        x += 6
        y += 6
        pygame.draw.polygon(windowSurface, CHILDB, ((x - 3, y - 3), (x + 3, y - 3), (x + 3, y + 3), (x - 3, y + 3)))
    elif board[x / 8][y / 8][0] == 12:
        x += 6
        y += 6
        pygame.draw.polygon(windowSurface, TEENB, ((x - 3, y - 3), (x + 3, y - 3), (x + 3, y + 3), (x - 3, y + 3)))
    elif board[x / 8][y / 8][0] == 13:
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


def draw_virus(x, y):
    x += 6
    y += 6
    pygame.draw.polygon(windowSurface, VIRUS, ((x - 2, y - 2), (x + 2, y - 2), (x + 2, y + 2), (x - 2, y + 2)))


def draw_marker(x, y):
    x += 6
    y += 6
    pygame.draw.polygon(windowSurface, (255, 116, ii), ((x - 2, y - 2), (x + 2, y - 2), (x + 2, y + 2), (x - 2, y + 2)))


def draw_black(x, y):
    x += 6
    y += 6
    pygame.draw.polygon(windowSurface, BLACK, ((x - 2, y - 2), (x + 2, y - 2), (x + 2, y + 2), (x - 2, y + 2)))


def draw_cure(x, y):
    x += 6
    y += 6
    pygame.draw.polygon(windowSurface, WHITE, ((x - 2, y - 2), (x + 2, y - 2), (x + 2, y + 2), (x - 2, y + 2)))


for x in xrange(len(board)):
    aux[x][0][0] = 10
    aux[x][86][0] = 10
for y in xrange(len(board[0])):
    aux[0][y][0] = 10
    aux[161][y][0] = 10
while running:
    for x in xrange(len(board)):
        aux[x][0][0] = 10
        aux[x][86][0] = 10
    for y in xrange(len(board[0])):
        aux[0][y][0] = 10
        aux[161][y][0] = 10
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            (mouseX, mouseY) = pygame.mouse.get_pos()
            mouseX -= 3
            mouseY -= 3
            if erase:
                erase = (True, False)[erase]
                for x in xrange(5):
                    for y in xrange(5):
                        aux[mouseX / 8 - x][mouseY / 8 - y][0] = 0
                        aux[mouseX / 8 - x][mouseY / 8 + y][0] = 0
                        aux[mouseX / 8 + x][mouseY / 8 - y][0] = 0
                        aux[mouseX / 8 + x][mouseY / 8 + y][0] = 0
                        gerate(mouseX / 8 - x, mouseY / 8 - y)
                        gerate(mouseX / 8 - x, mouseY / 8 + y)
                        gerate(mouseX / 8 + x, mouseY / 8 - y)
                        gerate(mouseX / 8 + x, mouseY / 8 + y)
            elif wall:
                aux[mouseX / 8][mouseY / 8][0] = 10
                gerate(mouseX / 8, mouseY / 8)
            elif poison:
                aux[mouseX / 8][mouseY / 8][0] = 100
                gerate(mouseX / 8, mouseY / 8)
            elif B:
                aux[mouseX / 8][mouseY / 8][0] = 11
                gerate(mouseX / 8, mouseY / 8)
            elif Y:
                aux[mouseX / 8][mouseY / 8][0] = 1
                gerate(mouseX / 8, mouseY / 8)
            elif virus:
                for x in xrange(5):
                    for y in xrange(5):
                        aux[mouseX / 8 - x][mouseY / 8 - y][1] = 1
                        aux[mouseX / 8 - x][mouseY / 8 + y][1] = 1
                        aux[mouseX / 8 + x][mouseY / 8 - y][1] = 1
                        aux[mouseX / 8 + x][mouseY / 8 + y][1] = 1
                        gerate(mouseX / 8 - x, mouseY / 8 - y)
                        gerate(mouseX / 8 - x, mouseY / 8 + y)
                        gerate(mouseX / 8 + x, mouseY / 8 - y)
                        gerate(mouseX / 8 + x, mouseY / 8 + y)
            elif marker:
                aux[mouseX / 8][mouseY / 8][1] = 2
                gerate(mouseX / 8, mouseY / 8)
            elif black:
                aux[mouseX / 8][mouseY / 8][1] = 3
                gerate(mouseX / 8, mouseY / 8)
            elif cure:
                for x in xrange(5):
                    for y in xrange(5):
                        aux[mouseX / 8 - x][mouseY / 8 - y][1] = 4
                        aux[mouseX / 8 - x][mouseY / 8 + y][1] = 4
                        aux[mouseX / 8 + x][mouseY / 8 - y][1] = 4
                        aux[mouseX / 8 + x][mouseY / 8 + y][1] = 4
                        gerate(mouseX / 8 - x, mouseY / 8 - y)
                        gerate(mouseX / 8 - x, mouseY / 8 + y)
                        gerate(mouseX / 8 + x, mouseY / 8 - y)
                        gerate(mouseX / 8 + x, mouseY / 8 + y)
            else:
                aux[mouseX / 8][mouseY / 8][0] = 0
                gerate(mouseX / 8, mouseY / 8)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = (True, False)[paused]
                if paused:
                    pygame.display.set_caption("Paused...")
                else:
                    pygame.display.set_caption("Running!")
            elif event.key == pygame.K_c:
                for x in xrange(len(board)):
                    for y in xrange(len(board[0])):
                        aux[x][y][0] = 0
                        aux[x][y][1] = 0
                for x in xrange(len(board)):
                    for y in xrange(len(board[0])):
                        gerate(x, y)
            elif event.key == pygame.K_DELETE:
                erase = (True, False)[erase]
                wall = False
                poison = False
                B = False
                Y = False
                virus = False
                marker = False
            elif event.key == pygame.K_F1:
                wall = (True, False)[wall]
                erase = False
                poison = False
                B = False
                Y = False
                virus = False
                marker = False
            elif event.key == pygame.K_F2:
                poison = (True, False)[poison]
                erase = False
                wall = False
                B = False
                Y = False
                virus = False
                marker = False
            elif event.key == pygame.K_b:
                B = (True, False)[B]
                erase = False
                wall = False
                poison = False
                Y = False
                virus = False
                marker = False
            elif event.key == pygame.K_y:
                Y = (True, False)[Y]
                erase = False
                wall = False
                poison = False
                B = False
                virus = False
            elif event.key == pygame.K_F3:
                virus = (True, False)[virus]
                erase = False
                wall = False
                poison = False
                B = False
                Y = False
                marker = False
            elif event.key == pygame.K_v:
                for x in range(len(board)):
                    for y in range(len(board[0])):
                        board[x][y][1] = 0
                        aux[x][y][1] = 0
                printPygame()
                pygame.display.update()
            elif event.key == pygame.K_m:
                marker = (True, False)[marker]
                virus = False
                erase = False
                wall = False
                poison = False
                B = False
                Y = False
            elif event.key == pygame.K_d:
                black = (True, False)[black]
                virus = False
                erase = False
                wall = False
                poison = False
                B = False
                Y = False
                marker = False
            elif event.key == pygame.K_f:
                cure = (True, False)[cure]
                virus = False
                erase = False
                wall = False
                poison = False
                B = False
                Y = False
                marker = False
                black = False
    if not paused:
        ii += 5
        if ii > 255:
            ii = 0
        for x in xrange(len(aux)):
            for y in xrange(len(aux[0])):
                check(x, y)
        for x in range(len(aux)):
            for y in range(len(aux[0])):
                gerate(x, y)
    print_pygame()
    pygame.display.update()
pygame.quit()

