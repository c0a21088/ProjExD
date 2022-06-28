import tkinter as tk
import tkinter.messagebox as tkm
import maze_maker as mm
from random import randint as ri                #randintをriとしている
def key_down(event):
    global key, gt, ogx, ogy, gy, gx
    key=event.keysym
    gt+=1                                       #s工科とんが動くと1増えるようにしている

def key_up(event):
    global key
    key = ""
    
def main_proc():
    global cx, cy, key, mx, my, gy, gx, gt, ogx, ogy
    hoge={                  #コマンド入力
        "Up"    :[0, -1],
        "Down"  :[0, +1],
        "Left"  :[-1, 0],
        "Right" :[+1,0],
    }
    try:
        if mz_list[my+hoge[key][1]][mx+hoge[key][0]] == 0: #もし移動先が床なら
            my,mx = my+hoge[key][1], mx+hoge[key][0]
    except:
        pass
    if gt >= 2:                                             #s工科とんが2回動くと、
        gt-=2                                               #gtを2減らすことでループを回している。(gtは破壊されてしまう)
        ogx+=ri(-1,1)                                       #ランダムでg工科トンのx軸が動く計算
        ogy+=ri(-1,1)                                       #ランダムでg工科トンのy軸が動く計算
    gx, gy = ogx*100+750, ogy*100+450                       #同じ
    canvas.coords("goal", gx, gy)                           #動かしている
    cx, cy = mx*100+50,my*100+50
    canvas.coords("tori", cx, cy)
    if gx == cx and gy == cy :
        tkm.showinfo("任務完了","よくやった！")
        canvas.master.destroy()
    root.after(90,main_proc)    








if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷える工科とん")
    canvas = tk.Canvas(root,width=1500,height=900,bg="black")
    canvas.pack()
    mz_list = mm.make_maze(15,9)            #mzのリストを返す
    mm.show_maze(canvas,mz_list)            #canvasにmaze_bg絵御描く
    tori = tk.PhotoImage(file="fig/5.png")  #startの工科とんの絵
    goal = tk.PhotoImage(file="fig/6.png")  #goalの工科とんの絵
    mx,my = 1,1
    cx, cy = mx*100+50,my*100+50
    canvas.create_image(cx,cy, image=tori,tag="tori")
    ogx, ogy = 1,1                          #mx,myと同様にゴールの工科とんの座標を決める
    gx, gy = ogx*100+750, ogy*100+450       #ogx,ogyに依存させることで後々升目に合わせて移動するようにする
    canvas.create_image(gx,gy, image=goal,tag="goal")
    
    key = ""
    gt = 0                                  #s工科とんが何手動いたか数えるためのgtを初期化
    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>",key_up)
    



    main_proc()
    root.mainloop()


