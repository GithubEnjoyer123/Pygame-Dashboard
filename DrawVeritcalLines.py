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


def drawVertWinLine( column, player ):
    posX = column * SQUARESIZE + DIVSIZE
    
    if player == 1:
        color = circleColor
    elif player == 2:
        color = EXCOLOR
        
    pygame.draw.line( screen, color, (posX, 15), (posX, HEIGHT), 6 )
    
    
def drawVertWinLineMidddle( column, player ):
    posX = column * SQUARESIZE + DIVSIZE
    downY = 480
    
    if player == 1:
        color = circleColor
    elif player == 2:
        color = EXCOLOR
        
    pygame.draw.line( screen, color, (posX, downY), (posX, HEIGHT), 6 )
    
    
def drawVertWinLineBottom( column, player ):
    posX = column * SQUARESIZE + DIVSIZE
    downY = 720
    
    if player == 1:
        color = circleColor
    elif player == 2:
        color = EXCOLOR
        
    pygame.draw.line( screen, color, (posX, downY), (posX, 490), 6 )