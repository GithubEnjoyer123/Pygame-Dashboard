import pygame, sys
import numpy as np
import math
import sys

pygame.init()

#dimension constants
WIDTH = 240
HEIGHT = 240

#screen/line dimensions
screen = pygame.display.set_mode((720, 720))
pygame.display.set_caption('SDEV 220 - Ultimate Tic Tac Toe')
clock = pygame.time.Clock()

#colors for X and 0
circleColor = ( 221, 218, 191 )
EXCOLOR = ( 100, 100, 150 )
#dimensions/colors for shapes
CIRCLERADIUS = 30
CIRCLELOOP = 6

EXWIDTH = 10
SPACE = 15


#size of each square
SQUARESIZE = 80
DIVSIZE = SQUARESIZE/2

#board dimensioms
BOARDROWS = 9
BOARDCOLUMNS = 9

#color constants
BGCOLOR = ( 34, 37, 64 )

# Main line width
MAINLINEWIDTH = 12

#Main lines color
MAINLINECOLOR = ( 221, 218, 191  )

#line width
LINEWIDTH = 6

#lines color
LINECOLOR = ( 100, 100, 150 )

#background color
screen.fill( BGCOLOR )


board = np.zeros( (BOARDROWS, BOARDCOLUMNS) )
#line drawing function
def drawLines():
    #smaller horizotntal lines
    pygame.draw.line( screen, LINECOLOR, (0,80), (720,80), LINEWIDTH )
    pygame.draw.line( screen, LINECOLOR, (0,160), (720,160), LINEWIDTH )
    pygame.draw.line( screen, LINECOLOR, (0,320), (720,320), LINEWIDTH )
    pygame.draw.line( screen, LINECOLOR, (0,400), (720,400), LINEWIDTH )
    pygame.draw.line( screen, LINECOLOR, (0,560), (720,560), LINEWIDTH )
    pygame.draw.line( screen, LINECOLOR, (0,640), (720,640), LINEWIDTH )
    
    #smaller vertical lines
    pygame.draw.line( screen, LINECOLOR, (80,0), (80,720), LINEWIDTH )
    pygame.draw.line( screen, LINECOLOR, (160,0), (160,720), LINEWIDTH )
    pygame.draw.line( screen, LINECOLOR, (320,0), (320,720), LINEWIDTH )
    pygame.draw.line( screen, LINECOLOR, (400,0), (400,720), LINEWIDTH )
    pygame.draw.line( screen, LINECOLOR, (560,0), (560,720), LINEWIDTH )
    pygame.draw.line( screen, LINECOLOR, (640,0), (640,720), LINEWIDTH )
    
    # main horizontal lines (on bottom so they render above)
    pygame.draw.line( screen, MAINLINECOLOR, (0,240), (720,240), MAINLINEWIDTH )
    pygame.draw.line( screen, MAINLINECOLOR, (0,480), (720,480), MAINLINEWIDTH )
    
    # main vertical lines
    pygame.draw.line( screen, MAINLINECOLOR, (240,0), (240,720), MAINLINEWIDTH )
    pygame.draw.line( screen, MAINLINECOLOR, (480,0), (480,720), MAINLINEWIDTH ) 

#marking square based on user
def markSquare(row,column, player):
    board[row][column] = player
 
# checks if square is avaliable  if zero return 0   
def avaliableSquare(row, column):
    return board[row][column] == 0

#checking if board is full
def isBoardFull():
    #checking range of rows
    for row in range(BOARDROWS):
            #checking range of columns
        for column in range(BOARDCOLUMNS):
            if board[row][column] == 0:
                return False
    return True   

def checkWIn(player):
    #check vertical wins
    for column in range(BOARDCOLUMNS):
        for row in range(BOARDROWS):
            if board[0][column] == player and board[1][column] == player and board[2][column] == player:
                drawVertWinLine( column, player )
                return True
            if board[row][0] == player and board[row][1] == player and board[row][2] == player or board[row][3] == player and board[row][4] == player and board[row][5] == player:
                drawHorzWinLine( row, player )
                return True

    #check desc diagonal win top corner grid - working
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        drawDescLine( player )
        return True    
        
    return False
def drawVertWinLine( column, player ):
    posX = column * SQUARESIZE + DIVSIZE
    
    if player == 1:
        color = circleColor
    elif player == 2:
        color = EXCOLOR
        
    pygame.draw.line( screen, color, (posX, 15), (posX, HEIGHT - 15), 6 )
l
def drawHorzWinLine( row, player ):
    posY = row * SQUARESIZE + DIVSIZE
    
    if player == 1:
        color = circleColor
    elif player == 2:
        color = EXCOLOR
    
    pygame.draw.line( screen, color, (15, posY), (WIDTH -15, posY), 6 )

def drawAscLine( player ):
    
    if player == 1:
        color = circleColor
    elif player == 2:
        color = EXCOLOR
        
    pygame.draw.line( screen, color,(15,HEIGHT - 15), (WIDTH - 15, 15), 6 )
        

def drawDescLine( player ):
    
    if player == 1:
        color = circleColor
    elif player == 2:
        color = EXCOLOR
        
    pygame.draw.line( screen, color, (15,15), (WIDTH - 15,HEIGHT - 15), 6)
    
def restart():
    pass

drawLines()
 #start with first player
player = 1
#function to draw the shapes, in their respective squares
def drawFigures():
    for row in range(BOARDROWS):
        for column in range(BOARDCOLUMNS):
            if board[row][column] == 1:
                #place circle at the center of the square
                pygame.draw.circle( screen, circleColor, (int(column * SQUARESIZE + DIVSIZE), int(row * SQUARESIZE + DIVSIZE)), CIRCLERADIUS, CIRCLELOOP)
            elif board[row][column] == 2:
                pygame.draw.line( screen, EXCOLOR, (column * SQUARESIZE + SPACE, row * SQUARESIZE + SQUARESIZE - SPACE), (column * SQUARESIZE + SQUARESIZE - SPACE, row * SQUARESIZE + SPACE), EXWIDTH )
                pygame.draw.line( screen, EXCOLOR, (column * SQUARESIZE + SPACE, row * SQUARESIZE + SPACE), (column * SQUARESIZE + SQUARESIZE - SPACE, row * SQUARESIZE + SQUARESIZE - SPACE), EXWIDTH )
#main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #assiging mouse clicks to a variable    
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX = event.pos[0]
            mouseY = event.pos[1]
            
            #80 is the distance between each square
            clickedRow = int(mouseY // 80)
            clickedColumn = int(mouseX // 80)
            
            #if player one goes set to player 2, if player to goes set to player 1. It's changing turns.
            if avaliableSquare( clickedRow, clickedColumn):
                if player == 1:
                    markSquare( clickedRow, clickedColumn, 1)
                    checkWIn( player )
                    player = 2
                    
                    
                elif player == 2:
                    markSquare( clickedRow, clickedColumn, 2)
                    checkWIn( player )
                    player = 1
            drawFigures()
            
            
    pygame.display.update()
    pygame.display.flip()
   
pygame.quit()
sys.exit()