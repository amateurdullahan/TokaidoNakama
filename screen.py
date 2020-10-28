#!/usr/bin/python3
"""Main code for Tokaido Nakama"""
import pygame
import pygame_menu
from player import Player
from init import current_player, HSDeck, MDeck, SVDeck, ENCDeck, player_list, GreenPlayer, BluePlayer, YellowPlayer, PurplePlayer, GreyPlayer, board_1_list, board_2_list, board_3_list
from location import *
from buttons import Button
from deck import Deck

# import sys
# import time
# from pygame.locals import *

if __name__ == '__main__':
    # Declaring global variables
    global screen

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
    gold = (210, 132, 47)

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

        if board_position in [1, 8, 29, 37, 48, 57, 65]:
            # Code for Villages Menu & updating stuff
            print("Village stuff")
            village_menu(screen)
            update_current_player()
        elif board_position in [2, 9, 20, 25, 44, 55]:
            # Code for Temples Menu & updating stuff
            print("Temple stuff")
            temple_menu(screen)
            update_current_player()
        elif board_position in [3, 10, 24, 38, 46, 56, 61]:
            # Code for Encounter Menu & updating stuff
            print("Encounter stuff")
            encounter_menu(screen)
            update_current_player()
        elif board_position in [4, 22, 36, 43, 63]:
            # Code for Pano_Paddy
            print("Pano paddy stuff")
            pano_paddy_menu(screen)
            update_current_player()
        elif board_position in [5, 13, 26, 41, 54, 60]:
            # Code for Hot Springs
            print("Hot spring stuff")
            hot_springs_menu(screen)
            update_current_player()
        elif board_position in [6, 12, 23, 27, 40, 62]:
            # Code for Pano_Mt
            print("Pano mt stuff")
            pano_mt_menu(screen)
            update_current_player()
        elif board_position in [7, 21, 30, 39, 45, 59]:
            # Code for Farm
            print("Farm stuff")
            farm_menu(screen)
            update_current_player()
        elif board_position in [11, 19, 28, 42, 47, 58, 64]:
            # Code for Pano_Sea
            print("Pano sea stuff")
            pano_sea_menu(screen)
            update_current_player()
        elif board_position in [14, 15, 16, 17, 18, 31, 32, 33, 34, 35, 49, 50, 51, 52, 53, 66,
                                67, 68, 69, 70]:
            # Code for Inn
            print("Inn stuff")
            inn_menu(screen)
            update_current_player

    # def player_info(playercount, list of colors):
    # Generates player's info displays, depending on number of players & assigns colors

    # update current player
    def update_current_player():
        global current_player
        for player in player_list:
            if player.board_space < current_player.board_space:
                current_player = player
        print("Current Player: {}", current_player.color)

    # Player Colors & Associated RGB values
    colors_rgb = {
        "Green": (73, 114, 16), "Blue": (122, 165, 184), "Yellow": (243, 175, 1),
        "Grey": (145, 147, 156), "Purple": (98, 55, 114)}

    # Font Section
    def title_selector(current_player):
        """Changes title for current player"""

        # Retrieve current player's RGB value
        rgb = colors_rgb.get(current_player.color)
        # for key in colors_rgb:
            # if key == current_player.color:
                # rgb = colors_rgb.get(key)
        # Create title font, first param is font file in pygame, second is size
        font_title = pygame.font.SysFont('Arial', 50)
        # Create a string from current player's color
        text_current_player = current_player.color + '\'s Turn'
        # Create a text surface object, on which text is drawn on.
        text_title = font_title.render(text_current_player, True, rgb)
        # Create a rectangular object for the text surface object
        text_title_rect = text_title.get_rect()
        # Set the center of the rectangular object
        text_title_rect.center = (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT * .03)
        screen.blit(text_title, text_title_rect)

    def score_prob_display():
        """bunch of buttons to display score and Probability"""
        from probability import CostProb, PointProb, EncTypeProb, SubTypeProb
        # Builds Meal Cost Display
        btn_mcp_title = Button(0, 585, 50, 25, screen, black)
        btn_mcp_title.add_text("Meal Cost", 18)
        btn_mcp_1 = Button(0, 610, 50, 20, screen, black)
        mcp_text = CostProb(MDeck)
        btn_mcp_1.add_text("1 Coin " + str(mcp_text[0]) + "%", 16)
        btn_mcp_2 = Button(0, 630, 50, 20, screen, black)
        btn_mcp_2.add_text("2 Coin " + str(mcp_text[1]) + "%", 16)
        btn_mcp_3 = Button(0, 650, 50, 20, screen, black)
        btn_mcp_3.add_text("3 Coin " + str(mcp_text[2]) + "%", 16)
        # Hot Springs Point Display
        btn_hsp_title = Button(0, 675, 50, 25, screen, black)
        btn_hsp_title.add_text("Hot Springs Points", 18)
        btn_hsp_1 = Button(0, 700, 50, 20, screen, black)
        hsp_text = PointProb(HSDeck)
        btn_hsp_1.add_text("2 Points " + str(hsp_text[0]) + "%", 16)
        btn_hsp_2 = Button(0, 720, 50, 20, screen, black)
        btn_hsp_2.add_text("3 Points " + str(hsp_text[1]) + "%", 16)
        # Builds Souvenir Cost Display
        btn_svcp_title = Button(175, 585, 50, 25, screen, black)
        btn_svcp_title.add_text("Souvenir Cost", 18)
        btn_svcp_1 = Button(175, 610, 50, 20, screen, black)
        svcp_text = CostProb(SVDeck)
        btn_svcp_1.add_text("1 Coin " + str(svcp_text[0]) + "%", 16)
        btn_svcp_2 = Button(175, 630, 50, 20, screen, black)
        btn_svcp_2.add_text("2 Coin " + str(svcp_text[1]) + "%", 16)
        btn_svcp_3 = Button(175, 650, 50, 20, screen, black)
        btn_svcp_3.add_text("3 Coin " + str(svcp_text[2]) + "%", 16)
        # Builds Souvenir Subtype Display
        btn_svsp_title = Button(175, 675, 50, 25, screen, black)
        btn_svsp_title.add_text("Souvenir Type", 18)
        btn_svsp_1 = Button(175, 700, 50, 20, screen, black)
        svsp_text = SubTypeProb(SVDeck)
        btn_svsp_1.add_text("Small Item " + str(svsp_text[0]) + "%", 16)
        btn_svsp_2 = Button(175, 720, 50, 20, screen, black)
        btn_svsp_2.add_text("Food & Drink " + str(svsp_text[1]) + "%", 16)
        btn_svsp_3 = Button(175, 740, 50, 20, screen, black)
        btn_svsp_3.add_text("Clothing " + str(svsp_text[2]) + "%", 16)
        btn_svsp_4 = Button(175, 760, 50, 20, screen, black)
        btn_svsp_4.add_text("Art " + str(svsp_text[2]) + "%", 16)
        # Builds Encounter Type Display
        btn_entp_title = Button(350, 585, 50, 25, screen, black)
        btn_entp_title.add_text("Encounter Type", 18)
        btn_entp_1 = Button(350, 610, 50, 20, screen, black)
        entp_text = EncTypeProb(ENCDeck)
        btn_entp_1.add_text("Kuge " + str(entp_text[0]) + "%", 16)
        btn_entp_2 = Button(350, 630, 50, 20, screen, black)
        btn_entp_2.add_text("Miko " + str(entp_text[1]) + "%", 16)
        btn_entp_3 = Button(350, 650, 50, 20, screen, black)
        btn_entp_3.add_text("Samurai " + str(entp_text[2]) + "%", 16)
        btn_entp_4 = Button(350, 670, 50, 20, screen, black)
        btn_entp_4.add_text("Shokunin " + str(entp_text[3]) + "%", 16)
        btn_entp_5 = Button(350, 690, 50, 20, screen, black)
        btn_entp_5.add_text("Annaibito: Paddy " + str(entp_text[4]) + "%", 16)
        btn_entp_6 = Button(350, 710, 50, 20, screen, black)
        btn_entp_6.add_text("Annaibito: Mountain " + str(entp_text[5]) + "%", 16)
        btn_entp_7 = Button(350, 730, 50, 20, screen, black)
        btn_entp_7.add_text("Annaibito: Sea" + str(entp_text[6]) + "%", 16)
        # Retrieve current player's RGB value
        rgb = colors_rgb.get(current_player.color)
        # for key in colors_rgb:
            # if key == current_player.color:
                # rgb = colors_rgb.get(key)
        # Create title font, first param is font file in pygame, second is size
        font_title = pygame.font.SysFont('Arial', 50)
        # Create a string from current player's color
        text_current_player = current_player.color + '\'s Turn'
        # Create a text surface object, on which text is drawn on.
        text_title = font_title.render(text_current_player, True, rgb)
        # Create a rectangular object for the text surface object
        text_title_rect = text_title.get_rect()
        # Set the center of the rectangular object
        text_title_rect.center = (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT * .03)
        screen.blit(text_title, text_title_rect)
        # player 1 score display
        p1_title = pygame.font.SysFont('Arial', 30)
        p1_rgb = colors_rgb.get(player_list[0].color)
        p1_color = str(player_list[0].color)
        p1_text = p1_title.render(p1_color, True, p1_rgb)
        p1_text_rect = p1_text.get_rect()
        p1_text_rect.center = (DISPLAY_WIDTH * .745, DISPLAY_HEIGHT * .745)
        screen.blit(p1_text, p1_text_rect)
        p1_coin = pygame.image.load('media/coin_small.png')
        p1_coin_rect = p1_coin.get_rect()
        p1_coin_rect.center = (DISPLAY_WIDTH * .81, DISPLAY_HEIGHT * .787)
        screen.blit(p1_coin, p1_coin_rect)
        p1_coins_title = pygame.font.SysFont('Arial', 18)
        p1_coins = p1_coins_title.render(str(player_list[0].coins), True, gold)
        p1_coins_rect = p1_coins.get_rect()
        p1_coins_rect.center = (DISPLAY_WIDTH * .787, DISPLAY_HEIGHT * .785)
        screen.blit(p1_coins, p1_coins_rect)
        p1_score_title = pygame.font.SysFont('Arial', 30)
        p1_score = p1_score_title.render(str(player_list[0].score), True, p1_rgb)
        p1_score_rect = p1_score.get_rect()
        p1_score_rect.center = (DISPLAY_WIDTH * .719, DISPLAY_HEIGHT * .785)
        screen.blit(p1_score, p1_score_rect)
        p1_bird = pygame.image.load('media/points.png')
        p1_bird_rect = p1_bird.get_rect()
        p1_bird_rect.center = (DISPLAY_WIDTH * .75, DISPLAY_HEIGHT * .787)
        screen.blit(p1_bird, p1_bird_rect)
        # Player 2
        p2_title = pygame.font.SysFont('Arial', 30)
        p2_rgb = colors_rgb.get(player_list[1].color)
        p2_text = p2_title.render(player_list[1].color, True, p2_rgb)
        p2_text_rect = p2_text.get_rect()
        p2_text_rect.center = (DISPLAY_WIDTH * .91, DISPLAY_HEIGHT * .745)
        screen.blit(p2_text, p2_text_rect)
        p2_coin = pygame.image.load('media/coin_small.png')
        p2_coin_rect = p2_coin.get_rect()
        p2_coin_rect.center = (DISPLAY_WIDTH * .97, DISPLAY_HEIGHT * .787)
        screen.blit(p2_coin, p2_coin_rect)
        p2_coins_title = pygame.font.SysFont('Arial', 18)
        p2_coins = p2_coins_title.render(str(player_list[1].coins), True, gold)
        p2_coins_rect = p2_coins.get_rect()
        p2_coins_rect.center = (DISPLAY_WIDTH * .947, DISPLAY_HEIGHT * .785)
        screen.blit(p2_coins, p2_coins_rect)
        p2_score_title = pygame.font.SysFont('Arial', 30)
        p2_score = p2_score_title.render(str(player_list[1].score), True, p2_rgb)
        p2_score_rect = p2_score.get_rect()
        p2_score_rect.center = (DISPLAY_WIDTH * .879, DISPLAY_HEIGHT * .785)
        screen.blit(p2_score, p2_score_rect)
        p2_bird = pygame.image.load('media/points.png')
        p2_bird_rect = p2_bird.get_rect()
        p2_bird_rect.center = (DISPLAY_WIDTH * .91, DISPLAY_HEIGHT * .787)
        screen.blit(p2_bird, p2_bird_rect)
        # Player 3
        p3_title = pygame.font.SysFont('Arial', 30)
        p3_rgb = colors_rgb.get(player_list[2].color)
        p3_text = p3_title.render(player_list[2].color, True, p3_rgb)
        p3_text_rect = p3_text.get_rect()
        p3_text_rect.center = (DISPLAY_WIDTH * .745, DISPLAY_HEIGHT * .845)
        screen.blit(p3_text, p3_text_rect)
        p3_coin = pygame.image.load('media/coin_small.png')
        p3_coin_rect = p3_coin.get_rect()
        p3_coin_rect.center = (DISPLAY_WIDTH * .81, DISPLAY_HEIGHT * .885)
        screen.blit(p3_coin, p3_coin_rect)
        p3_coins_title = pygame.font.SysFont('Arial', 18)
        p3_coins = p3_coins_title.render(str(player_list[2].coins), True, gold)
        p3_coins_rect = p3_coins.get_rect()
        p3_coins_rect.center = (DISPLAY_WIDTH * .787, DISPLAY_HEIGHT * .884)
        screen.blit(p3_coins, p3_coins_rect)
        p3_score_title = pygame.font.SysFont('Arial', 30)
        p3_score = p3_score_title.render(str(player_list[2].score), True, p3_rgb)
        p3_score_rect = p3_score.get_rect()
        p3_score_rect.center = (DISPLAY_WIDTH * .719, DISPLAY_HEIGHT * .885)
        screen.blit(p3_score, p3_score_rect)
        p3_bird = pygame.image.load('media/points.png')
        p3_bird_rect = p3_bird.get_rect()
        p3_bird_rect.center = (DISPLAY_WIDTH * .75, DISPLAY_HEIGHT * .886)
        screen.blit(p3_bird, p3_bird_rect)

    # Creates list in order of players, at limit goes into main screen
    def player_add(player_color):
        """Adds player color to game"""
        global current_player
        if len(player_list) < 3:
            if player_color == 'Green' and 'player_green' not in player_list:
                player_green = GreenPlayer
                player_list.append(player_green)
                print(player_green)
                player_green.icon = pygame.image.load('media/player_green.png')
                # pygame.transform.scale(player_green.icon, (34, 60))
                green_button.set_position(1000, 1000)
                if len(player_list) == 3:
                    print(player_list)
                    # current_player = GreenPlayer
                    print('GO RIGHT INTO MAIN')
                    start_menu.disable()
                    main_screen(1)
            elif player_color == 'Blue' and 'player_blue' not in player_list:
                player_blue = BluePlayer
                player_list.append(player_blue)
                print(player_blue)
                player_blue.icon = pygame.image.load('media/player_blue.png')
                # pygame.transform.scale(player_blue.icon, (34, 60))
                blue_button.set_position(1000, 1000)
                if len(player_list) == 3:
                    print(player_list)
                    # current_player = BluePlayer
                    print('GO RIGHT INTO MAIN')
                    start_menu.disable()
                    main_screen(1)
            elif player_color == 'Grey' and 'player_grey' not in player_list:
                player_grey = GreyPlayer
                player_list.append(player_grey)
                print(player_grey)
                player_grey.icon = pygame.image.load('media/player_grey.png')
                # pygame.transform.scale(player_grey.icon, (34, 60))
                grey_button.set_position(1000, 1000)
                if len(player_list) == 3:
                    print(player_list)
                    # current_player = GreyPlayer
                    print('GO RIGHT INTO MAIN')
                    start_menu.disable()
                    main_screen(1)
            elif player_color == 'Yellow' and 'player_yellow' not in player_list:
                player_yellow = YellowPlayer
                player_list.append(player_yellow)
                print(player_yellow)
                player_yellow.icon = pygame.image.load('media/player_yellow.png')
                # pygame.transform.scale(player_yellow.icon, (34, 60))
                yellow_button.set_position(1000, 1000)
                if len(player_list) == 3:
                    print(player_list)
                    # current_player = YellowPlayer
                    print('GO RIGHT INTO MAIN')
                    start_menu.disable()
                    main_screen(1)
            elif player_color == 'Purple' and 'player_purple' not in player_list:
                player_purple = PurplePlayer
                player_list.append(player_purple)
                print(player_purple)
                player_purple.icon = pygame.image.load('media/player_purple.png')
                # pygame.transform.scale(player_purple.icon, (34, 60))
                purple_button.set_position(1000, 1000)
                if len(player_list) == 3:
                    print(player_list)
                    # current_player = PurplePlayer
                    print('GO RIGHT INTO MAIN')
                    start_menu.disable()
                    main_screen(1)
        else:
            print("How did you get here?")
            quitter()

    # Function for clean quit
    def quitter():
        """quits pygame and python"""
        pygame.quit()
        quit()

    # Start Menu & Buttons
    start_menu = pygame_menu.Menu(height=400, width=420, theme=pygame_menu.themes.THEME_DEFAULT, title='Select 3 Players', onclose=quitter)
    start_menu.add_label('In Starting Order:')
    green_button = start_menu.add_button('Green', player_add, 'Green')
    blue_button = start_menu.add_button('Blue', player_add, 'Blue')
    grey_button = start_menu.add_button('Grey', player_add, 'Grey')
    yellow_button = start_menu.add_button('Yellow', player_add, 'Yellow')
    purple_button = start_menu.add_button('Purple', player_add, 'Purple')

    # Player space dictionaries, by board number, so inn spaces don't conflict
    spaces_b1 = {-3: (80, 385), -2: (80, 336), -1: (80, 283), 1: (149, 215), 2: (195, 213),
                 3: (245, 191), 4: (299, 192), 5: (360, 218), 6: (413, 242), 7: (466, 269),
                 8: (512, 309), 9: (570, 306), 10: (625, 273), 11: (664, 237), 12: (712, 169),
                 13: (737, 125), 14: (801, 376), 15: (801, 327), 16: (801, 277), 17: (801, 227),
                 18: (801, 176)}
    spaces_b2 = {14: (48, 350), 15: (48, 309), 16: (48, 261), 17: (48, 217), 18: (48, 170),
                 19: (132, 141), 20: (180, 162), 21: (229, 197), 22: (282, 219), 23: (334, 250),
                 24: (434, 290), 25: (440, 321), 26: (496, 374), 27: (549, 387), 28: (602, 384),
                 29: (659, 384), 30: (711, 375), 31: (799, 126), 32: (799, 170), 33: (799, 214),
                 34: (799, 259), 35: (799, 304)}
    spaces_b3 = {31: (53, 113), 32: (53, 155), 33: (53, 199), 34: (53, 244), 35: (53, 290),
                 36: (134, 333), 37: (180, 324), 38: (229, 325), 39: (287, 310), 40: (335, 304),
                 41: (381, 286), 42: (440, 250), 43: (484, 226), 44: (533, 213), 45: (577, 191),
                 46: (625, 161), 47: (666, 127), 48: (716, 121), 49: (795, 343), 50: (795, 299),
                 51: (795, 253), 52: (795, 210), 53: (795, 167)}
    spaces_b4 = {49: (50, 116), 50: (50, 161), 51: (50, 207), 52: (50, 252), 53: (50, 298),
                 54: (133, 337), 55: (180, 326), 56: (404, 302), 57: (269, 284), 58: (307, 258),
                 59: (357, 239), 60: (406, 214), 61: (457, 211), 62: (506, 204), 63: (550, 213),
                 64: (619, 207), 65: (680, 166), 66: (766, 341), 67: (766, 296), 68: (766, 251),
                 69: (766, 205), 70: (766, 159)}

    def player_positioning(board_number):
        """Checks player positions & blits pieces"""
        player_list.reverse()
        for player in player_list:
            print("Board Number:", board_number)
            print("Board Space:", player.board_space)
            if board_number == 1:
                loc = spaces_b1.get(player.board_space)
            elif board_number == 2:
                loc = spaces_b2.get(player.board_space)
            elif board_number == 3:
                loc = spaces_b3.get(player.board_space)
            elif board_number == 4:
                loc = spaces_b4.get(player.board_space)
            print("Line 364:", loc)
            screen.blit(player.icon, loc)
        player_list.reverse()

    # Main Game Loop
    def main_screen(board_number):
        """Main game loop"""
        global current_player

        # Flag for Updating Screen. Flagged at main loop,
        # startup for each board section & after selecting a board space.
        screen_update = 1

        print(current_player)
        # Start Menu
        if board_number == 0:
            start_menu.enable()
            start_menu.mainloop(screen)
        # Board One
        if board_number == 1:
            # Rect(left, top, width, height)
            rect1 = pygame.Rect(155, 150, 21, 122)
            # rect 1_1 is additional rect for position 1
            rect1_1 = pygame.Rect(135, 87, 62, 82)
            rect2 = pygame.Rect(205, 256, 14, 120)
            rect2_1 = pygame.Rect(180, 302, 63, 76)
            rect3 = pygame.Rect(254, 124, 16, 124)
            rect3_1 = pygame.Rect(229, 124, 62, 78)
            rect4 = pygame.Rect(309, 235, 16, 124)
            rect4_1 = pygame.Rect(286, 282, 60, 78)
            rect5 = pygame.Rect(370, 87, 16, 188)
            rect5_1 = pygame.Rect(343, 87, 66, 81)
            rect6 = pygame.Rect(423, 284, 15, 186)
            rect6_1 = pygame.Rect(400, 392, 62, 81)
            rect7 = pygame.Rect(477, 138, 14, 188)
            rect7_1 = pygame.Rect(449, 138, 68, 78)
            rect8 = pygame.Rect(523, 350, 15, 124)
            rect8_1 = pygame.Rect(497, 350, 66, 122)
            rect9 = pygame.Rect(578, 177, 16, 186)
            rect9_1 = pygame.Rect(553, 177, 66, 77)
            rect10 = pygame.Rect(633, 316, 16, 125)
            rect10_1 = pygame.Rect(612, 316, 61, 124)
            rect11 = pygame.Rect(675, 109, 14, 186)
            rect11_1 = pygame.Rect(649, 109, 62, 184)
            rect12 = pygame.Rect(724, 211, 16, 120)
            rect12_1 = pygame.Rect(701, 211, 65, 123)
            rect13 = pygame.Rect(743, 55, 16, 127)
            rect13_1 = pygame.Rect(717, 55, 55, 81)
            rect14 = pygame.Rect(778, 117, 78, 76)
            rect14_1 = pygame.Rect(800, 70, 34, 364)
            # Starting spots
            start_list = [-3, -2, -1]
            current_player = player_list[0]
            for player, position in zip(player_list, start_list):
                player.board_space = position
                print(player.board_space)
        if board_number == 2:
            rect19 = pygame.Rect(140, 186, 17, 107)
            rect19_1 = pygame.Rect(113, 226, 70, 68)
            rect20 = pygame.Rect(187, 108, 18, 112)
            rect20_1 = pygame.Rect(160, 111, 73, 68)
            rect21 = pygame.Rect(237, 240, 18, 171)
            rect21_1 = pygame.Rect(211, 337, 75, 71)
            rect22 = pygame.Rect(290, 106, 18, 172)
            rect22_1 = pygame.Rect(262, 106, 71, 71)
            rect23 = pygame.Rect(343, 295, 17, 169)
            rect23_1 = pygame.Rect(314, 393, 75, 71)
            rect24 = pygame.Rect(408, 177, 17, 171)
            rect24_1 = pygame.Rect(379, 175, 73, 74)
            rect25 = pygame.Rect(448, 365, 18, 101)
            rect25_1 = pygame.Rect(418, 407, 73, 70)
            rect26 = pygame.Rect(505, 258, 16, 172)
            rect26_1 = pygame.Rect(476, 258, 73, 72)
            rect27 = pygame.Rect(558, 430, 17, 115)
            rect27_1 = pygame.Rect(527, 471, 78, 72)
            rect28 = pygame.Rect(609, 273, 18, 169)
            rect28_1 = pygame.Rect(576, 273, 79, 73)
            rect29 = pygame.Rect(668, 427, 18, 111)
            rect29_1 = pygame.Rect(639, 469, 77, 70)
            rect30 = pygame.Rect(719, 320, 18, 113)
            rect30_1 = pygame.Rect(688, 320, 75, 71)
            rect31 = pygame.Rect(795, 148, 40, 332)
            rect31_1 = pygame.Rect(769, 367, 95, 69)
        if board_number == 3:
            rect36 = pygame.Rect(142, 378, 17, 109)
            rect36_1 = pygame.Rect(116, 417, 69, 71)
            rect37 = pygame.Rect(188, 273, 18, 108)
            rect37_1 = pygame.Rect(164, 273, 66, 70)
            rect38 = pygame.Rect(237, 368, 17, 168)
            rect38_1 = pygame.Rect(212, 465, 70, 69)
            rect39 = pygame.Rect(291, 258, 18, 109)
            rect39_1 = pygame.Rect(263, 258, 72, 70)
            rect40 = pygame.Rect(343, 348, 17, 169)
            rect40_1 = pygame.Rect(315, 446, 75, 70)
            rect41 = pygame.Rect(389, 232, 17, 112)
            rect41_1 = pygame.Rect(361, 232, 70, 70)
            rect42 = pygame.Rect(448, 295, 17, 164)
            rect42_1 = pygame.Rect(420, 390, 69, 69)    # Nice
            rect43 = pygame.Rect(493, 174, 16, 109)
            rect43_1 = pygame.Rect(466, 174, 68, 70)
            rect44 = pygame.Rect(541, 255, 18, 168)
            rect44_1 = pygame.Rect(515, 550, 72, 74)
            rect45 = pygame.Rect(584, 81, 18, 168)
            rect45_1 = pygame.Rect(557, 81, 71, 70)
            rect46 = pygame.Rect(632, 202, 19, 114)
            rect46_1 = pygame.Rect(611, 245, 66, 71)
            rect47 = pygame.Rect(673, 76, 19, 109)
            rect47_1 = pygame.Rect(648, 76, 65, 69)
            rect48 = pygame.Rect(725, 166, 17, 164)
            rect48_1 = pygame.Rect(699, 262, 70, 70)
            rect49 = pygame.Rect(793, 69, 36, 332)
            rect49_1 = pygame.Rect(764, 116, 92, 69)
        if board_number == 4:
            rect54 = pygame.Rect(143, 278, 16, 117)
            rect54_1 = pygame.Rect(119, 278, 64, 74)
            rect55 = pygame.Rect(188, 370, 17, 171)
            rect55_1 = pygame.Rect(163, 470, 69, 74)
            rect56 = pygame.Rect(231, 245, 17, 115)
            rect56_1 = pygame.Rect(207, 245, 65, 73)
            rect57 = pygame.Rect(278, 328, 16, 168)
            rect57_1 = pygame.Rect(254, 428, 67, 69)
            rect58 = pygame.Rect(316, 204, 16, 111)
            rect58_1 = pygame.Rect(293, 204, 63, 71)
            rect59 = pygame.Rect(366, 281, 16, 173)
            rect59_1 = pygame.Rect(339, 381, 70, 74)
            rect60 = pygame.Rect(415, 98, 16, 175)
            rect60_1 = pygame.Rect(389, 98, 67, 74)
            rect61 = pygame.Rect(466, 254, 17, 116)
            rect61_1 = pygame.Rect(440, 296, 69, 74)
            rect62 = pygame.Rect(515, 151, 17, 111)
            rect62_1 = pygame.Rect(489, 151, 69, 71)
            rect63 = pygame.Rect(569, 257, 16, 172)
            rect63_1 = pygame.Rect(546, 357, 64, 73)
            rect64 = pygame.Rect(628, 95, 17, 169)
            rect64_1 = pygame.Rect(601, 95, 69, 69)
            rect65 = pygame.Rect(689, 209, 16, 112)
            rect65_1 = pygame.Rect(663, 251, 68, 70)
            rect66 = pygame.Rect(767, 91, 34, 307)
            rect66_1 = pygame.Rect(739, 91, 89, 88)
        # For Cleanup:
        # Function that takes in number and 4 coordinates,
        # that makes rect with our naming convention
        print(current_player.color)
        # Outer Loop Flag
        running = True
        # Outer loop
        while running:
            # Inner Loop for Events
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:   # If The Window's 'X' Button is Clicked
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1: # Left  mouse button.
                        # Check if the rect collides with the mouse pos.
                        if board_number == 1:
                            if rect1.collidepoint(event.pos) or rect1_1.collidepoint(event.pos):
                                if current_player.board_space < 1:
                                    print('Village selected.')
                                    encounter_selection(1)
                                    current_player.board_space = 1
                                    update_current_player()
                                    screen_update = 1
                            if rect2.collidepoint(event.pos) or rect2_1.collidepoint(event.pos):
                                if current_player.board_space < 2:
                                    print('Temple selected.')
                                    encounter_selection(2)
                                    current_player.board_space = 2
                                    update_current_player()
                                    screen_update = 1
                            if rect3.collidepoint(event.pos) or rect3_1.collidepoint(event.pos):
                                if current_player.board_space < 3:
                                    print('Encounter selected.')
                                    encounter_selection(3)
                                    current_player.board_space = 3
                                    update_current_player()
                                    screen_update = 1
                            if rect4.collidepoint(event.pos) or rect4_1.collidepoint(event.pos):
                                if current_player.board_space < 4:
                                    print('Panorama: Paddy selected.')
                                    encounter_selection(4)
                                    current_player.board_space = 4
                                    update_current_player()
                                    screen_update = 1
                            if rect5.collidepoint(event.pos) or rect5_1.collidepoint(event.pos):
                                if current_player.board_space < 5:
                                    print('Hot Springs selected.')
                                    encounter_selection(5)
                                    current_player.board_space = 5
                                    update_current_player()
                                    screen_update = 1
                            if rect6.collidepoint(event.pos) or rect6_1.collidepoint(event.pos):
                                if current_player.board_space < 6:
                                    print('Panorama: Mt selected.')
                                    encounter_selection(6)
                                    current_player.board_space = 6
                                    update_current_player()
                                    screen_update = 1
                            if rect7.collidepoint(event.pos) or rect7_1.collidepoint(event.pos):
                                if current_player.board_space < 7:
                                    print('Farm selected.')
                                    encounter_selection(7)
                                    current_player.board_space = 7
                                    update_current_player()
                                    screen_update = 1
                            if rect8.collidepoint(event.pos) or rect8_1.collidepoint(event.pos):
                                if current_player.board_space < 8:
                                    print('Village selected.')
                                    encounter_selection(8)
                                    current_player.board_space = 8
                                    update_current_player()
                                    screen_update = 1
                            if rect9.collidepoint(event.pos) or rect9_1.collidepoint(event.pos):
                                if current_player.board_space < 9:
                                    print('Temple selected.')
                                    encounter_selection(9)
                                    current_player.board_space = 9
                                    update_current_player()
                                    screen_update = 1
                            if rect10.collidepoint(event.pos) or rect10_1.collidepoint(event.pos):
                                if current_player.board_space < 10:
                                    print('Encounter selected.')
                                    encounter_selection(10)
                                    current_player.board_space = 10
                                    update_current_player()
                                    screen_update = 1
                            if rect11.collidepoint(event.pos) or rect11_1.collidepoint(event.pos):
                                if current_player.board_space < 11:
                                    print('Panorama: Sea selected.')
                                    encounter_selection(11)
                                    current_player.board_space = 11
                                    update_current_player()
                                    screen_update = 1
                            if rect12.collidepoint(event.pos) or rect12_1.collidepoint(event.pos):
                                if current_player.board_space < 12:
                                    print('Panorama: Mountain selected.')
                                    encounter_selection(12)
                                    current_player.board_space = 12
                                    update_current_player()
                                    screen_update = 1
                            if rect13.collidepoint(event.pos) or rect13_1.collidepoint(event.pos):
                                if current_player.board_space < 13:
                                    print('Hot Spring selected.')
                                    encounter_selection(13)
                                    current_player.board_space = 13
                                    update_current_player()
                                    screen_update = 1
                            if rect14.collidepoint(event.pos) or rect14_1.collidepoint(event.pos):
                                if current_player.board_space < 14:
                                    print('We\'re INN IT NOW BOYS')
                                    encounter_selection(14)
                                    if board_number == 1:
                                        if len(board_1_list) == 0:
                                            current_player.board_space = 18
                                            board_1_list.append(current_player)
                                        elif len(board_1_list) == 1:
                                            current_player.board_space = 17
                                            board_1_list.append(current_player)
                                        elif len(board_1_list) == 2:
                                            current_player.board_space = 16
                                            board_1_list.append(current_player)
                                            update_current_player()
                                            running = False
                                            main_screen(2)
                                    update_current_player()
                                    screen_update = 1
                        if board_number == 2:
                            if rect19.collidepoint(event.pos) or rect19_1.collidepoint(event.pos):
                                if current_player.board_space < 19:
                                    print('Panorama: Sea selected.')
                                    encounter_selection(19)
                                    current_player.board_space = 19
                                    update_current_player()
                                    screen_update = 1
                            if rect20.collidepoint(event.pos) or rect20_1.collidepoint(event.pos):
                                if current_player.board_space < 20:
                                    print('Temple selected.')
                                    encounter_selection(20)
                                    current_player.board_space = 20
                                    update_current_player()
                                    screen_update = 1
                            if rect21.collidepoint(event.pos) or rect21_1.collidepoint(event.pos):
                                if current_player.board_space < 21:
                                    print('Farm selected.')
                                    encounter_selection(21)
                                    current_player.board_space = 21
                                    update_current_player()
                                    screen_update = 1
                            if rect22.collidepoint(event.pos) or rect22_1.collidepoint(event.pos):
                                if current_player.board_space < 22:
                                    print('Panorama: Paddy selected.')
                                    encounter_selection(22)
                                    current_player.board_space = 22
                                    update_current_player()
                                    screen_update = 1
                            if rect23.collidepoint(event.pos) or rect23_1.collidepoint(event.pos):
                                if current_player.board_space < 23:
                                    print('Panorama: Mountain selected.')
                                    encounter_selection(23)
                                    current_player.board_space = 23
                                    update_current_player()
                                    screen_update = 1
                            if rect24.collidepoint(event.pos) or rect24_1.collidepoint(event.pos):
                                if current_player.board_space < 24:
                                    print('Encounter selected.')
                                    encounter_selection(24)
                                    current_player.board_space = 24
                                    update_current_player()
                                    screen_update = 1
                            if rect25.collidepoint(event.pos) or rect25_1.collidepoint(event.pos):
                                if current_player.board_space < 25:
                                    print('Temple selected.')
                                    encounter_selection(25)
                                    current_player.board_space = 25
                                    update_current_player()
                                    screen_update = 1
                            if rect26.collidepoint(event.pos) or rect26_1.collidepoint(event.pos):
                                if current_player.board_space < 26:
                                    print('Hot Spring selected.')
                                    encounter_selection(26)
                                    current_player.board_space = 26
                                    update_current_player()
                                    screen_update = 1
                            if rect27.collidepoint(event.pos) or rect27_1.collidepoint(event.pos):
                                if current_player.board_space < 27:
                                    print('Panorama: Mountain selected.')
                                    encounter_selection(27)
                                    current_player.board_space = 27
                                    update_current_player()
                                    screen_update = 1
                            if rect28.collidepoint(event.pos) or rect28_1.collidepoint(event.pos):
                                if current_player.board_space < 28:
                                    print('Panorama: Sea selected.')
                                    encounter_selection(28)
                                    current_player.board_space = 28
                                    update_current_player()
                                    screen_update = 1
                            if rect29.collidepoint(event.pos) or rect29_1.collidepoint(event.pos):
                                if current_player.board_space < 29:
                                    print('Village selected.')
                                    encounter_selection(29)
                                    current_player.board_space = 29
                                    update_current_player()
                                    screen_update = 1
                            if rect30.collidepoint(event.pos) or rect30_1.collidepoint(event.pos):
                                if current_player.board_space < 30:
                                    print('Farm selected.')
                                    encounter_selection(30)
                                    current_player.board_space = 30
                                    update_current_player()
                                    screen_update = 1
                            if rect31.collidepoint(event.pos) or rect31_1.collidepoint(event.pos):
                                if current_player.board_space < 31:
                                    print('We\'re INN IT NOW BOYS')
                                    encounter_selection(31)
                                    if board_number == 1:
                                        if len(board_1_list) == 0:
                                            current_player.board_space = 35
                                            board_1_list.append(current_player)
                                        elif len(board_1_list) == 1:
                                            current_player.board_space = 34
                                            board_1_list.append(current_player)
                                        elif len(board_1_list) == 2:
                                            current_player.board_space = 33
                                            board_1_list.append(current_player)
                                            update_current_player()
                                            running = False
                                            main_screen(3)
                                    update_current_player()
                                    screen_update = 1
                        if board_number == 3:
                            if rect36.collidepoint(event.pos) or rect36_1.collidepoint(event.pos):
                                if current_player.board_space < 36:
                                    print('Panorama: Paddy selected.')
                                    encounter_selection(36)
                                    current_player.board_space = 36
                                    update_current_player()
                                    screen_update = 1
                            if rect37.collidepoint(event.pos) or rect37_1.collidepoint(event.pos):
                                if current_player.board_space < 37:
                                    print('Village selected.')
                                    encounter_selection(37)
                                    current_player.board_space = 37
                                    update_current_player()
                                    screen_update = 1
                            if rect38.collidepoint(event.pos) or rect38_1.collidepoint(event.pos):
                                if current_player.board_space < 38:
                                    print('Encounter selected.')
                                    encounter_selection(38)
                                    current_player.board_space = 38
                                    update_current_player()
                                    screen_update = 1
                            if rect39.collidepoint(event.pos) or rect39_1.collidepoint(event.pos):
                                if current_player.board_space < 39:
                                    print('Farm selected.')
                                    encounter_selection(39)
                                    current_player.board_space = 39
                                    update_current_player()
                                    screen_update = 1
                            if rect40.collidepoint(event.pos) or rect40_1.collidepoint(event.pos):
                                if current_player.board_space < 40:
                                    print('Panorama: Mountain selected.')
                                    encounter_selection(40)
                                    current_player.board_space = 40
                                    update_current_player()
                                    screen_update = 1
                            if rect41.collidepoint(event.pos) or rect41_1.collidepoint(event.pos):
                                if current_player.board_space < 41:
                                    print('Hot Spring selected.')
                                    encounter_selection(41)
                                    current_player.board_space = 41
                                    update_current_player()
                                    screen_update = 1
                            if rect42.collidepoint(event.pos) or rect42_1.collidepoint(event.pos):
                                if current_player.board_space < 42:
                                    print('Panorama: Sea selected.')
                                    encounter_selection(42)
                                    current_player.board_space = 42
                                    update_current_player()
                                    screen_update = 1
                            if rect43.collidepoint(event.pos) or rect43_1.collidepoint(event.pos):
                                if current_player.board_space < 43:
                                    print('Panorama: Paddy selected.')
                                    encounter_selection(43)
                                    current_player.board_space = 43
                                    update_current_player()
                                    screen_update = 1
                            if rect44.collidepoint(event.pos) or rect44_1.collidepoint(event.pos):
                                if current_player.board_space < 44:
                                    print('Temple selected.')
                                    encounter_selection(44)
                                    current_player.board_space = 44
                                    update_current_player()
                                    screen_update = 1
                            if rect45.collidepoint(event.pos) or rect45_1.collidepoint(event.pos):
                                if current_player.board_space < 45:
                                    print('Farm selected.')
                                    encounter_selection(45)
                                    current_player.board_space = 45
                                    update_current_player()
                                    screen_update = 1
                            if rect46.collidepoint(event.pos) or rect46_1.collidepoint(event.pos):
                                if current_player.board_space < 46:
                                    print('Encounter selected.')
                                    encounter_selection(46)
                                    current_player.board_space = 46
                                    update_current_player()
                                    screen_update = 1
                            if rect47.collidepoint(event.pos) or rect47_1.collidepoint(event.pos):
                                if current_player.board_space < 47:
                                    print('Panorama: Sea selected.')
                                    encounter_selection(47)
                                    current_player.board_space = 47
                                    update_current_player()
                                    screen_update = 1
                            if rect48.collidepoint(event.pos) or rect48_1.collidepoint(event.pos):
                                if current_player.board_space < 48:
                                    print('Village selected.')
                                    encounter_selection(48)
                                    current_player.board_space = 48
                                    update_current_player()
                                    screen_update = 1
                            if rect49.collidepoint(event.pos) or rect49_1.collidepoint(event.pos):
                                if current_player.board_space < 49:
                                    print('We\'re INN IT NOW BOYS')
                                    encounter_selection(49)
                                    if board_number == 1:
                                        if len(board_1_list) == 0:
                                            current_player.board_space = 53
                                            board_1_list.append(current_player)
                                        elif len(board_1_list) == 1:
                                            current_player.board_space = 52
                                            board_1_list.append(current_player)
                                        elif len(board_1_list) == 2:
                                            current_player.board_space = 51
                                            board_1_list.append(current_player)
                                            update_current_player()
                                            running = False
                                            main_screen(4)
                                    update_current_player()
                                    screen_update = 1
                        if board_number == 4:
                            if rect54.collidepoint(event.pos) or rect54_1.collidepoint(event.pos):
                                if current_player.board_space < 54:
                                    print('Hot Spring selected.')
                                    encounter_selection(54)
                                    current_player.board_space = 54
                                    update_current_player()
                                    screen_update = 1
                            if rect55.collidepoint(event.pos) or rect5_1.collidepoint(event.pos):
                                if current_player.board_space < 55:
                                    print('Temple selected.')
                                    encounter_selection(55)
                                    current_player.board_space = 55
                                    update_current_player()
                                    screen_update = 1
                            if rect56.collidepoint(event.pos) or rect56_1.collidepoint(event.pos):
                                if current_player.board_space < 56:
                                    print('Encounter selected.')
                                    encounter_selection(56)
                                    current_player.board_space = 56
                                    update_current_player()
                                    screen_update = 1
                            if rect57.collidepoint(event.pos) or rect57_1.collidepoint(event.pos):
                                if current_player.board_space < 57:
                                    print('Village selected.')
                                    encounter_selection(57)
                                    current_player.board_space = 57
                                    update_current_player()
                                    screen_update = 1
                            if rect58.collidepoint(event.pos) or rect58_1.collidepoint(event.pos):
                                if current_player.board_space < 58:
                                    print('Panorama: Sea selected.')
                                    encounter_selection(58)
                                    current_player.board_space = 58
                                    update_current_player()
                                    screen_update = 1
                            if rect59.collidepoint(event.pos) or rect59_1.collidepoint(event.pos):
                                if current_player.board_space < 59:
                                    print('Farm selected.')
                                    encounter_selection(59)
                                    current_player.board_space = 59
                                    update_current_player()
                                    screen_update = 1
                            if rect60.collidepoint(event.pos) or rect60_1.collidepoint(event.pos):
                                if current_player.board_space < 60:
                                    print('Hot Spring selected.')
                                    encounter_selection(60)
                                    current_player.board_space = 60
                                    update_current_player()
                                    screen_update = 1
                            if rect61.collidepoint(event.pos) or rect61_1.collidepoint(event.pos):
                                if current_player.board_space < 61:
                                    print('Encounter selected.')
                                    encounter_selection(61)
                                    current_player.board_space = 61
                                    update_current_player()
                                    screen_update = 1
                            if rect62.collidepoint(event.pos) or rect62_1.collidepoint(event.pos):
                                if current_player.board_space < 62:
                                    print('Panorama: Mountain selected.')
                                    encounter_selection(62)
                                    current_player.board_space = 62
                                    update_current_player()
                                    screen_update = 1
                            if rect63.collidepoint(event.pos) or rect63_1.collidepoint(event.pos):
                                if current_player.board_space < 63:
                                    print('Panorama: Paddy selected.')
                                    encounter_selection(63)
                                    current_player.board_space = 63
                                    update_current_player()
                                    screen_update = 1
                            if rect64.collidepoint(event.pos) or rect64_1.collidepoint(event.pos):
                                if current_player.board_space < 64:
                                    print('Panorama: Sea selected.')
                                    encounter_selection(64)
                                    current_player.board_space = 64
                                    update_current_player()
                                    screen_update = 1
                            if rect65.collidepoint(event.pos) or rect65_1.collidepoint(event.pos):
                                if current_player.board_space < 65:
                                    print('Village selected.')
                                    encounter_selection(65)
                                    current_player.board_space = 65
                                    update_current_player()
                                    screen_update = 1
                            if rect66.collidepoint(event.pos) or rect66_1.collidepoint(event.pos):
                                if current_player.board_space < 66:
                                    print('We\'re INN IT NOW BOYS')
                                    encounter_selection(66)
                                    if board_number == 1:
                                        if len(board_1_list) == 0:
                                            current_player.board_space = 70
                                            board_1_list.append(current_player)
                                        elif len(board_1_list) == 1:
                                            current_player.board_space = 69
                                            board_1_list.append(current_player)
                                        elif len(board_1_list) == 2:
                                            current_player.board_space = 68
                                            board_1_list.append(current_player)
                                            update_current_player()
                                            running = False
                                            # results_menu(screen)
                                    update_current_player()
                                    screen_update = 1

                # Remove comment below to get list of events to terminal
                # print(event)

            # Endpoint for initialization, aka main_screen(0)
            if start_menu.is_enabled():
                start_menu.update(events)
                start_menu.draw(screen)

            # Only update screen if needed, blits in functions
            if screen_update == 1:
                # Filling screen
                screen.fill(white)
                # Player turn indicator
                title_selector(current_player)
                # Scores & probabilities
                score_prob_display()
                # Current board section
                board(X_BOARD_COORD, Y_BOARD_COORD, board_number)
                # Player position checks
                player_positioning(board_number)
                # After all screen items are blitted(sp?), update display
                pygame.display.update()
            # Reset Flag
            screen_update = 0


    def hot_springs_menu(screen):
        """Hot Springs Menu"""
        global current_player
        paused = True
        hs_screen_update = 1
        text_select = pygame.font.SysFont('Arial', 50)
        text_select_r = text_select.render('Select Card:', True, black)
        text_select_rect = text_select_r.get_rect()
        text_select_rect.center = (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT * .2)
        hs_2 = pygame.image.load('media/hs_2.png')
        hs_3 = pygame.image.load('media/hs_3.png')
        hs_2_rect = hs_2.get_rect()
        hs_3_rect = hs_3.get_rect()
        hs_2_rect.center = (DISPLAY_WIDTH * .32, DISPLAY_HEIGHT * .51)
        hs_3_rect.center = (DISPLAY_WIDTH * .68, DISPLAY_HEIGHT * .51)
        while paused:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    quitter()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if hs_2_rect.collidepoint(event.pos):
                            current_player = Hot_Spring_Loc(current_player, 2)
                            return
                        elif hs_3_rect.collidepoint(event.pos):
                            current_player = Hot_Spring_Loc(current_player, 3)
                            return
            if hs_screen_update == 1:
                screen.fill((255, 255, 255))
                screen.blit(text_select_r, text_select_rect)
                screen.blit(hs_2, hs_2_rect)
                screen.blit(hs_3, hs_3_rect)
                hs_screen_update = 0
                pygame.display.update()
        return False

    def farm_menu(screen):
        """Farm Menu"""
        global current_player
        paused = True
        farm_screen_update = 1
        farm_text_style = pygame.font.SysFont('Arial', 50)
        farm_collect_text = farm_text_style.render('Farm: Collect 3 Coins!', True, black)
        farm_collect_rect = farm_collect_text.get_rect()
        farm_collect_rect.center = (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT * .2)
        farm_confirmation_text = farm_text_style.render('Click Anywhere To Continue', True, black)
        farm_confirmation_rect = farm_confirmation_text.get_rect()
        farm_confirmation_rect.center = (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT * .7)
        coinpile = pygame.image.load('media/coins_three.png')
        coinpile_rect = coinpile.get_rect()
        coinpile_rect.center = (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT * .45)
        while paused:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    quitter()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        current_player = Farm_Loc(current_player)
                        return
            if farm_screen_update == 1:
                screen.fill((255, 255, 255))
                screen.blit(farm_collect_text, farm_collect_rect)
                screen.blit(farm_confirmation_text, farm_confirmation_rect)
                screen.blit(coinpile, coinpile_rect)
                farm_screen_update = 0
                pygame.display.update()
        return False

    def pano_paddy_menu(screen):
        """Panorama Paddy Menu"""
        global current_player
        paused = True
        paddy_screen_update = 1
        if current_player.pano_paddy == 0:
            paddy_cards = pygame.image.load('media/paddy_1.png')
        if current_player.pano_paddy == 1:
            paddy_cards = pygame.image.load('media/paddy_2.png')
        if current_player.pano_paddy == 2:
            paddy_cards = pygame.image.load('media/paddy_3.png')
        paddy_cards_rect = paddy_cards.get_rect()
        paddy_cards_rect.center = (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT * .45)
        paddy_text_style = pygame.font.SysFont('Arial', 50)
        paddy_collect_text = paddy_text_style.render('Panorama: Rice Paddy', True, black)
        paddy_collect_rect = paddy_collect_text.get_rect()
        paddy_collect_rect.center = (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT * .2)
        paddy_confirmation_text = paddy_text_style.render('Click Anywhere To Continue', True, black)
        paddy_confirmation_rect = paddy_confirmation_text.get_rect()
        paddy_confirmation_rect.center = (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT * .7)
        while paused:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    quitter()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        current_player = Pano_Paddy_Loc(current_player)
                        return
            if paddy_screen_update == 1:
                screen.fill((255, 255, 255))
                screen.blit(paddy_collect_text, paddy_collect_rect)
                screen.blit(paddy_confirmation_text, paddy_confirmation_rect)
                screen.blit(paddy_cards, paddy_cards_rect)
                paddy_screen_update = 0
                pygame.display.update()
        return False

    def pano_mt_menu(screen):
        """Panorama Mountain Menu"""
        global current_player
        paused = True
        mt_screen_update = 1
        if current_player.pano_mt == 0:
            mt_cards = pygame.image.load('media/mt_1.png')
        if current_player.pano_mt == 1:
            mt_cards = pygame.image.load('media/mt_2.png')
        if current_player.pano_mt == 2:
            mt_cards = pygame.image.load('media/mt_3.png')
        if current_player.pano_mt == 3:
            mt_cards = pygame.image.load('media/mt_4.png')
        mt_cards_rect = mt_cards.get_rect()
        mt_cards_rect.center = (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT * .45)
        mt_text_style = pygame.font.SysFont('Arial', 50)
        mt_collect_text = mt_text_style.render('Panorama: Mountains', True, black)
        mt_collect_rect = mt_collect_text.get_rect()
        mt_collect_rect.center = (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT * .2)
        mt_confirmation_text = mt_text_style.render('Click Anywhere To Continue', True, black)
        mt_confirmation_rect = mt_confirmation_text.get_rect()
        mt_confirmation_rect.center = (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT * .7)
        while paused:
            screen.fill((255, 255, 255))
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    quitter()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        current_player = Pano_Mt_Loc(current_player)
                        return
            if mt_screen_update == 1:
                screen.fill((255, 255, 255))
                screen.blit(mt_collect_text, mt_collect_rect)
                screen.blit(mt_confirmation_text, mt_confirmation_rect)
                screen.blit(mt_cards, mt_cards_rect)
                mt_screen_update = 0
                pygame.display.update()
        return False

    def pano_sea_menu(screen):
        """Panorama Sea Menu"""
        global current_player
        paused = True
        sea_screen_update = 1
        if current_player.pano_sea == 0:
            sea_cards = pygame.image.load('media/sea_1.png')
        if current_player.pano_sea == 1:
            sea_cards = pygame.image.load('media/sea_2.png')
        if current_player.pano_sea == 2:
            sea_cards = pygame.image.load('media/sea_3.png')
        if current_player.pano_sea == 3:
            sea_cards = pygame.image.load('media/sea_4.png')
        if current_player.pano_sea == 4:
            sea_cards = pygame.image.load('media/sea_5.png')
        sea_cards_rect = sea_cards.get_rect()
        sea_cards_rect.center = (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT * .45)
        sea_text_style = pygame.font.SysFont('Arial', 50)
        sea_collect_text = sea_text_style.render('Panorama: Sea', True, black)
        sea_collect_rect = sea_collect_text.get_rect()
        sea_collect_rect.center = (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT * .2)
        sea_confirmation_text = sea_text_style.render('Click Anywhere To Continue', True, black)
        sea_confirmation_rect = sea_confirmation_text.get_rect()
        sea_confirmation_rect.center = (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT * .7)
        while paused:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    quitter()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        current_player = Pano_Sea_Loc(current_player)
                        return
            if sea_screen_update == 1:
                screen.fill((255, 255, 255))
                screen.blit(sea_collect_text, sea_collect_rect)
                screen.blit(sea_confirmation_text, sea_confirmation_rect)
                screen.blit(sea_cards, sea_cards_rect)
                sea_screen_update = 0
                pygame.display.update()
        return False

    def encounter_menu(screen):
        """Encounter Menu"""
        global current_player
        paused = True
        enc_screen_update = 1
        enc_anna_mt = pygame.image.load('media/anna_mt.png')
        enc_anna_mt_rect = enc_anna_mt.get_rect()
        enc_anna_mt_rect.center = (DISPLAY_WIDTH * .44, DISPLAY_HEIGHT * .68)
        enc_anna_paddy = pygame.image.load('media/anna_paddy.png')
        enc_anna_paddy_rect = enc_anna_paddy.get_rect()
        enc_anna_paddy_rect.center = (DISPLAY_WIDTH * .29, DISPLAY_HEIGHT * .68)
        enc_anna_sea = pygame.image.load('media/anna_sea.png')
        enc_anna_sea_rect = enc_anna_sea.get_rect()
        enc_anna_sea_rect.center = (DISPLAY_WIDTH * .59, DISPLAY_HEIGHT * .68)
        enc_kuge = pygame.image.load('media/kuge.png')
        enc_kuge_rect = enc_kuge.get_rect()
        enc_kuge_rect.center = (DISPLAY_WIDTH * .29, DISPLAY_HEIGHT * .4)
        enc_miko = pygame.image.load('media/miko.png')
        enc_miko_rect = enc_miko.get_rect()
        enc_miko_rect.center = (DISPLAY_WIDTH * .44, DISPLAY_HEIGHT * .4)
        enc_samurai = pygame.image.load('media/samurai.png')
        enc_samurai_rect = enc_samurai.get_rect()
        enc_samurai_rect.center = (DISPLAY_WIDTH * .59, DISPLAY_HEIGHT * .4)
        enc_shokunin = pygame.image.load('media/shokunin.png')
        enc_shokunin_rect = enc_shokunin.get_rect()
        enc_shokunin_rect.center = (DISPLAY_WIDTH * .74, DISPLAY_HEIGHT * .54)
        enc_text_style = pygame.font.SysFont('Arial', 50)
        enc_select_text = enc_text_style.render('Select Encounter:', True, black)
        enc_select_rect = enc_select_text.get_rect()
        enc_select_rect.center = (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT * .2)
        while paused:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    quitter()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if enc_kuge_rect.collidepoint(event.pos):
                            current_player = Encounter_Loc(current_player, "Kuge")
                            return
                        elif enc_miko_rect.collidepoint(event.pos):
                            current_player = Encounter_Loc(current_player, "Miko")
                            return
                        elif enc_samurai_rect.collidepoint(event.pos):
                            current_player = Encounter_Loc(current_player, "Samurai")
                            return
                        elif enc_shokunin_rect.collidepoint(event.pos):
                            current_player = Encounter_Loc(current_player, "Shokunin")
                            return
                        elif enc_anna_paddy_rect.collidepoint(event.pos):
                            current_player = Encounter_Loc(current_player, "Annaibito: Paddy")
                            return
                        elif enc_anna_mt_rect.collidepoint(event.pos):
                            current_player = Encounter_Loc(current_player, "Annaibito: Mountain")
                            return
                        elif enc_anna_sea_rect.collidepoint(event.pos):
                            current_player = Encounter_Loc(current_player, "Annaibito: Sea")
                            return
            if enc_screen_update == 1:
                screen.fill((255, 255, 255))
                screen.blit(enc_select_text, enc_select_rect)
                screen.blit(enc_anna_mt, enc_anna_mt_rect)
                screen.blit(enc_anna_paddy, enc_anna_paddy_rect)
                screen.blit(enc_anna_sea, enc_anna_sea_rect)
                screen.blit(enc_kuge, enc_kuge_rect)
                screen.blit(enc_miko, enc_miko_rect)
                screen.blit(enc_samurai, enc_samurai_rect)
                screen.blit(enc_shokunin, enc_shokunin_rect)
                print("UPDATE")
                enc_screen_update = 0
                pygame.display.update()
        return False

    def inn_menu(screen):
        global current_player
        paused = True
        while paused:
            screen.fill((255, 255, 255))
            but_miso = Button(DISPLAY_WIDTH / 3 + 150, (DISPLAY_HEIGHT // 3), ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)
            but_dango = Button(DISPLAY_WIDTH / 3 + 150, ((DISPLAY_HEIGHT // 3) + 50), ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)
            but_nigiri = Button(DISPLAY_WIDTH / 3 + 150, (DISPLAY_HEIGHT // 3) + 100, ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)
            but_tempura = Button(DISPLAY_WIDTH / 3 + 150, ((DISPLAY_HEIGHT // 3) + 150), ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)
            but_soba = Button(DISPLAY_WIDTH / 3 + 150, (DISPLAY_HEIGHT // 3) - 50, ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)
            but_yakitori = Button(DISPLAY_WIDTH / 3 + 150, ((DISPLAY_HEIGHT // 3) - 100), ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)
            but_tofu = Button(DISPLAY_WIDTH / 3 + 150, (DISPLAY_HEIGHT // 3) - 150, ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)
            but_sushi = Button(DISPLAY_WIDTH / 3 - 50, (DISPLAY_HEIGHT // 3), ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)
            but_fugu = Button(DISPLAY_WIDTH / 3 - 50, ((DISPLAY_HEIGHT // 3) + 50), ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)
            but_donburi = Button(DISPLAY_WIDTH / 3 - 50, (DISPLAY_HEIGHT // 3) + 100, ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)
            but_sashimi = Button(DISPLAY_WIDTH / 3 - 50, ((DISPLAY_HEIGHT // 3) + 150), ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)
            but_udon = Button(DISPLAY_WIDTH / 3 - 50, (DISPLAY_HEIGHT // 3) - 50, ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)
            but_unagi = Button(DISPLAY_WIDTH / 3 - 50, ((DISPLAY_HEIGHT // 3) - 100), ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)
            but_taimeshi = Button(DISPLAY_WIDTH / 3 - 50, (DISPLAY_HEIGHT // 3) - 150, ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)

            but_miso.add_text('Miso')
            but_dango.add_text('Dango')
            but_nigiri.add_text('Nigiri')
            but_tempura.add_text('Tempura')
            but_soba.add_text('Soba')
            but_yakitori.add_text('Yakitori')
            but_tofu.add_text('Tofu')
            but_sushi.add_text('Sushi')
            but_fugu.add_text('Fugu')
            but_donburi.add_text('Donburi')
            but_sashimi.add_text('Sashimi')
            but_udon.add_text('Udon')
            but_unagi.add_text('Ungai')
            but_taimeshi.add_text('Tai Meshi')

            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    quitter()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if but_miso.collidepoint(event.pos):
                            current_player = Inn_Loc(current_player, "Miso")
                            return
                        elif but_dango.collidepoint(event.pos):
                            current_player = Inn_Loc(current_player, "Dango")
                            return
                        elif but_nigiri.collidepoint(event.pos):
                            current_player = Inn_Loc(current_player, "Nigiri")
                            return
                        elif but_tempura.collidepoint(event.pos):
                            current_player = Inn_Loc(current_player, "Tempura")
                            return
                        elif but_soba.collidepoint(event.pos):
                            current_player = Inn_Loc(current_player, "Soba")
                            return
                        elif but_yakitori.collidepoint(event.pos):
                            current_player = Inn_Loc(current_player, "Yakitori")
                            return
                        elif but_tofu.collidepoint(event.pos):
                            current_player = Inn_Loc(current_player, "Tofu")
                            return
                        elif but_sushi.collidepoint(event.pos):
                            current_player = Inn_Loc(current_player, "Sushi")
                            return
                        elif but_fugu.collidepoint(event.pos):
                            current_player = Inn_Loc(current_player, "Fugu")
                            return
                        elif but_donburi.collidepoint(event.pos):
                            current_player = Encounter_Loc(current_player, "Donburi")
                            return
                        elif but_sashimi.collidepoint(event.pos):
                            current_player = Inn_Loc(current_player, "Sashimi")
                            return
                        elif but_udon.collidepoint(event.pos):
                            current_player = Inn_Loc(current_player, "Udon")
                            return
                        elif but_unagi.collidepoint(event.pos):
                            current_player = Inn_Loc(current_player, "Unagi")
                            return
                        elif but_taimeshi.collidepoint(event.pos):
                            current_player = Inn_Loc(current_player, "Tai Meshi")
                            return
            pygame.display.update()
        return False

    def village_menu(screen):
        """Village Menu"""
        global current_player
        paused = True
        counter = 0
        while paused and counter < 3:
            screen.fill((255, 255, 255))
            but_gofu = Button(DISPLAY_WIDTH / 3 + 50, (DISPLAY_HEIGHT // 3), ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)
            but_koma = Button(DISPLAY_WIDTH / 3 + 50, ((DISPLAY_HEIGHT // 3) + 50), ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)
            but_yunomi = Button(DISPLAY_WIDTH / 3 + 50, (DISPLAY_HEIGHT // 3) + 100, ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)
            but_washi = Button(DISPLAY_WIDTH / 3 + 50, ((DISPLAY_HEIGHT // 3) + 150), ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)
            but_uchiwa = Button(DISPLAY_WIDTH / 3 + 50, (DISPLAY_HEIGHT // 3) - 50, ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)
            but_hashi = Button(DISPLAY_WIDTH / 3 + 50, ((DISPLAY_HEIGHT // 3) - 100), ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)
            but_konpeito = Button(DISPLAY_WIDTH / 3 + 50, (DISPLAY_HEIGHT // 3) - 150, ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)
            but_kamaboko = Button(DISPLAY_WIDTH / 3 - 150, (DISPLAY_HEIGHT // 3), ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)
            but_manju = Button(DISPLAY_WIDTH / 3 - 150, ((DISPLAY_HEIGHT // 3) + 50), ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)
            but_daifuku = Button(DISPLAY_WIDTH / 3 - 150, (DISPLAY_HEIGHT // 3) + 100, ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)
            but_ocha = Button(DISPLAY_WIDTH / 3 - 150, ((DISPLAY_HEIGHT // 3) + 150), ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)
            but_sake = Button(DISPLAY_WIDTH / 3 - 150, (DISPLAY_HEIGHT // 3) - 50, ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)
            but_yukata = Button(DISPLAY_WIDTH / 3 - 150, ((DISPLAY_HEIGHT // 3) - 100), ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)
            but_kanzashi = Button(DISPLAY_WIDTH / 3 - 150, (DISPLAY_HEIGHT // 3) - 150, ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)
            but_geta = Button(DISPLAY_WIDTH / 3 + 200, (DISPLAY_HEIGHT // 3), ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)
            but_haori = Button(DISPLAY_WIDTH / 3 + 200, ((DISPLAY_HEIGHT // 3) + 50), ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)
            but_furoshiki = Button(DISPLAY_WIDTH / 3 + 200, (DISPLAY_HEIGHT // 3) + 100, ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)
            but_sandogasa = Button(DISPLAY_WIDTH / 3 + 200, ((DISPLAY_HEIGHT // 3) + 150), ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)
            but_netsuke = Button(DISPLAY_WIDTH / 3 + 200, (DISPLAY_HEIGHT // 3) - 50, ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)
            but_shikki = Button(DISPLAY_WIDTH / 3 + 200, ((DISPLAY_HEIGHT // 3) - 100), ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)
            but_jubako = Button(DISPLAY_WIDTH / 3 + 200, (DISPLAY_HEIGHT // 3) - 150, ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)
            but_ukiyoe = Button(DISPLAY_WIDTH / 3 - 300, ((DISPLAY_HEIGHT // 3)) - 150, ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)
            but_sumie = Button(DISPLAY_WIDTH / 3 - 300, (DISPLAY_HEIGHT // 3) - 100, ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)
            but_shamisen = Button(DISPLAY_WIDTH / 3 - 300, ((DISPLAY_HEIGHT // 3) - 50), ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)

            but_gofu.add_text('Gofu')
            but_koma.add_text('Koma')
            but_yunomi.add_text('Yunomi')
            but_washi.add_text('Washi')
            but_uchiwa.add_text('Uchiwa')
            but_hashi.add_text('Hashi')
            but_konpeito.add_text('Konpeito')
            but_kamaboko.add_text('Kamaboko')
            but_manju.add_text('Manju')
            but_daifuku.add_text('Daifuku')
            but_ocha.add_text('Ocha')
            but_sake.add_text('Sake')
            but_yukata.add_text('Yukata')
            but_kanzashi.add_text('Kan Zashi')
            but_geta.add_text('Geta')
            but_haori.add_text('Haori')
            but_furoshiki.add_text('Furoshiki')
            but_sandogasa.add_text('Sandogasa')
            but_netsuke.add_text('Netsuke')
            but_shikki.add_text('Shikki')
            but_jubako.add_text('Jubako')
            but_ukiyoe.add_text('Ukiyoe')
            but_sumie.add_text('Sumie')
            but_shamisen.add_text('Shamisen')

            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    quitter()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if but_gofu.collidepoint(event.pos):
                            current_player = Village_Loc(current_player, "Gofu")
                            counter += 1
                        elif but_koma.collidepoint(event.pos):
                            current_player = Village_Loc(current_player, "Koma")
                            counter += 1
                        elif but_yunomi.collidepoint(event.pos):
                            current_player = Village_Loc(current_player, "Yunomi")
                            counter += 1
                        elif but_washi.collidepoint(event.pos):
                            current_player = Village_Loc(current_player, "Washi")
                            counter += 1
                        elif but_uchiwa.collidepoint(event.pos):
                            current_player = Village_Loc(current_player, "Uchiwa")
                            counter += 1
                        elif but_hashi.collidepoint(event.pos):
                            current_player = Village_Loc(current_player, "Hashi")
                            counter += 1
                        elif but_konpeito.collidepoint(event.pos):
                            current_player = Village_Loc(current_player, "Konpeito")
                            counter += 1
                        elif but_kamaboko.collidepoint(event.pos):
                            current_player = Village_Loc(current_player, "Kamaboko")
                            counter += 1
                        elif but_manju.collidepoint(event.pos):
                            current_player = Village_Loc(current_player, "Manju")
                            counter += 1
                        elif but_daifuku.collidepoint(event.pos):
                            current_player = Village_Loc(current_player, "Daifuku")
                            counter += 1
                        elif but_ocha.collidepoint(event.pos):
                            current_player = Village_Loc(current_player, "Ocha")
                            counter += 1
                        elif but_sake.collidepoint(event.pos):
                            current_player = Village_Loc(current_player, "Sake")
                            counter += 1
                        elif but_yukata.collidepoint(event.pos):
                            current_player = Village_Loc(current_player, "Yukata")
                            counter += 1
                        elif but_kanzashi.collidepoint(event.pos):
                            current_player = Village_Loc(current_player, "Kan Zashi")
                            counter += 1
                        elif but_geta.collidepoint(event.pos):
                            current_player = Village_Loc(current_player, "Geta")
                            counter += 1
                        elif but_haori.collidepoint(event.pos):
                            current_player = Village_Loc(current_player, "Haori")
                            counter += 1
                        elif but_furoshiki.collidepoint(event.pos):
                            current_player = Village_Loc(current_player, "Furoshiki")
                            counter += 1
                        elif but_sandogasa.collidepoint(event.pos):
                            current_player = Village_Loc(current_player, "Sandogasa")
                            counter += 1
                        elif but_netsuke.collidepoint(event.pos):
                            current_player = Village_Loc(current_player, "Netsuke")
                            counter += 1
                        elif but_shikki.collidepoint(event.pos):
                            current_player = Village_Loc(current_player, "Shikki")
                            counter += 1
                        elif but_jubako.collidepoint(event.pos):
                            current_player = Village_Loc(current_player, "Jubako")
                            counter += 1
                        elif but_ukiyoe.collidepoint(event.pos):
                            current_player = Village_Loc(current_player, "Ukiyoe")
                            counter += 1
                        elif but_sumie.collidepoint(event.pos):
                            current_player = Village_Loc(current_player, "Sumie")
                            counter += 1
                        elif but_shamisen.collidepoint(event.pos):
                            current_player = Village_Loc(current_player, "Shamisen")
                            counter += 1
                    elif event.button == 3:
                        if but_gofu.collidepoint(event.pos):
                            discard(SVDeck, "Gofu")
                            counter += 1
                        elif but_koma.collidepoint(event.pos):
                            discard(SVDeck, "Koma")
                            counter += 1
                        elif but_yunomi.collidepoint(event.pos):
                            discard(SVDeck, "Yunomi")
                            counter += 1
                        elif but_washi.collidepoint(event.pos):
                            discard(SVDeck, "Washi")
                            counter += 1
                        elif but_uchiwa.collidepoint(event.pos):
                            discard(SVDeck, "Uchiwa")
                            counter += 1
                        elif but_hashi.collidepoint(event.pos):
                            discard(SVDeck, "Hashi")
                            counter += 1
                        elif but_konpeito.collidepoint(event.pos):
                            discard(SVDeck, "Konpeito")
                            counter += 1
                        elif but_kamaboko.collidepoint(event.pos):
                            discard(SVDeck, "Kamaboko")
                            counter += 1
                        elif but_manju.collidepoint(event.pos):
                            discard(SVDeck, "Manju")
                            counter += 1
                        elif but_daifuku.collidepoint(event.pos):
                            discard(SVDeck, "Daifuku")
                            counter += 1
                        elif but_ocha.collidepoint(event.pos):
                            discard(SVDeck, "Ocha")
                            counter += 1
                        elif but_sake.collidepoint(event.pos):
                            discard(SVDeck, "Sake")
                            counter += 1
                        elif but_yukata.collidepoint(event.pos):
                            discard(SVDeck, "Yukata")
                            counter += 1
                        elif but_kanzashi.collidepoint(event.pos):
                            discard(SVDeck, "Kan Zashi")
                            counter += 1
                        elif but_geta.collidepoint(event.pos):
                            discard(SVDeck, "Geta")
                            counter += 1
                        elif but_haori.collidepoint(event.pos):
                            discard(SVDeck, "Haori")
                            counter += 1
                        elif but_furoshiki.collidepoint(event.pos):
                            discard(SVDeck, "Furoshiki")
                            counter += 1
                        elif but_sandogasa.collidepoint(event.pos):
                            discard(SVDeck, "Sandogasa")
                            counter += 1
                        elif but_netsuke.collidepoint(event.pos):
                            discard(SVDeck, "Netsuke")
                            counter += 1
                        elif but_shikki.collidepoint(event.pos):
                            discard(SVDeck, "Shikki")
                            counter += 1
                        elif but_jubako.collidepoint(event.pos):
                            discard(SVDeck, "Jubako")
                            counter += 1
                        elif but_ukiyoe.collidepoint(event.pos):
                            discard(SVDeck, "Ukiyoe")
                            counter += 1
                        elif but_sumie.collidepoint(event.pos):
                            discard(SVDeck, "Sumie")
                            counter += 1
                        elif but_shamisen.collidepoint(event.pos):
                            discard(SVDeck, "Shamisen")
                            counter += 1
            pygame.display.update()
        return False

    def temple_menu(screen):
        """Temple Menu"""
        global current_player
        paused = True
        while paused:
            screen.fill((255, 255, 255))
            but_1 = Button(DISPLAY_WIDTH / 3 + 50, (DISPLAY_HEIGHT // 3), ((DISPLAY_WIDTH / 3) - 100), 40, screen, green, black)
            but_2 = Button(DISPLAY_WIDTH / 3 + 50, ((DISPLAY_HEIGHT // 3)+ 50), ((DISPLAY_WIDTH / 3) - 100), 40, screen, green, black)
            but_3 = Button(DISPLAY_WIDTH / 3 + 50, ((DISPLAY_HEIGHT // 3)+ 100), ((DISPLAY_WIDTH / 3) - 100), 40, screen, green, black)
            but_4 = Button(DISPLAY_WIDTH / 3 + 50, ((DISPLAY_HEIGHT // 3)+ 150), ((DISPLAY_WIDTH / 3) - 100), 40, screen, green, black)
            but_1.add_text('Temple Donation:')
            but_2.add_text('One Coin')
            but_3.add_text('Two Coins')
            but_4.add_text('Three Coins')
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    quitter()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if but_2.collidepoint(event.pos):
                            current_player = Temple_Loc(current_player, 1)
                            return
                        if but_3.collidepoint(event.pos):
                            current_player = Temple_Loc(current_player, 2)
                            return
                        if but_4.collidepoint(event.pos):
                            current_player = Temple_Loc(current_player, 3)
                            return
            pygame.display.update()
        return False


    # Run Sequence Below
    main_screen(0)
    # results screen()
    quitter()
