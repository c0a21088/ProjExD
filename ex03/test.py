import tkinter as tk
from tkinter import font
import tkinter.messagebox as tkm
def count_up():
    global tmr, jid
    tmr = tmr+1
    label["text"] = tmr
    jid = root.after(1000,count_up)#after(遅延ミリ秒、呼び出す関数)

def key_down(event):
    global jid
    if jid != None:
        root.after_cancel(jid)
        jid = None
        return
    key=event.keysym#どのキーが押されたか判定する
    tkm.showinfo("キー押下",f"{key}キーが押されました")
    jid = root.after(1000,count_up)

if __name__ == "__main__":
    root = tk.Tk()
    label = tk.Label(root,text="Nemoto G Yuu",
            font= ("Times New Roman",80),
            )
    label.pack()
    tmr = 0 # グローバル変数
    jid = None #job番号を初期化
    root.bind("<KeyPress>",key_down)
    root.mainloop()

