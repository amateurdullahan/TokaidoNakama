import pygame
import sys
import time

pygame.init()

# Screen Creation
display_width = 800
display_height = 600
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
clock = pygame.time.Clock()

# Board images
board_one = pygame.image.load('board_one.png')
board_two = pygame.image.load('board_two.png')
board_three = pygame.image.load('board_three.png')
board_four = pygame.image.load('board_four.png')

# Piece images
player_green = 
player_blue = 
player_grey = 
player_yelloworange = 
player_purple = 

def board()



# def game_intro():
#
#    intro = True
#
#   while intro:
#        for event in pygame.event.get():
#            print(event)
#            if event.type == pygame.QUIT:
#                pygame.quit()
#                quit()



# Game Loop
running = True
while running:
    # Creates list of events per frame, per second
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Shows list of events
        print(event)

    # RGB - Red, Green, Blue
    screen.fill((255, 255, 255))
    pygame.display.update()
pygame.quit()
quit()