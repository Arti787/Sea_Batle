import pygame
import sys


# Переменные
Width = 700
Height = 800
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)



if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((Width, Height))
    pygame.display.set_caption("Морской бой")

    #СОЗДАЮ ЭКЗЕМПЛЯР КЛАССА

    while True:


        for event in pygame.event.get(): # Закрытие программы при нажатии на крестик
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()



