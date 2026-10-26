from tkinter import *

window = Tk()

window.title("Miles To Kilometer Converter")
window.config(padx=20, pady=20)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=1, row=2)

input = Entry()
input.insert(END, "0")
input.grid(column=2, row=1)
value = input.get()

conversion_label = Label(text="0")
conversion_label.grid(column=2, row=2)


def calculate():
    miles = int(input.get())
    km = miles * 1.609344
    conversion_label.config(text=round(km, 2))


calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(column=2, row=3)

miles_label = Label(text="Miles")
miles_label.grid(column=3, row=1)

km_label = Label(text="Km")
km_label.grid(column=3, row=2)


window.mainloop()
