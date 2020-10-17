"""Main code for Tokaido Nakama"""
import pygame
from tkinter import *
from tkinter import messagebox
# import sys
# import time
# from pygame.locals import *


# Pygame Module Initialization
pygame.init()

# Screen Creation
# Stretch goal of resizing display
display_width = 900
display_height = 800
screen = pygame.display.set_mode((display_width, display_height))

# Colors defined
black = (0, 0, 0)
white = (255, 255, 255)
green = (73, 114, 16)
blue = (122, 165, 184)
yelloworange = (243, 175, 1)
grey = (145, 147, 156)
purple = (98, 55, 114)
 
# Title and Icon
pygame.display.set_caption("Tokaido Nakama")
icon = pygame.image.load('cherrytreeicon.png')
pygame.display.set_icon(icon)

# Clock, if we want a timer
# clock = pygame.time.Clock()

# Board images
board_one = pygame.image.load('board_one.png')
# board_two = pygame.image.load('/images/board_two.png')
# board_three = pygame.image.load('/images/board_three.png')
# board_four = pygame.image.load('/images/board_four.png')

# Piece images
# player_green = ('player_green.png')
# player_blue = ('player_blue.png')
# player_grey = ('player_grey.png')
# player_yellow = ('player_yellow.png')
# player_purple = ('player_purple.png')

# Coordinates for board
x_board_coord = (display_width * 0.02)
y_board_coord = (display_height * 0.062)

# Function for board, will check for which board to load
def board(x_board, y_board):
    """Sets up board & switches board as needed"""

    # if check on which board to load, depending on game progress
    # if all players at space 14 && food has been chosen, board 2
    # section for generating landing spots based off board
    # Blit board, while scaling it to uniform size
    current_board = pygame.transform.scale(board_one, (850, 500))
    # board_spaces(1)
    screen.blit(current_board, (x_board, y_board))

def encounter_selection(board_position):
    """Generates drop down menu / contextual menu based off encounter chosen."""
    Tk().wm_withdraw() # to hide main window?
    messagebox.showinfo('Continue', )


# def player_info(playercount, list of colors):
# Generates player's info displays, depending on number of players & assigns colors

# def board_spaces(board_number):
#     """Generates spaces for pieces to land, depending on board #"""
#    if board_number == 1:
    # rects for board positions

# Font Section
# Create title font, first param is font file in pygame, second is size
font_title = pygame.font.Font('freesansbold.ttf', 50)
# Create a text surface object, on which text is drawn on.
text_title = font_title.render('Color\'s Turn', True, black)
# Create a rectangular object for the text surface object
text_title_rect = text_title.get_rect()
# Set the center of the rectangular object
text_title_rect.center = (display_width / 2, display_height * .03)

# def start_screen():
#
#   intro = True
#   while intro:
#        for event in pygame.event.get():
#            print(event)
#            if event.type == pygame.QUIT:
#                pygame.quit()
#                quit()
# parameters selected here will be passed to main_screen


# Main Game Loop
def main_screen():
    """Main game loop"""
    running = True
    rect1 = pygame.Rect(155, 150, 21, 122)
    rect11 = pygame.Rect(135, 87, 62, 82)
    rect5 = pygame.Rect(343, 87, 61, 190)
    while running:
        # Inner loop of events & logic based off that (mouse clicks, selections, etc)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # Left  mouse button.
                    # Check if the rect collides with the mouse pos.
                    if rect1.collidepoint(event.pos) or rect11.collidepoint(event.pos):
                        print('Area 1 clicked.')
                        encounter_selection(1)
                    if rect5.collidepoint(event.pos):
                        print('Area 5 clicked.')
                        encounter_selection(5)
            #

            # Shows list of events on ya terminal. To be removed, but fun to see
            print(event)

        # Filling screen
        screen.fill(white)

        # Render title text & rect
        screen.blit(text_title, text_title_rect)

        # Call Board Function
        board(x_board_coord, y_board_coord)

        # Update display after event logic is complete in inner for loop
        pygame.display.update()

# Results Screen
# def results_screen():
#
#  stuff goes here
#
#  and here!
# 
#

# Run Sequence Below

# start_screen()
main_screen()
# results_screen()
pygame.quit()
quit()