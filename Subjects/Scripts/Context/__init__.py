import pygame
pygame.init()

class Context():
    def __init__(self):
        """Раздел Графических переменных"""
        # Цветовые Переменные
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)

        self.LIGHT_GRAY = (170, 170, 170)

        self.RED = (210, 60, 60)
        self.LIGHT_RED = (255, 60, 60)

        self.GREEN = (90, 170, 80)
        self.LIGHT_GREEN = (90, 210, 80)

        self.YELLOW = (240, 200, 100)
        self.LIGHT_YELLOW = (255, 200, 40)
        self.SUPER_LIGHT_YELLOW = (255, 255, 180)

        self.ORANGE = (255, 98, 0)
        self.LIGHT_ORANGE = (255, 138, 62)
        self.SUPER_LIGHT_ORANGE = (255, 169, 116)

        self.TEAL = (0, 165, 129)  # Бирюзовый
        self.LIGHT_TEAL = (48, 211, 176)  # Светло бирюзовый

        self.MAIN_BUTTON_COLLOR = self.TEAL

        self.MAIN_BUTTON_COLLOR_HOWER = self.LIGHT_TEAL

        self.SEC_BUTTON_COLLOR = self.ORANGE

        self.SEC_BUTTON_COLLOR_HOWER = self.LIGHT_ORANGE

         

        
        
          
        
        """Раздел Функциональных переменных"""
        # разрешения экрана
        self.screen_resolution = [[854, 480], [1280,720], [1920, 1080]]
        # id текущего разрешения экрана
        self.res_id = 0
        # главная переменная экрана
        self.screen = pygame.display.set_mode(self.screen_resolution[self.res_id]) 
        # включить полноэкранный режим ?
        self.full_screen = False

        # позиция курсора
        self.mouse_pos = []
        # переменная, помнящая предыдущию позицию курсора
        self.mem_mouse_pos = []

        # номинальная ширина кнопки
        self.nominal_button_width = 160
        # номинальная высота кнопки
        self.nominal_button_height = 40

        # номинальный отступ между всеми кнопками
        self.nominal_indent = 7
        
        # коефицент для пропорционального соотношения номинальной высоты кнопки к высоте выбранного разрешения экрана
        self.button_height_coef = (self.nominal_button_height*100/self.nominal_button_width) / 100 

        # коефицент для пропорционального соотношения номинальной ширины кнопки к ширине выбранного разрешения экрана
        self.button_width_coef = 100 * self.nominal_button_width / self.screen_resolution[0][0]

        # ширина кнопки
        self.button_width = self.button_width_coef / (100 / self.screen_resolution[self.res_id][0])
        # высота кнопки
        self.button_height = self.button_width * self.button_height_coef

        # размер кнопки
        self.button_size = [self.button_width, self.button_height]

        # шрифт, используемый в программе
        self.main_font = pygame.font.SysFont('Impact', int(self.button_height * 0.85))
        
        # id нажатой клавиши
        self.key = 0
        # если = 1, то был клик мышкой
        self.mouse_click = 0

        # Если True, то выполняется основной цикл в main.py
        self.running = True

        # находиться ли игрок в меню?
        self.in_menu = True
        # Находится ли игрок в настройках?
        self.in_settings = False
        # Находится ли игрок в игровом меню, где реализован основной геймплей?
        self.in_game = False

    def update_button_scale(self):

        self.button_height_coef = (40*100/self.nominal_button_width) / 100

        self.button_width_coef = 100 * self.nominal_button_width / self.screen_resolution[0][0]

        self.button_width = self.button_width_coef / (100 / self.screen_resolution[self.res_id][0])

        self.button_height = self.button_width * self.button_height_coef

        self.button_size = [self.button_width, self.button_height]

        self.main_font = pygame.font.SysFont('Impact', int(self.button_height * 0.85))

