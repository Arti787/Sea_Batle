import pygame

from Subjects.Scripts.Context import Context
from Subjects.Scripts.Main_menu import Main_menu
from Subjects.Scripts.Settings import Settings
from Subjects.Scripts.Playing_field import Playing_field

"""---------------------------------------------Объявление экземпляров класса---------------------------------------------"""

context = Context()
main_menu = Main_menu()
settings = Settings()
playing_field = Playing_field()

"""-----------------------------------------------------------------------------------------------------------------------"""

pygame.init()
pygame.display.set_caption("Sea Battle by Sergaris and GriGA")
screen = pygame.display.set_mode(context.screen_resolution[context.res_id])
running = True

tmp = 0


while running:
    screen.fill(context.WHITE)

    for event in pygame.event.get():
        # записываем координаты курсора в context (mouse_pose[0] - x позиция, mouse_pose[1] - y позиция)
        context.mouse_pos = pygame.mouse.get_pos() 

        # проверить закрытие окна
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            # записываем id нажатой кнопки в context
            context.key = event.key

        if event.type == pygame.MOUSEBUTTONDOWN:
            context.mem_mouse_pos = context.mouse_pos
            context.mouse_click += 1

        if event.type == pygame.MOUSEBUTTONUP:
            context.mouse_click = 0

        settings.test()



    pygame.display.flip()
