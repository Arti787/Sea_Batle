import pygame as pg
import sys

pg.init()
sc = pg.display.set_mode((400, 300))

pg.mixer.music.load('Sounds/piraty-karibskogo-morja-saundtrek-hes-a-pirate-glavnaja-tema(mp3gid.me).mp3')
pg.mixer.music.play()

pg.mixer.music.set_volume(0.2)
while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()

        elif i.type == pg.K_1:
            if i.key == pg.K_1:
                pg.mixer.music.pause()

            elif i.key == pg.K_2:
                pg.mixer.music.set_volume(30)
            elif i.key == pg.K_3:
                pg.mixer.music.unpause()
                # pygame.mixer.music.play()




    pg.time.delay(20)