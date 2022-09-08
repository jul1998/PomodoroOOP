import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 3
SHORT_BREAK_MIN = 2
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global reps
    reps = 0
    wn.after_cancel(str(timer))
    start_button.config(state="normal")
    canvas.itemconfig(timer_text, text=f"00:00")
    timer_label.config(text="Timer")

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    work_session = WORK_MIN
    short_break_session = SHORT_BREAK_MIN
    long_break_session = LONG_BREAK_MIN
    if reps % 8 == 0:
        timer_label.config(text="Long break")
        countdown(long_break_session)
    elif reps % 2 == 0:
        timer_label.config(text="Short break")
        countdown(short_break_session)
    else:
        timer_label.config(text="Work time")
        countdown(work_session)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(count):
    global reps
    start_button.config(state="disabled")
    min = math.floor(count/60)
    sec = math.floor(count % 60)
    if sec < 10:
        sec = f"0{sec}"
    if min < 10:
        min = f"0{min}"
    canvas.itemconfig(timer_text, text=f"{min}:{sec}")
    if count > 0:
       global timer
       timer = wn.after(1000, countdown, count-1)
    else:
        start_timer()
        checks = ""
        for _ in range(math.floor(reps/2)):
            checks+= "✔"
        check_mark.config(text=checks)


# ---------------------------- UI SETUP ------------------------------- #


wn = Tk()
wn.title("Pomodoro Timer")
wn.config(bg=YELLOW, pady=50, padx=80)

#Set image in canvas
image = PhotoImage(file="tomato.png")
canvas = Canvas(width=220, height=220, highlightthickness=0, bg=YELLOW)
canvas.create_image(110, 100, image=image)
timer_text = canvas.create_text(110, 120, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(column=1, row=1)

#Timer label
timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN, highlightthickness=0, font=(FONT_NAME, 28, "bold"))
timer_label.grid(column=1, row=0)

#Start button
start_button = Button(text="Start", state="normal", command=start_timer)
start_button.grid(column=0, row=2)

#Reset button
reset_button = Button(text="Reset", state="normal", command=reset)
reset_button.grid(column=2, row=2)

#Check Mark label
check_mark = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
check_mark.grid(column=1, row=3)


wn.mainloop()
