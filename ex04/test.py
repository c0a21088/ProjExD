import pygame as pg
import sys


def main():
    clock = pg.time.Clock()

    pg.display.set_caption("初めてのpygame") #surface
    screen = pg.display.set_mode((800,600)) #surface
    
    tori_img = pg.image.load("../ex03/fig/10.jpg") #surface
    tori_img = pg.transform.rotozoom(tori_img, 0, 2.0)
    tori_rect = tori_img.get_rect()            #rect       
    tori_rect.center = 700, 400
    screen.blit(tori_img, tori_rect)
    pg.display.update()

    clock.tick(0.2) #フレームレート

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
