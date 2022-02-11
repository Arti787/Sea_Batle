import pygame
import sys

from pygame import display

pygame.init()

class Display(object):
    def __init__(self):
        """Раздел Графических переменных"""
        # Цветовые Переменные
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.LIGHT_GRAY = (170, 170, 170)
        self.GRAY = (100, 100, 100)
        self.PINCK = (255, 192, 203)


        """Раздел Функциональных переменных"""
        # Размеры Экрана
        self.res = (720, 720)

        # Инициализация пространства отрисовки
        self.screen = pygame.display.set_mode(self.res)

        # Размеры пространства отрисовки в пиксилях
        self.screen_height = self.screen.get_height()
        self.screen_width = self.screen.get_width()

        # Эта штука нужна для того, чтобы надписи не смещались (выверена империсеским путём)
        self.KONST = 53.14285714285711



""""---------------------------------------------Раздел проектировки главного меню---------------------------------------------"""

class Main_menu(object):
    def __init__(self):
        #Цвет фона главного меню
        display.screen.fill(display.WHITE)

        #Размеры Кнопки
        self.size_button = (140, 40)

        #Координаты отрисовки предметов
        self.draw_button_play = ((display.screen_width / 2) - self.size_button[0] / 2, (display.screen_height / 2) - self.size_button[1] / 2 - 60)
        self.draw_button_settings = ((display.screen_width/2) - self.size_button[0]/2, (display.screen_height/2)-self.size_button[1] / 2 + 0)
        self.draw_button = ((display.screen_width / 2) - self.size_button[0] / 2, (display.screen_height / 2) - self.size_button[1] / 2 + 60)


        # Шрифтовые переменные и их свойства
        self.font_for_main_menu = pygame.font.SysFont('arial', 33)

        #Текст, приминяемый в функции
        self.Main_menu_Button_play = "Play"
        self.Main_menu_Button_settings = "Settings"
        self.Main_menu_Button_Quit = "Quit"





    # Кнопка Play
    def Start_button_hovered(self):
        global mouse_pose

        if self.draw_button_play[0] <= mouse_pose[0] <= self.draw_button_play[0]+self.size_button[0] and self.draw_button_play[1] <= mouse_pose[1] <= self.draw_button_play[1]+self.size_button[1]:
            pygame.draw.rect(display.screen, display.LIGHT_GRAY, [self.draw_button_play, self.size_button])
            self.text_for_main_menu_1 = self.font_for_main_menu.render(self.Main_menu_Button_play, 1, display.WHITE, display.LIGHT_GRAY)
        else:
            pygame.draw.rect(display.screen, display.GRAY, [self.draw_button_play, self.size_button])
            self.text_for_main_menu_1 = self.font_for_main_menu.render(self.Main_menu_Button_play, 1, display.WHITE, display.GRAY)

    def Start_button_pressed(self):
        global mouse_pose
        global in_menu
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if self.draw_button_play[0] <= mouse_pose[0] <= self.draw_button_play[0] + self.size_button[0] and self.draw_button_play[1] <= mouse_pose[1] <= self.draw_button_play[1] + self.size_button[1]:

                in_menu = False
                # Закрашиваю белым все квадраты
                self.text_for_main_menu_1 = self.font_for_main_menu.render(self.Main_menu_Button_play, 1, display.WHITE,display.WHITE)
                self.text_for_main_menu = self.font_for_main_menu.render(self.Main_menu_Button_Quit, 1, display.WHITE,display.WHITE)
                self.text_for_main_menu_2 = self.font_for_main_menu.render(self.Main_menu_Button_Quit, 1, display.WHITE,display.WHITE)

                #Закрашиваю белым все надписи
                pygame.draw.rect(display.screen, display.WHITE, [self.draw_button_settings, self.size_button])
                pygame.draw.rect(display.screen, display.WHITE, [self.draw_button, self.size_button])
                pygame.draw.rect(display.screen, display.WHITE, [self.draw_button_play, self.size_button])
                #Предметы отладки
                #self.text_for_main_menu_1 = self.font_for_main_menu.render(self.Main_menu_Button_play, 1, display.WHITE,display.PINCK)
                #print(self.draw_button_play[0]+self.draw_button_play[0]/7-(display.KONST*((display.res[0]/720) - 1)))

    # Кнопка Settings
    def Settings_button_hovered(self):
        global mouse_pose

        if self.draw_button_settings[0] <= mouse_pose[0] <= self.draw_button_settings[0] + self.size_button[0] and self.draw_button_settings[1] <= mouse_pose[1] <= self.draw_button_settings[1] + self.size_button[1]:
            pygame.draw.rect(display.screen, display.LIGHT_GRAY, [self.draw_button_settings, self.size_button])
            self.text_for_main_menu_2 = self.font_for_main_menu.render(self.Main_menu_Button_settings, 1, display.WHITE, display.LIGHT_GRAY)

        else:
            pygame.draw.rect(display.screen, display.GRAY, [self.draw_button_settings, self.size_button])
            self.text_for_main_menu_2 = self.font_for_main_menu.render(self.Main_menu_Button_settings, 1, display.WHITE, display.GRAY)

    def Settings_button_pressed(self):
        global mouse_pose
        global in_menu
        global in_settings

        if ev.type == pygame.MOUSEBUTTONDOWN:
            if self.draw_button_settings[0] <= mouse_pose[0] <= self.draw_button_settings[0] + self.size_button[0] and self.draw_button_settings[1] <= mouse_pose[1] <= self.draw_button_settings[1] + self.size_button[1]:
                in_menu = False
                # Закрашиваю белым все квадраты
                self.text_for_main_menu_1 = self.font_for_main_menu.render(self.Main_menu_Button_play, 1, display.WHITE,display.WHITE)
                self.text_for_main_menu = self.font_for_main_menu.render(self.Main_menu_Button_Quit, 1, display.WHITE,display.WHITE)
                self.text_for_main_menu_2 = self.font_for_main_menu.render(self.Main_menu_Button_Quit, 1, display.WHITE,display.WHITE)

                # Закрашиваю белым все надписи
                pygame.draw.rect(display.screen, display.WHITE, [self.draw_button_settings, self.size_button])
                pygame.draw.rect(display.screen, display.WHITE, [self.draw_button, self.size_button])
                pygame.draw.rect(display.screen, display.WHITE, [self.draw_button_play, self.size_button])

                # Делаю видимым меню настроек
                in_settings = True


    # Кнопка Quit
    def Quit_button_hovered(self):
        global mouse_pose
        if  self.draw_button[0] <= mouse_pose[0] <= self.draw_button[0]+self.size_button[0] and self.draw_button[1] <= mouse_pose[1] <= self.draw_button[1]+self.size_button[1]:
            pygame.draw.rect(display.screen, display.LIGHT_GRAY, [self.draw_button, self.size_button])
            self.text_for_main_menu = self.font_for_main_menu.render(self.Main_menu_Button_Quit, 1, display.WHITE, display.LIGHT_GRAY)
        else:
            pygame.draw.rect(display.screen, display.GRAY, [self.draw_button, self.size_button])
            self.text_for_main_menu = self.font_for_main_menu.render(self.Main_menu_Button_Quit, 1, display.WHITE, display.GRAY)

    def Quit_button_pressed(self):
        global mouse_pose
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if self.draw_button[0] <= mouse_pose[0] <= self.draw_button[0]+self.size_button[0] and self.draw_button[1] <= mouse_pose[1] <= self.draw_button[1]+self.size_button[1]:
                pygame.quit()


    #Отрисовка текста в главном меню
    def building_text(self):
        global in_settings

        display.screen.blit(self.text_for_main_menu_1, ((self.draw_button_play[0]+self.draw_button_play[0]/7)-(display.KONST*((display.res[0]/720) - 1)), self.draw_button_play[1]))
        display.screen.blit(self.text_for_main_menu_2, ((-21) + (self.draw_button_settings[0] + self.draw_button_settings[0] / 7) - (display.KONST * ((display.res[0] / 720) - 1) ), self.draw_button_settings[1]))
        display.screen.blit(self.text_for_main_menu, (self.draw_button[0]+self.draw_button[0]/7-(display.KONST*((display.res[0]/720) - 1)), self.draw_button[1]))




