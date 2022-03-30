import pygame

class Main_menu():
    def __init__(self, context):
        self.ctx = context

        # корды отрисовки кнопки
        self.button_cords = [ self.ctx.screen_resolution[self.ctx.res_id][0]/2 - self.ctx.button_size[0]/2, self.ctx.screen_resolution[self.ctx.res_id][1]/2 - self.ctx.button_size[1]/2]
        
        #print(self.ctx.button_size)

        # отступ между кнопками
        self.indent = self.ctx.button_height * self.ctx.nominal_indent / self.ctx.nominal_button_height  + self.ctx.button_size[1]


        # Текст кнопки start"
        self.start_text = self.ctx.main_font.render("start", True , self.ctx.WHITE)

        # Текст кнопки "settings"
        self.settings_text = self.ctx.main_font.render("settings", True , self.ctx.WHITE)

        # Текст кнопки "exit"
        self.exit_text = self.ctx.main_font.render("exit", True , self.ctx.WHITE)
        


    def start_button(self):
        #print(self.ctx.mouse_click)

        if self.button_cords[0] < self.ctx.mouse_pos[0] < self.button_cords[0] + self.ctx.button_size[0] and self.button_cords[1] - self.indent < self.ctx.mouse_pos[1] < self.button_cords[1] - self.indent + self.ctx.button_size[1]:
            pygame.draw.rect(self.ctx.screen, self.ctx.MAIN_BUTTON_COLLOR_HOWER, [[self.button_cords[0], self.button_cords[1] - self.indent], self.ctx.button_size])

            # если было нажатие
            if self.ctx.mouse_click == 1 and self.ctx.mouse_pos == self.ctx.mem_mouse_pos:
                self.ctx.mouse_click = 0
                print("клик")
        else:
            pygame.draw.rect(self.ctx.screen, self.ctx.MAIN_BUTTON_COLLOR, [[self.button_cords[0], self.button_cords[1] - self.indent], self.ctx.button_size])

        # отрисовываю текст по центру кнопки
        self.ctx.screen.blit(self.start_text, self.start_text.get_rect(center=([self.button_cords[0] + self.ctx.button_size[0] / 2, self.button_cords[1] - self.indent + self.ctx.button_size[1] / 2])))

    
    def settings_button(self):
        if self.button_cords[0] < self.ctx.mouse_pos[0] < self.button_cords[0] + self.ctx.button_size[0] and self.button_cords[1] < self.ctx.mouse_pos[1] < self.button_cords[1] + self.ctx.button_size[1]:
            pygame.draw.rect(self.ctx.screen, self.ctx.MAIN_BUTTON_COLLOR_HOWER, [self.button_cords, self.ctx.button_size])

            # если было нажатие
            if self.ctx.mouse_click == 1 and self.ctx.mouse_pos == self.ctx.mem_mouse_pos:
                self.ctx.mouse_click = 0
                print("клик")
                self.ctx.in_menu = False
                self.ctx.in_settings = True
        else:
            pygame.draw.rect(self.ctx.screen, self.ctx.MAIN_BUTTON_COLLOR, [self.button_cords, self.ctx.button_size])

        # отрисовываю текст по центру кнопки
        self.ctx.screen.blit(self.settings_text, self.settings_text.get_rect(center=([self.button_cords[0] + self.ctx.button_size[0] / 2, self.button_cords[1] + self.ctx.button_size[1] / 2])))
            

    def exit (self):
        if self.button_cords[0] < self.ctx.mouse_pos[0] < self.button_cords[0] + self.ctx.button_size[0] and self.button_cords[1] + self.indent < self.ctx.mouse_pos[1] < self.button_cords[1] + self.indent + self.ctx.button_size[1]:
            pygame.draw.rect(self.ctx.screen, self.ctx.SEC_BUTTON_COLLOR_HOWER, [[self.button_cords[0], self.button_cords[1] + self.indent], self.ctx.button_size])

            # если было нажатие
            if self.ctx.mouse_click == 1 and self.ctx.mouse_pos == self.ctx.mem_mouse_pos:
                self.ctx.mouse_click = 0
                print("клик")
                self.ctx.running = False
        else:
           pygame.draw.rect(self.ctx.screen, self.ctx.SEC_BUTTON_COLLOR, [[self.button_cords[0], self.button_cords[1] + self.indent], self.ctx.button_size]) 

        # отрисовываю текст по центру кнопки
        self.ctx.screen.blit(self.exit_text, self.exit_text.get_rect(center=([self.button_cords[0] + self.ctx.button_size[0] / 2, self.button_cords[1] + self.indent  + self.ctx.button_size[1] / 2])))
        