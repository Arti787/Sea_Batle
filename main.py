import pygame

from pygame import display

from Obects.Scripts.Display import Display
from Obects.Scripts.Main_menu import Main_menu
from Obects.Scripts.Setings_menu import Setings_menu
from Obects.Scripts.Playing_field import Playing_field
from Obects.Scripts.Context import Context

pygame.init()
pygame.display.set_caption("Sea Battle by Sergaris and GriGA")


""""Раздел булевых переменных, отвечающих за отображение различных вещей на дисплее игрока"""


""""---------------------------------------------Раздел специальных функций---------------------------------------------"""


# Перезапуск инициализирующих функций для применения новых настроек
def Update_Fuking_function():
    global Save_Changes
    Save_Changes = False

    display.__init__()
    main_menu.__init__()
    playing_field.__init__()
    Update_Fuking_volume()


# установка необходимого уровн звука
def Update_Fuking_volume():
    pygame.mixer.music.set_volume(setings_menu.game_sound_Default)
    display.sound_for_change_button.set_volume(setings_menu.game_sound_effect_Default)


def sound_play():
    display.sound_for_change_button.play()

# Отрисовка текста
def building_text():

    # отрисовка текста в меню
    if context.in_menu:
        # отрисовка кнопок старт, настроки и выход
        display.screen.blit(main_menu.text_for_main_menu_1, (main_menu.draw_button_play[0] + (main_menu.size_button[0] - 53) / 2, main_menu.draw_button_play[1]))
        display.screen.blit(main_menu.text_for_main_menu_2, (main_menu.draw_button_settings[0] + (main_menu.size_button[0] - 99) / 2, main_menu.draw_button_settings[1]))

        display.screen.blit(main_menu.text_for_main_menu, (main_menu.draw_button[0] + (main_menu.size_button[0] - 50) / 2, main_menu.draw_button[1]))

    # отрисовка текста в настройках
    if context.in_settings:
        # Oтрисовка кнопки Back
        display.screen.blit(setings_menu.text_for_main_menu_3, main_menu.draw_button_back)
        # Отрисовка стрелочек выбора разрешения и текста между ними
        display.screen.blit(setings_menu.text_for_main_menu_screen_resolution,
                            main_menu.coordinates_of_text_for_main_menu_screen_resolution)
        display.screen.blit(setings_menu.text_for_setting_menu_Left_Vibirator_permission, (
            main_menu.coordinates_of_text_for_main_menu_screen_resolution[0] + 200,
            main_menu.coordinates_of_text_for_main_menu_screen_resolution[1] - 3))
        display.screen.blit(setings_menu.text_for_main_menu_screen_resolution_size, (
            main_menu.coordinates_of_text_for_main_menu_screen_resolution[0] + 220,
            main_menu.coordinates_of_text_for_main_menu_screen_resolution[1]))
        # Отрисовка правой стрелочки выбора разрешения
        if (context.screen_resolution_Default == 0) or (context.screen_resolution_Default == 1):
            display.screen.blit(setings_menu.text_for_setting_menu_Right_Vibirator_permission, (
                main_menu.coordinates_of_text_for_main_menu_screen_resolution[0] + 315,
                main_menu.coordinates_of_text_for_main_menu_screen_resolution[1] - 3))

        if (context.screen_resolution_Default == 2):
            display.screen.blit(setings_menu.text_for_setting_menu_Right_Vibirator_permission, (
                main_menu.coordinates_of_text_for_main_menu_screen_resolution[0] + 325,
                main_menu.coordinates_of_text_for_main_menu_screen_resolution[1] - 3))

        if (context.screen_resolution_Default == 3) or (context.screen_resolution_Default == 4):
            display.screen.blit(setings_menu.text_for_setting_menu_Right_Vibirator_permission, (
                main_menu.coordinates_of_text_for_main_menu_screen_resolution[0] + 335,
                main_menu.coordinates_of_text_for_main_menu_screen_resolution[1] - 3))

        # Отрисовка текста на кнопке Apply
        display.screen.blit(setings_menu.text_for_setting_menu_Apply,
                            (main_menu.draw_button_back[0] + 150, main_menu.draw_button_back[1]))
        # Отрисовка текста около выбора экранного режима
        display.screen.blit(setings_menu.text_for_main_menu_screen_mode, (
            main_menu.coordinates_of_text_for_main_menu_screen_resolution[0],
            main_menu.coordinates_of_text_for_main_menu_screen_resolution[1] + 50))

        # отрисовка состояния звука
        main_menu.text_for_setting_menu_sound_percentage = main_menu.font_for_Screen_resolution_settings.render(
            str(round(setings_menu.game_sound_Default * 100)) + " %", 1, display.BLACK, display.PINCK)

        main_menu.text_for_setting_menu_effect_percentage = main_menu.font_for_Screen_resolution_settings.render(
            str(round(setings_menu.game_sound_effect_Default * 100)) + " %", 1, display.BLACK, display.PINCK)


        # Отрисовка прибавления и убавления звука
        display.screen.blit(setings_menu.text_for_setting_menu_set_volume, (
            main_menu.coordinates_of_text_for_main_menu_selection_volume[0],
            main_menu.coordinates_of_text_for_main_menu_screen_resolution[1] + 100))
        display.screen.blit(setings_menu.text_for_setting_menu_turn_down_the_sound, (
            main_menu.coordinates_of_text_for_main_menu_selection_volume[0] + 100,
            main_menu.coordinates_of_text_for_main_menu_screen_resolution[1] + 95))
        display.screen.blit(main_menu.text_for_setting_menu_sound_percentage, (
            main_menu.coordinates_of_text_for_main_menu_selection_volume[0] + 125,
            main_menu.coordinates_of_text_for_main_menu_screen_resolution[1] + 102))
        display.screen.blit(setings_menu.text_for_setting_menu_turn_up_the_sound, (
            main_menu.coordinates_of_text_for_main_menu_selection_volume[0] + 185,
            main_menu.coordinates_of_text_for_main_menu_screen_resolution[1] + 95))

        display.screen.blit(setings_menu.text_for_setting_menu_set_volume_for_effect, (main_menu.coordinates_of_text_for_main_menu_selection_volume[0],main_menu.coordinates_of_text_for_main_menu_screen_resolution[1] + 150))
        display.screen.blit(setings_menu.text_for_setting_menu_turn_down_the_sound, (main_menu.coordinates_of_text_for_main_menu_selection_volume[0] + 100,main_menu.coordinates_of_text_for_main_menu_screen_resolution[1] + 145))
        display.screen.blit(main_menu.text_for_setting_menu_effect_percentage, (main_menu.coordinates_of_text_for_main_menu_selection_volume[0] + 125,main_menu.coordinates_of_text_for_main_menu_screen_resolution[1] + 152))
        display.screen.blit(setings_menu.text_for_setting_menu_turn_up_the_sound, (main_menu.coordinates_of_text_for_main_menu_selection_volume[0] + 185,main_menu.coordinates_of_text_for_main_menu_screen_resolution[1] + 145))

    # отрисовка текста на игровом поле
    if context.in_playing:
        # Oтрисовка кнопки Back
        display.screen.blit(setings_menu.text_for_main_menu_3, (
        main_menu.draw_button_back[0] + (20 - 20 * playing_field.now_Screen_Size[1] / playing_field.now_Screen_Size[0]),
        main_menu.draw_button_back[1] + (20 - 20 * playing_field.now_Screen_Size[1] / playing_field.now_Screen_Size[0])))
        # Oтрисовка кнопки play
        display.screen.blit(playing_field.text_for_Playing_field_play, (playing_field.draw_play_button[0] + 44,playing_field.draw_play_button[1] + (20 - 20 *playing_field.now_Screen_Size[1] /playing_field.now_Screen_Size[0])))


