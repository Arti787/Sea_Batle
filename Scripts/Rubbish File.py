import pygame
import pygame as pg
import sys

from tkinter import *
from tkinter import messagebox as mb
from pygame import display

WIDTH = 360
HEIGHT = 480
FPS = 30

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()


#pg.mixer.music.load('Sounds/piraty-karibskogo-morja-saundtrek-hes-a-pirate-glavnaja-tema(mp3gid.me).mp3')
#pg.mixer.music.play(-1)
pg.mixer.music.set_volume(0.5)

pg.mixer.music.load('Sounds/piraty-karibskogo-morja-saundtrek-hes-a-pirate-glavnaja-tema(mp3gid.me).mp3')
pg.mixer.music.play()

s = pygame.mixer.Sound('Sounds/for_buttons/3.mp3')
s.set_volume(0.3)

# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for ev in pygame.event.get():
        # check for closing window
        if ev.type == pygame.QUIT:
            running = False

        elif ev.type == pygame.KEYDOWN:

            if ev.key == pygame.K_3:
                running = False

            if ev.key == pygame.K_1:

                s.play()







    # Обновление

    # Рендеринг
    screen.fill(BLACK)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()