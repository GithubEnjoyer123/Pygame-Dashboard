import pygame

# Size of each square
SQUARESIZE = 80
DIVSIZE = SQUARESIZE / 2

# Dimension constants
WIDTH = 240
HEIGHT = 240

# Colors for X and O
circleColor = (221, 218, 191)
EXCOLOR = (100, 100, 150)

screen = pygame.display.set_mode((720, 720))


def drawHorzWinLine( row, player ):
    posY = row * SQUARESIZE + DIVSIZE
    
    if player == 1:
        color = circleColor
    elif player == 2:
        color = EXCOLOR
    
    pygame.draw.line( screen, color, (15, posY), (WIDTH -15, posY), 6 )
    return 1
    
def drawHorzLineMiddle( row, player ):
    posY = row * SQUARESIZE + DIVSIZE
    downX = 480
    
    if player == 1:
        color = circleColor
    elif player == 2:
        color = EXCOLOR
    
    pygame.draw.line( screen, color, (downX, posY), (WIDTH, posY), 6 )
    return 1


def drawHorzWinLineBottom( row, player ):
    posY = row * SQUARESIZE + DIVSIZE
    downX = 720
    
    if player == 1:
        color = circleColor
    elif player == 2:
        color = EXCOLOR
    
    pygame.draw.line( screen, color, (downX, posY), (490, posY), 6 )
    return 1
