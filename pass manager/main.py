from tkinter import *
from tkinter import  messagebox
import random
import pyperclip
import json
# ---------------------------- Search ------------------------------- #
def search():
    website = website_entry.get()
    try:
        with open("data.json","r") as data_file:
            data = json.load(data_file)

        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title="Search",message= f"email: {email} \n password :  {password}")
            pyperclip.copy(password)
        else:
            messagebox.showinfo(title="search", message="You are new to website ")
    except:
        messagebox.showinfo(title="search",message="NO such data found ")




# ---------------------------- PASSWORD GENERATOR ------------------------------- #


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
def password_gen():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)


    password_letters = [random.choice(letters) for item in range(nr_letters)]
    password_symbols = [random.choice(symbols) for item in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for item in range(nr_numbers)]

    password_list = password_letters+password_symbols+password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0,password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_name = website_entry.get()
    password = password_entry.get()
    email = email_entry.get()
    new_data = {
        website_name: {
            "email" : email,
            "password" : password,
        }
    }

    if len(website_name) == 0:
        messagebox.showinfo(title="ERROR" , message="enter the website name")
    elif len(password) == 0:
        messagebox.showinfo(title="ERROR" , message="enter the password ")
    elif len(email) == 0:
        messagebox.showinfo(title="ERROR" , message="enter the email ")
    else:
        is_ok = messagebox.askokcancel(title=website_name, message=f"These are the details you have entered :  \n Email : {email}  \n Passowrd : {password} \n\n You want to save it for sure ?")

        if is_ok:
            try:
                with open("data.json","r") as data_file:
                    # read old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
                    #update the data
            except json.decoder.JSONDecodeError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                    # write the data
                with open("data.json", "w") as data_file:
                    json.dump(data,data_file,indent=4)
            finally:
                website_entry.delete(0,END)
                password_entry.delete(0,END)
            pyperclip.copy(password)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50,highlightthickness=0)
# window.minsize(width=400,height=400)

canvas = Canvas(width=200,height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image = lock_img)
canvas.grid(column=1,row=0)

#   website

website_label = Label(text="Website : ")
website_label.grid(column=0,row=1)

website_entry = Entry(width=39)
website_entry.grid(column=1,row=1,columnspan=2)
website_entry.focus()

#  email label
email_label = Label(text="Email/Username :")
email_label.grid(column=0 ,row=2)

email_entry = Entry(width=39)
email_entry.grid(column=1,row=2,columnspan=2)
email_entry.insert(0,"791shivamsingh@gmail.com")
# password
password_label = Label(text="Password : ")
password_label.grid(column=0,row=3)

password_entry = Entry(width=21)
password_entry.grid(column=1,row=3)

gen_password = Button(text="Generate Password",command=password_gen)
gen_password.grid(column=2,row=3)

add_button = Button(text="Add",width=34,command=save)
add_button.grid(column=1,row=4,columnspan=2)

search_button = Button(text="Search",command=search)
search_button.grid(column=2,row=1)




window.mainloop()