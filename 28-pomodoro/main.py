from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
CHECK_MARK = "✓"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
countdown_timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(countdown_timer)
    canvas.itemconfig(timer, text="00:00")
    timer_label.config(text="Timer")
    checkmarks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    reps += reps
    if reps % 2 == 1:
        timer_label.config(text="Work", fg=GREEN)
        count_down(work_sec)
    elif reps % 8 == 0:
        timer_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        timer_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer, text=f"{minutes}:{seconds}")
    if count > 0:
        global countdown_timer
        countdown_timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += CHECK_MARK
        checkmarks.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image= tomato_img)
timer = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", highlightthickness=0)
reset_button.grid(column=2, row=2)

checkmarks = Label(fg=GREEN, bg=YELLOW)
checkmarks.grid(column=1, row=3)

timer_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50), bg=YELLOW)
timer_label.grid(column=1, row=0)



window.mainloop()