#!/usr/bin/python3
"""Main code for Tokaido Nakama"""
import pygame
import pygame_menu
from player import Player
from init import current_player, HSDeck, MDeck, SVDeck, ENCDeck, player_list, GreenPlayer, BluePlayer, YellowPlayer, PurplePlayer, GreyPlayer
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
            update_current_player
        elif board_position in [14, 15, 16, 17, 18, 31, 32, 33, 34, 35, 49, 50, 51, 52, 53, 66, 67, 68, 69, 70]:
            # Code for Inn
            print("Inn stuff")

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

        # Loop to retrieve proper value
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
                    # current_player = GreenPlayer
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
                    # current_player = BluePlayer
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
                    # current_player = GreyPlayer
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
                    # current_player = YellowPlayer
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

    def player_positioning(board_number):
        """Checks player positions & blits pieces"""
        player_list.reverse()
        for player in player_list:
            if board_number == 1:
                if player.board_space == -3:
                    screen.blit(player.icon, (80, 385))
                if player.board_space == -2:
                    screen.blit(player.icon, (80, 336))
                if player.board_space == -1:
                    screen.blit(player.icon, (80, 283))
                if player.board_space == 1:
                    screen.blit(player.icon, (149, 215))
                if player.board_space == 2:
                    screen.blit(player.icon, (195, 213))
                if player.board_space == 3:
                    screen.blit(player.icon, (245, 191))
                if player.board_space == 4:
                    screen.blit(player.icon, (299, 192))
                if player.board_space == 5:
                    screen.blit(player.icon, (360, 218))
                if player.board_space == 6:
                    screen.blit(player.icon, (413, 242))
                if player.board_space == 7:
                    screen.blit(player.icon, (466, 269))
                if player.board_space == 8:
                    screen.blit(player.icon, (512, 309))
                if player.board_space == 9:
                    screen.blit(player.icon, (570, 306))
                if player.board_space == 10:
                    screen.blit(player.icon, (625, 273))
                if player.board_space == 11:
                    screen.blit(player.icon, (664, 237))
                if player.board_space == 12:
                    screen.blit(player.icon, (712, 169))
                if player.board_space == 13:
                    screen.blit(player.icon, (737, 125))
                if player.board_space == 14:
                    screen.blit(player.icon, (801, 376))
                if player.board_space == 15:
                    screen.blit(player.icon, (801, 327))
                if player.board_space == 16:
                    screen.blit(player.icon, (801, 277))
                if player.board_space == 17:
                    screen.blit(player.icon, (801, 227))
                if player.board_space == 18:
                    screen.blit(player.icon, (801, 176))
            elif board_number == 2:
                if player.board_space == 14:
                    screen.blit(player.icon, (48, 350))
                if player.board_space == 15:
                    screen.blit(player.icon, (48, 309))
                if player.board_space == 16:
                    screen.blit(player.icon, (48, 261))
                if player.board_space == 17:
                    screen.blit(player.icon, (48, 217))
                if player.board_space == 18:
                    screen.blit(player.icon, (48, 170))
                if player.board_space == 19:
                    screen.blit(player.icon, (132, 141))
                if player.board_space == 20:
                    screen.blit(player.icon, (180, 162))
                if player.board_space == 21:
                    screen.blit(player.icon, (229, 197))
                if player.board_space == 22:
                    screen.blit(player.icon, (282, 219))
                if player.board_space == 23:
                    screen.blit(player.icon, (334, 250))
                if player.board_space == 24:
                    screen.blit(player.icon, (434, 290))
                if player.board_space == 25:
                    screen.blit(player.icon, (440, 321))
                if player.board_space == 26:
                    screen.blit(player.icon, (496, 374))
                if player.board_space == 27:
                    screen.blit(player.icon, (549, 387))
                if player.board_space == 28:
                    screen.blit(player.icon, (602, 384))
                if player.board_space == 29:
                    screen.blit(player.icon, (659, 384))
                if player.board_space == 30:
                    screen.blit(player.icon, (711, 375))
                if player.board_space == 31:
                    screen.blit(player.icon, (799, 126))
                if player.board_space == 32:
                    screen.blit(player.icon, (799, 170))
                if player.board_space == 33:
                    screen.blit(player.icon, (799, 214))
                if player.board_space == 34:
                    screen.blit(player.icon, (799, 259))
                if player.board_space == 35:
                    screen.blit(player.icon, (799, 304))

        player_list.reverse()
        # for cleanup, maybe make dictionary with board_space(key) and associated coords(value)


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
        # Rect(left, top, width, height)
        # if board_number == 2:
            #rect19 = pygame.Rect(, , ,)
            #rect19_1 = pygame.Rect(, , ,)
            #rect20 = pygame.Rect()
            #rect20_1 = pygame.Rect()
            #rect21 = pygame.Rect()
        # if board_number == 3:

        # if board_number == 4:

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
                                    # append to player list (which will be cleared as player pieces are set)
                                    # if all players on inn:
                                    # food menu.
                        # if board_number == 2:
                            # if
                        # if board_number == 3:
                            # if
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
        while paused:
            screen.fill((255, 255, 255))
            but_1 = Button(DISPLAY_WIDTH / 3 + 50, (DISPLAY_HEIGHT // 3), ((DISPLAY_WIDTH / 3) - 100), 40, screen, green, black)
            but_2 = Button(DISPLAY_WIDTH / 3 + 50, ((DISPLAY_HEIGHT // 3)+ 50), ((DISPLAY_WIDTH / 3) - 100), 40, screen, green, black)
            but_3 = Button(DISPLAY_WIDTH / 3 + 50, ((DISPLAY_HEIGHT // 3) + 100), ((DISPLAY_WIDTH / 3) - 100), 40, screen, green, black)
            but_1.add_text('Hot Spring Value:')
            but_2.add_text('2 Points')
            but_3.add_text('3 Points')
            #but_2.draw(black)
            #but_3.draw(black)
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    quitter()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if but_2.collidepoint(event.pos):
                            current_player = Hot_Spring_Loc(current_player, 2)
                            return
                        elif but_3.collidepoint(event.pos):
                            current_player = Hot_Spring_Loc(current_player, 3)
                            return
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
            #but_2.draw(black)
            #but_3.draw(black)
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
            #but_2.draw(black)
            #but_3.draw(black)
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
            #but_2.draw(black)
            #but_3.draw(black)
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
            #but_2.draw(black)
            #but_3.draw(black)
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
            but_anna_mtn = Button(DISPLAY_WIDTH / 3 + 50, ((DISPLAY_HEIGHT // 3) + 100), ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)
            but_anna_sea = Button(DISPLAY_WIDTH / 3 + 50, (DISPLAY_HEIGHT // 3) + 150, ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)

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
            but_miso = Button(DISPLAY_WIDTH / 3 + 50, (DISPLAY_HEIGHT // 3), ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)
            but_dango = Button(DISPLAY_WIDTH / 3 + 50, ((DISPLAY_HEIGHT // 3) + 50), ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)
            but_nigiri = Button(DISPLAY_WIDTH / 3 + 50, (DISPLAY_HEIGHT // 3) + 100, ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)
            but_tempura = Button(DISPLAY_WIDTH / 3 + 50, ((DISPLAY_HEIGHT // 3) + 150), ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)
            but_soba = Button(DISPLAY_WIDTH / 3 + 50, (DISPLAY_HEIGHT // 3) - 50, ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)
            but_yakitori = Button(DISPLAY_WIDTH / 3 + 50, ((DISPLAY_HEIGHT // 3) + 100), ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)
            but_tofu = Button(DISPLAY_WIDTH / 3 + 50, (DISPLAY_HEIGHT // 3) + 150, ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)
            but_sushi = Button(DISPLAY_WIDTH / 3 + 50, (DISPLAY_HEIGHT // 3), ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)
            but_fugu = Button(DISPLAY_WIDTH / 3 + 50, ((DISPLAY_HEIGHT // 3) + 50), ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)
            but_donburi = Button(DISPLAY_WIDTH / 3 + 50, (DISPLAY_HEIGHT // 3) + 100, ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)
            but_sashimi = Button(DISPLAY_WIDTH / 3 + 50, ((DISPLAY_HEIGHT // 3) + 150), ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)
            but_udon = Button(DISPLAY_WIDTH / 3 + 50, (DISPLAY_HEIGHT // 3) - 50, ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)
            but_unagi = Button(DISPLAY_WIDTH / 3 + 50, ((DISPLAY_HEIGHT // 3) + 100), ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)
            but_taimeshi = Button(DISPLAY_WIDTH / 3 + 50, (DISPLAY_HEIGHT // 3) + 150, ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)

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
            but_taimeshi.add_test('Tai Meshi')

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
            but_hashi = Button(DISPLAY_WIDTH / 3 + 50, ((DISPLAY_HEIGHT // 3) + 100), ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)
            but_konpeito = Button(DISPLAY_WIDTH / 3 + 50, (DISPLAY_HEIGHT // 3) + 150, ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)
            but_kamaboko = Button(DISPLAY_WIDTH / 3 + 50, (DISPLAY_HEIGHT // 3), ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)
            but_manju = Button(DISPLAY_WIDTH / 3 + 50, ((DISPLAY_HEIGHT // 3) + 50), ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)
            but_daifuku = Button(DISPLAY_WIDTH / 3 + 50, (DISPLAY_HEIGHT // 3) + 100, ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)
            but_ocha = Button(DISPLAY_WIDTH / 3 + 50, ((DISPLAY_HEIGHT // 3) + 150), ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)
            but_sake = Button(DISPLAY_WIDTH / 3 + 50, (DISPLAY_HEIGHT // 3) - 50, ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)
            but_yukata = Button(DISPLAY_WIDTH / 3 + 50, ((DISPLAY_HEIGHT // 3) + 100), ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)
            but_kanzashi = Button(DISPLAY_WIDTH / 3 + 50, (DISPLAY_HEIGHT // 3) + 150, ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)
            but_geta = Button(DISPLAY_WIDTH / 3 + 50, (DISPLAY_HEIGHT // 3), ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)
            but_haori = Button(DISPLAY_WIDTH / 3 + 50, ((DISPLAY_HEIGHT // 3) + 50), ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)
            but_furoshiki = Button(DISPLAY_WIDTH / 3 + 50, (DISPLAY_HEIGHT // 3) + 100, ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)
            but_sandogasa = Button(DISPLAY_WIDTH / 3 + 50, ((DISPLAY_HEIGHT // 3) + 150), ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)
            but_netsuke = Button(DISPLAY_WIDTH / 3 + 50, (DISPLAY_HEIGHT // 3) - 50, ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)
            but_shikki = Button(DISPLAY_WIDTH / 3 + 50, ((DISPLAY_HEIGHT // 3) + 100), ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)
            but_jubako = Button(DISPLAY_WIDTH / 3 + 50, (DISPLAY_HEIGHT // 3), ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)
            but_ukiyoe = Button(DISPLAY_WIDTH / 3 + 50, ((DISPLAY_HEIGHT // 3) + 50), ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)
            but_sumie = Button(DISPLAY_WIDTH / 3 + 50, (DISPLAY_HEIGHT // 3) + 100, ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)
            but_shamisen = Button(DISPLAY_WIDTH / 3 + 50, ((DISPLAY_HEIGHT // 3) + 150), ((DISPLAY_WIDTH / 3) - 100), 40, screen, green)

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
            #but_2.draw(black)
            #but_3.draw(black)
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
