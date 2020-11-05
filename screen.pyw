#!/usr/bin/python3
"""Main code for Tokaido Nakama"""
import pygame
import pygame_menu
from player import Player
from init import current_player, HSDeck, MDeck, SVDeck, ENCDeck, player_list, GreenPlayer, BluePlayer, YellowPlayer, PurplePlayer, GreyPlayer, board_1_list, board_2_list, board_3_list, board_4_list
from location import *
from buttons import Button
from deck import Deck
from operator import attrgetter

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
    pink = (213, 123, 169)
    light_blue = (64, 202, 187)
    red = (243, 0, 0)

    # Title and Icon
    pygame.display.set_caption("Tokaido Nakama")
    icon = pygame.image.load('media/cherrytreeicon.png')
    pygame.display.set_icon(icon)

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

    # Calls correct function with board_position, based off board_position.
    def encounter_selection(board_position):
        """Generates drop down menu / contextual menu based off encounter chosen."""

        if board_position in [1, 8, 29, 37, 48, 57, 65]:
            # Code for Villages Menu & updating stuff
            print("Village stuff")
            completion = village_menu(screen)
            if completion is True:
                update_current_player()
                return True
            return False
        elif board_position in [2, 9, 20, 25, 44, 55]:
            # Code for Temples Menu & updating stuff
            print("Temple stuff")
            completion = temple_menu(screen)
            if completion is True:
                update_current_player()
                return True
            return False
        elif board_position in [3, 10, 24, 38, 46, 56, 61]:
            # Code for Encounter Menu & updating stuff
            print("Encounter stuff")
            completion = encounter_menu(screen)
            if completion is True:
                update_current_player()
                return True
            return False
        elif board_position in [4, 22, 36, 43, 63]:
            # Code for Pano_Paddy
            print("Pano paddy stuff")
            completion = pano_paddy_menu(screen)
            if completion is True:
                update_current_player()
                return True
            return False
        elif board_position in [5, 13, 26, 41, 54, 60]:
            # Code for Hot Springs
            print("Hot spring stuff")
            # Menu returns true if an action was completed
            completion = hot_springs_menu(screen)
            # Update only if completion of turn. This block can be moved to end of function to 
            # save redundancy once all menus are switched to this return style.
            if completion is True:
                update_current_player()
                return True
            return False
        elif board_position in [6, 12, 23, 27, 40, 62]:
            # Code for Pano_Mt
            print("Pano mt stuff")
            completion = pano_mt_menu(screen)
            if completion is True:
                update_current_player()
                return True
            return False
        elif board_position in [7, 21, 30, 39, 45, 59]:
            # Code for Farm
            print("Farm stuff")
            completion = farm_menu(screen)
            if completion is True:
                update_current_player()
                return True
            return False
        elif board_position in [11, 19, 28, 42, 47, 58, 64]:
            # Code for Pano_Sea
            print("Pano sea stuff")
            completion = pano_sea_menu(screen)
            if completion is True:
                update_current_player()
                return True
            return False
        elif board_position in [14, 15, 16, 17, 18, 31, 32, 33, 34, 35, 49, 50, 51, 52, 53, 66,
                                67, 68, 69, 70]:
            # Code for Inn
            print("Inn stuff")
            completion = inn_menu(screen)
            if completion is True:
                update_current_player()
                return True
            return False

    # Checks for & updates current player.
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

    # Text for turn indicator
    def title_selector(current_player):
        """Changes title for current player"""
        # Retrieve current player's RGB value
        rgb = colors_rgb.get(current_player.color)
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

    # Probabilities & score displays
    def score_prob_display():
        """Updates player scores & all probabilities."""
        from probability import CostProb, PointProb, EncTypeProb, SubTypeProb
        # Builds Meal Cost Display
        btn_mcp_title = Button(0, 585, 50, 25, screen, red)
        btn_mcp_title.add_text("Meal Cost", 18)
        btn_mcp_1 = Button(0, 610, 50, 20, screen, black)
        mcp_text = CostProb(MDeck)
        btn_mcp_1.add_text("1 Coin " + str(mcp_text[0]) + "%", 16)
        btn_mcp_2 = Button(0, 630, 50, 20, screen, black)
        btn_mcp_2.add_text("2 Coin " + str(mcp_text[1]) + "%", 16)
        btn_mcp_3 = Button(0, 650, 50, 20, screen, black)
        btn_mcp_3.add_text("3 Coin " + str(mcp_text[2]) + "%", 16)
        # Hot Springs Point Display
        btn_hsp_title = Button(0, 675, 50, 25, screen, light_blue)
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
        btn_entp_title = Button(350, 585, 50, 25, screen, pink)
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
                player_green.icon = pygame.image.load('media/player_green.png')
                green_button.set_position(1000, 1000)
                if len(player_list) == 3:
                    start_menu.disable()
                    main_screen(1)
            elif player_color == 'Blue' and 'player_blue' not in player_list:
                player_blue = BluePlayer
                player_list.append(player_blue)
                player_blue.icon = pygame.image.load('media/player_blue.png')
                blue_button.set_position(1000, 1000)
                if len(player_list) == 3:
                    start_menu.disable()
                    main_screen(1)
            elif player_color == 'Grey' and 'player_grey' not in player_list:
                player_grey = GreyPlayer
                player_list.append(player_grey)
                player_grey.icon = pygame.image.load('media/player_grey.png')
                grey_button.set_position(1000, 1000)
                if len(player_list) == 3:
                    start_menu.disable()
                    main_screen(1)
            elif player_color == 'Yellow' and 'player_yellow' not in player_list:
                player_yellow = YellowPlayer
                player_list.append(player_yellow)
                player_yellow.icon = pygame.image.load('media/player_yellow.png')
                yellow_button.set_position(1000, 1000)
                if len(player_list) == 3:
                    start_menu.disable()
                    main_screen(1)
            elif player_color == 'Purple' and 'player_purple' not in player_list:
                player_purple = PurplePlayer
                player_list.append(player_purple)
                player_purple.icon = pygame.image.load('media/player_purple.png')
                purple_button.set_position(1000, 1000)
                if len(player_list) == 3:
                    start_menu.disable()
                    main_screen(1)
        else:
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
                 24: (400, 290), 25: (440, 321), 26: (496, 374), 27: (549, 387), 28: (602, 384),
                 29: (659, 384), 30: (711, 375), 31: (799, 126), 32: (799, 170), 33: (799, 214),
                 34: (799, 259), 35: (799, 304)}
    spaces_b3 = {31: (53, 113), 32: (53, 155), 33: (53, 199), 34: (53, 244), 35: (53, 290),
                 36: (134, 333), 37: (180, 324), 38: (229, 325), 39: (287, 310), 40: (335, 304),
                 41: (381, 286), 42: (440, 250), 43: (484, 226), 44: (533, 213), 45: (577, 191),
                 46: (625, 161), 47: (666, 127), 48: (716, 121), 49: (795, 343), 50: (795, 299),
                 51: (795, 253), 52: (795, 210), 53: (795, 167)}
    spaces_b4 = {49: (60, 116), 50: (60, 161), 51: (60, 207), 52: (60, 252), 53: (60, 298),
                 54: (133, 337), 55: (180, 326), 56: (223, 302), 57: (269, 284), 58: (307, 258),
                 59: (357, 239), 60: (406, 214), 61: (455, 211), 62: (507, 204), 63: (560, 213),
                 64: (619, 207), 65: (680, 166), 66: (766, 341), 67: (766, 296), 68: (766, 251),
                 69: (766, 205), 70: (766, 159)}

    def player_positioning(board_number):
        """Checks player positions & blits pieces"""

        # Ascend flag is for inns with ascending spaces. Helps for blit order at inns
        ascend = False
        for player in player_list:
            if player.board_space in [31, 32, 33, 34, 35]:
                ascend = True
            elif player.board_space in [49, 50, 51, 52, 53] and board_number == 4:
                ascend = True
        # Player list sorted by player attribute board_space, reverse for descending order
        if ascend is True:
            blit_player_list = sorted(player_list, key=attrgetter("board_space"))
        else:
            blit_player_list = sorted(player_list, key=attrgetter("board_space"), reverse=True)
        for player in blit_player_list:
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


    # Main Game Loop
    def main_screen(board_number):
        """Main game loop"""

        global current_player
        # Flag for Updating Screen. Flagged at startup for each
        # board section & after selecting a board space.
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
        # Function that takes in number and 4 coordinates,
        # that makes rect with our naming convention ??!?

        # Outer loop flag
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
                                    enc_cont = encounter_selection(1)
                                    if enc_cont is True:
                                        current_player.board_space = 1
                                        update_current_player()
                                    screen_update = 1
                            if rect2.collidepoint(event.pos) or rect2_1.collidepoint(event.pos):
                                if current_player.board_space < 2:
                                    print('Temple selected.')
                                    enc_cont = encounter_selection(2)
                                    if enc_cont is True:
                                        current_player.board_space = 2
                                        update_current_player()
                                    screen_update = 1
                            if rect3.collidepoint(event.pos) or rect3_1.collidepoint(event.pos):
                                if current_player.board_space < 3:
                                    print('Encounter selected.')
                                    enc_cont = encounter_selection(3)
                                    if enc_cont is True:
                                        current_player.board_space = 3
                                        update_current_player()
                                    screen_update = 1
                            if rect4.collidepoint(event.pos) or rect4_1.collidepoint(event.pos):
                                if current_player.board_space < 4:
                                    print('Panorama: Paddy selected.')
                                    enc_cont = encounter_selection(4)
                                    if enc_cont is True:
                                        current_player.board_space = 4
                                        update_current_player()
                                    screen_update = 1
                            if rect5.collidepoint(event.pos) or rect5_1.collidepoint(event.pos):
                                if current_player.board_space < 5:
                                    print('Hot Springs selected.')
                                    enc_cont = encounter_selection(5)
                                    if enc_cont is True:
                                        current_player.board_space = 5
                                        update_current_player()
                                    screen_update = 1
                            if rect6.collidepoint(event.pos) or rect6_1.collidepoint(event.pos):
                                if current_player.board_space < 6:
                                    print('Panorama: Mt selected.')
                                    enc_cont = encounter_selection(6)
                                    if enc_cont is True:
                                        current_player.board_space = 6
                                        update_current_player()
                                    screen_update = 1
                            if rect7.collidepoint(event.pos) or rect7_1.collidepoint(event.pos):
                                if current_player.board_space < 7:
                                    print('Farm selected.')
                                    enc_cont = encounter_selection(7)
                                    if enc_cont is True:
                                        current_player.board_space = 7
                                        update_current_player()
                                    screen_update = 1
                            if rect8.collidepoint(event.pos) or rect8_1.collidepoint(event.pos):
                                if current_player.board_space < 8:
                                    print('Village selected.')
                                    enc_cont = encounter_selection(8)
                                    if enc_cont is True:
                                        current_player.board_space = 8
                                        update_current_player()
                                    screen_update = 1
                            if rect9.collidepoint(event.pos) or rect9_1.collidepoint(event.pos):
                                if current_player.board_space < 9:
                                    print('Temple selected.')
                                    enc_cont = encounter_selection(9)
                                    if enc_cont is True:
                                        current_player.board_space = 9
                                        update_current_player()
                                    screen_update = 1
                            if rect10.collidepoint(event.pos) or rect10_1.collidepoint(event.pos):
                                if current_player.board_space < 10:
                                    print('Encounter selected.')
                                    enc_cont = encounter_selection(10)
                                    if enc_cont is True:
                                        current_player.board_space = 10
                                        update_current_player()
                                    screen_update = 1
                            if rect11.collidepoint(event.pos) or rect11_1.collidepoint(event.pos):
                                if current_player.board_space < 11:
                                    print('Panorama: Sea selected.')
                                    enc_cont = encounter_selection(11)
                                    if enc_cont is True:
                                        current_player.board_space = 11
                                        update_current_player()
                                    screen_update = 1
                            if rect12.collidepoint(event.pos) or rect12_1.collidepoint(event.pos):
                                if current_player.board_space < 12:
                                    print('Panorama: Mountain selected.')
                                    enc_cont = encounter_selection(12)
                                    if enc_cont is True:
                                        current_player.board_space = 12
                                        update_current_player()
                                    screen_update = 1
                            if rect13.collidepoint(event.pos) or rect13_1.collidepoint(event.pos):
                                if current_player.board_space < 13:
                                    print('Hot Spring selected.')
                                    enc_cont = encounter_selection(13)
                                    if enc_cont is True:
                                        current_player.board_space = 13
                                        update_current_player()
                                    screen_update = 1
                            if rect14.collidepoint(event.pos) or rect14_1.collidepoint(event.pos):
                                if current_player.board_space < 14:
                                    print('We\'re INN IT NOW BOYS')
                                    enc_cont = encounter_selection(14)
                                    if enc_cont is True:
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
                                    enc_cont = encounter_selection(19)
                                    if enc_cont is True:
                                        current_player.board_space = 19
                                        update_current_player()
                                    screen_update = 1
                            if rect20.collidepoint(event.pos) or rect20_1.collidepoint(event.pos):
                                if current_player.board_space < 20:
                                    print('Temple selected.')
                                    enc_cont = encounter_selection(20)
                                    if enc_cont is True:
                                        current_player.board_space = 20
                                        update_current_player()
                                    screen_update = 1
                            if rect21.collidepoint(event.pos) or rect21_1.collidepoint(event.pos):
                                if current_player.board_space < 21:
                                    print('Farm selected.')
                                    enc_cont = encounter_selection(21)
                                    if enc_cont is True:
                                        current_player.board_space = 21
                                        update_current_player()
                                    screen_update = 1
                            if rect22.collidepoint(event.pos) or rect22_1.collidepoint(event.pos):
                                if current_player.board_space < 22:
                                    print('Panorama: Paddy selected.')
                                    enc_cont = encounter_selection(22)
                                    if enc_cont is True:
                                        current_player.board_space = 22
                                        update_current_player()
                                    screen_update = 1
                            if rect23.collidepoint(event.pos) or rect23_1.collidepoint(event.pos):
                                if current_player.board_space < 23:
                                    print('Panorama: Mountain selected.')
                                    enc_cont = encounter_selection(23)
                                    if enc_cont is True:
                                        current_player.board_space = 23
                                        update_current_player()
                                    screen_update = 1
                            if rect24.collidepoint(event.pos) or rect24_1.collidepoint(event.pos):
                                if current_player.board_space < 24:
                                    print('Encounter selected.')
                                    enc_cont = encounter_selection(24)
                                    if enc_cont is True:
                                        current_player.board_space = 24
                                        update_current_player()
                                    screen_update = 1
                            if rect25.collidepoint(event.pos) or rect25_1.collidepoint(event.pos):
                                if current_player.board_space < 25:
                                    print('Temple selected.')
                                    enc_cont = encounter_selection(25)
                                    if enc_cont is True:
                                        current_player.board_space = 25
                                        update_current_player()
                                    screen_update = 1
                            if rect26.collidepoint(event.pos) or rect26_1.collidepoint(event.pos):
                                if current_player.board_space < 26:
                                    print('Hot Spring selected.')
                                    enc_cont = encounter_selection(26)
                                    if enc_cont is True:
                                        current_player.board_space = 26
                                        update_current_player()
                                    screen_update = 1
                            if rect27.collidepoint(event.pos) or rect27_1.collidepoint(event.pos):
                                if current_player.board_space < 27:
                                    print('Panorama: Mountain selected.')
                                    enc_cont = encounter_selection(27)
                                    if enc_cont is True:
                                        current_player.board_space = 27
                                        update_current_player()
                                    screen_update = 1
                            if rect28.collidepoint(event.pos) or rect28_1.collidepoint(event.pos):
                                if current_player.board_space < 28:
                                    print('Panorama: Sea selected.')
                                    enc_cont = encounter_selection(28)
                                    if enc_cont is True:
                                        current_player.board_space = 28
                                        update_current_player()
                                    screen_update = 1
                            if rect29.collidepoint(event.pos) or rect29_1.collidepoint(event.pos):
                                if current_player.board_space < 29:
                                    print('Village selected.')
                                    enc_cont = encounter_selection(29)
                                    if enc_cont is True:
                                        current_player.board_space = 29
                                        update_current_player()
                                    screen_update = 1
                            if rect30.collidepoint(event.pos) or rect30_1.collidepoint(event.pos):
                                if current_player.board_space < 30:
                                    print('Farm selected.')
                                    enc_cont = encounter_selection(30)
                                    if enc_cont is True:
                                        current_player.board_space = 30
                                        update_current_player()
                                    screen_update = 1
                            if rect31.collidepoint(event.pos) or rect31_1.collidepoint(event.pos):
                                if current_player.board_space < 51:
                                    print('We\'re INN IT NOW BOYS')
                                    enc_cont = encounter_selection(31)
                                    if enc_cont is True:
                                        if board_number == 2:
                                            if len(board_2_list) == 0:
                                                current_player.board_space = 35
                                                board_2_list.append(current_player)
                                            elif len(board_2_list) == 1:
                                                current_player.board_space = 34
                                                board_2_list.append(current_player)
                                            elif len(board_2_list) == 2:
                                                current_player.board_space = 33
                                                board_2_list.append(current_player)
                                                update_current_player()
                                                running = False
                                                main_screen(3)
                                        update_current_player()
                                    screen_update = 1
                        if board_number == 3:
                            if rect36.collidepoint(event.pos) or rect36_1.collidepoint(event.pos):
                                if current_player.board_space < 36:
                                    print('Panorama: Paddy selected.')
                                    enc_cont = encounter_selection(36)
                                    if enc_cont is True:
                                        current_player.board_space = 36
                                        update_current_player()
                                    screen_update = 1
                            if rect37.collidepoint(event.pos) or rect37_1.collidepoint(event.pos):
                                if current_player.board_space < 37:
                                    print('Village selected.')
                                    enc_cont = encounter_selection(37)
                                    if enc_cont is True:
                                        current_player.board_space = 37
                                        update_current_player()
                                    screen_update = 1
                            if rect38.collidepoint(event.pos) or rect38_1.collidepoint(event.pos):
                                if current_player.board_space < 38:
                                    print('Encounter selected.')
                                    enc_cont = encounter_selection(38)
                                    if enc_cont is True:
                                        current_player.board_space = 38
                                        update_current_player()
                                    screen_update = 1
                            if rect39.collidepoint(event.pos) or rect39_1.collidepoint(event.pos):
                                if current_player.board_space < 39:
                                    print('Farm selected.')
                                    enc_cont = encounter_selection(39)
                                    if enc_cont is True:
                                        current_player.board_space = 39
                                        update_current_player()
                                    screen_update = 1
                            if rect40.collidepoint(event.pos) or rect40_1.collidepoint(event.pos):
                                if current_player.board_space < 40:
                                    print('Panorama: Mountain selected.')
                                    enc_cont = encounter_selection(40)
                                    if enc_cont is True:
                                        current_player.board_space = 40
                                        update_current_player()
                                    screen_update = 1
                            if rect41.collidepoint(event.pos) or rect41_1.collidepoint(event.pos):
                                if current_player.board_space < 41:
                                    print('Hot Spring selected.')
                                    enc_cont = encounter_selection(41)
                                    if enc_cont is True:
                                        current_player.board_space = 41
                                        update_current_player()
                                    screen_update = 1
                            if rect42.collidepoint(event.pos) or rect42_1.collidepoint(event.pos):
                                if current_player.board_space < 42:
                                    print('Panorama: Sea selected.')
                                    enc_cont = encounter_selection(42)
                                    if enc_cont is True:
                                        current_player.board_space = 42
                                        update_current_player()
                                    screen_update = 1
                            if rect43.collidepoint(event.pos) or rect43_1.collidepoint(event.pos):
                                if current_player.board_space < 43:
                                    print('Panorama: Paddy selected.')
                                    enc_cont = encounter_selection(43)
                                    if enc_cont is True:
                                        current_player.board_space = 43
                                        update_current_player()
                                    screen_update = 1
                            if rect44.collidepoint(event.pos) or rect44_1.collidepoint(event.pos):
                                if current_player.board_space < 44:
                                    print('Temple selected.')
                                    enc_cont = encounter_selection(44)
                                    if enc_cont is True:
                                        current_player.board_space = 44
                                        update_current_player()
                                    screen_update = 1
                            if rect45.collidepoint(event.pos) or rect45_1.collidepoint(event.pos):
                                if current_player.board_space < 45:
                                    print('Farm selected.')
                                    enc_cont = encounter_selection(45)
                                    if enc_cont is True:
                                        current_player.board_space = 45
                                        update_current_player()
                                    screen_update = 1
                            if rect46.collidepoint(event.pos) or rect46_1.collidepoint(event.pos):
                                if current_player.board_space < 46:
                                    print('Encounter selected.')
                                    enc_cont = encounter_selection(46)
                                    if enc_cont is True:
                                        current_player.board_space = 46
                                        update_current_player()
                                    screen_update = 1
                            if rect47.collidepoint(event.pos) or rect47_1.collidepoint(event.pos):
                                if current_player.board_space < 47:
                                    print('Panorama: Sea selected.')
                                    enc_cont = encounter_selection(47)
                                    if enc_cont is True:
                                        current_player.board_space = 47
                                        update_current_player()
                                    screen_update = 1
                            if rect48.collidepoint(event.pos) or rect48_1.collidepoint(event.pos):
                                if current_player.board_space < 48:
                                    print('Village selected.')
                                    enc_cont = encounter_selection(48)
                                    if enc_cont is True:
                                        current_player.board_space = 48
                                        update_current_player()
                                    screen_update = 1
                            if rect49.collidepoint(event.pos) or rect49_1.collidepoint(event.pos):
                                if current_player.board_space < 49:
                                    print('We\'re INN IT NOW BOYS')
                                    enc_cont = encounter_selection(49)
                                    if enc_cont is True:
                                        if board_number == 3:
                                            if len(board_3_list) == 0:
                                                current_player.board_space = 53
                                                board_3_list.append(current_player)
                                            elif len(board_3_list) == 1:
                                                current_player.board_space = 52
                                                board_3_list.append(current_player)
                                            elif len(board_3_list) == 2:
                                                current_player.board_space = 51
                                                board_3_list.append(current_player)
                                                update_current_player()
                                                running = False
                                                main_screen(4)
                                        update_current_player()
                                    screen_update = 1
                        if board_number == 4:
                            if rect54.collidepoint(event.pos) or rect54_1.collidepoint(event.pos):
                                if current_player.board_space < 54:
                                    print('Hot Spring selected.')
                                    enc_cont = encounter_selection(54)
                                    if enc_cont is True:
                                        current_player.board_space = 54
                                        update_current_player()
                                    screen_update = 1
                            if rect55.collidepoint(event.pos) or rect55_1.collidepoint(event.pos):
                                if current_player.board_space < 55:
                                    print('Temple selected.')
                                    enc_cont = encounter_selection(55)
                                    if enc_cont is True:
                                        current_player.board_space = 55
                                        update_current_player()
                                    screen_update = 1
                            if rect56.collidepoint(event.pos) or rect56_1.collidepoint(event.pos):
                                if current_player.board_space < 56:
                                    print('Encounter selected.')
                                    enc_cont = encounter_selection(56)
                                    if enc_cont is True:
                                        current_player.board_space = 56
                                        update_current_player()
                                    screen_update = 1
                            if rect57.collidepoint(event.pos) or rect57_1.collidepoint(event.pos):
                                if current_player.board_space < 57:
                                    print('Village selected.')
                                    enc_cont = encounter_selection(57)
                                    if enc_cont is True:
                                        current_player.board_space = 57
                                        update_current_player()
                                    screen_update = 1
                            if rect58.collidepoint(event.pos) or rect58_1.collidepoint(event.pos):
                                if current_player.board_space < 58:
                                    print('Panorama: Sea selected.')
                                    enc_cont = encounter_selection(58)
                                    if enc_cont is True:
                                        current_player.board_space = 58
                                        update_current_player()
                                    screen_update = 1
                            if rect59.collidepoint(event.pos) or rect59_1.collidepoint(event.pos):
                                if current_player.board_space < 59:
                                    print('Farm selected.')
                                    enc_cont = encounter_selection(59)
                                    if enc_cont is True:
                                        current_player.board_space = 59
                                        update_current_player()
                                    screen_update = 1
                            if rect60.collidepoint(event.pos) or rect60_1.collidepoint(event.pos):
                                if current_player.board_space < 60:
                                    print('Hot Spring selected.')
                                    enc_cont = encounter_selection(60)
                                    if enc_cont is True:
                                        current_player.board_space = 60
                                        update_current_player()
                                    screen_update = 1
                            if rect61.collidepoint(event.pos) or rect61_1.collidepoint(event.pos):
                                if current_player.board_space < 61:
                                    print('Encounter selected.')
                                    enc_cont = encounter_selection(61)
                                    if enc_cont is True:
                                        current_player.board_space = 61
                                        update_current_player()
                                    screen_update = 1
                            if rect62.collidepoint(event.pos) or rect62_1.collidepoint(event.pos):
                                if current_player.board_space < 62:
                                    print('Panorama: Mountain selected.')
                                    enc_cont = encounter_selection(62)
                                    if enc_cont is True:
                                        current_player.board_space = 62
                                        update_current_player()
                                    screen_update = 1
                            if rect63.collidepoint(event.pos) or rect63_1.collidepoint(event.pos):
                                if current_player.board_space < 63:
                                    print('Panorama: Paddy selected.')
                                    enc_cont = encounter_selection(63)
                                    if enc_cont is True:
                                        current_player.board_space = 63
                                        update_current_player()
                                    screen_update = 1
                            if rect64.collidepoint(event.pos) or rect64_1.collidepoint(event.pos):
                                if current_player.board_space < 64:
                                    print('Panorama: Sea selected.')
                                    enc_cont = encounter_selection(64)
                                    if enc_cont is True:
                                        current_player.board_space = 64
                                        update_current_player()
                                    screen_update = 1
                            if rect65.collidepoint(event.pos) or rect65_1.collidepoint(event.pos):
                                if current_player.board_space < 65:
                                    print('Village selected.')
                                    enc_cont = encounter_selection(65)
                                    if enc_cont is True:
                                        current_player.board_space = 65
                                        update_current_player()
                                    screen_update = 1
                            if rect66.collidepoint(event.pos) or rect66_1.collidepoint(event.pos):
                                if current_player.board_space < 66:
                                    print('We\'re INN IT NOW BOYS')
                                    enc_cont = encounter_selection(66)
                                    if enc_cont is True:
                                        if board_number == 4:
                                            if len(board_4_list) == 0:
                                                current_player.board_space = 70
                                                board_4_list.append(current_player)
                                            elif len(board_4_list) == 1:
                                                current_player.board_space = 69
                                                board_4_list.append(current_player)
                                            elif len(board_4_list) == 2:
                                                current_player.board_space = 68
                                                board_4_list.append(current_player)
                                                update_current_player()
                                                running = False
                                                results_menu(screen)
                                        update_current_player()
                                    screen_update = 1

                # Remove comment below to get list of events to terminal
                # print(event)

            # Endpoint for initialization, aka main_screen(0)
            if start_menu.is_enabled():
                start_menu.update(events)
                start_menu.draw(screen)
                running = False

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
        back_arrow = pygame.image.load('media/arrow_back.png')
        back_arrow_r = back_arrow.get_rect()
        back_arrow_r.center = (DISPLAY_WIDTH * .945, DISPLAY_HEIGHT * .06)
        while paused:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    quitter()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if hs_2_rect.collidepoint(event.pos):
                            current_player = Hot_Spring_Loc(current_player, 2)
                            return True
                        elif hs_3_rect.collidepoint(event.pos):
                            current_player = Hot_Spring_Loc(current_player, 3)
                            return True
                        elif back_arrow_r.collidepoint(event.pos):
                            return False
            if hs_screen_update == 1:
                screen.fill((255, 255, 255))
                screen.blit(text_select_r, text_select_rect)
                screen.blit(back_arrow, back_arrow_r)
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
        farm_sub_text_style = pygame.font.SysFont('Arial', 38)
        farm_collect_text = farm_text_style.render('Farm: Collect 3 Coins!', True, black)
        farm_collect_rect = farm_collect_text.get_rect()
        farm_collect_rect.center = (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT * .2)
        farm_confirmation_text = farm_sub_text_style.render('Click Anywhere To Continue', True, black)
        farm_confirmation_rect = farm_confirmation_text.get_rect()
        farm_confirmation_rect.center = (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT * .7)
        coinpile = pygame.image.load('media/coins_three.png')
        coinpile_rect = coinpile.get_rect()
        coinpile_rect.center = (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT * .45)
        farm_back_arrow = pygame.image.load('media/arrow_back.png')
        farm_back_arrow_r = farm_back_arrow.get_rect()
        farm_back_arrow_r.center = (DISPLAY_WIDTH * .945, DISPLAY_HEIGHT * .06)
        while paused:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    quitter()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if not farm_back_arrow_r.collidepoint(event.pos):
                            current_player = Farm_Loc(current_player)
                            return True
                        elif farm_back_arrow_r.collidepoint(event.pos):
                            return False
            if farm_screen_update == 1:
                screen.fill((255, 255, 255))
                screen.blit(farm_collect_text, farm_collect_rect)
                screen.blit(farm_confirmation_text, farm_confirmation_rect)
                screen.blit(coinpile, coinpile_rect)
                screen.blit(farm_back_arrow, farm_back_arrow_r)
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
        click_text_style = pygame.font.SysFont('Arial', 38)
        paddy_collect_text = paddy_text_style.render('Panorama: Rice Paddy', True, black)
        paddy_collect_rect = paddy_collect_text.get_rect()
        paddy_collect_rect.center = (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT * .2)
        paddy_confirmation_text = click_text_style.render('Click Anywhere To Continue', True, black)
        paddy_confirmation_rect = paddy_confirmation_text.get_rect()
        paddy_confirmation_rect.center = (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT * .7)
        pad_back = pygame.image.load('media/arrow_back.png')
        pad_back_r = pad_back.get_rect()
        pad_back_r.center = (DISPLAY_WIDTH * .945, DISPLAY_HEIGHT * .06)
        while paused:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    quitter()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if not pad_back_r.collidepoint(event.pos):
                            current_player = Pano_Paddy_Loc(current_player)
                            return True
                        elif pad_back_r.collidepoint(event.pos):
                            return False
            if paddy_screen_update == 1:
                screen.fill((255, 255, 255))
                screen.blit(paddy_collect_text, paddy_collect_rect)
                screen.blit(paddy_confirmation_text, paddy_confirmation_rect)
                screen.blit(paddy_cards, paddy_cards_rect)
                screen.blit(pad_back, pad_back_r)
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
        click_text_style = pygame.font.SysFont('Arial', 38)
        mt_collect_text = mt_text_style.render('Panorama: Mountains', True, black)
        mt_collect_rect = mt_collect_text.get_rect()
        mt_collect_rect.center = (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT * .2)
        mt_confirmation_text = click_text_style.render('Click Anywhere To Continue', True, black)
        mt_confirmation_rect = mt_confirmation_text.get_rect()
        mt_confirmation_rect.center = (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT * .7)
        mt_back = pygame.image.load('media/arrow_back.png')
        mt_back_r = mt_back.get_rect()
        mt_back_r.center = (DISPLAY_WIDTH * .945, DISPLAY_HEIGHT * .06)
        while paused:
            screen.fill((255, 255, 255))
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    quitter()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if not mt_back_r.collidepoint(event.pos):
                            current_player = Pano_Mt_Loc(current_player)
                            return True
                        elif mt_back_r.collidepoint(event.pos):
                            return False
            if mt_screen_update == 1:
                screen.fill((255, 255, 255))
                screen.blit(mt_collect_text, mt_collect_rect)
                screen.blit(mt_confirmation_text, mt_confirmation_rect)
                screen.blit(mt_cards, mt_cards_rect)
                screen.blit(mt_back, mt_back_r)
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
        click_text_style = pygame.font.SysFont('Arial', 38)
        sea_collect_text = sea_text_style.render('Panorama: Sea', True, black)
        sea_collect_rect = sea_collect_text.get_rect()
        sea_collect_rect.center = (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT * .2)
        sea_confirmation_text = click_text_style.render('Click Anywhere To Continue', True, black)
        sea_confirmation_rect = sea_confirmation_text.get_rect()
        sea_confirmation_rect.center = (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT * .7)
        sea_back = pygame.image.load('media/arrow_back.png')
        sea_back_r = sea_back.get_rect()
        sea_back_r.center = (DISPLAY_WIDTH * .945, DISPLAY_HEIGHT * .06)
        while paused:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    quitter()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if not sea_back_r.collidepoint(event.pos):
                            current_player = Pano_Sea_Loc(current_player)
                            return True
                        elif sea_back_r.collidepoint(event.pos):
                            return False
            if sea_screen_update == 1:
                screen.fill((255, 255, 255))
                screen.blit(sea_collect_text, sea_collect_rect)
                screen.blit(sea_confirmation_text, sea_confirmation_rect)
                screen.blit(sea_cards, sea_cards_rect)
                screen.blit(sea_back, sea_back_r)
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
        enc_back = pygame.image.load('media/arrow_back.png')
        enc_back_r = enc_back.get_rect()
        enc_back_r.center = (DISPLAY_WIDTH * .945, DISPLAY_HEIGHT * .06)
        enc_dict = {}
        for enc in ENCDeck.card_list:
            if enc.name == 'Shokunin':
                enc_dict[enc_shokunin] = enc_shokunin_rect
            elif enc.name == 'Samurai':
                enc_dict[enc_samurai] = enc_samurai_rect
            elif enc.name == 'Miko':
                enc_dict[enc_miko] = enc_miko_rect
            elif enc.name == 'Kuge':
                enc_dict[enc_kuge] = enc_kuge_rect
            elif enc.name == 'Annaibito: Paddy':
                enc_dict[enc_anna_paddy] = enc_anna_paddy_rect
            elif enc.name == 'Annaibito: Mountain':
                enc_dict[enc_anna_mt] = enc_anna_mt_rect
            elif enc.name == 'Annaibito: Sea':
                enc_dict[enc_anna_sea] = enc_anna_sea_rect
        while paused:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    quitter()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if enc_kuge_rect.collidepoint(event.pos):
                            current_player = Encounter_Loc(current_player, "Kuge")
                            return True
                        elif enc_miko_rect.collidepoint(event.pos):
                            current_player = Encounter_Loc(current_player, "Miko")
                            return True
                        elif enc_samurai_rect.collidepoint(event.pos):
                            current_player = Encounter_Loc(current_player, "Samurai")
                            return True
                        elif enc_shokunin_rect.collidepoint(event.pos):
                            current_player = Encounter_Loc(current_player, "Shokunin")
                            return True
                        elif enc_anna_paddy_rect.collidepoint(event.pos):
                            current_player = Encounter_Loc(current_player, "Annaibito: Paddy")
                            return True
                        elif enc_anna_mt_rect.collidepoint(event.pos):
                            current_player = Encounter_Loc(current_player, "Annaibito: Mountain")
                            return True
                        elif enc_anna_sea_rect.collidepoint(event.pos):
                            current_player = Encounter_Loc(current_player, "Annaibito: Sea")
                            return True
                        elif enc_back_r.collidepoint(event.pos):
                            return False
            if enc_screen_update == 1:
                screen.fill((255, 255, 255))
                screen.blit(enc_select_text, enc_select_rect)
                screen.blit(enc_back, enc_back_r)
                for i in enc_dict:
                    screen.blit(i, enc_dict[i])
                enc_screen_update = 0
                pygame.display.update()
        return False

    def inn_menu(screen):
        """Inn Menu"""
        global current_player
        paused = True
        inn_screen_update = 1
        inn_text_style = pygame.font.SysFont('Arial', 50)
        skip_text_style = pygame.font.SysFont('Arial', 38)
        inn_select_text = inn_text_style.render('Select Meal:', True, black)
        inn_select_text_rect = inn_select_text.get_rect()
        inn_select_text_rect.center = (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT * .2)
        inn_back = pygame.image.load('media/arrow_back.png')
        inn_back_r = inn_back.get_rect()
        inn_back_r.center = (DISPLAY_WIDTH * .945, DISPLAY_HEIGHT * .06)
        meal_skip = skip_text_style.render('Skip Meal', True, black)
        meal_skip_rect = meal_skip.get_rect()
        meal_skip_rect.center = (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT * .8)
        meal_miso = pygame.image.load('media/miso.png')
        meal_miso_rect = meal_miso.get_rect()
        meal_miso_rect.center = (DISPLAY_WIDTH * .5, DISPLAY_HEIGHT * .37)
        meal_dango = pygame.image.load('media/dango.png')
        meal_dango_rect = meal_dango.get_rect()
        meal_dango_rect.center = (DISPLAY_WIDTH * .38, DISPLAY_HEIGHT * .37)
        meal_nigiri = pygame.image.load('media/nigiri.png')
        meal_nigiri_rect = meal_nigiri.get_rect()
        meal_nigiri_rect.center = (DISPLAY_WIDTH * .26, DISPLAY_HEIGHT * .37)
        meal_soba = pygame.image.load('media/soba.png')
        meal_soba_rect = meal_soba.get_rect()
        meal_soba_rect.center = (DISPLAY_WIDTH * .14, DISPLAY_HEIGHT * .37)
        meal_sushi = pygame.image.load('media/sushi.png')
        meal_sushi_rect = meal_sushi.get_rect()
        meal_sushi_rect.center = (DISPLAY_WIDTH * .62, DISPLAY_HEIGHT * .37)
        meal_tempura = pygame.image.load('media/tempura.png')
        meal_tempura_rect = meal_tempura.get_rect()
        meal_tempura_rect.center = (DISPLAY_WIDTH * .74, DISPLAY_HEIGHT * .37)
        meal_tofu = pygame.image.load('media/tofu.png')
        meal_tofu_rect = meal_tofu.get_rect()
        meal_tofu_rect.center = (DISPLAY_WIDTH * .86, DISPLAY_HEIGHT * .37)
        meal_yakitori = pygame.image.load('media/yakitori.png')
        meal_yakitori_rect = meal_yakitori.get_rect()
        meal_yakitori_rect.center = (DISPLAY_WIDTH * .38, DISPLAY_HEIGHT * .6)
        meal_donburi = pygame.image.load('media/donburi.png')
        meal_donburi_rect = meal_donburi.get_rect()
        meal_donburi_rect.center = (DISPLAY_WIDTH * .26, DISPLAY_HEIGHT * .6)
        meal_fugu = pygame.image.load('media/fugu.png')
        meal_fugu_rect = meal_fugu.get_rect()
        meal_fugu_rect.center = (DISPLAY_WIDTH * .14, DISPLAY_HEIGHT * .6)
        meal_sashimi = pygame.image.load('media/sashimi.png')
        meal_sashimi_rect = meal_sashimi.get_rect()
        meal_sashimi_rect.center = (DISPLAY_WIDTH * .5, DISPLAY_HEIGHT * .6)
        meal_tai_meshi = pygame.image.load('media/tai_meshi.png')
        meal_tai_meshi_rect = meal_tai_meshi.get_rect()
        meal_tai_meshi_rect.center = (DISPLAY_WIDTH * .74, DISPLAY_HEIGHT * .6)
        meal_udon = pygame.image.load('media/udon.png')
        meal_udon_rect = meal_udon.get_rect()
        meal_udon_rect.center = (DISPLAY_WIDTH * .86, DISPLAY_HEIGHT * .6)
        meal_unagi = pygame.image.load('media/unagi.png')
        meal_unagi_rect = meal_unagi.get_rect()
        meal_unagi_rect.center = (DISPLAY_WIDTH * .62, DISPLAY_HEIGHT * .6)
        while paused:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    quitter()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if meal_miso_rect.collidepoint(event.pos):
                            current_player = Inn_Loc(current_player, "Misoshiru")
                            return True
                        elif meal_dango_rect.collidepoint(event.pos):
                            current_player = Inn_Loc(current_player, "Dango")
                            return True
                        elif meal_nigiri_rect.collidepoint(event.pos):
                            current_player = Inn_Loc(current_player, "Nigirimeshi")
                            return True
                        elif meal_tempura_rect.collidepoint(event.pos):
                            current_player = Inn_Loc(current_player, "Tempura")
                            return True
                        elif meal_soba_rect.collidepoint(event.pos):
                            current_player = Inn_Loc(current_player, "Soba")
                            return True
                        elif meal_yakitori_rect.collidepoint(event.pos):
                            current_player = Inn_Loc(current_player, "Yakitori")
                            return True
                        elif meal_tofu_rect.collidepoint(event.pos):
                            current_player = Inn_Loc(current_player, "Tofu")
                            return True
                        elif meal_sushi_rect.collidepoint(event.pos):
                            current_player = Inn_Loc(current_player, "Sushi")
                            return True
                        elif meal_fugu_rect.collidepoint(event.pos):
                            current_player = Inn_Loc(current_player, "Fugu")
                            return True
                        elif meal_donburi_rect.collidepoint(event.pos):
                            current_player = Inn_Loc(current_player, "Donburi")
                            return True
                        elif meal_sashimi_rect.collidepoint(event.pos):
                            current_player = Inn_Loc(current_player, "Sashimi")
                            return True
                        elif meal_udon_rect.collidepoint(event.pos):
                            current_player = Inn_Loc(current_player, "Udon")
                            return True
                        elif meal_unagi_rect.collidepoint(event.pos):
                            current_player = Inn_Loc(current_player, "Unagi")
                            return True
                        elif meal_tai_meshi_rect.collidepoint(event.pos):
                            current_player = Inn_Loc(current_player, "Tai Meshi")
                            return True
                        elif meal_skip_rect.collidepoint(event.pos):
                            current_player = Inn_Loc(current_player, 'Skip')
                            return True
                        elif inn_back_r.collidepoint(event.pos):
                            return False
            if inn_screen_update == 1:
                screen.fill((255, 255, 255))
                screen.blit(inn_select_text, inn_select_text_rect)
                screen.blit(inn_back, inn_back_r)
                screen.blit(meal_skip, meal_skip_rect)
                screen.blit(meal_miso, meal_miso_rect)
                screen.blit(meal_dango, meal_dango_rect)
                screen.blit(meal_nigiri, meal_nigiri_rect)
                screen.blit(meal_soba, meal_soba_rect)
                screen.blit(meal_sushi, meal_sushi_rect)
                screen.blit(meal_tempura, meal_tempura_rect)
                screen.blit(meal_tofu, meal_tofu_rect)
                screen.blit(meal_yakitori, meal_yakitori_rect)
                screen.blit(meal_donburi, meal_donburi_rect)
                screen.blit(meal_fugu, meal_fugu_rect)
                screen.blit(meal_sashimi, meal_sashimi_rect)
                screen.blit(meal_tai_meshi, meal_tai_meshi_rect)
                screen.blit(meal_udon, meal_udon_rect)
                screen.blit(meal_unagi, meal_unagi_rect)
                inn_screen_update = 0
                pygame.display.update()
        return False

    def village_menu(screen):
        """Village Menu"""
        global current_player
        paused = True
        village_screen_update = 1
        counter = 0
        village_text_style = pygame.font.SysFont('Arial', 50)
        desc_text_style = pygame.font.SysFont('Arial', 38)
        village_select_text = village_text_style.render('Choose 3 Souvenirs:', True, black)
        village_select_text_rect = village_select_text.get_rect()
        village_select_text_rect.center = (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT * .1)
        desc_text = desc_text_style.render('Left-Click to Add, Right-Click to Discard', True, black)
        desc_text_rect = desc_text.get_rect()
        desc_text_rect.center = (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT * .2)
        koma = pygame.image.load('media/koma.png')
        koma_rect = koma.get_rect()
        koma_rect.center = (DISPLAY_WIDTH * .08, DISPLAY_HEIGHT * .37)
        kamaboko = pygame.image.load('media/kamaboko.png')
        kamaboko_rect = kamaboko.get_rect()
        kamaboko_rect.center = (DISPLAY_WIDTH * .2, DISPLAY_HEIGHT * .37)
        hashi = pygame.image.load('media/hashi.png')
        hashi_rect = hashi.get_rect()
        hashi_rect.center = (DISPLAY_WIDTH * .32, DISPLAY_HEIGHT * .37)
        gofu = pygame.image.load('media/gofu.png')
        gofu_rect = gofu.get_rect()
        gofu_rect.center = (DISPLAY_WIDTH * .44, DISPLAY_HEIGHT * .37)
        konpeito = pygame.image.load('media/konpeito.png')
        konpeito_rect = konpeito.get_rect()
        konpeito_rect.center = (DISPLAY_WIDTH * .56, DISPLAY_HEIGHT * .37)
        manju = pygame.image.load('media/manju.png')
        manju_rect = manju.get_rect()
        manju_rect.center = (DISPLAY_WIDTH * .68, DISPLAY_HEIGHT * .37)
        uchiwa = pygame.image.load('media/uchiwa.png')
        uchiwa_rect = uchiwa.get_rect()
        uchiwa_rect.center = (DISPLAY_WIDTH * .8, DISPLAY_HEIGHT * .37)
        washi = pygame.image.load('media/washi.png')
        washi_rect = washi.get_rect()
        washi_rect.center = (DISPLAY_WIDTH * .92, DISPLAY_HEIGHT * .37)
        yunomi = pygame.image.load('media/yunomi.png')
        yunomi_rect = yunomi.get_rect()
        yunomi_rect.center = (DISPLAY_WIDTH * .08, DISPLAY_HEIGHT * .6)
        daifuku = pygame.image.load('media/daifuku.png')
        daifuku_rect = daifuku.get_rect()
        daifuku_rect.center = (DISPLAY_WIDTH * .2, DISPLAY_HEIGHT * .6)
        furoshiki = pygame.image.load('media/furoshiki.png')
        furoshiki_rect = furoshiki.get_rect()
        furoshiki_rect.center = (DISPLAY_WIDTH * .32, DISPLAY_HEIGHT * .6)
        geta = pygame.image.load('media/geta.png')
        geta_rect = geta.get_rect()
        geta_rect.center = (DISPLAY_WIDTH * .44, DISPLAY_HEIGHT * .6)
        haori = pygame.image.load('media/haori.png')
        haori_rect = haori.get_rect()
        haori_rect.center = (DISPLAY_WIDTH * .56, DISPLAY_HEIGHT * .6)
        jubako = pygame.image.load('media/jubako.png')
        jubako_rect = jubako.get_rect()
        jubako_rect.center = (DISPLAY_WIDTH * .68, DISPLAY_HEIGHT * .6)
        kan_zashi = pygame.image.load('media/kan_zashi.png')
        kan_zashi_rect = kan_zashi.get_rect()
        kan_zashi_rect.center = (DISPLAY_WIDTH * .8, DISPLAY_HEIGHT * .6)
        netsuke = pygame.image.load('media/netsuke.png')
        netsuke_rect = netsuke.get_rect()
        netsuke_rect.center = (DISPLAY_WIDTH * .92, DISPLAY_HEIGHT * .6)
        ocha = pygame.image.load('media/ocha.png')
        ocha_rect = ocha.get_rect()
        ocha_rect.center = (DISPLAY_WIDTH * .08, DISPLAY_HEIGHT * .83)
        sake = pygame.image.load('media/sake.png')
        sake_rect = sake.get_rect()
        sake_rect.center = (DISPLAY_WIDTH * .2, DISPLAY_HEIGHT * .83)
        sandogasa = pygame.image.load('media/sandogasa.png')
        sandogasa_rect = sandogasa.get_rect()
        sandogasa_rect.center = (DISPLAY_WIDTH * .32, DISPLAY_HEIGHT * .83)
        shikki = pygame.image.load('media/shikki.png')
        shikki_rect = shikki.get_rect()
        shikki_rect.center = (DISPLAY_WIDTH * .44, DISPLAY_HEIGHT * .83)
        yukata = pygame.image.load('media/yukata.png')
        yukata_rect = yukata.get_rect()
        yukata_rect.center = (DISPLAY_WIDTH * .56, DISPLAY_HEIGHT * .83)
        shamisen = pygame.image.load('media/shamisen.png')
        shamisen_rect = shamisen.get_rect()
        shamisen_rect.center = (DISPLAY_WIDTH * .68, DISPLAY_HEIGHT * .83)
        sumie = pygame.image.load('media/sumie.png')
        sumie_rect = sumie.get_rect()
        sumie_rect.center = (DISPLAY_WIDTH * .8, DISPLAY_HEIGHT * .83)
        ukiyoe = pygame.image.load('media/ukiyoe.png')
        ukiyoe_rect = ukiyoe.get_rect()
        ukiyoe_rect.center = (DISPLAY_WIDTH * .92, DISPLAY_HEIGHT * .83)
        v_back = pygame.image.load('media/arrow_back.png')
        v_back_r = v_back.get_rect()
        v_back_r.center = (DISPLAY_WIDTH * .945, DISPLAY_HEIGHT * .06)
        while paused and counter < 3:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    quitter()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if v_back_r.collidepoint(event.pos):
                            return False
                        elif gofu_rect.collidepoint(event.pos):
                            current_player = Village_Loc(current_player, "Gofu")
                            counter += 1
                        elif koma_rect.collidepoint(event.pos):
                            current_player = Village_Loc(current_player, "Koma")
                            counter += 1
                        elif yunomi_rect.collidepoint(event.pos):
                            current_player = Village_Loc(current_player, "Yunomi")
                            counter += 1
                        elif washi_rect.collidepoint(event.pos):
                            current_player = Village_Loc(current_player, "Washi")
                            counter += 1
                        elif uchiwa_rect.collidepoint(event.pos):
                            current_player = Village_Loc(current_player, "Uchiwa")
                            counter += 1
                        elif hashi_rect.collidepoint(event.pos):
                            current_player = Village_Loc(current_player, "Hashi")
                            counter += 1
                        elif konpeito_rect.collidepoint(event.pos):
                            current_player = Village_Loc(current_player, "Konpeito")
                            counter += 1
                        elif kamaboko_rect.collidepoint(event.pos):
                            current_player = Village_Loc(current_player, "Kamaboko")
                            counter += 1
                        elif manju_rect.collidepoint(event.pos):
                            current_player = Village_Loc(current_player, "Manju")
                            counter += 1
                        elif daifuku_rect.collidepoint(event.pos):
                            current_player = Village_Loc(current_player, "Daifuku")
                            counter += 1
                        elif ocha_rect.collidepoint(event.pos):
                            current_player = Village_Loc(current_player, "Ocha")
                            counter += 1
                        elif sake_rect.collidepoint(event.pos):
                            current_player = Village_Loc(current_player, "Sake")
                            counter += 1
                        elif yukata_rect.collidepoint(event.pos):
                            current_player = Village_Loc(current_player, "Yukata")
                            counter += 1
                        elif kan_zashi_rect.collidepoint(event.pos):
                            current_player = Village_Loc(current_player, "Kan Zashi")
                            counter += 1
                        elif geta_rect.collidepoint(event.pos):
                            current_player = Village_Loc(current_player, "Geta")
                            counter += 1
                        elif haori_rect.collidepoint(event.pos):
                            current_player = Village_Loc(current_player, "Haori")
                            counter += 1
                        elif furoshiki_rect.collidepoint(event.pos):
                            current_player = Village_Loc(current_player, "Furoshiki")
                            counter += 1
                        elif sandogasa_rect.collidepoint(event.pos):
                            current_player = Village_Loc(current_player, "Sandogasa")
                            counter += 1
                        elif netsuke_rect.collidepoint(event.pos):
                            current_player = Village_Loc(current_player, "Netsuke")
                            counter += 1
                        elif shikki_rect.collidepoint(event.pos):
                            current_player = Village_Loc(current_player, "Shikki")
                            counter += 1
                        elif jubako_rect.collidepoint(event.pos):
                            current_player = Village_Loc(current_player, "Jubako")
                            counter += 1
                        elif ukiyoe_rect.collidepoint(event.pos):
                            current_player = Village_Loc(current_player, "Ukiyoe")
                            counter += 1
                        elif sumie_rect.collidepoint(event.pos):
                            current_player = Village_Loc(current_player, "Sumie")
                            counter += 1
                        elif shamisen_rect.collidepoint(event.pos):
                            current_player = Village_Loc(current_player, "Shamisen")
                            counter += 1
                    elif event.button == 3:
                        if gofu_rect.collidepoint(event.pos):
                            discard(SVDeck, "Gofu")
                            counter += 1
                        elif koma_rect.collidepoint(event.pos):
                            discard(SVDeck, "Koma")
                            counter += 1
                        elif yunomi_rect.collidepoint(event.pos):
                            discard(SVDeck, "Yunomi")
                            counter += 1
                        elif washi_rect.collidepoint(event.pos):
                            discard(SVDeck, "Washi")
                            counter += 1
                        elif uchiwa_rect.collidepoint(event.pos):
                            discard(SVDeck, "Uchiwa")
                            counter += 1
                        elif hashi_rect.collidepoint(event.pos):
                            discard(SVDeck, "Hashi")
                            counter += 1
                        elif konpeito_rect.collidepoint(event.pos):
                            discard(SVDeck, "Konpeito")
                            counter += 1
                        elif kamaboko_rect.collidepoint(event.pos):
                            discard(SVDeck, "Kamaboko")
                            counter += 1
                        elif manju_rect.collidepoint(event.pos):
                            discard(SVDeck, "Manju")
                            counter += 1
                        elif daifuku_rect.collidepoint(event.pos):
                            discard(SVDeck, "Daifuku")
                            counter += 1
                        elif ocha_rect.collidepoint(event.pos):
                            discard(SVDeck, "Ocha")
                            counter += 1
                        elif sake_rect.collidepoint(event.pos):
                            discard(SVDeck, "Sake")
                            counter += 1
                        elif yukata_rect.collidepoint(event.pos):
                            discard(SVDeck, "Yukata")
                            counter += 1
                        elif kan_zashi_rect.collidepoint(event.pos):
                            discard(SVDeck, "Kan Zashi")
                            counter += 1
                        elif geta_rect.collidepoint(event.pos):
                            discard(SVDeck, "Geta")
                            counter += 1
                        elif haori_rect.collidepoint(event.pos):
                            discard(SVDeck, "Haori")
                            counter += 1
                        elif furoshiki_rect.collidepoint(event.pos):
                            discard(SVDeck, "Furoshiki")
                            counter += 1
                        elif sandogasa_rect.collidepoint(event.pos):
                            discard(SVDeck, "Sandogasa")
                            counter += 1
                        elif netsuke_rect.collidepoint(event.pos):
                            discard(SVDeck, "Netsuke")
                            counter += 1
                        elif shikki_rect.collidepoint(event.pos):
                            discard(SVDeck, "Shikki")
                            counter += 1
                        elif jubako_rect.collidepoint(event.pos):
                            discard(SVDeck, "Jubako")
                            counter += 1
                        elif ukiyoe_rect.collidepoint(event.pos):
                            discard(SVDeck, "Ukiyoe")
                            counter += 1
                        elif sumie_rect.collidepoint(event.pos):
                            discard(SVDeck, "Sumie")
                            counter += 1
                        elif shamisen_rect.collidepoint(event.pos):
                            discard(SVDeck, "Shamisen")
                            counter += 1
            if village_screen_update == 1:
                screen.fill((255, 255, 255))
                screen.blit(village_select_text, village_select_text_rect)
                screen.blit(desc_text, desc_text_rect)
                screen.blit(v_back, v_back_r)
                screen.blit(gofu, gofu_rect)
                screen.blit(hashi, hashi_rect)
                screen.blit(kamaboko, kamaboko_rect)
                screen.blit(koma, koma_rect)
                screen.blit(konpeito, konpeito_rect)
                screen.blit(manju, manju_rect)
                screen.blit(uchiwa, uchiwa_rect)
                screen.blit(washi, washi_rect)
                screen.blit(yunomi, yunomi_rect)
                screen.blit(daifuku, daifuku_rect)
                screen.blit(furoshiki, furoshiki_rect)
                screen.blit(geta, geta_rect)
                screen.blit(haori, haori_rect)
                screen.blit(jubako, jubako_rect)
                screen.blit(kan_zashi, kan_zashi_rect)
                screen.blit(netsuke, netsuke_rect)
                screen.blit(ocha, ocha_rect)
                screen.blit(sake, sake_rect)
                screen.blit(sandogasa, sandogasa_rect)
                screen.blit(shikki, shikki_rect)
                screen.blit(yukata, yukata_rect)
                screen.blit(shamisen, shamisen_rect)
                screen.blit(sumie, sumie_rect)
                screen.blit(ukiyoe, ukiyoe_rect)
                village_screen_update = 0
                pygame.display.update()
        return True

    def temple_menu(screen):
        """Temple Menu"""
        global current_player
        paused = True
        temple_screen_update = 1
        text_select = pygame.font.SysFont('Arial', 50)
        text_select_r = text_select.render('Select Amount:', True, black)
        text_select_rect = text_select_r.get_rect()
        text_select_rect.center = (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT * .2)
        coins_1 = pygame.image.load('media/coin.png')
        coins_2 = pygame.image.load('media/coins_two.png')
        coins_3 = pygame.image.load('media/coins_three.png')
        coins_1_rect = coins_1.get_rect()
        coins_2_rect = coins_2.get_rect()
        coins_3_rect = coins_3.get_rect()
        coins_1_rect.center = (DISPLAY_WIDTH * .25, DISPLAY_HEIGHT * .45)
        coins_2_rect.center = (DISPLAY_WIDTH * .5, DISPLAY_HEIGHT * .46)
        coins_3_rect.center = (DISPLAY_WIDTH * .75, DISPLAY_HEIGHT * .46)
        temple_back = pygame.image.load('media/arrow_back.png')
        temple_back_r = temple_back.get_rect()
        temple_back_r.center = (DISPLAY_WIDTH * .945, DISPLAY_HEIGHT * .06)
        while paused:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    quitter()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if coins_1_rect.collidepoint(event.pos):
                            current_player = Temple_Loc(current_player, 1)
                            return True
                        if coins_2_rect.collidepoint(event.pos):
                            current_player = Temple_Loc(current_player, 2)
                            return True
                        if coins_3_rect.collidepoint(event.pos):
                            current_player = Temple_Loc(current_player, 3)
                            return True
                        elif temple_back_r.collidepoint(event.pos):
                            return False
            if temple_screen_update == 1:
                screen.fill((255, 255, 255))
                screen.blit(text_select_r, text_select_rect)
                screen.blit(temple_back, temple_back_r)
                screen.blit(coins_1, coins_1_rect)
                screen.blit(coins_2, coins_2_rect)
                screen.blit(coins_3, coins_3_rect)
                temple_screen_update = 0
                pygame.display.update()        
        return False

    def results_menu(screen):
        """Results screen! Will show breakdown of player points"""
        paused = True
        results_screen_update = 1
        text_results = pygame.font.SysFont('Arial', 50)
        results_player_list = sorted(player_list, key=attrgetter("score"))
        first_place = text_results.render('First', True, black)
        first_place_rect = first_place.get_rect()
        first_place_rect.center = (DISPLAY_WIDTH * .30, DISPLAY_HEIGHT * .2)
        second_place = text_results.render('Second', True, black)
        second_place_rect = second_place.get_rect()
        second_place_rect.center = (DISPLAY_WIDTH * .30, DISPLAY_HEIGHT * .5)
        third_place = text_results.render('Third', True, black)
        third_place_rect = third_place.get_rect()
        third_place_rect.center = (DISPLAY_WIDTH * .30, DISPLAY_HEIGHT * .8)
        first_player = text_results.render(results_player_list[2].color, True, black)
        first_player_rect = first_player.get_rect()
        first_player_rect.center = (DISPLAY_WIDTH * .5, DISPLAY_HEIGHT * .2)
        second_player = text_results.render(results_player_list[1].color, True, black)
        second_player_rect = second_player.get_rect()
        second_player_rect.center = (DISPLAY_WIDTH * .5, DISPLAY_HEIGHT * .5)
        third_player = text_results.render(results_player_list[0].color, True, black)
        third_player_rect = third_player.get_rect()
        third_player_rect.center = (DISPLAY_WIDTH * .5, DISPLAY_HEIGHT * .8)
        first_score = text_results.render(str(results_player_list[2].score), True, black)
        first_score_rect = first_score.get_rect()
        first_score_rect.center = (DISPLAY_WIDTH * .7, DISPLAY_HEIGHT * .2)
        second_score = text_results.render(str(results_player_list[1].score), True, black)
        second_score_rect = second_score.get_rect()
        second_score_rect.center = (DISPLAY_WIDTH * .7, DISPLAY_HEIGHT * .5)
        third_score = text_results.render(str(results_player_list[0].score), True, black)
        third_score_rect = third_score.get_rect()
        third_score_rect.center = (DISPLAY_WIDTH * .7, DISPLAY_HEIGHT * .8)
        while paused:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    quitter()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        quitter()
            if results_screen_update == 1:
                screen.fill((255, 255, 255))
                screen.blit(first_place, first_place_rect)
                screen.blit(first_player, first_player_rect)
                screen.blit(first_score, first_score_rect)
                screen.blit(second_place, second_place_rect)
                screen.blit(second_player, second_player_rect)
                screen.blit(second_score, second_score_rect)
                screen.blit(third_place, third_place_rect)
                screen.blit(third_player, third_player_rect)
                screen.blit(third_score, third_score_rect)
                results_screen_update = 0
                pygame.display.update()
        return False

    # Run Sequence Below
    main_screen(0)
    # results screen()
    quitter()
