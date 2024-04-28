import pygame, sys
from button import Button
import subprocess
""" from pygame import mixer """
from menu import *

""" # Starting the mixer 
mixer.init()  """
  
""" # Loading the song 
mixer.music.load("assets/theme.mp3")  """
  
""" # Setting the volume 
mixer.music.set_volume(0.2)  """
  
""" # Start playing the song 
mixer.music.play()  """

pygame.init()

SCREEN = pygame.display.set_mode((720, 720))
pygame.display.set_caption("Game Over")

BG = pygame.image.load("assets/Background.png")

# color variables
black = (0, 0, 0)
white = (255, 255, 255)
col_spd = 1

col_dir_breathe = [1, 1, 1]
col_dir_breathe = [1, -1, -1]
def_col_breathe = [221, 218, 191]
def_col_breathe = [100,0,100]

minimum = 0
maximum = 255

hovering_color="Red"


playerWinner = 1

def winner( playerWinner ):
    if playerWinner == 1:
        draw_text("Player 1 is the winner!", 30, def_col_breathe, 360, 260)
    else:
        draw_text("Player 2 is the winner!", 30, def_col_breathe, 360, 260)
        

def reset_button():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        RESET_TEXT = get_font(20).render("The game has been reset", True, "Black")
        RESET_RECT = RESET_TEXT.get_rect(center=(360, 100))
        SCREEN.blit(RESET_TEXT, RESET_RECT)

        OPTIONS_BACK = Button(image=None, pos=(360, 230), 
                            text_input="BACK", font=get_font(30), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    reset_menu()

        pygame.display.update()

def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

def col_change_breathe(color: list, direction: list) -> None:

    for i in range(3):
        color[i] += col_spd * direction[i]
        if color[i] >= maximum or color[i] <= minimum:
            direction[i] *= -1
        if color[i] >= maximum:
            color[i] = maximum
        elif color[i] <= minimum:
            color[i] = minimum


def draw_text(text: str, size: int, col: list, x: int, y: int) -> None:

    font_object = pygame.font.Font("assets/font.ttf", size)
    text_surface = font_object.render(text, False, col)
    text_rect = text_surface.get_rect(center=(x, y))
    SCREEN.blit(text_surface, text_rect)


def reset_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(360, 400), 
                            text_input="Main Menu", font=get_font(30), base_color=( 221, 218, 191 ), hovering_color="Green")
        RESET_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(360, 550), 
                            text_input="Reset Game", font=get_font(30), base_color=( 221, 218, 191 ), hovering_color="Red")

        for button in [RESET_BUTTON, MENU_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if MENU_BUTTON.checkForInput(MENU_MOUSE_POS):
                    subprocess.run(["python", "menu.py"])
                    pygame.quit()
                if RESET_BUTTON.checkForInput(MENU_MOUSE_POS):
                    reset_button()

        # color update
        col_change_breathe(def_col_breathe, col_dir_breathe)
        col_change_breathe(def_col_breathe, col_dir_breathe)

        # text displaying
        draw_text("Game Over", 70, def_col_breathe, 360, 140)
        winner(2)
    
        pygame.display.update()

reset_menu()