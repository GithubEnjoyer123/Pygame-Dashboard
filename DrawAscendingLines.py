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


def drawAscLine( player ):
    
    if player == 1:
        color = circleColor
    elif player == 2:
        color = EXCOLOR
        
    pygame.draw.line( screen, color,(15,HEIGHT - 15), (WIDTH - 15, 15), 6 )
    return 1
    
def drawAscLineTopMiddle( player ):
    
    if player == 1:
        color = circleColor
    elif player == 2:
        color = EXCOLOR
        
    pygame.draw.line( screen, color,(240,240), (480,0), 6 )
    return 1
    
def drawAscLineTopRight( player ):
    
    if player == 1:
        color = circleColor
    elif player == 2:
        color = EXCOLOR
        
    pygame.draw.line( screen, color,(480,240), (720,0), 6 )
    return 1
    
def drawAscLineMiddleLeft( player ):
    
    if player == 1:
        color = circleColor
    elif player == 2:
        color = EXCOLOR
        
    pygame.draw.line( screen, color,(0,480), (240,240), 6 )
    return 1
    
def drawAscLineMiddle( player ):
    
    if player == 1:
        color = circleColor
    elif player == 2:
        color = EXCOLOR
        
    pygame.draw.line( screen, color,(240,480), (480,240), 6 )
    return 1
    
def drawAscLineMiddleRight( player ):
    
    if player == 1:
        color = circleColor
    elif player == 2:
        color = EXCOLOR
        
    pygame.draw.line( screen, color,(480,480), (720,240), 6 )
    return 1
    
def drawAscLineBottomLeft( player ):
    
    if player == 1:
        color = circleColor
    elif player == 2:
        color = EXCOLOR
        
    pygame.draw.line( screen, color,(0,720), (240,480), 6 )
    return 1
    
def drawAscLineBottomMiddle( player ):
    
    if player == 1:
        color = circleColor
    elif player == 2:
        color = EXCOLOR
        
    pygame.draw.line( screen, color,(240,720), (480,480), 6 )
    return 1
    
def drawAscLineBottomRight( player ):
    
    if player == 1:
        color = circleColor
    elif player == 2:
        color = EXCOLOR
        
    pygame.draw.line( screen, color,(480,720), (720,480), 6 )
    return 1