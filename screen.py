"""Main code for Tokaido Nakama"""
import pygame
import pygame_menu
from player import Player
# import sys
# import time
# from pygame.locals import *


# Pygame Module Initialization
pygame.init()

# Screen Creation
# Stretch goal of resizing display
DISPLAY_WIDTH = 900
DISPLAY_HEIGHT = 800
screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

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
X_BOARD_COORD = (DISPLAY_WIDTH * 0.02)
Y_BOARD_COORD = (DISPLAY_HEIGHT * 0.062)

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

    if board_position in [1, 8, 25, 29, 45, 45, 53]:
        # Code for Villages
        print("Village stuff")
    elif board_position in [2, 9, 16, 21, 36, 43]:
        # Code for Temples
        print("Temple stuff")
    elif board_position in [3, 10, 20, 30, 38, 44, 49]:
        # Code for Encounter
        print("Encounter stuff")
    elif board_position in [4, 18, 28, 35, 51]:
        # Code for Pano_Paddy
        print("Pano paddy stuff")
    elif board_position in [5, 13, 22, 33, 42, 48]:
        # Code for Hot Springs
        print("Hot spring stuff")
    elif board_position in [6, 12, 19, 23, 32, 50]:
        # Code for Pano_Mt
        print("Pano mt stuff")
    elif board_position in [7, 17, 26, 31, 37, 47]:
        # Code for Farm
        print("Farm stuff")
    elif board_position in [11, 15, 24, 34, 39, 46, 52]:
        # Code for Pano_Sea
        print("Pano sea stuff")
    elif board_position in [14, 27, 41, 54]:
        # Code for Inn
        print("Inn stuff")





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
text_title_rect.center = (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT * .03)

# Setup

# Creates list in order of players, at limit goes into main screen
player_list = []    # makes empty list
def player_add(player_color):   # button fun
    """Adds player color to game"""
    if len(player_list) < 3:
        if player_color == 'Green' and 'Green' not in player_list:
            player_green = Player(player_color)
            player_list.append(player_color)
            print(player_green)
            green_button.set_position(1000, 1000)
            # Hides it off the surface. Could just change color like below:
            # green_button.set_background_color((73, 114, 16))
            if len(player_list) == 3:
                print(player_list)
                print('GO RIGHT INTO MAIN')
        elif player_color == 'Blue' and 'Blue' not in player_list:
            player_blue = Player(player_color)
            player_list.append(player_color)
            print(player_blue)
            blue_button.set_position(1000, 1000)
            if len(player_list) == 3:
                print(player_list)
                print('GO RIGHT INTO MAIN')
        elif player_color == 'Grey' and 'Grey' not in player_list:
            player_grey = Player(player_color)
            player_list.append(player_color)
            print(player_grey)
            grey_button.set_position(1000, 1000)
            if len(player_list) == 3:
                print(player_list)
                print('GO RIGHT INTO MAIN')
        elif player_color == 'Yellow' and 'Yellow' not in player_list:
            player_yellow = Player(player_color)
            player_list.append(player_color)
            print(player_yellow)
            yellow_button.set_position(1000, 1000)
            if len(player_list) == 3:
                print(player_list)
                print('GO RIGHT INTO MAIN')
        elif player_color == 'Purple' and 'Purple' not in player_list:
            player_purple = Player(player_color)
            player_list.append(player_color)
            print(player_purple)
            purple_button.set_position(1000, 1000)
            if len(player_list) == 3:
                print(player_list)
                print('GO RIGHT INTO MAIN')
    else:
        print(player_list)
        print('THIS CODE SHOULD NOT RUN ONCE EVERYTHING IS GOING')

# Function for clean quit
def quitter():
    """quits pygame and python"""
    pygame.quit()
    quit()

# Start Menu & Buttons
start_menu = pygame_menu.Menu(height=400, width=420, theme=pygame_menu.themes.THEME_GREEN,
                              title='Select 3 Players', onclose=quitter)
start_menu.add_label('In Starting Order:')
green_button = start_menu.add_button('Green', player_add, 'Green')
blue_button = start_menu.add_button('Blue', player_add, 'Blue')
grey_button = start_menu.add_button('Grey', player_add, 'Grey')
yellow_button = start_menu.add_button('Yellow', player_add, 'Yellow')
purple_button = start_menu.add_button('Purple', player_add, 'Purple')


# Main Game Loop
def main_screen():
    """Main game loop"""

    running = True
    rect1 = pygame.Rect(155, 150, 21, 122)
    rect11 = pygame.Rect(135, 87, 62, 82)
    rect5 = pygame.Rect(343, 87, 61, 190)
    # rect00 = pygame.Rect()
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
                        # encounter_selection(1)
                    if rect5.collidepoint(event.pos):
                        print('Area 5 clicked.')
                        # encounter_selection(5)

            # Shows list of events on ya terminal. To be removed, but fun to see
            print(event)

        # Filling screen
        screen.fill(white)

        # Render title text & rect
        screen.blit(text_title, text_title_rect)

        # Call Board Function
        board(X_BOARD_COORD, Y_BOARD_COORD)

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

screen.fill(white)
screen.blit(text_title, text_title_rect)
board(X_BOARD_COORD, Y_BOARD_COORD)
start_menu.mainloop(screen)
# results_screen()
quitter()
