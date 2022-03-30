import pygame
class Settings():
    def __init__(self, context):
        self.ctx = context

        # отступ кнопки от края
        self.indent = self.ctx.button_height * self.ctx.nominal_indent / self.ctx.nominal_button_height

        # корды отрисовки кнопки
        self.back_button_cords = [0 + self.indent,0 + self.indent]

        # Текст кнопки "back"
        self.back_text = self.ctx.main_font.render("back", True , self.ctx.WHITE)

        # Текст "Теущее разрешение"
        self.resolution_text = self.ctx.main_font.render("back", True , self.ctx.WHITE, self.ctx.SEC_BUTTON_COLLOR)


    def back_button(self):
        if self.back_button_cords[0] < self.ctx.mouse_pos[0] < self.back_button_cords[0] + self.ctx.button_size[0] and self.back_button_cords[1] < self.ctx.mouse_pos[1] < self.back_button_cords[1] + self.ctx.button_size[1]:
            pygame.draw.rect(self.ctx.screen, self.ctx.SEC_BUTTON_COLLOR_HOWER, [self.back_button_cords, self.ctx.button_size])

            # если было нажатие
            if self.ctx.mouse_click == 1 and self.ctx.mouse_pos == self.ctx.mem_mouse_pos:
                self.ctx.mouse_click = 0
                print("клик")
                self.ctx.in_settings = False
                self.ctx.in_menu = True
                
        else:
            pygame.draw.rect(self.ctx.screen, self.ctx.SEC_BUTTON_COLLOR, [self.back_button_cords, self.ctx.button_size])

        # отрисовываю текст по центру кнопки
        self.ctx.screen.blit(self.back_text, self.back_text.get_rect(center=([self.back_button_cords[0] + self.ctx.button_size[0] / 2, self.back_button_cords[1] + self.ctx.button_size[1] / 2])))

    def settings_body(self):
        print()
        pygame.draw.rect(self.ctx.screen, self.ctx.SEC_BUTTON_COLLOR, ((self.ctx.screen_resolution[self.ctx.res_id][0]/2 - self.ctx.button_size[0] / 2, self.ctx.button_size[1] + self.indent), self.ctx.button_size))
        self.ctx.screen.blit(self.resolution_text, self.resolution_text.get_rect(center=(self.ctx.screen_resolution[self.ctx.res_id][0]/2 , self.ctx.button_size[1]*1.5 + self.indent) ))


