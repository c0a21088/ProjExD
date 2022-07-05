import pygame as pg
import sys

def main():
    clock = pg.time.Clock()

    pg.display.set_caption("逃げろ！こうかとん")
    screen_sfc = pg.display.set_mode((1600, 900)) #surface
    screen_rct = screen_sfc.get_rect()            #rect

    bgimg_sfc = pg.image.load("../ex03/fig/pg_bg.jpg") #surface
    bgimg_rct = bgimg_sfc.get_rect()              #rect
    screen_sfc.blit(bgimg_sfc,bgimg_rct)

    kk_sfc = pg.image.load("../ex03/fig/6.png")
    kk_sfc = pg.transform.rotozoom(kk_sfc, 0, 2.0)
    kk_rct = kk_sfc.get_rect()
    kk_rct.center = 900, 400
    

    while True:
        screen_sfc.blit(bgimg_sfc,bgimg_rct)

        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return

        key_states = pg.key.get_pressed()
        if key_states[pg.K_UP] == True:
            kk_rct.centery -=1
        if key_states[pg.K_DOWN] == True:
            kk_rct.centery +=1
        if key_states[pg.K_LEFT] == True:
            kk_rct.centerx -=1
        if key_states[pg.K_RIGHT] == True:
            kk_rct.centerx +=1
        screen_sfc.blit(kk_sfc, kk_rct)

        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()