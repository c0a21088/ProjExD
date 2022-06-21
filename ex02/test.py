print("hello world")
import tkinter as tk
import tkinter.messagebox as tkm

root = tk.Tk()
root.title("おためしか")
root.geometry("500x200")

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    tkm.showinfo(txt,f"[{txt}]ボタンが押されました")

#def button_click():
#    tkm.showwarning("警告","地獄に落ちてください。")

label = tk.Label(root,
                text="ラベルを書いてみた件",
                font=("ricty Diminished",20)
                )
label.pack()

button = tk.Button(root,text="押すなよ",command=button_click)
button.bind("<1>",button_click)
button.pack()


entry = tk.Entry(width=20)
entry.insert(tk.END,"fugapiyo")
entry.pack()
root.mainloop()
