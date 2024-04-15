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
LONG_BREAK_MIN = 30
reps = 0
my_timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(my_timer)
    canvas.itemconfig(timer_text, text=f"00:00")
    timer.config(text="Timer")
    check_marks.config(text= "")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps% 8 == 0:
        count_down(long_break_sec)
        timer.config(text="Long Break" , fg=RED)

    elif reps%2 == 0:
        count_down(short_break_sec)
        timer.config(text="Short Break", fg=PINK)
    else:
        count_down(work_sec)
        timer.config(text="Work", fg=GREEN)
        mark = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            mark += "✔"
        check_marks.config(text=mark)




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    min = math.floor(count/60)
    sec = count%60
    if sec < 10:
        sec = f"0{sec}"


    canvas.itemconfig(timer_text,text= f"{min}:{sec}" )
    if count> 0:
        global  my_timer
        my_timer = window.after(1000,count_down,count-1)
    else:
        start_timer()




# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Lets Focus")
window.config(padx=100,pady=80,bg=YELLOW)



canvas = Canvas(width=200,height=224,bg=YELLOW, highlightthickness=0)
tom_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image = tom_img)
canvas.grid(column=1,row=1)
timer_text = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))


timer = Label(text="Timer", fg=GREEN,bg=YELLOW)
timer.config(font=(FONT_NAME,50,"bold"))
timer.grid(column=1,row=0)

start = Button()
start.config(text="Start",highlightthickness=0,command=start_timer)
start.grid(column=0,row=3)

reset = Button()
reset.config(text="Reset",highlightthickness=0, command=reset_timer)
reset.grid(column=2,row=3)

check_marks = Label(text="")
check_marks.config(bg=YELLOW,fg=GREEN,font=(FONT_NAME,18,"bold"))
check_marks.grid(column=1,row=4)


window.mainloop()

