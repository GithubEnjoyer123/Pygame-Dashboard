import pygame, sys
import numpy as np
import math
import sys
from DrawVeritcalLines import * 
from DrawDescendingLines import *
from DrawHorizontalLines import *
from DrawAscendingLines import *
from boardCheck import *

def restart():
    pass

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

            #Will update the logic here when board win overlay is finished
            '''if isBoardFull(clickedRow, clickedColumn):
            nextPass = 0'''
                
            #Since nextpass is set to 0 we skip our first iteration. Then we check to see if the player clicked on the proper board. 
            #If our values are mismatched we redo and get our next click coordinates
            if nextPass != 0:
                if currentBoard(clickedRow, clickedColumn) != nextPass:
                    continue

            #if player one goes set to player 2, if player to goes set to player 1. It's changing turns.
            if avaliableSquare(clickedRow, clickedColumn):
                if player == 1:
                    markSquare( clickedRow, clickedColumn, 1)
                    boardDraw(clickedRow, clickedColumn)
                    checkWIn( player ) 
                    player = 2
                    nextPass = nextBoard(clickedRow, clickedColumn) #Set our next pass through loop to what board we're supposed to be on next
                        
                elif player == 2:
                    markSquare( clickedRow, clickedColumn, 2)
                    boardDraw(clickedRow, clickedColumn)
                    checkWIn( player )
                    player = 1
                    nextPass = nextBoard(clickedRow, clickedColumn)
                            
    pygame.display.update()
    pygame.display.flip()
   
pygame.quit()
sys.exit()