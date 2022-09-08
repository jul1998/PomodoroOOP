from tkinter import *
from brain import Brain

# Constants
YELLOW = "#f7f5dd"


wn = Tk()
wn.title("Pomodoro Timer")
wn.config(bg=YELLOW, pady=50, padx=80)

# Brain will manage the whole mechanism behind this program
Brain(wn)


wn.mainloop()






