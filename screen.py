#!/usr/bin/python3
"""Main code for Tokaido Nakama"""
import pygame
import pygame_menu
from player import Player
from init import current_player, HSDeck, player_list, GreenPlayer, BluePlayer, YellowPlayer, PurplePlayer, GreyPlayer
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

        if board_position in [1, 8, 25, 29, 45, 45, 53]:
            # Code for Villages Menu & updating stuff
            print("Village stuff")
            update_current_player()
        elif board_position in [2, 9, 16, 21, 36, 43]:
            # Code for Temples Menu & updating stuff
            print("Temple stuff")
            temple_menu(screen)
            update_current_player()
        elif board_position in [3, 10, 20, 30, 38, 44, 49]:
            # Code for Encounter Menu & updating stuff
            print("Encounter stuff")
            update_current_player()
        elif board_position in [4, 18, 28, 35, 51]:
            # Code for Pano_Paddy
            print("Pano paddy stuff")
            pano_paddy_menu(screen)
            update_current_player()
        elif board_position in [5, 13, 22, 33, 42, 48]:
            # Code for Hot Springs
            print("Hot spring stuff")
            hot_springs_menu(screen)
            update_current_player()
        elif board_position in [6, 12, 19, 23, 32, 50]:
            # Code for Pano_Mt
            print("Pano mt stuff")
            pano_mt_menu(screen)
            update_current_player()
        elif board_position in [7, 17, 26, 31, 37, 47]:
            # Code for Farm
            print("Farm stuff")
            farm_menu(screen)
            update_current_player()
        elif board_position in [11, 15, 24, 34, 39, 46, 52]:
            # Code for Pano_Sea
            print("Pano sea stuff")
            pano_sea_menu(screen)
            update_current_player
        elif board_position in [14, 27, 41, 54]:
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
        
        colors_rgb = {
        "Green": (73, 114, 16),
        "Blue": (122, 165, 184),
        "Yellow": (243, 175, 1),
        "Grey": (145, 147, 156),
        "Purple": (98, 55, 114)
        }

        for key in colors_rgb:
            if key == current_player.color:
                rgb = colors_rgb.get(key)
        # Create title font, first param is font file in pygame, second is size
        font_title = pygame.font.Font('freesansbold.ttf', 50)
        # Create a text surface object, on which text is drawn on.
        text_current_player = current_player.color + '\'s Turn'
        text_title = font_title.render(text_current_player, True, rgb)
        # Create a rectangular object for the text surface object
        text_title_rect = text_title.get_rect()
        # Set the center of the rectangular object
        text_title_rect.center = (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT * .03)
        screen.blit(text_title, text_title_rect)

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

    def player_positioning():
        """Checks player positions & blits pieces"""
        player_list.reverse()
        for player in player_list:
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
                screen.blit(player.icon, (801, 176))
            if player.board_space == 15:
                screen.blit(player.icon, (801, 227))
            if player.board_space == 16:
                screen.blit(player.icon, (801, 277))
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
        # if board_number == 2:

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
                        if rect1.collidepoint(event.pos) or rect1_1.collidepoint(event.pos):
                            print('Village selected.')
                            encounter_selection(1)
                            current_player.board_space = 1
                            update_current_player()
                            screen_update = 1
                        if rect2.collidepoint(event.pos) or rect2_1.collidepoint(event.pos):
                            print('Temple selected.')
                            encounter_selection(2)
                            current_player.board_space = 2
                            update_current_player()
                            screen_update = 1
                        if rect3.collidepoint(event.pos) or rect3_1.collidepoint(event.pos):
                            print('Encounter selected.')
                            encounter_selection(3)
                            current_player.board_space = 3
                            update_current_player()
                            screen_update = 1
                        if rect4.collidepoint(event.pos) or rect4_1.collidepoint(event.pos):
                            print('Panorama: Paddy selected.')
                            encounter_selection(4)
                            current_player.board_space = 4
                            update_current_player()
                            screen_update = 1
                        if rect5.collidepoint(event.pos) or rect5_1.collidepoint(event.pos):
                            print('Hot Springs selected.')
                            encounter_selection(5)
                            current_player.board_space = 5
                            update_current_player()
                            screen_update = 1
                        if rect6.collidepoint(event.pos) or rect6_1.collidepoint(event.pos):
                            print('Panorama: Mt selected.')
                            encounter_selection(6)
                            current_player.board_space = 6
                            update_current_player()
                            screen_update = 1
                        if rect7.collidepoint(event.pos) or rect7_1.collidepoint(event.pos):
                            print('Farm selected.')
                            encounter_selection(7)
                            current_player.board_space = 7
                            update_current_player()
                            screen_update = 1
                        if rect8.collidepoint(event.pos) or rect8_1.collidepoint(event.pos):
                            print('Village selected.')
                            encounter_selection(8)
                            current_player.board_space = 8
                            update_current_player()
                            screen_update = 1
                        if rect9.collidepoint(event.pos) or rect9_1.collidepoint(event.pos):
                            print('Temple selected.')
                            encounter_selection(9)
                            current_player.board_space = 9
                            update_current_player()
                            screen_update = 1
                        if rect10.collidepoint(event.pos) or rect10_1.collidepoint(event.pos):
                            print('Encounter selected.')
                            encounter_selection(10)
                            current_player.board_space = 10
                            update_current_player()
                            screen_update = 1
                        if rect11.collidepoint(event.pos) or rect11_1.collidepoint(event.pos):
                            print('Panorama: Sea selected.')
                            encounter_selection(11)
                            current_player.board_space = 11
                            update_current_player()
                            screen_update = 1
                        if rect12.collidepoint(event.pos) or rect12_1.collidepoint(event.pos):
                            print('Panorama: Mountain selected.')
                            encounter_selection(12)
                            current_player.board_space = 12
                            update_current_player()
                            screen_update = 1
                        if rect13.collidepoint(event.pos) or rect13_1.collidepoint(event.pos):
                            print('Hot Spring selected.')
                            encounter_selection(13)
                            current_player.board_space = 13
                            update_current_player()
                            screen_update = 1
                    # if rect for inn collision:
                            # append to player list (which will be cleared as player pieces are set)
                            # if all players on inn:
                            # food menu.

                # Shows list of events on ya terminal. To be removed, but fun to seeprint(event)
                # print(event)    

            # hopefully fixes start_menu
            if start_menu.is_enabled():
                start_menu.update(events)
                start_menu.draw(screen)


            if screen_update == 1:
                # Filling screen
                screen.fill(white)

                # Render title text & rect
                title_selector(current_player)

                # Call Board Function
                board(X_BOARD_COORD, Y_BOARD_COORD, board_number)

                # Piece Space Function
                player_positioning()
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
                            current_player = Ecounter_Loc(current_player, "Miko")
                            return
                        elif but_samurai.collidepoint(event.pos):
                            current_player = Ecounter_Loc(current_player, "Samurai")
                            return
                        elif but_shokunin.collidepoint(event.pos):
                            current_player = Ecounter_Loc(current_player, "Shokunin")
                            return
                        elif but_anna_pad.collidepoint(event.pos):
                            current_player = Ecounter_Loc(current_player, "Annaibito: Paddy")
                            return
                        elif but_anna_mtn.collidepoint(event.pos):
                            current_player = Ecounter_Loc(current_player, "Annaibito: Mountain")
                            return
                        elif but_anna_sea.collidepoint(event.pos):
                            current_player = Ecounter_Loc(current_player, "Annaibito: Sea")
                            return
            pygame.display.update()
        return False

    def inn_menu(screen):
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
                            current_player = Ecounter_Loc(current_player, "Donburi")
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
        paused = True
        while paused:
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
                            return
                        elif but_koma.collidepoint(event.pos):
                            current_player = Village_Loc(current_player, "Koma")
                            return
                        elif but_yunomi.collidepoint(event.pos):
                            current_player = Village_Loc(current_player, "Yunomi")
                            return
                        elif but_washi.collidepoint(event.pos):
                            current_player = Village_Loc(current_player, "Washi")
                            return
                        elif but_uchiwa.collidepoint(event.pos):
                            current_player = Village_Loc(current_player, "Uchiwa")
                            return
                        elif but_hashi.collidepoint(event.pos):
                            current_player = Village_Loc(current_player, "Hashi")
                            return
                        elif but_konpeito.collidepoint(event.pos):
                            current_player = Village_Loc(current_player, "Konpeito")
                            return
                        elif but_kamaboko.collidepoint(event.pos):
                            current_player = Village_Loc(current_player, "Kamaboko")
                            return
                        elif but_manju.collidepoint(event.pos):
                            current_player = Village_Loc(current_player, "Manju")
                            return
                        elif but_daifuku.collidepoint(event.pos):
                            current_player = Village_Loc(current_player, "Daifuku")
                            return
                        elif but_ocha.collidepoint(event.pos):
                            current_player = Village_Loc(current_player, "Ocha")
                            return
                        elif but_sake.collidepoint(event.pos):
                            current_player = Village_Loc(current_player, "Sake")
                            return
                        elif but_yukata.collidepoint(event.pos):
                            current_player = Village_Loc(current_player, "Yukata")
                            return
                        elif but_kanzashi.collidepoint(event.pos):
                            current_player = Village_Loc(current_player, "Kan Zashi")
                            return
                        elif but_geta.collidepoint(event.pos):
                            current_player = Village_Loc(current_player, "Geta")
                            return
                        elif but_haori.collidepoint(event.pos):
                            current_player = Village_Loc(current_player, "Haori")
                            return
                        elif but_furoshiki.collidepoint(event.pos):
                            current_player = Village_Loc(current_player, "Furoshiki")
                            return
                        elif but_sandogasa.collidepoint(event.pos):
                            current_player = Village_Loc(current_player, "Sandogasa")
                            return
                        elif but_netsuke.collidepoint(event.pos):
                            current_player = Village_Loc(current_player, "Netsuke")
                            return
                        elif but_shikki.collidepoint(event.pos):
                            current_player = Village_Loc(current_player, "Shikki")
                            return
                        elif but_jubako.collidepoint(event.pos):
                            current_player = Village_Loc(current_player, "Jubako")
                            return
                        elif but_ukiyoe.collidepoint(event.pos):
                            current_player = Village_Loc(current_player, "Ukiyoe")
                            return
                        elif but_sumie.collidepoint(event.pos):
                            current_player = Village_Loc(current_player, "Sumie")
                            return
                        elif but_shamisen.collidepoint(event.pos):
                            current_player = Village_Loc(current_player, "Shamisen")
                            return
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
