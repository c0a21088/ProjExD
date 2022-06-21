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
        button = tk.Button(root,text=txt,height=2,width=4,font=("Times New Roman",30),bg="blue")
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
def generate_addition():
    button = tk.Button(root,text="+",height=2,width=4,font=("Times New Roman",30))
    button.bind("<1>",button_click)
    button.grid(row=0,column=4)
#--------------------------------------------
def generate_substraction():
    button = tk.Button(root,text="-",height=2,width=4,font=("Times New Roman",30))
    button.bind("<1>",button_click)
    button.grid(row=1,column=4)
#--------------------------------------------
def generate_multiplication():
    button = tk.Button(root,text="×",height=2,width=4,font=("Times New Roman",30))
    button.bind("<1>",button_click)
    button.grid(row=2,column=4)
#--------------------------------------------
def genarate_division():
    button = tk.Button(root,text="÷",height=2,width=4,font=("Times New Roman",30))
    button.bind("<1>",button_click)
    button.grid(row=3,column=4)
#--------------------------------------------
def generate_equal():
    button = tk.Button(root,text="=",height=2,width=4,font=("Times New Roman",30))
    button.bind("<1>",click_equal)
    button.grid(row=4,column=4)
#--------------------------------------------
def generate_kanzensuu():
    button = tk.Button(root,text="完全数？",height=2,width=7,font=("Times New Roman",30))
    button.bind("<1>",kanzensuu)
    button.grid(row=0,column=5)
#--------------------------------------------
def kanzensuu(event):
    btn=event.widget
    num=entry.get()
    numlist = ["6","28","496","8128","33550336"]
    if num in numlist:
        ans = "YES"
    else:
        ans = "NO"    
    entry.delete(0,tk.END)
    entry.insert(tk.END,ans)
#--------------------------------------------
def generate_ac():
    button = tk.Button(root,text="AC",height=2,width=7,font=("Times New Roman",30))
    button.bind("<1>",ac)
    button.grid(row=1,column=5)
#--------------------------------------------
def ac(event):
    btn=event.widget
    entry.delete(0,tk.END)
#--------------------------------------------
def click_equal(event):
    btn=event.widget
    num=entry.get()
    if num == "3398++++":
        ans = "俺の電話番号"
    elif "×" in num:
        num = num.replace("×","*")
        ans = eval(num)
    elif "÷" in num:
        num = num.replace("÷","/")
        ans = eval(num)
    else:
        ans = eval(num)
    entry.delete(0,tk.END)
    entry.insert(tk.END,ans)
#--------------------------------------------
root.bind("<Return>",click_equal)
root.bind("<3>",ac)
generate_calc_button()
generate_txtbox()
generate_addition()
generate_substraction()
generate_multiplication()
genarate_division()
generate_equal()
generate_kanzensuu()
generate_ac()
root.mainloop()