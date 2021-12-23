import tkinter as tk
from tkinter.constants import *


class MyDialog:
    def __init__(self, window):
        DIALOG = tk.Toplevel(window)
        DIALOG.title("DIALOG")
        DIALOG.geometry("400x300+100+100")

        self.littletext = tk.Text(DIALOG, height=15)
        self.littletext.pack()

        btn1 = tk.Button(DIALOG, text="POST TO MAIN WINDOW", command=self.GetFromDIALOG)
        btn1.pack(side="left")

        btn2 = tk.Button(DIALOG, text="EXIT", command=DIALOG.destroy)
        btn2.pack(side="left")

    def GetFromDIALOG(self):
        X = self.littletext.get("1.0", END)
        print(X)


if __name__ == '__main__':
    window = tk.Tk()
    window.title("main")

    menubar = tk.Menu(window)
    filemenu = tk.Menu(menubar, tearoff=0)
    filemenu.add_command(label="RUN A DIALOG", command=lambda: MyDialog(window))
    filemenu.add_command(label="Exit", command=window.destroy)
    menubar.add_cascade(label="FILE", menu=filemenu)
    window.config(menu=menubar)

    BIGTEXT = tk.Text(window)
    BIGTEXT.pack()

    BUTTON = tk.Button(window, text="Post", command=lambda: MyDialog(window))
    BUTTON.pack()

    window.mainloop()