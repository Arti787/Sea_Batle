import pygame
pygame.init()

class Sound_control():

    def main_menu():
        pygame.mixer.music.load('Sea_Batle/Sounds/background.mp3')
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.05)
