import pygame as pg
import sys
import random


class Screen:
    def __init__(self, title, wh:tuple, img_fname):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh)       # Surface
        self.rct = self.sfc.get_rect()               # Rect
        self.bgimg_sfc = pg.image.load(img_fname)    # Surface
        self.bgimg_rct = self.bgimg_sfc.get_rect()   # Rect


    def blit(self):
        self.sfc.blit(self.bgimg_sfc, self.bgimg_rct)


class Bird:
    def __init__(self, img_fname, size, xy:tuple):
        self.sfc = pg.image.load(img_fname)    # Surface
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size)  # Surface
        self.rct = self.sfc.get_rect()          # Rect
        self.rct.center = xy

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr: Screen):
        key_states = pg.key.get_pressed() # 辞書
        if key_states[pg.K_UP]:
            self.rct.centery -= 1
        if key_states[pg.K_DOWN]: 
            self.rct.centery += 1
        if key_states[pg.K_LEFT]: 
            self.rct.centerx -= 1
        if key_states[pg.K_RIGHT]: 
            self.rct.centerx += 1
        # 練習7
        if check_bound(self.rct, scr.rct) != (1, 1): # 領域外だったら
            if key_states[pg.K_UP]    == True: 
                self.rct.centery += 1
            if key_states[pg.K_DOWN]  == True: 
                self.rct.centery -= 1
            if key_states[pg.K_LEFT]  == True: 
                self.rct.centerx += 1
            if key_states[pg.K_RIGHT] == True: 
                self.rct.centerx -= 1
        self.blit(scr)
        

class Bomb:
    def __init__(self, color:tuple, size, vxy:tuple, scr:Screen):
        self.sfc = pg.Surface((2*size, 2*size)) # Surface
        self.sfc.set_colorkey((0, 0, 0)) 
        pg.draw.circle(self.sfc, color, (size, size), size)
        self.rct = self.sfc.get_rect() # Rect
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = +1, +1 # 練習6

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        # 練習6
        self.rct.move_ip(self.vx, self.vy)
        # 練習5
        self.sfc.blit(self.sfc, self.rct)
        # 練習7
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr)



def main():
    clock = pg.time.Clock()

    # 練習1：スクリーンと背景画像
    # pg.display.set_caption("逃げろ！こうかとん")
    # screen_sfc = pg.display.set_mode((1600, 900)) # Surface
    # screen_rct = screen_sfc.get_rect()            # Rect
    # bgimg_sfc = pg.image.load("fig/pg_bg.jpg")    # Surface
    # bgimg_rct = bgimg_sfc.get_rect()              # Rect
    # screen_sfc.blit(bgimg_sfc, bgimg_rct)
    scr = Screen("逃げろ！こうかとん",(1600,900),"fig/pg_bg.jpg")

    # 練習3：こうかとん
    # kkimg_sfc = pg.image.load("fig/6.png")    # Surface
    # kkimg_sfc = pg.transform.rotozoom(kkimg_sfc, 0, 2.0)  # Surface
    # kkimg_rct = kkimg_sfc.get_rect()          # Rect
    # kkimg_rct.center = 900, 400
    kkt = Bird("fig/6.png", 2.0, (900, 400))

    # 練習5：爆弾
    # bmimg_sfc = pg.Surface((20, 20)) # Surface
    # bmimg_sfc.set_colorkey((0, 0, 0)) 
    # pg.draw.circle(bmimg_sfc, (255, 0, 0), (10, 10), 10)
    # bmimg_rct = bmimg_sfc.get_rect() # Rect
    # bmimg_rct.centerx = random.randint(0, screen_rct.width)
    # bmimg_rct.centery = random.randint(0, screen_rct.height)
    # vx, vy = +1, +1 # 練習6
    bomb = Bomb((255, 0, 0), 10, (+1,+1),scr)

    while True:
        scr.blit()

        # 練習2
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        # 練習4
        # key_states = pg.key.get_pressed() # 辞書
        # if key_states[pg.K_UP]    == True:
        #     kkimg_rct.centery -= 1
        # if key_states[pg.K_DOWN]  == True: 
        #     kkimg_rct.centery += 1
        # if key_states[pg.K_LEFT]  == True: 
        #     kkimg_rct.centerx -= 1
        # if key_states[pg.K_RIGHT] == True: 
        #     kkimg_rct.centerx += 1
        # # 練習7
        # if check_bound(kkimg_rct, screen_rct) != (1, 1): # 領域外だったら
        #     if key_states[pg.K_UP]    == True: 
        #         kkimg_rct.centery += 1
        #     if key_states[pg.K_DOWN]  == True: 
        #         kkimg_rct.centery -= 1
        #     if key_states[pg.K_LEFT]  == True: 
        #         kkimg_rct.centerx += 1
        #     if key_states[pg.K_RIGHT] == True: 
        #         kkimg_rct.centerx -= 1
        #screen_sfc.blit(kkimg_sfc, kkimg_rct)
        kkt.update(scr)

        # # 練習6
        # bmimg_rct.move_ip(vx, vy)
        # # 練習5
        # screen_sfc.blit(bmimg_sfc, bmimg_rct)
        # # 練習7
        # yoko, tate = check_bound(bmimg_rct, screen_rct)
        # vx *= yoko
        # vy *= tate
        bomb.update(scr)

        # 練習8
        if kkt.rct.colliderect(bomb.rct): 
            return

        pg.display.update()
        clock.tick(1000)


# 練習7
def check_bound(rct, scr_rct):
    '''
    [1] rct: こうかとん or 爆弾のRect
    [2] scr_rct: スクリーンのRect
    '''
    yoko, tate = +1, +1 # 領域内
    if rct.left < scr_rct.left or scr_rct.right  < rct.right : yoko = -1 # 領域外
    if rct.top  < scr_rct.top  or scr_rct.bottom < rct.bottom: tate = -1 # 領域外
    return yoko, tate



if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()