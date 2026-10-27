import random
import string
from tkinter import *
from tkinter import messagebox

import pyperclip

YOUR_EMAIL = "example-email.com"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Generates list of all ascii letters in lowercase
letters = list(string.ascii_lowercase)
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)


def generate_password():
    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(END, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure no field is empty.")
    else:
        is_ok = messagebox.askokcancel(
            title=website,
            message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?",
        )

        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=2, row=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=1, row=2)
email_user_label = Label(text="Email/Username:")
email_user_label.grid(column=1, row=3)
password_label = Label(text="Password:")
password_label.grid(column=1, row=4)

# Entries
website_entry = Entry(width=38)
website_entry.grid(column=2, row=2, columnspan=2)
website_entry.focus()
email_entry = Entry(width=38)
email_entry.grid(column=2, row=3, columnspan=2)
email_entry.insert(END, YOUR_EMAIL)
password_entry = Entry(width=21)
password_entry.grid(column=2, row=4)

# Buttons
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=3, row=4)
add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=2, row=5, columnspan=2)


window.mainloop()
