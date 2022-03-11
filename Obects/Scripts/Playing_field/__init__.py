import pygame

from ..Main_menu import Main_menu
from ..Display import Display
from ..Setings_menu import Setings_menu

main_menu = Main_menu()
display = Display()
setings_menu = Setings_menu()

class Playing_field(object):
    def __init__(self):

        self.now_Screen_Size = (display.Standard_Screen_Size[screen_resolution_Default])

        # Размеры кнопок
        self.size_button_from_settings_menu = (
        main_menu.size_button[0] + (25 - 25 * self.now_Screen_Size[1] / self.now_Screen_Size[0]),
        main_menu.size_button[1] + (25 - 25 * self.now_Screen_Size[1] / self.now_Screen_Size[0]))
        self.button_side_size = 40
        self.block_side_size = 25 + (25 - (25 * self.now_Screen_Size[1] / self.now_Screen_Size[0]))
        self.block_size = (self.block_side_size, self.block_side_size)
        self.size_button = (self.button_side_size - 25 + self.block_side_size,
                            self.button_side_size - 25 + self.block_side_size)  # размер для кнопок с картинками
        # Отступ
        self.indent = 2
        # список с постоянными значениями координат блоков поля
        self.BLOCK_PLACE = [display.res[0] * (1 / 5), 100]
        # список с изменяющимися значениями координат блоков поля
        self.block_place = [display.res[0] * (1 / 5), 100]
        # Доступна ли клетка для размещения кораблика?
        self.accessible_area = True
        # Цвет голограммы кораблика (Зелёный/Красный)
        self.hologram_color = display.DARK_GREEN

        #Название файла сохранения расстановки корабликов
        self.preset_name = 'save_1'

        #Путь + название + разширение файла расстановки корабликов
        self.preset_way = 'ships_preset\{0}.txt'.format(self.preset_name)

        #Список с данные о координатах и виде кораблика для сохранения
        self.save_ships_log = []

        self.i = 0

        #Инициализация и открытие файла сохранения
        self.ships_preset = open(self.preset_way,'w')

        # Координаты отрисовки кнопок
        self.draw_load_button = (display.res[0] * (1 / 3), 10)
        self.draw_save_button = (self.draw_load_button[0] + 50 - 25 + self.block_side_size, self.draw_load_button[1])
        self.draw_play_button = (self.draw_load_button[0] + 100 - 25 + self.block_side_size + (
                    25 - (25 * self.now_Screen_Size[1] / self.now_Screen_Size[0])), self.draw_load_button[1])

        #переменные, отвечеющие за то, чтобы программа проигрывала только один звук нажатия
        self.is_the_cursor_hovered = True
        self.is_the_cursor_hovered1 = True
        self.is_the_cursor_hovered2 = True
        self.is_the_cursor_hovered3 = True


    def one_deck_ship (self):
        pygame.draw.rect(display.screen, display.DARK_GREEN, [self.block_place, self.block_size])  

    def two_deck_ship (self,y):
        if y > 8:
            self.accessible_area = False
        else:
            self.accessible_area = True
        pygame.draw.rect(display.screen, self.hologram_color, [self.block_place, self.block_size])
        if y <= 8:
            pygame.draw.rect(display.screen, self.hologram_color, [[self.block_place[0] + self.indent + self.block_side_size, self.block_place[1]], self.block_size])

    def inv_two_deck_ship (self, x):
        if x > 8:
            self.accessible_area = False
        else:
            self.accessible_area = True
        pygame.draw.rect(display.screen, self.hologram_color, [self.block_place, self.block_size])
        if x <= 8:
            pygame.draw.rect(display.screen, self.hologram_color, [[self.block_place[0], self.block_place[1] + self.indent + self.block_side_size], self.block_size])

    def three_deck_ship (self,y):
        if y > 7:
            self.accessible_area = False
        else:
            self.accessible_area = True
        pygame.draw.rect(display.screen, self.hologram_color, [self.block_place, self.block_size])
        if y <= 8:
            pygame.draw.rect(display.screen, self.hologram_color, [[self.block_place[0] + self.indent + self.block_side_size, self.block_place[1]], self.block_size])
        if y <= 7:
            pygame.draw.rect(display.screen, self.hologram_color, [[self.block_place[0] + self.indent*2 + self.block_side_size*2, self.block_place[1]], self.block_size])

    def inv_three_deck_ship (self, x):
        if x > 7:
            self.accessible_area = False
        else:
            self.accessible_area = True
        pygame.draw.rect(display.screen, self.hologram_color, [self.block_place, self.block_size])
        if x <= 8:
            pygame.draw.rect(display.screen, self.hologram_color, [[self.block_place[0], self.block_place[1] + self.indent + self.block_side_size], self.block_size])
        if x <= 7:
            pygame.draw.rect(display.screen, self.hologram_color, [[self.block_place[0], self.block_place[1] + self.indent*2 + self.block_side_size*2], self.block_size])

    def four_deck_ship (self, y):
        if y > 6:
            self.accessible_area = False
        else:
            self.accessible_area = True
        pygame.draw.rect(display.screen, self.hologram_color, [self.block_place, self.block_size])
        if y <= 8:
            pygame.draw.rect(display.screen, self.hologram_color, [[self.block_place[0] + self.indent + self.block_side_size, self.block_place[1]], self.block_size])
        if y <= 7:
            pygame.draw.rect(display.screen, self.hologram_color, [[self.block_place[0] + self.indent*2 + self.block_side_size*2, self.block_place[1]], self.block_size])
        if y <= 6:
            pygame.draw.rect(display.screen, self.hologram_color, [[self.block_place[0] + self.indent*3 + self.block_side_size*3, self.block_place[1]], self.block_size])



    def inv_four_deck_ship (self, x):
        if x > 6:
            self.accessible_area = False
        else:
            self.accessible_area = True
        pygame.draw.rect(display.screen, self.hologram_color, [self.block_place, self.block_size])
        if x <= 8:
            pygame.draw.rect(display.screen, self.hologram_color, [[self.block_place[0], self.block_place[1] + self.indent + self.block_side_size], self.block_size])
        if x <= 7:
            pygame.draw.rect(display.screen, self.hologram_color, [[self.block_place[0], self.block_place[1] + self.indent*2 + self.block_side_size*2], self.block_size])
        if x <= 6:
            pygame.draw.rect(display.screen, self.hologram_color, [[self.block_place[0], self.block_place[1] + self.indent*3 + self.block_side_size*3], self.block_size])

    def draw_field(self):
        global mouse_pose, selected_ships, inv_ships
        # Отрисовываю поле 10 на 10
        for x in range(10):
            for y in range(10):
                pygame.draw.rect(display.screen, display.LIGHT_GRAY, [self.block_place, self.block_size])
                        

                self.block_place[0] += self.block_side_size
                self.block_place[0] += self.indent
            #обнуляю координаты икса, чтобы начать отрисовывать следующую строчку
            self.block_place[0] = self.BLOCK_PLACE[0]
            self.block_place[1] += self.block_side_size
            self.block_place[1] += self.indent

        self.block_place[1] = self.BLOCK_PLACE[1]

        # Отрисовываю кораблики при условии наведения мышки на клетку игрового поля
        for x in range(10):
            for y in range(10):
                if self.block_place[0] <= mouse_pose[0] <= self.block_place[0] + self.block_size[0] and self.block_place[1] <= mouse_pose[1] <= self.block_place[1] + self.block_size[1]:
                    if selected_ships == 1:
                        self.one_deck_ship()
                        if ev.type == pygame.MOUSEBUTTONDOWN and self.accessible_area == True:
                            self.i += 1
                            if self.i  == 1: self.save_ships_log.append("{0}{1}{2}".format(x,y,1))
                            #print(self.save_ships_log)
                        if ev.type == pygame.MOUSEBUTTONUP:
                            self.i = 0

                    elif selected_ships == 2:
                        if inv_ships == False:
                            self.two_deck_ship(y)
                            if ev.type == pygame.MOUSEBUTTONDOWN and self.accessible_area == True:
                                self.i += 1
                                if self.i  == 1: self.save_ships_log.append("{0}{1}{2}".format(x,y,2))
                                #print(self.save_ships_log)
                            if ev.type == pygame.MOUSEBUTTONUP:
                                self.i = 0
                        else:
                            self.inv_two_deck_ship(x)
                            if ev.type == pygame.MOUSEBUTTONDOWN and self.accessible_area == True:
                                self.i += 1
                                if self.i  == 1: self.save_ships_log.append("{0}{1}{2}".format(x,y,3))
                                #print(self.save_ships_log)
                            if ev.type == pygame.MOUSEBUTTONUP:
                                self.i = 0

                    elif selected_ships == 3:
                        if inv_ships == False:
                            self.three_deck_ship(y)
                            if ev.type == pygame.MOUSEBUTTONDOWN and self.accessible_area == True:
                                self.i += 1
                                if self.i  == 1: self.save_ships_log.append("{0}{1}{2}".format(x,y,4))
                                #print(self.save_ships_log)
                            if ev.type == pygame.MOUSEBUTTONUP:
                                self.i = 0
                        else:
                            self.inv_three_deck_ship(x)
                            if ev.type == pygame.MOUSEBUTTONDOWN and self.accessible_area == True:
                                self.i += 1
                                if self.i  == 1: self.save_ships_log.append("{0}{1}{2}".format(x,y,5))
                                #print(self.save_ships_log)
                            if ev.type == pygame.MOUSEBUTTONUP:
                                self.i = 0

                    elif selected_ships == 4:
                        if inv_ships == False:
                            self.four_deck_ship(y)
                            if ev.type == pygame.MOUSEBUTTONDOWN and self.accessible_area == True:
                                self.i += 1
                                if self.i  == 1: self.save_ships_log.append("{0}{1}{2}".format(x,y,6))
                                #print(self.save_ships_log)
                            if ev.type == pygame.MOUSEBUTTONUP:
                                self.i = 0
                                    
                        else:
                            self.inv_four_deck_ship(x)
                            if ev.type == pygame.MOUSEBUTTONDOWN and self.accessible_area == True:
                                self.i += 1
                                if self.i  == 1: self.save_ships_log.append("{0}{1}{2}".format(x,y,7))
                                #print(self.save_ships_log)
                            if ev.type == pygame.MOUSEBUTTONUP:
                                self.i = 0
                    
                    #print("x: " + str(x) + " y: " + str(y))
                    if self.accessible_area == False:
                        self.hologram_color = display.DARK_RED
                    else:
                        self.hologram_color = display.DARK_GREEN

                self.block_place[0] += self.block_side_size
                self.block_place[0] += self.indent
            #обнуляю координаты икса, чтобы начать отрисовывать следующую строчку
            self.block_place[0] = self.BLOCK_PLACE[0]
            self.block_place[1] += self.block_side_size
            self.block_place[1] += self.indent
        self.block_place[1] = self.BLOCK_PLACE[1]

        #Отрисовываю поставленные кораблики
        for n in range(len(self.save_ships_log)):
            for x in range(10):
                for y in range(10):
                    #print("{0} = {1} + {2} + {3}".format(self.save_ships_log[n], self.save_ships_log[n][0], self.save_ships_log[n][1] ,self.save_ships_log[n][2]))
                    if x == int(self.save_ships_log[n][0]) and y == int(self.save_ships_log[n][1]):
                        #print("log_x: {0} x: {1} log_y: {2} y: {3}".format(self.save_ships_log[n][0], x, self.save_ships_log[n][1], y))
                        if int(self.save_ships_log[n][2]) == 1:
                            pygame.draw.rect(display.screen, display.TEAL, [self.block_place, self.block_size])
                        if int(self.save_ships_log[n][2]) == 2:
                            pygame.draw.rect(display.screen, display.TEAL, [self.block_place, self.block_size])
                            pygame.draw.rect(display.screen, display.TEAL, [[self.block_place[0] + self.indent + self.block_side_size, self.block_place[1]], self.block_size])
                        if int(self.save_ships_log[n][2]) == 3:
                            pygame.draw.rect(display.screen, display.TEAL, [self.block_place, self.block_size])
                            pygame.draw.rect(display.screen, display.TEAL, [[self.block_place[0], self.block_place[1] + self.indent + self.block_side_size], self.block_size])
                        if int(self.save_ships_log[n][2]) == 4:
                            pygame.draw.rect(display.screen, display.TEAL, [self.block_place, self.block_size])
                            for c in range(2):
                                pygame.draw.rect(display.screen, display.TEAL, [[self.block_place[0] + self.indent * (c+1) + self.block_side_size * (c+1), self.block_place[1]], self.block_size])
                        if int(self.save_ships_log[n][2]) == 5:
                            pygame.draw.rect(display.screen, display.TEAL, [self.block_place, self.block_size])
                            for c in range(2):
                                pygame.draw.rect(display.screen, display.TEAL, [[self.block_place[0], self.block_place[1] + self.indent * (c+1) + self.block_side_size * (c+1)], self.block_size])
                        if int(self.save_ships_log[n][2]) == 6:
                            pygame.draw.rect(display.screen, display.TEAL, [self.block_place, self.block_size])
                            for c in range(3):
                                pygame.draw.rect(display.screen, display.TEAL, [[self.block_place[0] + self.indent * (c+1) + self.block_side_size * (c+1), self.block_place[1]], self.block_size])
                        if int(self.save_ships_log[n][2]) == 7:
                            pygame.draw.rect(display.screen, display.TEAL, [self.block_place, self.block_size])
                            for c in range(3):
                                pygame.draw.rect(display.screen, display.TEAL, [[self.block_place[0], self.block_place[1] + self.indent * (c+1) + self.block_side_size * (c+1)], self.block_size])
    
                    self.block_place[0] += self.block_side_size
                    self.block_place[0] += self.indent
                #обнуляю координаты икса, чтобы начать отрисовывать следующую строчку
                self.block_place[0] = self.BLOCK_PLACE[0]
                self.block_place[1] += self.block_side_size
                self.block_place[1] += self.indent

            self.block_place[1] = self.BLOCK_PLACE[1]

    # Кнопка Back
    def Back_button_pressed_in_playing(self):
        global mouse_pose
        global in_menu
        global in_settings
        global in_playing
        global apply

        # Кнопка back
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if setings_menu.draw_button_back_out_of_settings[0] <= mouse_pose[0] <= \
                    setings_menu.draw_button_back_out_of_settings[0] + self.size_button_from_settings_menu[0] and \
                    setings_menu.draw_button_back_out_of_settings[1] <= mouse_pose[1] <= \
                    setings_menu.draw_button_back_out_of_settings[1] + self.size_button_from_settings_menu[1]:
                # Делаю невидимым меню настроек
                in_settings = False
                in_playing = False
                in_menu = True
                pygame.draw.rect(display.screen, display.WHITE,
                                 [setings_menu.draw_button_back_out_of_settings, self.size_button_from_settings_menu])
                setings_menu.text_for_main_menu_3 = main_menu.font_for_main_menu.render(
                    setings_menu.Main_menu_Button_back_out_of_settings, 1, display.WHITE, display.WHITE)
                display.screen.fill(display.WHITE)

    def Back_button_hovered_in_playing(self):
        global mouse_pose

        if setings_menu.draw_button_back_out_of_settings[0] <= mouse_pose[0] <= \
                setings_menu.draw_button_back_out_of_settings[0] + \
                self.size_button_from_settings_menu[0] and setings_menu.draw_button_back_out_of_settings[1] <= \
                mouse_pose[1] <= \
                setings_menu.draw_button_back_out_of_settings[1] + self.size_button_from_settings_menu[1]:

            if self.is_the_cursor_hovered:
                sound_play()
                self.is_the_cursor_hovered = False

            pygame.draw.rect(display.screen, display.LIGHT_GRAY,
                             [setings_menu.draw_button_back_out_of_settings, self.size_button_from_settings_menu])
            setings_menu.text_for_main_menu_3 = main_menu.font_for_main_menu.render(
                setings_menu.Main_menu_Button_back_out_of_settings,
                1, display.WHITE, display.LIGHT_GRAY)
        else:

            self.is_the_cursor_hovered = True

            pygame.draw.rect(display.screen, display.GRAY,
                             [setings_menu.draw_button_back_out_of_settings, self.size_button_from_settings_menu])
            setings_menu.text_for_main_menu_3 = main_menu.font_for_main_menu.render(
                setings_menu.Main_menu_Button_back_out_of_settings,
                1, display.WHITE, display.GRAY)

    # Кнопка открытия проводника
    def load_button_hovered_in_playing(self):
        global mouse_pose
        global in_menu
        global in_settings
        global in_playing
        global apply

        if self.draw_load_button[0] <= mouse_pose[0] <= self.draw_load_button[0] + self.size_button[0] and \
                self.draw_load_button[1] <= mouse_pose[1] <= self.draw_load_button[1] + self.size_button[1]:

            if self.is_the_cursor_hovered1:
                sound_play()
                self.is_the_cursor_hovered1 = False

            pygame.draw.rect(display.screen, display.LIGHT_GRAY, [self.draw_load_button, self.size_button])

        else:

            self.is_the_cursor_hovered1 = True

            pygame.draw.rect(display.screen, display.GRAY, [self.draw_load_button, self.size_button])

    # Кнопка Сохрания планеровки в файловую систему
    def save_button_hovered_in_playing(self):
        global mouse_pose
        global in_menu
        global in_settings
        global in_playing
        global apply

        if self.draw_save_button[0] <= mouse_pose[0] <= self.draw_save_button[0] + self.size_button[0] and \
                self.draw_save_button[1] <= mouse_pose[1] <= self.draw_save_button[1] + self.size_button[1]:

            if self.is_the_cursor_hovered2:
                sound_play()
                self.is_the_cursor_hovered2 = False

            pygame.draw.rect(display.screen, display.LIGHT_GRAY, [self.draw_save_button, self.size_button])

        else:

            self.is_the_cursor_hovered2 = True

            pygame.draw.rect(display.screen, display.GRAY, [self.draw_save_button, self.size_button])

    # Кнопка play
    def play_button_hovered_in_playing(self):
        global mouse_pose
        global in_menu
        global in_settings
        global in_playing
        global apply

        if self.draw_play_button[0] <= mouse_pose[0] <= self.draw_play_button[0] + self.size_button_from_settings_menu[
            0] and self.draw_play_button[1] <= mouse_pose[1] <= self.draw_play_button[1] + \
                self.size_button_from_settings_menu[1]:

            if self.is_the_cursor_hovered3:
                sound_play()
                self.is_the_cursor_hovered3 = False

            pygame.draw.rect(display.screen, display.LIGHT_GRAY,
                             [self.draw_play_button, self.size_button_from_settings_menu])
            self.text_for_Playing_field_play = main_menu.font_for_main_menu.render(main_menu.Main_menu_Button_play, 1,
                                                                                   display.WHITE, display.LIGHT_GRAY)

        else:

            self.is_the_cursor_hovered3 = True

            pygame.draw.rect(display.screen, display.GRAY, [self.draw_play_button, self.size_button_from_settings_menu])
            self.text_for_Playing_field_play = main_menu.font_for_main_menu.render(main_menu.Main_menu_Button_play, 1,
                                                                                   display.WHITE, display.GRAY)