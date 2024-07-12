from tkinter import *

window = Tk()
window.title("Cameron's Mile to KM Converter")
window.config(padx=20, pady=20)

converted_number = Label(text="")
converted_number.grid(column=1, row=1)

empty_label = Label(text="")
empty_label.grid(column=0, row=0)

miles_label = Label(text="miles")
miles_label.grid(column=2, row=0)

user_input = Entry(width=10)
user_input.grid(column=1, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

km_label = Label(text="KM")
km_label.grid(column=2, row=1)

def convert_miles_to_km():
    if user_input.get() != "":
        converted_number.config(text=int(user_input.get()) * 1.609)

button = Button(text="calculate", command=convert_miles_to_km)
button.grid(column=1, row=2)



window.mainloop()
