import numpy as np
from DrawVeritcalLines import * 
from DrawDescendingLines import *
from DrawHorizontalLines import *
from DrawAscendingLines import *

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

#colors for overlay
OVERLAY = (255, 255, 255)
TRANSPARENT = (0, 0, 0, 75)
overlay_surface = pygame.Surface((720, 720), pygame.SRCALPHA)
overlay_surface.fill(TRANSPARENT)

EXWIDTH = 10
SPACE = 15

#Our pass for main loop, initialized as 0 for no value 
nextPass = 0

#size of each square
SQUARESIZE = 80
DIVSIZE = SQUARESIZE/2

#board dimensioms
BOARDROWS = 9
BOARDCOLUMNS = 9

board = np.zeros( (BOARDROWS, BOARDCOLUMNS) )
#line drawing function

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

#start with first player
player = 1

#marking square based on user
def markSquare(row,column, player):
    board[row][column] = player
    squareBool(row, column)

# checks if square is avaliable  if zero return 0   
def avaliableSquare(row, column):
    return board[row][column] == 0


def checkWIn(player):
    #check vertical wins
    for column in range(BOARDCOLUMNS):
        if board[0][column] == player and board[1][column] == player and board[2][column] == player:
            return drawVertWinLine( column, player )
            
        if board[3][column] == player and board[4][column] == player and board[5][column] == player:
            return drawVertWinLineMidddle( column, player )
            
        if board[6][column] == player and board[7][column] == player and board[8][column] == player:
            return drawVertWinLineBottom( column, player )
    #check horizontal wins
    for row in range(BOARDROWS):    
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            return drawHorzWinLine( row, player )
            
        if board[row][3] == player and board[row][4] == player and board[row][5] == player:
            return drawHorzLineMiddle( row, player )
            
        if board[row][6] == player and board[row][7] == player and board[row][8] == player:
            return drawHorzWinLineBottom( row, player ) 

    #check desc diagonal win 
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return drawDescLine( player )
        
    elif board[0][3] == player and board[1][4] == player and board[2][5] == player:
        return drawDescLineTopMiddle( player )
        
    elif board[0][6] == player and board[1][7] == player and board[2][8] == player:
        return drawDescLineTopRight( player )
        
    elif board[3][0] == player and board[4][1] == player and board[5][2] == player:
        return drawDescLineLeftMiddle( player )
        
    elif board[3][6] == player and board[4][7] == player and board[5][8] == player:
        return drawDescLineMiddleRight( player )
        
    elif board[6][0] == player and board[7][1] == player and board[8][2] == player:
        return drawDescLineLeftBottomCorner( player )
        
    elif board[6][6] == player and board[7][7] == player and board[8][8] == player:
        return drawDescLineRightBottomCorner( player )
        
    elif board[6][3] == player and board[7][4] == player and board[8][5] == player:
        return drawDescLineBottomMiddle( player )
        
    elif board[3][3] == player and board[4][4] == player and board[5][5] == player:
        return drawDescLineMiddle( player )
        
    #check ascending diagonal wins  
    elif board[2][0] == player and board[1][1] == player and board[0][2] == player:
        return drawAscLine( player )
        
    elif board[2][3] == player and board[1][4] == player and board[0][5] == player:
        return drawAscLineTopMiddle( player ) 
        
    elif board[2][6] == player and board[1][7] == player and board[0][8] == player:
        return drawAscLineTopRight( player )
        
    elif board[5][0] == player and board[4][1] == player and board[3][2] == player:
        return drawAscLineMiddleLeft( player ) 
    
    elif board[5][3] == player and board[4][4] == player and board[3][5] == player:
        return drawAscLineMiddle( player )
        
    elif board[5][6] == player and board[4][7] == player and board[3][8] == player:
        return drawAscLineMiddleRight( player ) 
        
    elif board[8][0] == player and board[7][1] == player and board[6][2] == player:
        return drawAscLineBottomLeft( player )
        
    elif board[8][3] == player and board[7][4] == player and board[6][5] == player:
        return drawAscLineBottomMiddle( player )      

    elif board[8][6] == player and board[7][7] == player and board[6][8] == player:
        return drawAscLineBottomRight( player ) 
    
    else:
        return 0
    
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

drawLines()

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

#checking if board is full
def isBoardFull(rows, columns):
    #checking range of rows
    for row in range(BOARDROWS):
            #checking range of columns
        for column in range(BOARDCOLUMNS):
            if board[row][column] == 0:
                return False
    return True   

