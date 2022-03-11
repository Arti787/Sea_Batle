import pygame

from ..Display import Display
from ...Sounds import Sound_control
from ..Setings_menu import Setings_menu
from ..Context import Context

display = Display()
sound_control = Sound_control()
setings_menu = Setings_menu()
context = Context()

class Main_menu(object):
    def __init__(self):
        # Цвет фона главного меню
        display.screen.fill(display.WHITE)
        # Размеры Кнопки
        self.size_button = (140, 40)
        # Координаты отрисовки предметов
        self.draw_button_play = ((display.screen_width / 2) - self.size_button[0] / 2, (display.screen_height / 2) - self.size_button[1] / 2 - 60)
        self.draw_button_settings = ( (display.screen_width / 2) - self.size_button[0] / 2, (display.screen_height / 2) - self.size_button[1] / 2 + 0)
        self.draw_button = ((display.screen_width / 2) - self.size_button[0] / 2, (display.screen_height / 2) - self.size_button[1] / 2 + 60)
        self.draw_button_back = (48, 10)
        # Координаты отрисовки предметов (та штука, что идёт следом очень важна для отрисовки почти всего меню настроек на основе её координат были спроектированы другие элементы раздела настроек)
        self.coordinates_of_text_for_main_menu_screen_resolution = (25, 70)
        self.coordinates_of_text_for_main_menu_selection_volume = (self.coordinates_of_text_for_main_menu_screen_resolution[0], self.coordinates_of_text_for_main_menu_screen_resolution[1] + 80)
        # Шрифтовые переменные и их свойства
        self.font_for_main_menu = pygame.font.SysFont('arial', 33)
        self.font_for_Screen_resolution_settings = pygame.font.SysFont('arial', 25)
        # Текст, приминяемый в функции
        self.Main_menu_Button_play = "Play"
        self.Main_menu_Button_settings = "Settings"
        self.Main_menu_Button_Quit = "Quit"

        self.Text_for_quit_the_game_title = "Exit the game"
        self.Text_for_quit_the_game_message = "Already leaving?"

        self.check = False


    # Кнопка Play
    def Start_button(self):
        if self.draw_button_play[0] <= context.mouse_pos[0] <= self.draw_button_play[0] + self.size_button[0] and self.draw_button_play[1] <= context.mouse_pos[1] <= self.draw_button_play[1] + self.size_button[1]:
            #Если был клик
            if context.click == 1:
                context.in_menu = False
                context.in_playing = True
                display.screen.fill(display.WHITE)

            else:
                pygame.draw.rect(display.screen, display.LIGHT_GRAY, [self.draw_button_play, self.size_button])
                self.text_for_main_menu_1 = self.font_for_main_menu.render(self.Main_menu_Button_play, 1, display.WHITE, display.LIGHT_GRAY)
        else:
            pygame.draw.rect(display.screen, display.GRAY, [self.draw_button_play, self.size_button])
            self.text_for_main_menu_1 = self.font_for_main_menu.render(self.Main_menu_Button_play, 1, display.WHITE, display.GRAY)
            self.is_the_cursor_hovered = True

    # Кнопка Settings
    def Settings_button(self):
        if self.draw_button_settings[0] <= context.mouse_pos[0] <= self.draw_button_settings[0] + self.size_button[0] and self.draw_button_settings[1] <= context.mouse_pos[1] <= self.draw_button_settings[1] + self.size_button[1]:
            #Если был клик
            if context.click == 1:
                context.in_menu = False
                # Делаю видимым меню настроек
                context.in_settings = True
                # Цвет фона меню настроек
                display.screen.fill(display.PINCK)
                self.temporary_storage_of_sound_level = setings_menu.game_sound_Default

            pygame.draw.rect(display.screen, display.LIGHT_GRAY, [self.draw_button_settings, self.size_button])
            self.text_for_main_menu_2 = self.font_for_main_menu.render(self.Main_menu_Button_settings, 1, display.WHITE, display.LIGHT_GRAY)

        else:

            pygame.draw.rect(display.screen, display.GRAY, [self.draw_button_settings, self.size_button])
            self.text_for_main_menu_2 = self.font_for_main_menu.render(self.Main_menu_Button_settings, 1, display.WHITE, display.GRAY)
      

    # Кнопка Quit
    def Quit_button(self):
        if self.draw_button[0] <= context.mouse_pos[0] <= self.draw_button[0] + self.size_button[0] and self.draw_button[1] <= context.mouse_pos[1] <= self.draw_button[1] + self.size_button[1]:

            if context.click == 1:
                self.check = context.checkung_change_of_user(self.Text_for_quit_the_game_title, self.Text_for_quit_the_game_message)
                if self.check:
                    pygame.quit()

            pygame.draw.rect(display.screen, display.LIGHT_GRAY, [self.draw_button, self.size_button])
            self.text_for_main_menu = self.font_for_main_menu.render(self.Main_menu_Button_Quit, 1, display.WHITE, display.LIGHT_GRAY)
        else:

            pygame.draw.rect(display.screen, display.GRAY, [self.draw_button, self.size_button])
            self.text_for_main_menu = self.font_for_main_menu.render(self.Main_menu_Button_Quit, 1, display.WHITE, display.GRAY)
                