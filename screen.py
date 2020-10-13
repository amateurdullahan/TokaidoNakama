import pygame
import sys
import time
from pygame.locals import *

pygame.init()

# Screen Creation
display_width = 1024
display_height = 900
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
board_one = pygame.image.load('board_one_rough_cutout.png')
# board_two = pygame.image.load('board_two.png')
# board_three = pygame.image.load('board_three.png')
# board_four = pygame.image.load('board_four.png')

# Piece images
# player_green = 
# player_blue = 
# player_grey = 
# player_yelloworange = 
# player_purple = 

def board(x, y):
    # if check on which board to load, depending on game progress
    screen.blit(pygame.transform.scale(board_one, (550, 450)), (x, y))

x = (display_width * 0.22)
y = (display_height * 0.2)

# def start_screen():
#
#   intro = True
#   while intro:
#        for event in pygame.event.get():
#            print(event)
#            if event.type == pygame.QUIT:
#                pygame.quit()
#                quit()
# start


# Game Loop
def main_screen():
    running = True
    while running:
        # Creates list of events per frame, per second
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Shows list of events on ya terminal. To be removed, but fun to see
            print(event)

        # RGB - Red, Green, Blue
        screen.fill(white)
        board(x, y)
        pygame.display.update()

# Results Screen
# def results_screen():
#
#  stuff goes here
#
#  and here!
#
#

# start_screen()
main_screen()
# results_screen()
pygame.quit()
quit()