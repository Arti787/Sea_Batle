import pygame
import sys
# Переменные
Width = 700
Height = 800
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)




class Button():

    def __init__(self):
        self.Nemo_Nom_Nom_Button = pygame.image.load("Images/Button.jpg")

    def output(self, screen):
        self.screen = screen



if __name__ == '__main__':


    pygame.init()
    screen = pygame.display.set_mode((Width, Height))
    pygame.display.set_caption("Летающие тарелки")

    #СОЗДАЮ ЭКЗЕМПЛЯР КЛАССА
    ButtonCL = Button()

    while True:

        ButtonCL.output(screen) #Вызов метода отрисовки кнопки


        for event in pygame.event.get(): # Зкрытие программы при нажатии на крестик
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
