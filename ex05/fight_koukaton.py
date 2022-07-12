import pygame as pg
import sys
import random


class Screen:
    def __init__(self, title, wh, image):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh)     # Surface
        self.rct = self.sfc.get_rect()         # Rect
        self.bgi_sfc = pg.image.load(image)    # Surface
        self.bgi_rct = self.bgi_sfc.get_rect() # Rect

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)


class Bird:
    def __init__(self, image: str, size: float, xy):
        self.sfc = pg.image.load(image)    # Surface
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
        # # 練習7
        if check_bound(self.rct, scr.rct) != (1, 1): # 領域外だったら
            if key_states[pg.K_UP]: 
                self.rct.centery += 1
            if key_states[pg.K_DOWN]: 
                self.rct.centery -= 1
            if key_states[pg.K_LEFT]: 
                self.rct.centerx += 1
            if key_states[pg.K_RIGHT]: 
                self.rct.centerx -= 1
        self.blit(scr)

    def reset(self, image: str, size: float, xy):
        self.sfc = pg.image.load(image)    # Surface
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size)  # Surface
        self.rct = self.sfc.get_rect()          # Rect
        self.rct.center = xy

class Bomb:
    def __init__(self, color, size, vxy, scr: Screen):
        self.sfc = pg.Surface((2*size, 2*size)) # Surface
        self.sfc.set_colorkey((0, 0, 0)) 
        pg.draw.circle(self.sfc, color, (size, size), size)
        self.rct = self.sfc.get_rect() # Rect
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy # 練習6

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr: Screen):
        # 練習6
        self.rct.move_ip(self.vx, self.vy)
        # 練習7
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate   
        # 練習5
        self.blit(scr)          


class Enemy:
    def __init__(self, image, size, vxy, scr: Screen):
        self.sfc = pg.image.load(image)    # Surface
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size)  # Surface
        self.rct = self.sfc.get_rect() # Rect
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy # 練習6
        self.randlit = [-1,1]

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen, frame):
        # 練習6
        self.rct.move_ip(self.vx, self.vy)
        # 練習7
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate  
        if frame % 100 == 0:
            self.vx *= self.randlit[random.randint(0,1)]
            self.vy *= self.randlit[random.randint(0,1)]
        #練習5
        self.blit(scr)   


class Item:
    def __init__(self, image: str, size: float, xy):
        self.sfc = pg.image.load(image)    # Surface
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size)  # Surface
        self.rct = self.sfc.get_rect()          # Rect
        self.rct.center = xy

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr: Screen):
        self.blit(scr)


class Frame:
    def __init__(self):
        self.frame = 0


class ok:
    def __init__(self):
        pass
    

def main():
    is_item = False
    is_sentou_mode = False
    is_tek = True
    is_tek2 = True
    is_tek3 = True
    frame = 0
    clock = pg.time.Clock()
    scr = Screen("戦え！こうかとん", (1600, 900), "fig/pg_bg.jpg")
    kkt = Bird("fig/6.png", 2.0, (900, 400))
    bkd = Bomb((0,0,255), 10, (+1,+1), scr)
    tek = Enemy("fig/enemy1.png", 0.5, (+1,+1), scr)
    dug = Item("fig/item.png", 2.0, (600, 200))
    tek2 = Enemy("fig/enemy1.png", 0.5, (+1,+1), scr)
    tek3 = Enemy("fig/enemy1.png", 0.5, (+1,+1), scr)
    while True:
        scr.blit()

        # 練習2
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return

        kkt.update(scr,)
        bkd.update(scr)
        if is_tek:
            tek.update(scr, frame)
        if is_tek2:
            tek2.update(scr, frame)
        if is_tek3:    
            tek3.update(scr, frame)
        
        if is_item:
            dug.update(scr)
        if kkt.rct.colliderect(bkd.rct):
            return
        if is_sentou_mode:
            if kkt.rct.colliderect(tek.rct):
                is_tek = False
            if kkt.rct.colliderect(tek2.rct):
                is_tek2 = False
            if kkt.rct.colliderect(tek3.rct):
                is_tek3 = False          
        else:
            if kkt.rct.colliderect(tek.rct) or kkt.rct.colliderect(tek2.rct) or kkt.rct.colliderect(tek3.rct):
                return
        if kkt.rct.colliderect(dug.rct):
            is_sentou_mode = True
            kkt.reset("fig/5.png", 2.0, kkt.rct.center)


        pg.display.update()
        clock.tick(1000)
        frame += 1
        if frame % 3000 == 0:
            bkd = Bomb((0,0,255), 10, (+1,+1), scr)
            is_item = True
        if is_tek==False and is_tek2==False and is_tek3==False:
            return


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

def start_game(fname):   #ゲームの起動画面の作成、以下シーン0とする
    clock = pg.time.Clock() 
    pg.display.set_caption("逃げろ！こうかとん")
    screen_sfc = pg.display.set_mode((1600, 900)) #surface
    screen_rct = screen_sfc.get_rect()            #rect
    bgimg_sfc = pg.image.load("../ex03/fig/pg_bg.jpg") #surface　#背景は同じ
    bgimg_rct = bgimg_sfc.get_rect()              #rect
    screen_sfc.blit(bgimg_sfc,bgimg_rct)

    s_sfc = pg.image.load(fname)  #S to Start という文字を表示
    s_sfc = pg.transform.rotozoom(s_sfc, 0, 1.0)
    s_rct = s_sfc.get_rect()
    s_rct.center = 900, 400

    while True:
        screen_sfc.blit(bgimg_sfc,bgimg_rct)
        screen_sfc.blit(s_sfc, s_rct)

        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
        
        key_states = pg.key.get_pressed()
        if key_states[pg.K_s]:             #Sを押すとこの関数が終了し、mainの関数に移行する。
            return
        pg.display.update()
        clock.tick(1000)

if __name__ == "__main__":
    pg.init()
    start_game("../ex03/fig/12.png")  #start画面の表示
    main()
    start_game("fig/lose.png")
    pg.quit()
    sys.exit()
