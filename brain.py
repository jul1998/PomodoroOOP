import math
import time
from tkinter import Button, Label, Canvas, PhotoImage, Tk

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0


class Brain:

    def __init__(self, screen):

        self.set_up_labels()
        self.screen = screen

        self.canvas = Canvas(width=220, height=220, highlightthickness=0, bg=YELLOW)
        self.image = PhotoImage(file="tomato.png")
        self.canvas.create_image(100, 100, image=self.image)
        self.timer_text = self.canvas.create_text(110, 120, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
        self.canvas.grid(column=1, row=1)

        self.start_button = Button(text="Start", state="normal", command=self.start_timer)
        self.start_button.grid(column=0, row=2)
        self.reset_button = Button(text="Reset", state="normal", command=self.reset)
        self.reset_button.grid(column=2, row=2)



    def set_up_labels(self):
        self.timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN, highlightthickness=0, font=(FONT_NAME, 28, "bold"))
        self.timer_label.grid(column=1, row=0)

        self.check_mark = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
        self.check_mark.grid(column=1, row=3)


    def countdown(self, count):
        min = math.floor(count/60)
        sec = math.floor(count % 60)
        if min < 10:
            min = f"0{min}"
        if sec < 10:
            sec = f"0{sec}"
        self.canvas.itemconfig(self.timer_text, text=f"{min}:{sec}")
        if count > 0:
            global timer
            timer = self.screen.after(1000, self.countdown, count-1)
            print(count)
        else:
            self.start_timer()
            checks = ""
            for _ in range(math.floor(reps/2)):
                checks+= "✔"
            self.check_mark.config(text=checks)


    def start_timer(self):
        self.start_button.config(state="disabled")
        global reps
        reps += 1
        work_session = WORK_MIN * 60
        short_break_session = SHORT_BREAK_MIN * 60
        long_break_session = LONG_BREAK_MIN * 60

        if reps % 8 == 0:
            self.timer_label.config(text="Long break")
            self.countdown(long_break_session)
        elif reps % 2 == 0:
            self.timer_label.config(text="Short break")
            self.countdown(short_break_session)
        else:
            self.timer_label.config(text="Work time")
            self.countdown(work_session)

    def reset(self):
        self.reset_button.config(state="normal")
        self.start_button.config(state="normal")
        self.screen.after_cancel(str(timer))
        self.canvas.itemconfig(self.timer_text, text=f"00:00")
        global reps
        reps = 0
        self.check_mark.config(text="")