#Logic to check our board number from left to right. Top left is 1, middle top is 2, top right is 3, middle left is 4, etc
#If you click in the top left of a board, it'll return 1 as that's supposed to be our next board the user needs to click on.
def nextBoard(row, column):
    if (row == 0 or row == 3 or row == 6) and (column == 0 or column == 3 or column == 6):
        return 1
    elif (row == 1 or row == 4 or row == 7) and (column == 0 or column == 3 or column == 6):
        return 4
    elif (row == 2 or row == 5 or row == 8) and (column == 0 or column == 3 or column == 6):
        return 7
    elif (row == 0 or row == 3 or row == 6) and (column == 1 or column == 4 or column == 7):
        return 2
    elif (row == 0 or row == 3 or row == 6) and (column == 2 or column == 5 or column == 8):
        return 3
    elif (row == 1 or row == 4 or row == 7) and (column == 1 or column == 4 or column == 7):
        return 5
    elif (row == 1 or row == 4 or row == 7) and (column == 2 or column == 5 or column == 8):
        return 6
    elif (row == 2 or row == 5 or row == 8) and (column == 1 or column == 4 or column == 7):
        return 8
    elif (row == 2 or row == 5 or row == 8) and (column == 2 or column == 5 or column == 8):
        return 9

#This checks the value of the current board we're supposed to be on    
def currentBoard(row, column):
    if (column == 0 or column == 1 or column == 2) and (row == 0 or row == 1 or row == 2):
        return 1
    elif (column == 0 or column == 1 or column == 2) and (row == 3 or row == 4 or row == 5):
        return 4
    elif (column == 0 or column == 1 or column == 2) and (row == 6 or row == 7 or row == 8):
        return 7
    elif (column == 3 or column == 4 or column == 5) and (row == 0 or row == 1 or row == 2):
        return 2
    elif (column == 6 or column == 7 or column == 8) and (row == 0 or row == 1 or row == 2):
        return 3
    elif (column == 3 or column == 4 or column == 5) and (row == 3 or row == 4 or row == 5):
        return 5
    elif (column == 6 or column == 7 or column == 8) and (row == 3 or row == 4 or row == 5):
        return 6
    elif (column == 3 or column == 4 or column == 5) and (row == 6 or row == 7 or row == 8):
        return 8
    elif (column == 6 or column == 7 or column == 8) and (row == 6 or row == 7 or row == 8):
        return 9

