import tkinter as tk
import tkinter.messagebox as tkm
root = tk.Tk()            #ウィンドウの設定
root.geometry("300x500")
#-----------------------------------------
def button_click(event):
    btn = event.widget
    txt = btn["text"]
    tkm.showinfo(txt,f"[{txt}]ボタンが押されました")
#-----------------------------------------
def generate_button(txt,rx,ry):              #ボタンのテキスト、x座標、y座標(0.0~1.0ウィンドウサイズ依存)
        button = tk.Button(root,text=txt,height=2,width=4,font=("Times New Roman",30))
        button.bind("<1>",button_click)
        button.grid(row=rx,column=ry)
#------------------------------------------ボタンを作る関数

def generate_calc_button():
    for i in range(10):
        rx=i//3
        ry=i%3
        generate_button(str(i),rx,ry)

generate_calc_button()
root.mainloop()