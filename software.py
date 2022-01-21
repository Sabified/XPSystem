# This is the main SOFTWARE file

import data_class
import tkinter as tk
import random

xp = data_class.Experience(limit=15)
line = "_____________________________________________________________________________________________________"

window = tk.Tk()
window.geometry("800x500")
window.title("XP System")
window.resizable(False, False)

def getXp():
    added = xp.get_limit() - random.randint(1, 5)
    xp.add(xp=random.randint(1, added))

    XpSlider.configure(state='normal')
    XpSlider.set(xp.get_xp())
    XpSlider.configure(state='disabled')
    XpLabel.config(text = str(xp.get_levels()))

def reset():
    xp.reset()

    XpSlider.configure(state='normal')
    XpSlider.set(0)
    XpSlider.configure(state='disabled')

    XpLabel.config(text="0")


ProgName = tk.Label(window, font=('Comic Sans MS',30,'bold'),text="XP System", fg="lime")
ProgName.place(x=400,y=30,anchor="center")

XpSlider = tk.Scale(window, from_=0,to=xp.get_limit(),orient='horizontal',width=15)
XpSlider.configure(state='disabled')
XpSlider.place(x=400,y=250, anchor="center")

LineLabel = tk.Label(window, font=('Comic Sans MS',50,'bold'),text=line)
LineLabel.place(x=400,y=100, anchor="center")

XpLabel = tk.Label(window, font=('Comic Sans MS',15,'bold'),text="0")
XpLabel.place(x=320,y=255, anchor="center")

GetXPButton = tk.Button(window,text="Get XP",height=1, width=7,font=('Comic Sans MS',15,'bold'),command=getXp)
GetXPButton.place(x=50,y=400)

RestartButton = tk.Button(window,text="Reset",height=1, width=7,font=('Comic Sans MS',15,'bold'),command=reset)
RestartButton.place(x=650,y=400)

window.mainloop()
