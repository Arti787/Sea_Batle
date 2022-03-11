from tkinter import *
from tkinter import messagebox as mb

class Context():
    def __init__(self):
        self.mouse_pos = []
        # Переменная, устанавливающая разрешение по умолчанию (если она True то разрешение ставится по умолчанию 720х720)
        self.change = True
        # Находится ли игрок в меню?
        self.in_menu = True
        # Находится ли игрок в настройках?
        self.in_settings = False
        # Находится ли игрок непосредствено игре?
        self.in_playing = False
        # Включить полноэкранный режим?
        self.Full_screen_mode = False
        # Стандартное разрешение экрана
        self.screen_resolution_Default = 1
        # Приминить значение?
        self.apply = False
        # Сохранены ли изменения?
        self.Save_Changes = False
        # Выбранный тип кораблика
        self.selected_ships = 1
        # Перевёрнут ли кораблик?
        self.inv_ships = False
        # Если равно 1, то было нажатие кнопкой мыши
        self.click = 0

    # вызов меню: -да -нет, где title - заголовок, а message - вопрос
    def checkung_change_of_user(title, message):
        answer = mb.askyesno(
            title=title,
            message=message)
        return answer