"""---------------------------------------------Объявление экземпляров класса---------------------------------------------"""
display = Display()
main_menu = Main_menu()
playing_field = Playing_field()
setings_menu = Setings_menu()
context = Context()

""""---------------------------------------------Раздел системных вызовов---------------------------------------------"""
if __name__ == "__main__":
    while True:
        # mouse_pos[0] - x позиция
        # mouse_pos[1] - y позиция
        context.mouse_pos = pygame.mouse.get_pos()

        for ev in pygame.event.get():

            # итерирует click пока нажата кнопка мыши
            if ev.type == pygame.MOUSEBUTTONDOWN:
                context.click += 1
            # обнуляет click при отпускании
            if ev.type == pygame.MOUSEBUTTONUP:
                context.click = 0

            if ev.type == pygame.QUIT:
                pygame.quit()

            elif ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_1:
                    context.selected_ships = 1
                    print("1")
                if ev.key == pygame.K_2:
                    context.selected_ships = 2
                    print("2")
                if ev.key == pygame.K_3:
                    context.selected_ships = 3
                    print("3")
                if ev.key == pygame.K_4:
                    context.selected_ships = 4
                    print("4")
                if ev.key == pygame.K_r:
                    inv_ships = not inv_ships
                    print(inv_ships)
        # Логика, функционирующая пока игрок в главном меню
        if context.in_menu:

            main_menu.Quit_button()

            main_menu.Settings_button()

            # Второй условный оператор нужен для того, чтобы невозникало бага, связанного с невозможностью исчезновения обной из кнопок
            if context.in_menu:
                main_menu.Start_button()


        # Логика, функционирующая пока игрок в меню настроек
        if context.in_settings:
            # Вызов функций, отвечающих за выбор разрешения экрана
            setings_menu.Left_setting_change_button_pressed()
            setings_menu.Right_setting_change_button_pressed()
            setings_menu.switch_screen_mode_hovered()
            setings_menu.switch_screen_mode_pressed()
            # Вызов функций, отвечающих за применение изменённых настроек экрана
            setings_menu.Apply_button_hovered()
            setings_menu.Apply_button_pressed()
            # Вызов функций, отвечающих за выход из менб настроек (ПРИМЕЧАНИЕ: СЛЕДУЮЩИЙ БЛОК ФУНКЦИЙ ОБЯЗАТЕЛЬНО СТАВИТЬ В КОНЕЦ)
            setings_menu.Back_button_hovered()
            setings_menu.Back_button_pressed()
            setings_menu.Button_turn_down_the_sound()
            setings_menu.Button_turn_up_the_sound()
            setings_menu.Button_turn_down_the_sound_of_effect()
            setings_menu.Button_turn_up_the_sound_of_effect()

        if context.in_playing:
            playing_field.draw_field()
            playing_field.load_button_hovered_in_playing()
            playing_field.save_button_hovered_in_playing()
            playing_field.play_button_hovered_in_playing()
            playing_field.Back_button_hovered_in_playing()
            playing_field.Back_button_pressed_in_playing()

        # Вызов функции отрисовки текста на кнопках в главном меню
        building_text()
        pygame.display.update()