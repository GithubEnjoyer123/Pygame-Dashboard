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


def drawDescLine( player ):
    
    if player == 1:
        color = circleColor
    elif player == 2:
        color = EXCOLOR
        
    pygame.draw.line( screen, color, (15,15), (WIDTH - 15,HEIGHT - 15), 6)
    
def drawDescLineMiddle( player ):
    
    if player == 1:
        color = circleColor
    elif player == 2:
        color = EXCOLOR
        
    pygame.draw.line( screen, color, (240,240), (480 - 15,480 - 15), 6)
    
def drawDescLineLeftMiddle( player ):
    
    if player == 1:
        color = circleColor
    elif player == 2:
        color = EXCOLOR
        
    pygame.draw.line( screen, color, (0,240), (240 - 15,480 - 15), 6)
    
    
def drawDescLineLeftBottomCorner( player ):
    
    if player == 1:
        color = circleColor
    elif player == 2:
        color = EXCOLOR
        
    pygame.draw.line( screen, color, (0,480), (240 - 15,720 - 15), 6)
    
    
def drawDescLineRightBottomCorner( player ):
    
    if player == 1:
        color = circleColor
    elif player == 2:
        color = EXCOLOR
        
    pygame.draw.line( screen, color, (480,480), (720 - 15,720 - 15), 6)
    
def drawDescLineTopMiddle( player ):
    
    if player == 1:
        color = circleColor
    elif player == 2:
        color = EXCOLOR
        
    pygame.draw.line( screen, color, (240,0), (480 - 15, 240 - 15), 6)
    
def drawDescLineTopRight( player ):
    
    if player == 1:
        color = circleColor
    elif player == 2:
        color = EXCOLOR
        
    pygame.draw.line( screen, color, (480,0), (720 - 15, 240 - 15), 6)
    
    
def drawDescLineMiddleRight( player ):
    
    if player == 1:
        color = circleColor
    elif player == 2:
        color = EXCOLOR
        
    pygame.draw.line( screen, color, (480,240), (720 - 15, 480 - 15), 6)
    
def drawDescLineBottomMiddle( player ):
    
    if player == 1:
        color = circleColor
    elif player == 2:
        color = EXCOLOR
        
    pygame.draw.line( screen, color, (240,480), (480 - 15, 720 - 15), 6)