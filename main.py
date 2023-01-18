from tkinter import *
import math

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
mark = ""
timer = None



# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():

    global time_label
    global mark
    global reps
    global check_label
    window.after_cancel(timer)
    time_label.config(text="Timer", fg=RED)
    mark = ""
    reps = 1
    canvas.itemconfig(timer_text, text="00:00")
    check_label.config(text=mark)





# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():

    global reps
    global time_label
    global check_label
    global mark
    work_min = WORK_MIN * 60
    short_break_min = SHORT_BREAK_MIN * 60
    long_break_min = LONG_BREAK_MIN * 60

    if reps < 9:
        if reps % 8 == 0:
            count_down(long_break_min)
            time_label.config(text="Break", fg=RED)
            mark += "✔"
            check_label.config(text=mark)
            #reps += 1
        elif reps % 2 == 0:
            count_down(short_break_min)
            time_label.config(text="Break", fg=PINK)
            mark += "✔"
            check_label.config(text=mark)
            # reps += 1
        else:
            count_down(work_min)
            time_label.config(text="Work", fg=GREEN)
            # reps += 1
        reps +=1
    else:
        time_label.config(text="DONE", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

time_label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
time_label.grid(column=1, row=0)

canvas = Canvas(width=210, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(105, 112, image=tomato_img)
timer_text = canvas.create_text(105, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_label = Label(text=mark, font=(FONT_NAME, 10, "bold"), fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)

window.mainloop()

print("Koniec")
