import pygame
from ..Main_menu import Main_menu
from ..Display import Display

main_menu = Main_menu()
display = Display()

class Setings_menu(object):
    global Full_screen_mode
    global in_settings
    global mouse_pose

    def __init__(self):
        global screen_resolution_Default



        # Координаты отрисовки предметов
        self.draw_button_back_out_of_settings = (10, 10)
        self.draw_button_sweech__screen_mode = (main_menu.coordinates_of_text_for_main_menu_screen_resolution[0] + 170,
                                                main_menu.coordinates_of_text_for_main_menu_screen_resolution[1] + 50)

        # Текст, приминяемый в функции
        self.Main_menu_Button_back_out_of_settings = "Back"
        self.Main_menu_Button_change_screen_mode = "Full screen mode:"
        self.Main_menu_Button_Left_setting_change = "<"
        self.Main_menu_Button_Right_setting_change = ">"
        self.Main_menu_Button_Apply = "Apply"
        self.Main_menu_Button_change_screen_resolution = "Screen resolution:"
        self.Main_menu_resolution_0 = "800 x 600"
        self.Main_menu_resolution_1 = "720 x 720"
        self.Main_menu_resolution_2 = "1024 x 768"
        self.Main_menu_resolution_3 = "1280 x 1024"
        self.Main_menu_resolution_4 = "1920 x 1080"

        self.Main_menu_Button_set_volume = "Music: "
        self.Main_menu_Button_turn_down_the_sound = "-"
        self.Main_menu_Button_turn_up_the_sound = "+"

        self.Main_menu_Button_set_volume_effect = "Effects: "

        self.Text_for_messagebox_title = "Changing game settings"
        self.Text_for_messagebox_message = "Apply Changes?"

        # Дефолтные настройки
        screen_resolution_Default = 1
        self.game_sound_Default = 0.05
        self.game_sound_effect_Default = 0.03

        # Размеры Кнопки
        self.size_button = (140, 40)
        self.size_button_resolution_selection = (14, 25)
        self.size_button_swich_screen_mode = (30, 30)
        self.size_button_sound_selection = (self.size_button_resolution_selection[0], self.size_button_resolution_selection[1])


        # Текст и его свойства, передаваемые в функцию building_text
        self.text_for_main_menu_3 = main_menu.font_for_main_menu.render(self.Main_menu_Button_back_out_of_settings, 1,
                                                                        display.BLACK, display.LIGHT_GRAY)
        self.text_for_main_menu_screen_resolution = main_menu.font_for_Screen_resolution_settings.render(
            self.Main_menu_Button_change_screen_resolution, 1, display.BLACK, display.PINCK)
        self.text_for_main_menu_screen_mode = main_menu.font_for_Screen_resolution_settings.render(
            self.Main_menu_Button_change_screen_mode, 1, display.BLACK, display.PINCK)
        self.text_for_setting_menu_Left_Vibirator_permission = main_menu.font_for_main_menu.render(
            self.Main_menu_Button_Left_setting_change, 1, display.BLACK, display.PINCK)
        self.text_for_setting_menu_Right_Vibirator_permission = main_menu.font_for_main_menu.render(
            self.Main_menu_Button_Right_setting_change, 1, display.BLACK, display.PINCK)

        self.text_for_setting_menu_set_volume = main_menu.font_for_Screen_resolution_settings.render(
            self.Main_menu_Button_set_volume, 1,
            display.BLACK, display.PINCK)
        self.text_for_setting_menu_turn_down_the_sound = main_menu.font_for_main_menu.render(
            self.Main_menu_Button_turn_down_the_sound, 1, display.BLACK, display.PINCK)
        self.text_for_setting_menu_turn_up_the_sound = main_menu.font_for_main_menu.render(
            self.Main_menu_Button_turn_up_the_sound, 1, display.BLACK, display.PINCK)

        self.text_for_setting_menu_set_volume_for_effect = main_menu.font_for_Screen_resolution_settings.render(
            self.Main_menu_Button_set_volume_effect, 1,
            display.BLACK, display.PINCK)

        #переменные, отвечеющие за то, чтобы программа проигрывала только один звук нажатия
        self.is_the_cursor_hovered = True
        self.is_the_cursor_hovered1 = True
        self.is_the_cursor_hovered2 = True

    # Кнопка Back
    def Back_button_hovered(self):
        global mouse_pose

        if self.draw_button_back_out_of_settings[0] <= mouse_pose[0] <= self.draw_button_back_out_of_settings[0] + \
                self.size_button[0] and self.draw_button_back_out_of_settings[1] <= mouse_pose[1] <= \
                self.draw_button_back_out_of_settings[1] + self.size_button[1]:

            if self.is_the_cursor_hovered:
                sound_play()
                self.is_the_cursor_hovered = False

            pygame.draw.rect(display.screen, display.LIGHT_GRAY,
                             [self.draw_button_back_out_of_settings, self.size_button])
            self.text_for_main_menu_3 = main_menu.font_for_main_menu.render(self.Main_menu_Button_back_out_of_settings,
                                                                            1, display.WHITE, display.LIGHT_GRAY)
        else:

            self.is_the_cursor_hovered = True

            pygame.draw.rect(display.screen, display.GRAY, [self.draw_button_back_out_of_settings, self.size_button])
            self.text_for_main_menu_3 = main_menu.font_for_main_menu.render(self.Main_menu_Button_back_out_of_settings,
                                                                            1, display.WHITE, display.GRAY)

    def Back_button_pressed(self):
        global mouse_pose
        global in_menu
        global in_settings
        global in_playing
        global apply

        global Save_Changes

        if ev.type == pygame.MOUSEBUTTONDOWN:
            if self.draw_button_back_out_of_settings[0] <= mouse_pose[0] <= self.draw_button_back_out_of_settings[0] + \
                    self.size_button[0] and self.draw_button_back_out_of_settings[1] <= mouse_pose[1] <= \
                    self.draw_button_back_out_of_settings[1] + self.size_button[1]:

                if Save_Changes:
                    slave = checkung_change_of_user(self.Text_for_messagebox_title, self.Text_for_messagebox_message)
                else:
                    slave = False

                if slave:

                    # приминяю текущие настройки
                    self.temporary_storage_of_sound_level = settings_menu.game_sound_Default
                    Update_Fuking_function()
                    apply = True

                    display.res = (display.Standard_Screen_Size[screen_resolution_Default])
                    if apply == False:
                        self.game_sound_Default = main_menu.temporary_storage_of_sound_level
                        Update_Fuking_volume()
                    apply = False

                    in_menu = True
                    # Делаю невидимым меню настроек
                    in_settings = False
                    in_playing = False
                    pygame.draw.rect(display.screen, display.WHITE,
                                     [self.draw_button_back_out_of_settings, self.size_button])
                    self.text_for_main_menu_3 = main_menu.font_for_main_menu.render(
                        self.Main_menu_Button_back_out_of_settings, 1, display.WHITE, display.WHITE)

                    display.screen.fill(display.WHITE)

                else:

                    display.res = (display.Standard_Screen_Size[screen_resolution_Default])
                    if apply == False:
                        self.game_sound_Default = main_menu.temporary_storage_of_sound_level
                        Update_Fuking_volume()
                    apply = False

                    in_menu = True
                    # Делаю невидимым меню настроек
                    in_settings = False
                    in_playing = False
                    pygame.draw.rect(display.screen, display.WHITE,
                                     [self.draw_button_back_out_of_settings, self.size_button])
                    self.text_for_main_menu_3 = main_menu.font_for_main_menu.render(
                        self.Main_menu_Button_back_out_of_settings, 1, display.WHITE, display.WHITE)

                    display.screen.fill(display.WHITE)

    # "Ползунки" смены разрешения
    def Left_setting_change_button_pressed(self):
        global mouse_pose
        global screen_resolution_Default
        global Save_Changes

        if ev.type == pygame.MOUSEBUTTONDOWN:

            if main_menu.coordinates_of_text_for_main_menu_screen_resolution[0] + 200 <= mouse_pose[0] <= \
                    main_menu.coordinates_of_text_for_main_menu_screen_resolution[0] + 200 + \
                    self.size_button_resolution_selection[0] and \
                    main_menu.coordinates_of_text_for_main_menu_screen_resolution[1] - 3 <= mouse_pose[1] <= \
                    main_menu.coordinates_of_text_for_main_menu_screen_resolution[1] - 3 + \
                    self.size_button_resolution_selection[1]:
                Save_Changes = True

                if screen_resolution_Default != 0:
                    screen_resolution_Default = screen_resolution_Default - 1

                else:
                    screen_resolution_Default = 4
            # Ожидание создано для того, чтобы программа не считывала сразу несколько кликов
            pygame.time.wait(display.WAITING_ME)

            # Это то, что будет отображаться при выборе того или иного разрешения
        if screen_resolution_Default == 0:
            display.screen.fill(display.PINCK)
            self.text_for_main_menu_screen_resolution_size = main_menu.font_for_Screen_resolution_settings.render(
                self.Main_menu_resolution_0, 1, display.BLACK, display.PINCK)


        elif screen_resolution_Default == 1:
            display.screen.fill(display.PINCK)
            self.text_for_main_menu_screen_resolution_size = main_menu.font_for_Screen_resolution_settings.render(
                self.Main_menu_resolution_1, 1, display.BLACK, display.PINCK)

        elif screen_resolution_Default == 2:
            display.screen.fill(display.PINCK)
            self.text_for_main_menu_screen_resolution_size = main_menu.font_for_Screen_resolution_settings.render(
                self.Main_menu_resolution_2, 1, display.BLACK, display.PINCK)

        elif screen_resolution_Default == 3:
            display.screen.fill(display.PINCK)
            self.text_for_main_menu_screen_resolution_size = main_menu.font_for_Screen_resolution_settings.render(
                self.Main_menu_resolution_3, 1, display.BLACK, display.PINCK)

        elif screen_resolution_Default == 4:
            display.screen.fill(display.PINCK)
            self.text_for_main_menu_screen_resolution_size = main_menu.font_for_Screen_resolution_settings.render(
                self.Main_menu_resolution_4, 1, display.BLACK, display.PINCK)

    def Right_setting_change_button_pressed(self):
        global mouse_pose
        global screen_resolution_Default
        global Save_Changes

        if ev.type == pygame.MOUSEBUTTONDOWN:

            if (screen_resolution_Default == 0 or screen_resolution_Default == 1) and \
                    main_menu.coordinates_of_text_for_main_menu_screen_resolution[0] + 315 <= mouse_pose[0] <= \
                    main_menu.coordinates_of_text_for_main_menu_screen_resolution[0] + 315 + \
                    self.size_button_resolution_selection[0] and \
                    main_menu.coordinates_of_text_for_main_menu_screen_resolution[1] - 3 <= mouse_pose[1] <= \
                    main_menu.coordinates_of_text_for_main_menu_screen_resolution[1] - 3 + \
                    self.size_button_resolution_selection[1]:

                Save_Changes = True

                if screen_resolution_Default != 4:
                    screen_resolution_Default = screen_resolution_Default + 1

                else:
                    screen_resolution_Default = 0

            if screen_resolution_Default == 2 and main_menu.coordinates_of_text_for_main_menu_screen_resolution[
                0] + 325 <= mouse_pose[0] <= main_menu.coordinates_of_text_for_main_menu_screen_resolution[0] + 325 + \
                    self.size_button_resolution_selection[0] and \
                    main_menu.coordinates_of_text_for_main_menu_screen_resolution[1] - 3 <= mouse_pose[1] <= \
                    main_menu.coordinates_of_text_for_main_menu_screen_resolution[1] - 3 + \
                    self.size_button_resolution_selection[1]:

                if screen_resolution_Default != 4:
                    screen_resolution_Default = screen_resolution_Default + 1

                else:
                    screen_resolution_Default = 0

            if (screen_resolution_Default == 3 or screen_resolution_Default == 4) and \
                    main_menu.coordinates_of_text_for_main_menu_screen_resolution[0] + 335 <= mouse_pose[0] <= \
                    main_menu.coordinates_of_text_for_main_menu_screen_resolution[0] + 335 + \
                    self.size_button_resolution_selection[0] and \
                    main_menu.coordinates_of_text_for_main_menu_screen_resolution[1] - 3 <= mouse_pose[1] <= \
                    main_menu.coordinates_of_text_for_main_menu_screen_resolution[1] - 3 + \
                    self.size_button_resolution_selection[1]:

                if screen_resolution_Default != 4:
                    screen_resolution_Default = screen_resolution_Default + 1

                else:
                    screen_resolution_Default = 0

            # Ожидание создано для того, чтобы программа не считывала сразу несколько кликов
            pygame.time.wait(display.WAITING_ME)

    # Кнопка полноэкранного режима
    def switch_screen_mode_hovered(self):
        global mouse_pose
        global Full_screen_mode

        # Условие при котором цвет кнопки будет менятся с красного на зеленый
        if Full_screen_mode:
            if self.draw_button_sweech__screen_mode[0] <= mouse_pose[0] <= self.draw_button_sweech__screen_mode[0] + \
                    self.size_button_swich_screen_mode[0] and self.draw_button_sweech__screen_mode[1] <= mouse_pose[
                1] <= self.draw_button_sweech__screen_mode[1] + self.size_button_swich_screen_mode[1]:

                if self.is_the_cursor_hovered1:
                    sound_play()
                    self.is_the_cursor_hovered1 = False

                pygame.draw.rect(display.screen, display.LIGHT_GREEN,
                                 [self.draw_button_sweech__screen_mode, self.size_button_swich_screen_mode])
            else:

                self.is_the_cursor_hovered1 = True

                pygame.draw.rect(display.screen, display.GREEN,
                                 [self.draw_button_sweech__screen_mode, self.size_button_swich_screen_mode])
        else:
            if self.draw_button_sweech__screen_mode[0] <= mouse_pose[0] <= self.draw_button_sweech__screen_mode[0] + \
                    self.size_button_swich_screen_mode[0] and self.draw_button_sweech__screen_mode[1] <= mouse_pose[
                1] <= self.draw_button_sweech__screen_mode[1] + self.size_button_swich_screen_mode[1]:

                if self.is_the_cursor_hovered1:
                    sound_play()
                    self.is_the_cursor_hovered1 = False

                pygame.draw.rect(display.screen, display.LIGHT_RED,
                                 [self.draw_button_sweech__screen_mode, self.size_button_swich_screen_mode])
            else:

                self.is_the_cursor_hovered1 = True

                pygame.draw.rect(display.screen, display.RED,
                                 [self.draw_button_sweech__screen_mode, self.size_button_swich_screen_mode])

    def switch_screen_mode_pressed(self):
        global mouse_pose
        global Full_screen_mode
        global Save_Changes

        if ev.type == pygame.MOUSEBUTTONDOWN:
            if Full_screen_mode:
                if self.draw_button_sweech__screen_mode[0] <= mouse_pose[0] <= self.draw_button_sweech__screen_mode[0] + \
                        self.size_button_swich_screen_mode[0] and self.draw_button_sweech__screen_mode[1] <= mouse_pose[
                    1] <= self.draw_button_sweech__screen_mode[1] + self.size_button_swich_screen_mode[1]:
                    Full_screen_mode = False
                    Save_Changes = True

            else:
                if self.draw_button_sweech__screen_mode[0] <= mouse_pose[0] <= self.draw_button_sweech__screen_mode[0] + \
                        self.size_button_swich_screen_mode[0] and self.draw_button_sweech__screen_mode[1] <= mouse_pose[
                    1] <= self.draw_button_sweech__screen_mode[1] + self.size_button_swich_screen_mode[1]:
                    Full_screen_mode = True
                    Save_Changes = True

    # Кнопка "применить"
    def Apply_button_hovered(self):
        global mouse_pose

        if main_menu.draw_button_back[0] + 115 <= mouse_pose[0] <= main_menu.draw_button_back[0] + 115 + \
                self.size_button[0] and main_menu.draw_button_back[1] <= mouse_pose[1] <= main_menu.draw_button_back[
            1] + self.size_button[1]:

            if self.is_the_cursor_hovered2:
                sound_play()
                self.is_the_cursor_hovered2 = False

            pygame.draw.rect(display.screen, display.LIGHT_GRAY,
                             [(main_menu.draw_button_back[0] + 115, main_menu.draw_button_back[1]), self.size_button])
            self.text_for_setting_menu_Apply = main_menu.font_for_main_menu.render(self.Main_menu_Button_Apply, 1,
                                                                                   display.WHITE, display.LIGHT_GRAY)
        else:

            self.is_the_cursor_hovered2 = True

            pygame.draw.rect(display.screen, display.GRAY,
                             [(main_menu.draw_button_back[0] + 115, main_menu.draw_button_back[1]), self.size_button])
            self.text_for_setting_menu_Apply = main_menu.font_for_main_menu.render(self.Main_menu_Button_Apply, 1,
                                                                                   display.WHITE, display.GRAY)

    def Apply_button_pressed(self):
        global mouse_pose
        global screen_resolution_Default
        global apply
        global Save_Changes
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if main_menu.draw_button_back[0] + 150 <= mouse_pose[0] <= main_menu.draw_button_back[0] + 150 + \
                    self.size_button[0] and main_menu.draw_button_back[1] <= mouse_pose[1] <= \
                    main_menu.draw_button_back[1] + self.size_button[1]:
                self.temporary_storage_of_sound_level = settings_menu.game_sound_Default
                Update_Fuking_function()
                apply = True
                Save_Changes = False

    # "Ползунки" смены уровня звука
    def Button_turn_down_the_sound(self):
        global Save_Changes
        global mouse_pose
        global screen_resolution_Default

        if ev.type == pygame.MOUSEBUTTONDOWN:
            if main_menu.coordinates_of_text_for_main_menu_selection_volume[0] + 100 <= mouse_pose[0] <= \
                    main_menu.coordinates_of_text_for_main_menu_selection_volume[0] + 100 + \
                    self.size_button_sound_selection[0] and \
                    main_menu.coordinates_of_text_for_main_menu_selection_volume[1] + 30 <= mouse_pose[1] <= \
                    main_menu.coordinates_of_text_for_main_menu_screen_resolution[1] + 100 + \
                    self.size_button_sound_selection[1]:

                Save_Changes = True

                if self.game_sound_Default > 0:
                    self.game_sound_Default -= 0.01
                    Update_Fuking_volume()

    def Button_turn_up_the_sound(self):
        global mouse_pose
        global screen_resolution_Default
        global Save_Changes

        if ev.type == pygame.MOUSEBUTTONDOWN:
            if main_menu.coordinates_of_text_for_main_menu_selection_volume[0] + 185 <= mouse_pose[0] <= \
                    main_menu.coordinates_of_text_for_main_menu_selection_volume[0] + 185 + \
                    self.size_button_sound_selection[0] and \
                    main_menu.coordinates_of_text_for_main_menu_selection_volume[1] + 30 <= mouse_pose[1] <= \
                    main_menu.coordinates_of_text_for_main_menu_screen_resolution[1] + 100 + \
                    self.size_button_sound_selection[1]:

                Save_Changes = True

                if self.game_sound_Default < 1:
                    self.game_sound_Default += 0.01
                    Update_Fuking_volume()



   # "Ползунки" смены уровня звука эффектов
    def Button_turn_down_the_sound_of_effect(self):
        global Save_Changes
        global mouse_pose
        global screen_resolution_Default

        if ev.type == pygame.MOUSEBUTTONDOWN:
            if main_menu.coordinates_of_text_for_main_menu_selection_volume[0] + 100 <= mouse_pose[0] <= \
                    main_menu.coordinates_of_text_for_main_menu_selection_volume[0] + 100 + \
                    self.size_button_sound_selection[0] and \
                    main_menu.coordinates_of_text_for_main_menu_selection_volume[1] + 80 <= mouse_pose[1] <= \
                    main_menu.coordinates_of_text_for_main_menu_screen_resolution[1] + 150 + \
                    self.size_button_sound_selection[1]:

                Save_Changes = True

                if self.game_sound_effect_Default > 0:
                    self.game_sound_effect_Default -= 0.01
                    Update_Fuking_volume()

    def Button_turn_up_the_sound_of_effect(self):
        global mouse_pose
        global screen_resolution_Default
        global Save_Changes

        if ev.type == pygame.MOUSEBUTTONDOWN:
            if main_menu.coordinates_of_text_for_main_menu_selection_volume[0] + 185 <= mouse_pose[0] <= \
                    main_menu.coordinates_of_text_for_main_menu_selection_volume[0] + 185 + \
                    self.size_button_sound_selection[0] and \
                    main_menu.coordinates_of_text_for_main_menu_selection_volume[1] + 80 <= mouse_pose[1] <= \
                    main_menu.coordinates_of_text_for_main_menu_screen_resolution[1] + 150 + \
                    self.size_button_sound_selection[1]:

                Save_Changes = True

                if self.game_sound_effect_Default < 1:
                    self.game_sound_effect_Default += 0.01
                    Update_Fuking_volume()