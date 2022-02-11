import pygame
import sys

pygame.init()

#Цветовые Переменные
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_GRAY = (170, 170, 170)
GRAY = (100, 100, 100)
PINCK = (255, 192, 203)


#Размеры Кнопки
size_button = (140,40)

#Размеры Экрана
res = (720,720)

#Инициализация пространства отрисовки
screen = pygame.display.set_mode(res)


screen_height = screen.get_height()
screen_width = screen.get_width()



def start_button_hovered():
    global mouse_pose
    width_start = (width/2)-70
    height_start = (height/2)-20
    if width_start <= mouse_pose[0] <= width_start+140 and height_start <= mouse_pose[1] <= height_start+40:
        pygame.draw.rect(screen, LIGHT_GRAY, [width_start, height_start, 140, 40])

    else:
        pygame.draw.rect(screen,GRAY,[width_start,height_start,140,40])

def start_button_pressed():
    global mouse_pose
    width_start = (width/2)-70
    height_start = (height/2)-20
    if ev.type == pygame.MOUSEBUTTONDOWN:
        if width_start <= mouse_pose[0] <= width_start+140 and height_start <= mouse_pose[1] <= height_start+40:
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
