import pygame

from Subjects.Scripts.Context import Context
from Subjects.Scripts.Main_menu import Main_menu
from Subjects.Scripts.Settings import Settings
from Subjects.Scripts.Playing_field import Playing_field

"""---------------------------------------------Объявление экземпляров класса---------------------------------------------"""

ctx = Context()
main_menu = Main_menu(ctx)
settings = Settings(ctx)
playing_field = Playing_field(ctx)

"""-----------------------------------------------------------------------------------------------------------------------"""

pygame.init()
pygame.display.set_caption("Sea Battle by Sergaris and GriGA")


while ctx.running:
    ctx.screen.fill(ctx.SUPER_LIGHT_YELLOW)

    for event in pygame.event.get():
        # записываем координаты курсора в context (mouse_pose[0] - x позиция, mouse_pose[1] - y позиция)
        ctx.mouse_pos = pygame.mouse.get_pos() 

        # проверить закрытие окна
        if event.type == pygame.QUIT:
            ctx.running = False

        if event.type == pygame.KEYDOWN:
            # записываем id нажатой кнопки в context
            ctx.key = event.key
            print(ctx.key)

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Запоминаем корды мышки после нажатия, чтобы в будущем не детектить повторые клики
            ctx.mem_mouse_pos = ctx.mouse_pos
            ctx.mouse_click = 1

        if ctx.key == 45 and ctx.res_id != 0:
            ctx.key = 0
            ctx.res_id -= 1
            ctx.screen = pygame.display.set_mode(ctx.screen_resolution[ctx.res_id])
            ctx.update_button_scale()
            print(ctx.res_id)

        if ctx.key == 61 and ctx.res_id != len(ctx.screen_resolution)-1:
            ctx.key = 0
            ctx.res_id += 1
            ctx.screen = pygame.display.set_mode(ctx.screen_resolution[ctx.res_id])
            ctx.update_button_scale()
            print(ctx.res_id)
        

    if ctx.in_menu == True:
        main_menu.start_button()
        main_menu.settings_button()
        main_menu.exit()
        main_menu.__init__(ctx)

    if ctx.in_settings == True:
        settings.back_button()
        settings.settings_body()
        settings.__init__(ctx)

    pygame.display.flip()
