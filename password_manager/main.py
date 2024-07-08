# pyperclip-cross platform python module for copy and paste function for clipboard
import pyperclip
import tkinter as tk
import tkinter.constants
from tkinter import messagebox
import random
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# list comprehension
    letters_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    symbols_list = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    number_list = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = letters_list + symbols_list + number_list
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert("0", password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
            website: {
                "email": username,
                "password": password,
            }
        }

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="ERROR", message="Fill all the entries.")

    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)

        else:
            data.update(new_data)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, tkinter.constants.END)
            password_entry.delete(0, tkinter.constants.END)


def find():
    website = website_entry.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showwarning(title="ERROR", message="No data file found.")

    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title="Confirmation", message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showwarning(title="ERROR", message=f"No detail for the {website} exist.")
# ---------------------------- UI SETUP ------------------------------- #


win = tk.Tk()
win.title("Password manager")
win.config(pady=50, padx=50)
win.eval('tk::PlaceWindow . center')
canvas = tk.Canvas(height=200, width=200,)
logo = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website_label = tk.Label(text="Website :")
website_label.grid(column=0, row=1)
website_label.focus()

username_label = tk.Label(text="Email/username :")
username_label.grid(column=0, row=2)

password_label = tk.Label(text="Password :")
password_label.grid(column=0, row=3)

generate_button = tk.Button(text="Generate Password", command=generate)
generate_button.grid(column=2, row=3)

add_button = tk.Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

password_entry = tk.Entry(width=21)
password_entry.grid(column=1, row=3)

username_entry = tk.Entry(width=38)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(tkinter.constants.END, string="Shreeribhu@gmail.com")
website_entry = tk.Entry(width=21)
website_entry.grid(column=1, row=1)

search_button = tk.Button(text="Search", background="blue", width=13, command=find)
search_button.grid(column=2, row=1)
win.mainloop()
