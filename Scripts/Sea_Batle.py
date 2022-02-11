import pygame
import sys

pygame.init()

class Main_menu(object):
    def __init__(self):
        #Цветовые Переменные
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.LIGHT_GRAY = (170, 170, 170)
        self.GRAY = (100, 100, 100)
        self.PINCK = (255, 192, 203)

        #Размеры Экрана
        self.res = (720,720)

        #Инициализация пространства отрисовки
        self.screen = pygame.display.set_mode(self.res)


        self.screen_height = self.screen.get_height()
        self.screen_width = self.screen.get_width()

        #Размеры Кнопки
        self.size_button = (140,40)
        self.draw_button = ((self.screen_width/2)-self.size_button[0]/2,(self.screen_height/2)-self.size_button[1]/2)



    def start_button_hovered(self):
        global mouse_pose
        if self.draw_button[0] <= mouse_pose[0] <= self.draw_button[0]+self.size_button[0] and self.draw_button[1] <= mouse_pose[1] <= self.draw_button[1]+self.size_button[1]:
            pygame.draw.rect(self.screen, self.LIGHT_GRAY, [self.draw_button, self.size_button])

        else:
            pygame.draw.rect(self.screen,self.GRAY,[self.draw_button,self.size_button])

    def start_button_pressed(self):
        global mouse_pose
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if self.draw_button[0] <= mouse_pose[0] <= self.draw_button[0]+self.size_button[0] and self.draw_button[1] <= mouse_pose[1] <= self.draw_button[1]+self.size_button[1]:
                pygame.quit()
                #pygame.draw.rect(screen, (255, 192, 203), [width_start, height_start, 140, 40])

main_menu = Main_menu()

while True:
    #mouse_pose[0] - x позиция
    #mouse_pose[1] - y позиция
    mouse_pose = pygame.mouse.get_pos()

    for ev in pygame.event.get():

        if ev.type == pygame.QUIT:
            pygame.quit()

    main_menu.start_button_hovered()
    main_menu.start_button_pressed()


    pygame.display.update()
