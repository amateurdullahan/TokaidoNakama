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
        elif board_position in [14, 15, 16, 17, 18, 31, 32, 33, 34, 35, 49, 50, 51, 52, 53, 66, 67, 68, 69, 70]:
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


    # Font Section
    def title_selector(current_player):
        """Changes title for current player"""

        # Player Colors & Associated RGB values
        colors_rgb = {
        "Green": (73, 114, 16),
        "Blue": (122, 165, 184),
        "Yellow": (243, 175, 1),
        "Grey": (145, 147, 156),
        "Purple": (98, 55, 114)
        }

        # Retrieve current player's RGB value
        rgb = colors_rgb.get(current_player.color)
        # for key in colors_rgb:
            # if key == current_player.color:
                # rgb = colors_rgb.get(key)
        # Create title font, first param is font file in pygame, second is size
        font_title = pygame.font.Font('freesansbold.ttf', 50)
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
        btn_svcp_title.add_text("Souvneir Cost", 18)
        btn_svcp_1 = Button(175, 610, 50, 20, screen, black)
        svcp_text = CostProb(SVDeck)
        btn_svcp_1.add_text("1 Coin " + str(svcp_text[0]) + "%", 16)
        btn_svcp_2 = Button(175, 630, 50, 20, screen, black)
        btn_svcp_2.add_text("2 Coin " + str(svcp_text[1]) + "%", 16)
        btn_svcp_3 = Button(175, 650, 50, 20, screen, black)
        btn_svcp_3.add_text("3 Coin " + str(svcp_text[2]) + "%", 16)
        # Builds Souvenir Subtype Display
        btn_svsp_title = Button(175, 675, 50, 25, screen, black)
        btn_svsp_title.add_text("Souvneir Type", 18)
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
        # player 1 score display
        btn_player_1_title = Button(725, 585, 50, 25, screen, black)
        btn_player_1_title.add_text(str(player_list[0].color))
        btn_player_1_score = Button(750, 625, 50, 25, screen, black)
        btn_player_1_score.add_text(str(player_list[0].score), 18)
        # player 2 score display
        btn_player_2_title = Button(725, 650, 50, 25, screen, black)
        btn_player_2_title.add_text(str(player_list[1].color))
        btn_player_2_score = Button(750, 690, 50, 25, screen, black)
        btn_player_2_score.add_text(str(player_list[1].score), 18)
        # player 3 score display
        btn_player_3_title = Button(725, 715, 50, 25, screen, black)
        btn_player_3_title.add_text(str(player_list[2].color))
        btn_player_3_score = Button(750, 755, 50, 25, screen, black)
        btn_player_3_score.add_text(str(player_list[2].score), 18)

    # Creates list in order of players, at limit goes into main screen
    def player_add(player_color):   # button fun
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
                # Hides it off the surface. Could just change color like below:
                # green_button.set_background_color((73, 114, 16))
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
            print(player_list)
            print('THIS CODE SHOULD NOT RUN ONCE EVERYTHING IS GOING')
            main_screen(1)

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
    # Hot Springs Menu

    # Player space dictionaries, by board number, so inn spaces are blitted(sp?) correctly
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
            # elif board_number == 4:
                # loc = spaces_b4.get(player.board_space)
            print("Line 364:", loc)
            screen.blit(player.icon, loc)
        player_list.reverse()

    # Main Game Loop
    def main_screen(board_number):
        """Main game loop"""
        global current_player

        # Flag for Updating Screen. Flagged at main loop startup for each board section & after selecting a board space.
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
            # rect 11 is additional rect for position 1
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
            # start_list = [0.1, 0.2, 0.3] CORRECT
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
        # if board_number == 3:
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
        # if board_number == 4:

        # For Cleanup:
        # Function that takes in number and 4 coordinates,
        # that makes rect with our naming convention
        print(current_player.color)
        running = True  # Main Loop Flag
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
                                            main_screen(4)
                                    update_current_player()
                                    screen_update = 1
                            
                        

                        # if board_number == 4:
                            # if
                # Shows list of events on ya terminal. To be removed, but fun to seeprint(event)
                print(event)

            # hopefully fixes start_menu (spoiler alert: it didn't, but it works now)
            if start_menu.is_enabled():
                start_menu.update(events)
                start_menu.draw(screen)

            # Only update screen if needed
            if screen_update == 1:
                # Filling screen
                screen.fill(white)

                # Render title text & rect
                title_selector(current_player)
                score_prob_display()
                # Call Board Function
                board(X_BOARD_COORD, Y_BOARD_COORD, board_number)

                # Piece Space Function
                player_positioning(board_number)
                print("Update")
                # After all screen items are blitted(sp?), update dat screen
                pygame.display.update()
            # Reset Flag
            screen_update = 0
            # If All Players At Inn
            # Call Food Menu
            # Then From Food Menu Call main_screen(NEXT BOARD NUMBER)


    # 900, 800
    # 400, 420
    def hot_springs_menu(screen):
        """Hot Spring Menu"""
        global current_player
        paused = True
        hs_screen_flag = 1
        text_select = pygame.font.Font('freesansbold.ttf', 50)
        text_select_r = text_select.render('Select Card:', True, black)
        text_select_rect = text_select_r.get_rect()
        text_select_rect.center = (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT * .20)
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
            if hs_screen_flag == 1:
                screen.fill((255, 255, 255))
                screen.blit(text_select_r, text_select_rect)
                screen.blit(hs_2, hs_2_rect)
                print("SCREEN UPDATE")
                screen.blit(hs_3, hs_3_rect)
                hs_screen_flag = 0
                pygame.display.update()
        return False

    # farm screen
    def farm_menu(screen):
        """farm screen"""
        global current_player
        paused = True
        while paused:
            screen.fill((255, 255, 255))
            but_1 = Button(DISPLAY_WIDTH / 3 + 50, (DISPLAY_HEIGHT // 3), ((DISPLAY_WIDTH / 3) - 100), 40, screen, green, black)
            but_2 = Button(DISPLAY_WIDTH / 3 + 50, ((DISPLAY_HEIGHT // 3)+ 50), ((DISPLAY_WIDTH / 3) - 100), 40, screen, green, black)
            but_1.add_text('Farm: Collect 3 Coins')
            but_2.add_text('Okay')
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    quitter()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if but_2.collidepoint(event.pos):
                            current_player = Farm_Loc(current_player)
                            return
            pygame.display.update()
        return False

    def pano_paddy_menu(screen):
        """Panorama Paddy Menu"""
        global current_player
        paused = True
        while paused:
            screen.fill((255, 255, 255))
            but_1 = Button(DISPLAY_WIDTH / 3 + 50, (DISPLAY_HEIGHT // 3), ((DISPLAY_WIDTH / 3) - 100), 40, screen, green, black)
            but_2 = Button(DISPLAY_WIDTH / 3 + 50, ((DISPLAY_HEIGHT // 3)+ 50), ((DISPLAY_WIDTH / 3) - 100), 40, screen, green, black)
            but_1.add_text('Panorama: Paddy')
            but_2.add_text('Okay')
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    quitter()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if but_2.collidepoint(event.pos):
                            current_player = Pano_Paddy_Loc(current_player)
                            return
            pygame.display.update()
        return False

    def pano_mt_menu(screen):
        """Panorama Mountain Menu"""
        global current_player
        paused = True
        while paused:
            screen.fill((255, 255, 255))
            but_1 = Button(DISPLAY_WIDTH / 3 + 50, (DISPLAY_HEIGHT // 3), ((DISPLAY_WIDTH / 3) - 100), 40, screen, green, black)
            but_2 = Button(DISPLAY_WIDTH / 3 + 50, ((DISPLAY_HEIGHT // 3)+ 50), ((DISPLAY_WIDTH / 3) - 100), 40, screen, green, black)
            but_1.add_text('Panorama: Mountain')
            but_2.add_text('Okay')
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    quitter()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if but_2.collidepoint(event.pos):
                            current_player = Pano_Mt_Loc(current_player)
                            return
            pygame.display.update()
        return False

    def pano_sea_menu(screen):
        """Panorama Sea Menu"""
        global current_player
        paused = True
        while paused:
            screen.fill((255, 255, 255))
            but_1 = Button(DISPLAY_WIDTH / 3 + 50, (DISPLAY_HEIGHT // 3), ((DISPLAY_WIDTH / 3) - 100), 40, screen, green, black)
            but_2 = Button(DISPLAY_WIDTH / 3 + 50, ((DISPLAY_HEIGHT // 3)+ 50), ((DISPLAY_WIDTH / 3) - 100), 40, screen, green, black)
            but_1.add_text('Panorama: Sea')
            but_2.add_text('Okay')
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    quitter()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if but_2.collidepoint(event.pos):
                            current_player = Pano_Sea_Loc(current_player)
                            return
            pygame.display.update()
        return False

    def encounter_menu(screen):
        """Encounter Menu"""
        global current_player
        paused = True
        while paused:
            screen.fill((255, 255, 255))
            but_kuge = Button(DISPLAY_WIDTH / 3 + 50, (DISPLAY_HEIGHT // 3), ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)
            but_miko = Button(DISPLAY_WIDTH / 3 + 50, ((DISPLAY_HEIGHT // 3) + 50), ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)
            but_samurai = Button(DISPLAY_WIDTH / 3 + 50, (DISPLAY_HEIGHT // 3) + 100, ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)
            but_shokunin = Button(DISPLAY_WIDTH / 3 + 50, ((DISPLAY_HEIGHT // 3) + 150), ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)
            but_anna_pad = Button(DISPLAY_WIDTH / 3 + 50, (DISPLAY_HEIGHT // 3) - 50, ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)
            but_anna_mtn = Button(DISPLAY_WIDTH / 3 + 50, ((DISPLAY_HEIGHT // 3) - 100), ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)
            but_anna_sea = Button(DISPLAY_WIDTH / 3 + 50, (DISPLAY_HEIGHT // 3) - 150, ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)

            but_kuge.add_text('Kuge')
            but_miko.add_text('Miko')
            but_samurai.add_text('Samurai')
            but_shokunin.add_text('Shokunin')
            but_anna_pad.add_text('Annaibito: Paddy')
            but_anna_mtn.add_text('Annaibito: Mountain')
            but_anna_sea.add_text('Annaibito: Sea')

            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    quitter()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if but_kuge.collidepoint(event.pos):
                            current_player = Encounter_Loc(current_player, "Kuge")
                            return
                        elif but_miko.collidepoint(event.pos):
                            current_player = Encounter_Loc(current_player, "Miko")
                            return
                        elif but_samurai.collidepoint(event.pos):
                            current_player = Encounter_Loc(current_player, "Samurai")
                            return
                        elif but_shokunin.collidepoint(event.pos):
                            current_player = Encounter_Loc(current_player, "Shokunin")
                            return
                        elif but_anna_pad.collidepoint(event.pos):
                            current_player = Encounter_Loc(current_player, "Annaibito: Paddy")
                            return
                        elif but_anna_mtn.collidepoint(event.pos):
                            current_player = Encounter_Loc(current_player, "Annaibito: Mountain")
                            return
                        elif but_anna_sea.collidepoint(event.pos):
                            current_player = Encounter_Loc(current_player, "Annaibito: Sea")
                            return
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
