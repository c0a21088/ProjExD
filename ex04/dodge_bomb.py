import pygame as pg
import sys
import random
import tkinter.messagebox as tkm
def main():
    clock = pg.time.Clock()

    #練習1　スクリーン定義
    pg.display.set_caption("逃げろ！こうかとん")
    screen_sfc = pg.display.set_mode((1600, 900)) #surface
    screen_rct = screen_sfc.get_rect()            #rect

    #練習2　バックグラウンド定義
    bgimg_sfc = pg.image.load("../ex03/fig/pg_bg.jpg") #surface
    bgimg_rct = bgimg_sfc.get_rect()              #rect
    screen_sfc.blit(bgimg_sfc,bgimg_rct)

    #練習3　こうかとん定義
    kk_sfc = pg.image.load("../ex03/fig/6.png")
    kk_sfc = pg.transform.rotozoom(kk_sfc, 0, 2.0)
    kk_rct = kk_sfc.get_rect()
    kk_rct.center = 900, 400
    
    #練習4　爆弾定義
    bmimg_sfc = pg.Surface((20, 20)) #surface
    bmimg_sfc.set_colorkey((0,0,0))
    pg.draw.circle(bmimg_sfc, (255,0,0), (10,10),10)
    bmimg_rct = bmimg_sfc.get_rect() #rect
    bmimg_rct.centerx = random.randint(0,screen_rct.width)
    bmimg_rct.centery = random.randint(0,screen_rct.height)
    vx,vy = +1, +1

    #メインループ
    while True:
        screen_sfc.blit(bgimg_sfc,bgimg_rct)

        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
        
        #こうかとんの動き
        key_states = pg.key.get_pressed()
        if key_states[pg.K_c]:
            kk_sfc = pg.image.load("../ex03/fig/11.png")
            kk_sfc = pg.transform.rotozoom(kk_sfc, 0, 0.2)     
        if key_states[pg.K_UP] == True:
            kk_rct.centery -=1
        if key_states[pg.K_DOWN] == True:
            kk_rct.centery +=1
        if key_states[pg.K_LEFT] == True:
            kk_rct.centerx -=1
        if key_states[pg.K_RIGHT] == True:
            kk_rct.centerx +=1

        if key_states[pg.K_w]:#WASDでも動けるように変更
            kk_rct.centery -=1
        if key_states[pg.K_s]:
            kk_rct.centery +=1
        if key_states[pg.K_a]:
            kk_rct.centerx -=1
        if key_states[pg.K_d]:
            kk_rct.centerx +=1

        
        if  check_bound(kk_rct,screen_rct) != (True, True):
            if key_states[pg.K_UP] == True:
                kk_rct.centery +=1
            if key_states[pg.K_DOWN] == True:
                kk_rct.centery -=1
            if key_states[pg.K_LEFT] == True:
                kk_rct.centerx +=1
            if key_states[pg.K_RIGHT] == True:
                kk_rct.centerx -=1

            if key_states[pg.K_w]:#WASDでも移動できるように変更
                kk_rct.centery +=1
            if key_states[pg.K_s]:
                kk_rct.centery -=1
            if key_states[pg.K_a]:
                kk_rct.centerx +=1
            if key_states[pg.K_d]:
                kk_rct.centerx -=1
        screen_sfc.blit(kk_sfc, kk_rct)

        #練習6　爆弾の動き
        bmimg_rct.move_ip(vx,vy)
        screen_sfc.blit(bmimg_sfc,bmimg_rct)
        yoko ,tate =  check_bound(bmimg_rct, screen_rct)
        if yoko == False:  #爆弾の速度を壁に当たるごとに1.2倍にする
            vx*=-1.2
        if tate == False:
            vy*=-1.2

        if kk_rct.colliderect(bmimg_rct): #ゲームオーバー時にウィンドウを表示する
            txt ="終了"
            tkm.showinfo(txt,f"[{txt}]です")
            return

        if key_states[pg.K_b]: 
            pass

        pg.display.update()
        clock.tick(1000)

def check_bound(rct, scr_rct):
    """
    [1] rct: こうかとん or 爆弾のrct
    [2] scr_rct: スクリーンのrect
    """
    yoko, tate = True, True
    if rct.left < scr_rct.left or scr_rct.right < rct.right:
        yoko = False
    if rct.top < scr_rct.top or scr_rct.bottom < rct.bottom:
        tate = False
    return yoko, tate
    
def start_game():   #ゲームの起動画面の作成、以下シーン0とする
    clock = pg.time.Clock() 
    pg.display.set_caption("逃げろ！こうかとん")
    screen_sfc = pg.display.set_mode((1600, 900)) #surface
    screen_rct = screen_sfc.get_rect()            #rect
    bgimg_sfc = pg.image.load("../ex03/fig/pg_bg.jpg") #surface　#背景は同じ
    bgimg_rct = bgimg_sfc.get_rect()              #rect
    screen_sfc.blit(bgimg_sfc,bgimg_rct)

    s_sfc = pg.image.load("../ex03/fig/12.png")  #S to Start という文字を表示
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
    start_game()  #start画面の表示
    main()        #ゲーム画面の表示
    pg.quit()
    sys.exit()