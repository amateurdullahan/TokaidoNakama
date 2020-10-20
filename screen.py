#!/usr/bin/python3
"""Main code for Tokaido Nakama"""
import pygame
import pygame_menu
from player import Player
from init import HSDeck, player_list
from location import Hot_Spring_Loc
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
icon = pygame.image.load('media/cherrytreeicon.png')
pygame.display.set_icon(icon)

# Clock, if we want a timer
# clock = pygame.time.Clock()

# Board images
board_one = pygame.image.load('media/board_one.png')
board_two = pygame.image.load('media/board_two.png')
board_three = pygame.image.load('media/board_three.png')
board_four = pygame.image.load('media/board_four.png')

# Coordinates for board
X_BOARD_COORD = (DISPLAY_WIDTH * 0.02)
Y_BOARD_COORD = (DISPLAY_HEIGHT * 0.062)

# Function for board, will check for which board to load
def board(x_board, y_board, current_board):
    """Sets up board & switches board as needed"""

    # if check on which board to load, depending on game progress
    # if all players at space 14 && food has been chosen, board 2
    # section for generating landing spots based off board
    # Blit board, while scaling it to uniform size
    if current_board == 1:
        current_board = pygame.transform.scale(board_one, (850, 500))
    if current_board == 2:
        current_board = pygame.transform.scale(board_two, (850, 500))
    if current_board == 3:
        current_board = pygame.transform.scale(board_three, (850, 500))
    if current_board == 4:
        current_board = pygame.transform.scale(board_four, (850, 500))
    screen.blit(current_board, (x_board, y_board))

def encounter_selection(board_position):
    """Generates drop down menu / contextual menu based off encounter chosen."""

    if board_position in [1, 8, 25, 29, 45, 45, 53]:
        # Code for Villages Menu & updating stuff
        print("Village stuff")
    elif board_position in [2, 9, 16, 21, 36, 43]:
        # Code for Temples Menu & updating stuff
        print("Temple stuff")
    elif board_position in [3, 10, 20, 30, 38, 44, 49]:
        # Code for Encounter Menu & updating stuff
        print("Encounter stuff")
    elif board_position in [4, 18, 28, 35, 51]:
        # Code for Pano_Paddy
        print("Pano paddy stuff")
    elif board_position in [5, 13, 22, 33, 42, 48]:
        # Code for Hot Springs
        hot_spring_popup.mainloop(screen)
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
def player_add(player_color):   # button fun
    """Adds player color to game"""
    if len(player_list) < 3:
        if player_color == 'Green' and 'player_green' not in player_list:
            player_green = Player(player_color)
            player_list.append(player_green)
            print(player_green)
            player_green.icon = pygame.image.load('media/player_green.png')
            # pygame.transform.scale(player_green.icon, (34, 60))
            green_button.set_position(1000, 1000)
            # Hides it off the surface. Could just change color like below:
            # green_button.set_background_color((73, 114, 16))
            if len(player_list) == 3:
                print(player_list)
                print('GO RIGHT INTO MAIN')
                start_menu.disable()
                main_screen(1)
        elif player_color == 'Blue' and 'player_blue' not in player_list:
            player_blue = Player(player_color)
            player_list.append(player_blue)
            print(player_blue)
            player_blue.icon = pygame.image.load('media/player_blue.png')
            # pygame.transform.scale(player_blue.icon, (34, 60))
            blue_button.set_position(1000, 1000)
            if len(player_list) == 3:
                print(player_list)
                print('GO RIGHT INTO MAIN')
                start_menu.disable()
                main_screen(1)
        elif player_color == 'Grey' and 'player_grey' not in player_list:
            player_grey = Player(player_color)
            player_list.append(player_grey)
            print(player_grey)
            player_grey.icon = pygame.image.load('media/player_grey.png')
            # pygame.transform.scale(player_grey.icon, (34, 60))
            grey_button.set_position(1000, 1000)
            if len(player_list) == 3:
                print(player_list)
                print('GO RIGHT INTO MAIN')
                start_menu.disable()
                main_screen(1)
        elif player_color == 'Yellow' and 'player_yellow' not in player_list:
            player_yellow = Player(player_color)
            player_list.append(player_yellow)
            print(player_yellow)
            player_yellow.icon = pygame.image.load('media/player_yellow.png')
            # pygame.transform.scale(player_yellow.icon, (34, 60))
            yellow_button.set_position(1000, 1000)
            if len(player_list) == 3:
                print(player_list)
                print('GO RIGHT INTO MAIN')
                start_menu.disable()
                main_screen(1)
        elif player_color == 'Purple' and 'player_purple' not in player_list:
            player_purple = Player(player_color)
            player_list.append(player_purple)
            print(player_purple)
            player_purple.icon = pygame.image.load('media/player_purple.png')
            # pygame.transform.scale(player_purple.icon, (34, 60))
            purple_button.set_position(1000, 1000)
            if len(player_list) == 3:
                print(player_list)
                print('GO RIGHT INTO MAIN')
                start_menu.disable()
                main_screen(1)
    else:
        print(player_list)
        print('THIS CODE SHOULD NOT RUN ONCE EVERYTHING IS GOING')

