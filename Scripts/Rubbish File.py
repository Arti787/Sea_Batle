import pygame
import sys

sc = pygame.display.set_mode((720, 720))
sc.fill((0, 0, 0))



Image = pygame.image.load('images/Papka.png')
Rect_Of_Image = Image.get_rect()

def r():
    sc.blit(Image, Rect_Of_Image)

while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
    pygame.time.delay(20)
    r()

