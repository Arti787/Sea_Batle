import pygame
import pygame as pg
import sys

from pygame import display

pygame.init()
pygame.display.set_caption("Sea Battle")

pg.mixer.music.load('Sounds/piraty-karibskogo-morja-saundtrek-hes-a-pirate-glavnaja-tema(mp3gid.me).mp3')
pg.mixer.music.play(-1)
""""Раздел булевых переменных, отвечающих за отображение различных вещей на дисплее игрока"""

# Переменная, устанавливающая разрешение по умолчанию (если она True то разрешение ставится по умолчанию 720х720)
change = True
# Находится ли игрок в меню?
in_menu = True
# Находится ли игрок в настройках?
in_settings = False
# Находится ли игрок непосредствено игре?
in_playing = False
# Включить полноэкранный режим?
Full_screen_mode = False
# Стандартное разрешение экрана
screen_resolution_Default = 1

""""Раздел вызова всех Функций инициализаторов"""
def Update_Fuking_function():
    display.__init__()
    main_menu.__init__()



""""Раздел, хранящий переменные настройки дисплея (разрешение, цвет, форма шрифта и т.д.)"""
class Display(object):
    def __init__(self):
        global change
        global Full_screen_mode
        global screen_resolution_Default
        #разрешения экрана 
        self.Standard_Screen_Size = [[800,600],[720,720],[1024,768],[1280,1024],[1920,1080]]

        
        if change:
            screen_resolution_Default = 1
            change = False



        """Раздел Графических переменных"""
        # Цветовые Переменные
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.LIGHT_GRAY = (170, 170, 170)
        self.GRAY = (100, 100, 100)
        self.PINCK = (255, 192, 203)
        self.LIGHT_GREEN =(0,255,0)
        self.GREEN =(0,170,0)
        self.DARK_GREEN =(0,100,0)
        self.LIGHT_RED = (255,0,0)
        self.RED = (170,0,0)
        self.DARK_RED = (100,0,0)
        self.AQUA = (0, 255, 255)  # МОРСКАЯ ВОЛНА
        self.BLUE = (0, 0, 255)  # СИНИЙ
        self.FUCHSIA = (255, 0, 255)  # ФУКСИЯ
        self.GRAY = (128, 128, 128)  # СЕРЫЙ
        self.MAROON = (128, 0, 0)  # ТЕМНО-БОРДОВЫЙ
        self.NAVY_BLUE = (0, 0, 128)  # ТЕМНО-СИНИЙ
        self.OLIVE = (128, 128, 0)  # ОЛИВКОВЫЙ
        self.PURPLE = (128, 0, 128)  # ФИОЛЕТОВЫЙ
        self.SILVER = (192, 192, 192)  # СЕРЕБРЯНЫЙ
        self.TEAL = (0, 128, 128)  # ЗЕЛЕНО-ГОЛУБОЙ
        self.YELLOW = (255, 255, 0)  # ЖЕЛТЫЙ

        """Раздел Функциональных переменных"""
        # Размеры Экрана
        self.res = (self.Standard_Screen_Size[screen_resolution_Default])

        # Инициализация пространства отрисовки (полноэкранный режим или нет)
        if Full_screen_mode:
            self.screen = pygame.display.set_mode((self.res), pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode(self.res)

        # Размеры пространства отрисовки в пиксилях
        self.screen_height = self.screen.get_height()
        self.screen_width = self.screen.get_width()

        # Ожидание в милисекундах
        self.WAITING_ME = 75

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
        self.draw_button_back = (48, 10)

        # Координаты отрисовки предметов (та штука, что идёт следом очень важна для отрисовки почти всего меню настроек на основе её координат были спроектированы другие элементы раздела настроек)
        self.coordinates_of_text_for_main_menu_screen_resolution = (25, 70)


        # Шрифтовые переменные и их свойства
        self.font_for_main_menu = pygame.font.SysFont('arial', 33)
        self.font_for_Screen_resolution_settings = pygame.font.SysFont('arial', 25)

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
        global in_playing
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if self.draw_button_play[0] <= mouse_pose[0] <= self.draw_button_play[0] + self.size_button[0] and self.draw_button_play[1] <= mouse_pose[1] <= self.draw_button_play[1] + self.size_button[1]:
                in_menu = False
                in_playing = True
                display.screen.fill(display.WHITE)

                #Остановка музыки
                pg.mixer.music.pause()
                #Воспроизведение  другой
                pg.mixer.music.load('Sounds/background.mp3')
                pg.mixer.music.play(-1, 1)


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
                # Делаю видимым меню настроек
                in_settings = True
                # Цвет фона меню настроек
                display.screen.fill(display.PINCK)


    # Кнопка Quit
    def Quit_button_hovered(self):
        global mouse_pose
        if self.draw_button[0] <= mouse_pose[0] <= self.draw_button[0]+self.size_button[0] and self.draw_button[1] <= mouse_pose[1] <= self.draw_button[1]+self.size_button[1]:
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
        global in_menu
        global screen_resolution_Default

        if in_menu:
            #отрисовка кнопок старт, настроки и выход
            display.screen.blit(self.text_for_main_menu_1, (self.draw_button_play[0] + (self.size_button[0] - 53)/2  , self.draw_button_play[1]))
            display.screen.blit(self.text_for_main_menu_2, (self.draw_button_settings[0] + (self.size_button[0] - 99)/2, self.draw_button_settings[1]))
            display.screen.blit(self.text_for_main_menu, (self.draw_button[0] + (self.size_button[0] - 50)/2, self.draw_button[1]))

        if in_settings:
            # Oтрисовка кнопки Back
            display.screen.blit(settings_menu.text_for_main_menu_3, self.draw_button_back)
            # Отрисовка стрелочек выбора разрешения и текста между ними
            display.screen.blit(settings_menu.text_for_main_menu_screen_resolution,  self.coordinates_of_text_for_main_menu_screen_resolution)
            display.screen.blit(settings_menu.text_for_setting_menu_Left_Vibirator_permission, ( self.coordinates_of_text_for_main_menu_screen_resolution[0] + 200,  self.coordinates_of_text_for_main_menu_screen_resolution[1] - 3))
            display.screen.blit(settings_menu.text_for_main_menu_screen_resolution_size, ( self.coordinates_of_text_for_main_menu_screen_resolution[0] + 220,  self.coordinates_of_text_for_main_menu_screen_resolution[1]))
                        # Отрисовка правой стрелочки выбора разрешения
            if (screen_resolution_Default == 0) or (screen_resolution_Default == 1):
                display.screen.blit(settings_menu.text_for_setting_menu_Right_Vibirator_permission, (self.coordinates_of_text_for_main_menu_screen_resolution[0] + 315,self.coordinates_of_text_for_main_menu_screen_resolution[1] - 3))

            if (screen_resolution_Default == 2):
                display.screen.blit(settings_menu.text_for_setting_menu_Right_Vibirator_permission, (self.coordinates_of_text_for_main_menu_screen_resolution[0] + 325,self.coordinates_of_text_for_main_menu_screen_resolution[1] - 3))

            if (screen_resolution_Default == 3) or (screen_resolution_Default == 4):
                display.screen.blit(settings_menu.text_for_setting_menu_Right_Vibirator_permission,( self.coordinates_of_text_for_main_menu_screen_resolution[0] + 335,  self.coordinates_of_text_for_main_menu_screen_resolution[1] - 3))

            #Отрисовка текста на кнопке Apply
            display.screen.blit(settings_menu.text_for_setting_menu_Apply, (self.draw_button_back[0] + 150, self.draw_button_back[1]))
            #Отрисовка текста около выбора экранного режима
            display.screen.blit(settings_menu.text_for_main_menu_screen_mode, (self.coordinates_of_text_for_main_menu_screen_resolution[0],self.coordinates_of_text_for_main_menu_screen_resolution[1]+50))

""""---------------------------------------------Раздел проектировки меню настроек---------------------------------------------"""
class Settings_menu(object):
    global Full_screen_mode
    global in_settings
    global mouse_pose


    def __init__(self):
        global screen_resolution_Default
        # Координаты отрисовки предметов
        self.draw_button_back_out_of_settings = (10, 10)
        self.draw_button_sweech__screen_mode = (main_menu.coordinates_of_text_for_main_menu_screen_resolution[0] + 170,main_menu.coordinates_of_text_for_main_menu_screen_resolution[1]+50)


        # Текст, приминяемый в функции
        self.Main_menu_Button_back_out_of_settings = "Back"
        self.Main_menu_Button_change_screen_resolution = "Screen resolution:"
        self.Main_menu_Button_change_screen_mode = "Full screen mode:"
        self.Main_menu_Button_Left_setting_change = "<"
        self.Main_menu_Button_Right_setting_change =">"
        self.Main_menu_Button_Apply = "Apply"

        self.Main_menu_resolution_0 = "800 x 600"
        self.Main_menu_resolution_1 = "720 x 720"
        self.Main_menu_resolution_2 = "1024 x 768"
        self.Main_menu_resolution_3 = "1280 x 1024"
        self.Main_menu_resolution_4 = "1920 x 1080"


        # Номер дефолтного разрешения
        screen_resolution_Default = 1

        #Размеры Кнопки
        self.size_button = (140, 40)
        self.size_button_resolution_selection = (14, 25)
        self.size_button_swich_screen_mode = (30,30)

        #Текст и его свойства, передаваемые в функцию building_text
        self.text_for_main_menu_3 = main_menu.font_for_main_menu.render(self.Main_menu_Button_back_out_of_settings, 1, display.BLACK, display.LIGHT_GRAY)
        self.text_for_main_menu_screen_resolution = main_menu.font_for_Screen_resolution_settings.render(self.Main_menu_Button_change_screen_resolution, 1, display.BLACK, display.PINCK)
        self.text_for_main_menu_screen_mode = main_menu.font_for_Screen_resolution_settings.render(self.Main_menu_Button_change_screen_mode, 1, display.BLACK, display.PINCK)
        self.text_for_setting_menu_Left_Vibirator_permission = main_menu.font_for_main_menu.render(self.Main_menu_Button_Left_setting_change, 1, display.BLACK, display.PINCK)
        self.text_for_setting_menu_Right_Vibirator_permission = main_menu.font_for_main_menu.render(self.Main_menu_Button_Right_setting_change, 1, display.BLACK, display.PINCK)


    # Кнопка Back
    def Back_button_hovered (self):
        global mouse_pose

        if self.draw_button_back_out_of_settings[0] <= mouse_pose[0] <= self.draw_button_back_out_of_settings[0]+self.size_button[0] and self.draw_button_back_out_of_settings[1] <= mouse_pose[1] <= self.draw_button_back_out_of_settings[1]+self.size_button[1]:
            pygame.draw.rect(display.screen, display.LIGHT_GRAY, [self.draw_button_back_out_of_settings, self.size_button])
            self.text_for_main_menu_3 = main_menu.font_for_main_menu.render(self.Main_menu_Button_back_out_of_settings, 1, display.WHITE, display.LIGHT_GRAY)
        else:
            pygame.draw.rect(display.screen, display.GRAY, [self.draw_button_back_out_of_settings, self.size_button])
            self.text_for_main_menu_3 = main_menu.font_for_main_menu.render(self.Main_menu_Button_back_out_of_settings, 1, display.WHITE, display.GRAY)

    def Back_button_pressed(self):
        global mouse_pose
        global in_menu
        global in_settings
        global in_playing

        if ev.type == pygame.MOUSEBUTTONDOWN:
            if self.draw_button_back_out_of_settings[0] <= mouse_pose[0] <= self.draw_button_back_out_of_settings[0]+self.size_button[0] and self.draw_button_back_out_of_settings[1] <= mouse_pose[1] <= self.draw_button_back_out_of_settings[1]+self.size_button[1]:
                in_menu = True
                # Делаю невидимым меню настроек
                in_settings = False
                in_playing = False
                pygame.draw.rect(display.screen, display.WHITE, [self.draw_button_back_out_of_settings, self.size_button])
                self.text_for_main_menu_3 = main_menu.font_for_main_menu.render(self.Main_menu_Button_back_out_of_settings, 1, display.WHITE, display.WHITE)

                display.screen.fill(display.WHITE)


    # "Ползунки" смены разрешения
    def Left_setting_change_button_pressed(self):
        global mouse_pose
        global screen_resolution_Default

        if ev.type == pygame.MOUSEBUTTONDOWN:

            if  main_menu.coordinates_of_text_for_main_menu_screen_resolution[0] + 200 <= mouse_pose[0] <= main_menu.coordinates_of_text_for_main_menu_screen_resolution[0] + 200 + self.size_button_resolution_selection[0] and main_menu.coordinates_of_text_for_main_menu_screen_resolution[1] -3 <= mouse_pose[1] <= main_menu.coordinates_of_text_for_main_menu_screen_resolution[1] - 3 + self.size_button_resolution_selection[1]:
                if screen_resolution_Default != 0:
                    screen_resolution_Default = screen_resolution_Default - 1

                else:
                    screen_resolution_Default = 4
            # Ожидание создано для того, чтобы программа не считывала сразу несколько кликов
            pygame.time.wait(display.WAITING_ME)

                    # Это то, что будет отображаться при выборе того или иного разрешения
        if screen_resolution_Default == 0:
           display.screen.fill(display.PINCK)
           self.text_for_main_menu_screen_resolution_size = main_menu.font_for_Screen_resolution_settings.render(self.Main_menu_resolution_0, 1, display.BLACK, display.PINCK)


        elif screen_resolution_Default == 1:
            display.screen.fill(display.PINCK)
            self.text_for_main_menu_screen_resolution_size = main_menu.font_for_Screen_resolution_settings.render(self.Main_menu_resolution_1, 1, display.BLACK, display.PINCK)

        elif screen_resolution_Default == 2:
            display.screen.fill(display.PINCK)
            self.text_for_main_menu_screen_resolution_size = main_menu.font_for_Screen_resolution_settings.render(self.Main_menu_resolution_2, 1, display.BLACK, display.PINCK)

        elif screen_resolution_Default == 3:
            display.screen.fill(display.PINCK)
            self.text_for_main_menu_screen_resolution_size = main_menu.font_for_Screen_resolution_settings.render(self.Main_menu_resolution_3, 1, display.BLACK, display.PINCK)

        elif screen_resolution_Default == 4:
            display.screen.fill(display.PINCK)
            self.text_for_main_menu_screen_resolution_size = main_menu.font_for_Screen_resolution_settings.render(self.Main_menu_resolution_4, 1, display.BLACK, display.PINCK)

    def Right_setting_change_button_pressed(self):
        global mouse_pose
        global screen_resolution_Default

        if ev.type == pygame.MOUSEBUTTONDOWN:

            if (screen_resolution_Default == 0 or screen_resolution_Default == 1) and main_menu.coordinates_of_text_for_main_menu_screen_resolution[0] + 315 <= mouse_pose[0] <= main_menu.coordinates_of_text_for_main_menu_screen_resolution[0] + 315 + self.size_button_resolution_selection[0] and main_menu.coordinates_of_text_for_main_menu_screen_resolution[1] - 3 <= mouse_pose[1] <= main_menu.coordinates_of_text_for_main_menu_screen_resolution[1] - 3 + self.size_button_resolution_selection[1]:

                if screen_resolution_Default != 4:
                    screen_resolution_Default = screen_resolution_Default + 1

                else:
                    screen_resolution_Default = 0

            if screen_resolution_Default == 2 and main_menu.coordinates_of_text_for_main_menu_screen_resolution[0] + 325 <= mouse_pose[0] <= main_menu.coordinates_of_text_for_main_menu_screen_resolution[0] + 325 + self.size_button_resolution_selection[0] and main_menu.coordinates_of_text_for_main_menu_screen_resolution[1] - 3 <= mouse_pose[1] <= main_menu.coordinates_of_text_for_main_menu_screen_resolution[1] - 3 + self.size_button_resolution_selection[1]:

                if screen_resolution_Default != 4:
                    screen_resolution_Default = screen_resolution_Default + 1

                else:
                    screen_resolution_Default = 0

            if (screen_resolution_Default == 3 or screen_resolution_Default == 4) and main_menu.coordinates_of_text_for_main_menu_screen_resolution[0] + 335 <= mouse_pose[0] <= main_menu.coordinates_of_text_for_main_menu_screen_resolution[0] + 335 + self.size_button_resolution_selection[0] and main_menu.coordinates_of_text_for_main_menu_screen_resolution[1] - 3 <= mouse_pose[1] <= main_menu.coordinates_of_text_for_main_menu_screen_resolution[1] - 3 + self.size_button_resolution_selection[1]:

                if screen_resolution_Default != 4:
                    screen_resolution_Default = screen_resolution_Default + 1

                else:
                    screen_resolution_Default = 0

            # Ожидание создано для того, чтобы программа не считывала сразу несколько кликов
            pygame.time.wait(display.WAITING_ME)


    #Кнопка полноэкранного режима
    def switch_screen_mode_hovered(self):
        global mouse_pose
        global Full_screen_mode

        #Условие при котором цвет кнопки будет менятся с красного на зеленый
        if Full_screen_mode:
            if self.draw_button_sweech__screen_mode[0] <= mouse_pose[0] <= self.draw_button_sweech__screen_mode[0] + self.size_button_swich_screen_mode[0] and self.draw_button_sweech__screen_mode[1] <= mouse_pose[1] <= self.draw_button_sweech__screen_mode[1] + self.size_button_swich_screen_mode[1]:
                pygame.draw.rect(display.screen, display.LIGHT_GREEN,[self.draw_button_sweech__screen_mode, self.size_button_swich_screen_mode])
            else:
                pygame.draw.rect(display.screen, display.GREEN, [self.draw_button_sweech__screen_mode, self.size_button_swich_screen_mode])
        else:
            if self.draw_button_sweech__screen_mode[0] <= mouse_pose[0] <= self.draw_button_sweech__screen_mode[0] + self.size_button_swich_screen_mode[0] and self.draw_button_sweech__screen_mode[1] <= mouse_pose[1] <= self.draw_button_sweech__screen_mode[1] + self.size_button_swich_screen_mode[1]:
                pygame.draw.rect(display.screen, display.LIGHT_RED,[self.draw_button_sweech__screen_mode, self.size_button_swich_screen_mode])
            else:
                pygame.draw.rect(display.screen, display.RED, [self.draw_button_sweech__screen_mode, self.size_button_swich_screen_mode])

    def switch_screen_mode_pressed(self):
        global mouse_pose
        global Full_screen_mode

        if ev.type == pygame.MOUSEBUTTONDOWN:
            if Full_screen_mode:
                if self.draw_button_sweech__screen_mode[0] <= mouse_pose[0] <= self.draw_button_sweech__screen_mode[0] + self.size_button_swich_screen_mode[0] and self.draw_button_sweech__screen_mode[1] <= mouse_pose[1] <= self.draw_button_sweech__screen_mode[1] + self.size_button_swich_screen_mode[1]:
                    Full_screen_mode = False
            else:
                if self.draw_button_sweech__screen_mode[0] <= mouse_pose[0] <= self.draw_button_sweech__screen_mode[0] + self.size_button_swich_screen_mode[0] and self.draw_button_sweech__screen_mode[1] <= mouse_pose[1] <= self.draw_button_sweech__screen_mode[1] + self.size_button_swich_screen_mode[1]:
                    Full_screen_mode = True


    # Кнопка "применить"
    def Apply_button_hovered(self):
        global mouse_pose

        if main_menu.draw_button_back[0]+115 <= mouse_pose[0] <= main_menu.draw_button_back[0]+ 115 + self.size_button[0] and main_menu.draw_button_back[1] <= mouse_pose[1] <= main_menu.draw_button_back[1] + self.size_button[1]:
            pygame.draw.rect(display.screen, display.LIGHT_GRAY, [(main_menu.draw_button_back[0] + 115, main_menu.draw_button_back[1]), self.size_button])
            self.text_for_setting_menu_Apply = main_menu.font_for_main_menu.render(self.Main_menu_Button_Apply, 1, display.WHITE, display.LIGHT_GRAY)
        else:
            pygame.draw.rect(display.screen, display.GRAY,[(main_menu.draw_button_back[0] + 115, main_menu.draw_button_back[1]), self.size_button])
            self.text_for_setting_menu_Apply = main_menu.font_for_main_menu.render(self.Main_menu_Button_Apply, 1,display.WHITE, display.GRAY)

    def Apply_button_pressed(self):
        global mouse_pose
        global screen_resolution_Default

        if ev.type == pygame.MOUSEBUTTONDOWN:
            if main_menu.draw_button_back[0] + 150 <= mouse_pose[0] <= main_menu.draw_button_back[0] + 150 + self.size_button[0] and main_menu.draw_button_back[1] <= mouse_pose[1] <= main_menu.draw_button_back[1] + self.size_button[1]:
                display.res = (display.Standard_Screen_Size[screen_resolution_Default])

                Update_Fuking_function()

""""---------------------------------------------Раздел проектировки игргового поля---------------------------------------------"""
class Playing_field(object):
    def __init__(self):
        self.block_side_size = 25
        self.block_size = (self.block_side_size, self.block_side_size)
        # Отступ
        self.indent = 2
        #список с постоянными значениями координат блоков поля
        self.BLOCK_PLACE = [200, 200]
        #список с изменяющимися значениями координат блоков поля
        self.block_place = [200, 200]
        #Доступна ли клетка для размещения кораблика?
        self.accessible_area = True
        #Цвет голограммы кораблика (Зелёный/Красный)
        self.hologram_color = display.DARK_GREEN

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
        if y > y:
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

                    elif selected_ships == 2:
                        if inv_ships == False:
                            self.two_deck_ship(y)
                        else:
                            self.inv_two_deck_ship(x)

                    elif selected_ships == 3:
                        if inv_ships == False:
                            self.three_deck_ship(y)
                        else:
                            self.inv_three_deck_ship(x)

                    elif selected_ships == 4:
                        if inv_ships == False:
                            self.four_deck_ship(y)
                        else:
                            self.inv_four_deck_ship(x)
                    
                    print("x: " + str(x) + " y: " + str(y))
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



"""---------------------------------------------Объявление экземпляров класса---------------------------------------------"""
display = Display()
main_menu = Main_menu()
playing_field = Playing_field()
settings_menu = Settings_menu()

selected_ships = 1
inv_ships = False

""""---------------------------------------------Раздел системных вызовов---------------------------------------------"""
while True:
    #mouse_pose[0] - x позиция
    #mouse_pose[1] - y позиция
    mouse_pose = pygame.mouse.get_pos()

    for ev in pygame.event.get():

        if ev.type == pygame.QUIT:
            pygame.quit()

        elif ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_1:
                selected_ships = 1
                print("1")
            if ev.key == pygame.K_2:
                selected_ships = 2
                print("2")
            if ev.key == pygame.K_3:
                selected_ships = 3
                print("3")
            if ev.key == pygame.K_4:
                selected_ships = 4
                print("4")
            if ev.key == pygame.K_r:
                inv_ships = not inv_ships
                print(inv_ships)

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



    # Логика, функционирующая пока игрок в меню настроек
    if in_settings:
        # Вызов функций, отвечающих за выбор разрешения экрана
        settings_menu.Left_setting_change_button_pressed()
        settings_menu.Right_setting_change_button_pressed()
        settings_menu.switch_screen_mode_hovered()
        settings_menu.switch_screen_mode_pressed()
        #Вызов функций, отвечающих за применение изменённых настроек экрана
        settings_menu.Apply_button_hovered()
        settings_menu.Apply_button_pressed()
        #Вызов функций, отвечающих за выход из менб настроек (ПРИМЕЧАНИЕ: СЛЕДУЮЩИЙ БЛОК ФУНКЦИЙ ОБЯЗАТЕЛЬНО СТАВИТЬ В КОНЕЦ)
        settings_menu.Back_button_hovered()
        settings_menu.Back_button_pressed()

    if in_playing:
        playing_field.draw_field()


    # Вызов функции отрисовки текста на кнопках в главном меню
    main_menu.building_text()

    pygame.display.update()