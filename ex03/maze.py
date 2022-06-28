import tkinter as tk
import tkinter.messagebox as tkm
import maze_maker as mm
def key_down(event):
    global key
    key=event.keysym
    print(key)
    
def key_up(event):
    global key
    key = ""
    print(key)
    
def main_proc():
    global cx, cy, key, mx, my
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
    cx, cy = mx*100+50,my*100+50
    canvas.coords("tori", cx, cy)
    root.after(100,main_proc)    







if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷える工科トン")
    canvas = tk.Canvas(root,width=1500,height=900,bg="black")
    canvas.pack()
    mz_list = mm.make_maze(15,9) #mzのリストを返す
    mm.show_maze(canvas,mz_list) #canvasにmaze_bg絵御描く
    tori = tk.PhotoImage(file="fig/5.png")
    mx,my = 1,1
    cx, cy = mx*100+50,my*100+50

    canvas.create_image(cx,cy, image=tori,tag="tori")

    key = ""
    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>",key_up)
    
    main_proc()


    root.mainloop()
