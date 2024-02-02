import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    checkmark_label.config(text=" ")
    reps = 1


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps > 8:
        reps = 0
    elif reps % 2 != 0:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)
    elif reps == 8:
        count_down(long_break)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break)
        timer_label.config(text="Break", fg=PINK)

    reps += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"  # dynamic typing

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        if reps % 2 == 0:
            checkmark_label.config(text="✓")
        else:
            checkmark_label.config(text=" ")
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Timer Label
timer_label = Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

# Canvas widget allows us to insert images into our window and arrange them into layers
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)  # creating a canvas
tomato_img = PhotoImage(file="tomato.png")  # This method gets hold of an image
canvas.create_image(100, 112,
                    image=tomato_img)  # inserting the image in our canvas, must give xcor, ycor and the image itself
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Buttons
start_bttn = Button(text="Start", highlightthickness=0, command=start_timer, highlightbackground=YELLOW)
start_bttn.grid(column=0, row=2)

reset_bttn = Button(text="Reset", highlightthickness=0, bg=YELLOW, command=reset_timer, highlightbackground=YELLOW)
reset_bttn.grid(column=2, row=2)

# Checkmark
checkmark_label = Label(text=" ", font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)
checkmark_label.grid(column=1, row=3)

window.mainloop()