#This function redraws the board based on our active board    
def makeBoard(row, column):
    if nextBoard(row, column) == 1:
        pygame.draw.line( screen, LINECOLOR, (0,80), (240,80), LINEWIDTH )
        pygame.draw.line( screen, LINECOLOR, (0,160), (240,160), LINEWIDTH )
        pygame.draw.line( screen, LINECOLOR, (80,0), (80,240), LINEWIDTH )
        pygame.draw.line( screen, LINECOLOR, (160,0), (160,240), LINEWIDTH )
        pygame.draw.line( screen, MAINLINECOLOR, (0,240), (240,240), MAINLINEWIDTH )
        pygame.draw.line( screen, MAINLINECOLOR, (240,0), (240,240), MAINLINEWIDTH )
        return 1
    if nextBoard(row, column) == 2:
        pygame.draw.line( screen, LINECOLOR, (240,80), (480,80), LINEWIDTH )
        pygame.draw.line( screen, LINECOLOR, (240,160), (480,160), LINEWIDTH )
        pygame.draw.line( screen, LINECOLOR, (320,0), (320,240), LINEWIDTH )
        pygame.draw.line( screen, LINECOLOR, (400,0), (400,240), LINEWIDTH )
        pygame.draw.line( screen, MAINLINECOLOR, (240,240), (480,240), MAINLINEWIDTH )
        pygame.draw.line( screen, MAINLINECOLOR, (240,0), (240,240), MAINLINEWIDTH )
        pygame.draw.line( screen, MAINLINECOLOR, (480,0), (480,240), MAINLINEWIDTH )
    elif nextBoard(row, column) == 3:
        pygame.draw.line( screen, LINECOLOR, (480,80), (720,80), LINEWIDTH )
        pygame.draw.line( screen, LINECOLOR, (480,160), (720,160), LINEWIDTH )
        pygame.draw.line( screen, LINECOLOR, (560,0), (560,240), LINEWIDTH )
        pygame.draw.line( screen, LINECOLOR, (640,0), (640,240), LINEWIDTH )
        pygame.draw.line( screen, MAINLINECOLOR, (480,240), (720,240), MAINLINEWIDTH )
        pygame.draw.line( screen, MAINLINECOLOR, (480,0), (480,240), MAINLINEWIDTH )
        pygame.draw.line( screen, MAINLINECOLOR, (720,0), (720,240), MAINLINEWIDTH )
        return 3
    elif nextBoard(row, column) == 4:
        pygame.draw.line( screen, LINECOLOR, (0,320), (240,320), LINEWIDTH )
        pygame.draw.line( screen, LINECOLOR, (0,400), (240,400), LINEWIDTH )
        pygame.draw.line( screen, LINECOLOR, (80,240), (80,480), LINEWIDTH )
        pygame.draw.line( screen, LINECOLOR, (160,240), (160,480), LINEWIDTH )
        pygame.draw.line( screen, MAINLINECOLOR, (0,480), (240,480), MAINLINEWIDTH )
        pygame.draw.line( screen, MAINLINECOLOR, (240,240), (240,480), MAINLINEWIDTH )
        pygame.draw.line( screen, MAINLINECOLOR, (0,240), (240,240), MAINLINEWIDTH )
        return 4
    elif nextBoard(row, column) == 5:
        pygame.draw.line( screen, LINECOLOR, (240,320), (480,320), LINEWIDTH )
        pygame.draw.line( screen, LINECOLOR, (240,400), (480,400), LINEWIDTH )
        pygame.draw.line( screen, LINECOLOR, (320,240), (320,480), LINEWIDTH )
        pygame.draw.line( screen, LINECOLOR, (400,240), (400,480), LINEWIDTH )
        pygame.draw.line( screen, MAINLINECOLOR, (240,480), (480,480), MAINLINEWIDTH )
        pygame.draw.line( screen, MAINLINECOLOR, (240,240), (240,480), MAINLINEWIDTH )
        pygame.draw.line( screen, MAINLINECOLOR, (480,240), (480,480), MAINLINEWIDTH )
        pygame.draw.line( screen, MAINLINECOLOR, (240,240), (480,240), MAINLINEWIDTH )
        return 5
    elif nextBoard(row, column) == 6:
        pygame.draw.line( screen, LINECOLOR, (480,320), (720,320), LINEWIDTH )
        pygame.draw.line( screen, LINECOLOR, (480,400), (720,400), LINEWIDTH )
        pygame.draw.line( screen, LINECOLOR, (560,240), (560,480), LINEWIDTH )
        pygame.draw.line( screen, LINECOLOR, (640,240), (640,480), LINEWIDTH )
        pygame.draw.line( screen, MAINLINECOLOR, (480,480), (720,480), MAINLINEWIDTH )
        pygame.draw.line( screen, MAINLINECOLOR, (480,240), (480,480), MAINLINEWIDTH )
        pygame.draw.line( screen, MAINLINECOLOR, (720,240), (720,480), MAINLINEWIDTH )
        pygame.draw.line( screen, MAINLINECOLOR, (480,240), (720,240), MAINLINEWIDTH )
        return 6
    elif nextBoard(row, column) == 7:
        pygame.draw.line( screen, LINECOLOR, (0,560), (240,560), LINEWIDTH )
        pygame.draw.line( screen, LINECOLOR, (0,640), (240,640), LINEWIDTH )
        pygame.draw.line( screen, LINECOLOR, (80,480), (80,720), LINEWIDTH )
        pygame.draw.line( screen, LINECOLOR, (160,480), (160,720), LINEWIDTH )
        pygame.draw.line( screen, MAINLINECOLOR, (0,720), (240,720), MAINLINEWIDTH )
        pygame.draw.line( screen, MAINLINECOLOR, (240,480), (240,720), MAINLINEWIDTH )
        pygame.draw.line( screen, MAINLINECOLOR, (0,480), (240,480), MAINLINEWIDTH )
        return 7
    elif nextBoard(row, column) == 8:
        pygame.draw.line( screen, LINECOLOR, (240,560), (480,560), LINEWIDTH )
        pygame.draw.line( screen, LINECOLOR, (240,640), (480,640), LINEWIDTH )
        pygame.draw.line( screen, LINECOLOR, (320,480), (320,720), LINEWIDTH )
        pygame.draw.line( screen, LINECOLOR, (400,480), (400,720), LINEWIDTH )
        pygame.draw.line( screen, MAINLINECOLOR, (240,720), (480,720), MAINLINEWIDTH )
        pygame.draw.line( screen, MAINLINECOLOR, (240,480), (240,720), MAINLINEWIDTH )
        pygame.draw.line( screen, MAINLINECOLOR, (480,480), (480,720), MAINLINEWIDTH )
        pygame.draw.line( screen, MAINLINECOLOR, (240,480), (480,480), MAINLINEWIDTH )
        return 8
    elif nextBoard(row, column) == 9:
        pygame.draw.line( screen, LINECOLOR, (480,560), (720,560), LINEWIDTH )
        pygame.draw.line( screen, LINECOLOR, (480,640), (720,640), LINEWIDTH )
        pygame.draw.line( screen, LINECOLOR, (560,480), (560,720), LINEWIDTH )
        pygame.draw.line( screen, LINECOLOR, (640,480), (640,720), LINEWIDTH )
        pygame.draw.line( screen, MAINLINECOLOR, (480,720), (720,720), MAINLINEWIDTH )
        pygame.draw.line( screen, MAINLINECOLOR, (480,480), (480,720), MAINLINEWIDTH )
        pygame.draw.line( screen, MAINLINECOLOR, (480,480), (720,480), MAINLINEWIDTH )
        return 9


def availableBoard(row, column, temp):
    if board[row][column] == 0:
        return 0
    elif temp != boardDraw(row, column):
        return 0
    else:
        return 1

#This is a bool setup for when I was messing around with dicts, ignore for now
def squareBool(row, column):
    pass

#Refills the screen with out correct colors (so our transparent overlay doesn't keep adding to itself and getting darker)
#If Once you click a square, it'll go to the next board number    
def boardDraw(row, column):
    screen.fill(BGCOLOR)
    drawLines()
    drawFigures()

    for boardNum in range(1, 10):
        if nextBoard(row, column) == boardNum:
            screen.blit(overlay_surface, (0, 0))
            makeBoard(row, column) #Redraws our active square
            return nextBoard(row, column) #Returns the board we're supposed to be on
