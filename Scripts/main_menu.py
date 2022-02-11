import pygame
import sys

pygame.init()

#Цветовые Переменные
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_GRAY = (170, 170, 170)
GRAY = (100, 100, 100)
PINCK = (255, 192, 203)

#Размеры Экрана
res = (720,720)

#Инициализация пространства отрисовки
screen = pygame.display.set_mode(res)


screen_height = screen.get_height()
screen_width = screen.get_width()

#Размеры Кнопки
size_button = (140,40)
draw_button = ((screen_width/2)-size_button[0]/2,(screen_height/2)-size_button[1]/2)



def start_button_hovered():
    global mouse_pose
    if draw_button[0] <= mouse_pose[0] <= draw_button[0]+size_button[0] and draw_button[1] <= mouse_pose[1] <= draw_button[1]+size_button[1]:
        pygame.draw.rect(screen, LIGHT_GRAY, [draw_button, size_button])

    else:
        pygame.draw.rect(screen,GRAY,[draw_button,size_button])

def start_button_pressed():
    global mouse_pose
    if ev.type == pygame.MOUSEBUTTONDOWN:
        if draw_button[0] <= mouse_pose[0] <= draw_button[0]+size_button[0] and draw_button[1] <= mouse_pose[1] <= draw_button[1]+size_button[1]:
            pygame.quit()
            #pygame.draw.rect(screen, (255, 192, 203), [width_start, height_start, 140, 40])


while True:
    #mouse_pose[0] - x позиция
    #mouse_pose[1] - y позиция
    mouse_pose = pygame.mouse.get_pos()

    for ev in pygame.event.get():

        if ev.type == pygame.QUIT:
            pygame.quit()

    start_button_hovered()
    start_button_pressed()


    pygame.display.update()
