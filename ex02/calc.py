import tkinter as tk
import tkinter.messagebox as tkm
root = tk.Tk()            #ウィンドウの設定
entry = tk.Entry(justify="right",width=10,font=("Times New Roman",40))
#-----------------------------------------
def button_click(event):
    btn = event.widget
    txt = btn["text"]
    entry.insert(tk.END,txt)
    #tkm.showinfo(txt,f"[{txt}]ボタンが押されました")
#-----------------------------------------
def generate_button(txt,rx,ry):              #ボタンのテキスト、x座標、y座標(0.0~1.0ウィンドウサイズ依存)
        button = tk.Button(root,text=txt,height=2,width=4,font=("Times New Roman",30))
        button.bind("<1>",button_click)
        button.grid(row=rx+1,column=ry)
#------------------------------------------ボタンを作る関数
def generate_txtbox():
    entry.insert(tk.END,"")
    entry.grid(columnspan=3)
    entry.grid(row=0)
#--------------------------------------------
def generate_calc_button():
    for i in range(10):
        k=10-i-1
        rx=k//3
        ry=k%3
        generate_button(str(i),rx,ry)
#--------------------------------------------
generate_calc_button()
generate_txtbox()
root.mainloop()