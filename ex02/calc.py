import tkinter as tk
root = tk.Tk()            #ウィンドウの設定
root.geometry("300x500")

#-----------------------------------------
def generate_button(txt,rx,ry):              #ボタンのテキスト、x座標、y座標(0.0~1.0ウィンドウサイズ依存)
        button = tk.Button(root,text=txt,height=10,width=10)
        button.pack()
        button.place(relx=rx,rely=ry)
#------------------------------------------ボタンを作る関数

def generate_calc_button():
    for i in range(10):
        if i <= 3:
            ry=0
        elif 3 < i <= 6:
            ry=1/4
        elif 6 < i <=9:
            ry=2/4
        elif i == 0:
            ry=3/4
        if i % 3 == 1:
            rx=0
        elif i % 3 == 2:
            rx=1/3
        elif i % 3 == 0:
            rx=2/3
        if i == 0:
            ry=0
        generate_button(str(i),rx,ry)

generate_calc_button()
root.mainloop()