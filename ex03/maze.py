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
    global cx, cy, key
    hoge={
        ""  :[0, 0],
        "Up":[0, -20],
        "Down":[0, +20],
        "Left":[-20, 0],
        "Right":[+20,0],
    }
    print(key)
    cx, cy = cx+hoge[key][0], cy+hoge[key][1]
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
    cx, cy = 300,400
    canvas.create_image(cx,cy, image=tori,tag="tori")

    key = ""
    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>",key_up)
    
    main_proc()


    root.mainloop()
