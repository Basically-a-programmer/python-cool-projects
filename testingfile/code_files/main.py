import tkinter

window = tkinter.Tk()
window.title("The first GUI")
window.minsize(width=500,height=300)

#label
my_label = tkinter.Label(text="I am  label",font=("Arial",16))
my_label.grid(column=0,row=0)
my_label["text"] = "the button is not clicked yet"

def button_click():
    my_label["text"] = input.get()
button = tkinter.Button(text="Click me",command=button_click)
button.grid(column=0,row=1)

input = tkinter.Entry(width=10)
input.grid(column=0,row=2)


window.mainloop()