""""---------------------------------------------Раздел проектировки меню настроек---------------------------------------------"""

class Settings_menu(object):

    global in_settings
    global mouse_pose

    def __init__(self):
        # Координаты отрисовки предметов
        self.draw_button_back_out_of_settings = (10, 10)

        # Текст, приминяемый в функции
        self.Main_menu_Button_back_out_of_settings = "Back"

        #Размеры Кнопки
        self.size_button = (140, 40)

    def Back_button_hovered (self):
        global mouse_pose
        if self.draw_button_back_out_of_settings[0] <= mouse_pose[0] <= self.draw_button_back_out_of_settings[0]+self.size_button[0] and self.draw_button_back_out_of_settings[1] <= mouse_pose[1] <= self.draw_button_back_out_of_settings[1]+self.size_button[1]:
            pygame.draw.rect(display.screen, display.LIGHT_GRAY, [self.draw_button_back_out_of_settings, self.size_button])
            self.text_for_main_menu_3 = main_menu.font_for_main_menu.render(self.Main_menu_Button_back_out_of_settings, 1, display.WHITE, display.LIGHT_GRAY)
        else:
            pygame.draw.rect(display.screen, display.GRAY, [self.draw_button_back_out_of_settings, self.size_button])
            self.text_for_main_menu_3 = main_menu.font_for_main_menu.render(self.Main_menu_Button_back_out_of_settings, 1, display.WHITE, display.GRAY)







""""---------------------------------------------Раздел проектировки игргового поля---------------------------------------------"""

class Playing_field(object):
    def __init__(self):
        self.block_size = (30, 30)                




""""---------------------------------------------Раздел системных вызовов---------------------------------------------"""

"""Объявление экземпляров класса"""
display = Display()
main_menu = Main_menu()
playing_field = Playing_field()
settings_menu = Settings_menu()


#Находится ли игрок в меню?
global in_menu
in_menu = True
#Находится ли игрок в настройках?
global in_settings
in_settings = False

while True:
    #mouse_pose[0] - x позиция
    #mouse_pose[1] - y позиция
    mouse_pose = pygame.mouse.get_pos()

    for ev in pygame.event.get():

        if ev.type == pygame.QUIT:
            pygame.quit()

    #Логика, функционирующая пока игрок в главном меню
    if in_menu:
        main_menu.Quit_button_hovered()
        main_menu.Quit_button_pressed()

        main_menu.Settings_button_hovered()
        main_menu.Settings_button_pressed()

        # Второй условный оператор нужен для того, чтобы невозникало бага, связанного с невозможностью исчезновения обной из кнопок
        if in_menu:
            main_menu.Start_button_hovered()
            main_menu.Start_button_pressed()

        # Вызов функции отрисовки текста на кнопках в главном меню
        main_menu.building_text()

    # Логика, функционирующая пока игрок в меню настроек
    if in_settings:
        settings_menu.Back_button_hovered()




    pygame.display.update()

