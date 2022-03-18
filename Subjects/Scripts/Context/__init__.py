import pygame

class Context():
    def __init__(self):
        print("Context")

        """Раздел Графических переменных"""
        # Цветовые Переменные
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.LIGHT_GRAY = (170, 170, 170)
        self.PINCK = (255, 192, 203)
        self.LIGHT_GREEN = (0, 255, 0)
        self.GREEN = (0, 170, 0)
        self.DARK_GREEN = (0, 100, 0)
        self.LIGHT_RED = (255, 0, 0)
        self.RED = (170, 0, 0) 
        self.DARK_RED = (100, 0, 0)
        self.AQUA = (0, 255, 255)  # МОРСКАЯ ВОЛНА
        self.BLUE = (0, 0, 255)  
        self.FUCHSIA = (255, 0, 255)  
        self.GRAY = (128, 128, 128)  
        self.MAROON = (128, 0, 0)  # ТЕМНО-БОРДОВЫЙ
        self.NAVY_BLUE = (0, 0, 128)  # ТЕМНО-СИНИЙ
        self.OLIVE = (128, 128, 0)  # ОЛИВКОВЫЙ
        self.PURPLE = (128, 0, 128)  
        self.SILVER = (192, 192, 192)  # СЕРЕБРЯНЫЙ
        self.TEAL = (0, 128, 128)  # ЗЕЛЕНО-ГОЛУБОЙ
        self.YELLOW = (255, 255, 0)  
        
        """Раздел Функциональных переменных"""
        # позиция курсора
        self.mouse_pos = []
        # переменная, помнящая предыдущию позицию курсора
        self.mem_mouse_pos = []
        # разрешения экрана
        self.screen_resolution = [[800, 600], [720, 720], [1024, 768], [1280, 1024], [1920, 1080]]
        # id текущего разрешения экрана
        self.res_id = 0
        # id нажатой кнопки
        self.key = 0
        # если = 1, то был клик мышкой
        self.mouse_click = 0

        # находиться ли игрок в меню?
        self.in_menu = True
        # Находится ли игрок в настройках?
        self.in_settings = False
        # Находится ли игрок непосредствено в игре?
        self.in_game = False