# Function for clean quit
def quitter():
    """quits pygame and python"""
    pygame.quit()
    quit()

# Start Menu & Buttons
start_menu = pygame_menu.Menu(height=400, width=420, theme=pygame_menu.themes.THEME_DEFAULT,
                              title='Select 3 Players', onclose=quitter)
start_menu.add_label('In Starting Order:')
green_button = start_menu.add_button('Green', player_add, 'Green')
blue_button = start_menu.add_button('Blue', player_add, 'Blue')
grey_button = start_menu.add_button('Grey', player_add, 'Grey')
yellow_button = start_menu.add_button('Yellow', player_add, 'Yellow')
purple_button = start_menu.add_button('Purple', player_add, 'Purple')
#Hot Spring popup menu
# hot_spring_popup = pygame_menu.Menu(height=300, width=400, theme=pygame_menu.themes.THEME_DEFAULT,
# title='Hot Spring', onclose=pygame_menu.events.BACK)
# hot_spring_popup.add_label('Select Point Value')
# hot_spring_popup.add_button('2 Points', Hot_Spring_Loc, 2)


def player_positioning():
    """Checks player positions & blits pieces"""
    for player in player_list:
        if player.board_space == 0.1:
            screen.blit(player.icon, (80, 283))
        if player.board_space == 0.2:
            screen.blit(player.icon, (80, 336))
        if player.board_space == 0.3:
            screen.blit(player.icon, (80, 385))
        if player.board_space == 1:
            screen.blit(player.icon, (149, 215))
    # for cleanup, maybe make dictionary with board_space(key) and associated coords(value)


# Main Game Loop
def main_screen(board_number):
    """Main game loop"""
    # Board One
    if board_number == 1:
        # Rect(left, top, width, height)
        rect1 = pygame.Rect(155, 150, 21, 122)
        # rect 11 is additional rect for position 1
        rect11 = pygame.Rect(135, 87, 62, 82)
        # rect2 = pygame.Rect(, , , ,)
        # rect3 = pygame.Rect(, , , ,)
        # rect4 = pygame.Rect(, , , ,)
        rect5 = pygame.Rect(343, 87, 61, 190)
        # rect6 = pygame.Rect(, , , ,)
        # rect7 = pygame.Rect(, , , ,)
        # rect8 = pygame.Rect(, , , ,)
        # rect9 = pygame.Rect(, , , ,)
        # rect10 = pygame.Rect(, , , ,)
        # rect11 = pygame.Rect(, , , ,)
        # rect12 = pygame.Rect(, , , ,)
        # rect13 = pygame.Rect(, , , ,)
        # rect14 = pygame.Rect(, , , ,)
        # 1400 is 14.01
        # rect1401 = pygame.Rect(, , , ,)
        # rect1402 = pygame.Rect(, , , ,)
        # rect1403 = pygame.Rect(, , , ,)
        # Starting inn rect
        start_list = [0.1, 0.2, 0.3]
        for player, position in zip(player_list, start_list):
            player.board_space = position
            print(player.board_space)
    # if board_number == 2:

    # if board_number == 3:

    # if board_number == 4:


    running = True  # Main Loop Flag
    while running:
        # Inner Loop for Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   # If The Window's 'X' Button is Clicked
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # Left  mouse button.
                    # Check if the rect collides with the mouse pos.
                    if rect1.collidepoint(event.pos) or rect11.collidepoint(event.pos):
                        print('Village selected.')
                        # encounter_selection(1)
                    if rect5.collidepoint(event.pos):
                        print('Hot Springs selected.')
                        encounter_selection(5)
                  # if rect for inn collision:
                        # append to player list (which will be cleared as player pieces are set)
                        # if all players on inn:
                        # food menu. Within food menu,
                        # determine board to load based off player pos # (which inn)

            # Shows list of events on ya terminal. To be removed, but fun to see
            print(event)

        # Filling screen
        screen.fill(white)

        # Render title text & rect
        screen.blit(text_title, text_title_rect)

        # Call Board Function
        board(X_BOARD_COORD, Y_BOARD_COORD, board_number)

        # Piece Space Function
        player_positioning()

        # Update display after event logic is complete in inner for loop
        pygame.display.update()

        # If All Players At Inn
        # Call Food Menu
        # Then From Food Menu Call main_screen(NEXT BOARD NUMBER)

# Results Screen
# def results_screen():
#
#  stuff goes here
#
#  and here!
#
#

# Run Sequence Below
start_menu.mainloop(screen)
# main_screen(1)
# results screen()
quitter()
