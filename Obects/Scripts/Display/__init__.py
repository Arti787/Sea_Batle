import pygame

from ..Context import Context
context = Context()

class Display(object):
    def __init__(self):
        # разрешения экрана
        self.Standard_Screen_Size = [[800, 600], [720, 720], [1024, 768], [1280, 1024], [1920, 1080]]

        if context.change:
            context.screen_resolution_Default = 1
            context.change = False

        """Раздел Графических переменных"""
        # Цветовые Переменные
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.LIGHT_GRAY = (170, 170, 170)
        self.GRAY = (100, 100, 100)
        self.PINCK = (255, 192, 203)
        self.LIGHT_GREEN = (0, 255, 0)
        self.GREEN = (0, 170, 0)
        self.DARK_GREEN = (0, 100, 0)
        self.LIGHT_RED = (255, 0, 0)
        self.RED = (170, 0, 0)
        self.DARK_RED = (100, 0, 0)
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
        self.res = (self.Standard_Screen_Size[context.screen_resolution_Default])

        # Инициализация пространства отрисовки (полноэкранный режим или нет)
        if context.Full_screen_mode:
            self.screen = pygame.display.set_mode((self.res), pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode(self.res)

        # Размеры пространства отрисовки в пиксилях
        self.screen_height = self.screen.get_height()
        self.screen_width = self.screen.get_width()

        # Ожидание в милисекундах
        self.WAITING_ME = 75

        # объявление спец. функции, отвечающей за проигрывание звука при наведении на объекты (+ настройка параметров звука)
        self.sound_for_change_button = pygame.mixer.Sound('Sounds/for_buttons/3.mp3')
        self.sound_for_change_button.set_volume(0.03)