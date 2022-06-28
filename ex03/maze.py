from cProfile import label
import tkinter as tk
from tkinter import font
import tkinter.messagebox as tkm
if __name__ == "__main__":
    root = tk.Tk()
    label = tk.Label(root,text="mayoerukoukaton",
            font= ("Times New Roman",80),
            )
    label.pack()
    root.mainloop()