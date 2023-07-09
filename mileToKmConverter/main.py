from tkinter import *


def calculate(event):
    miles = float(user_input.get())
    miles_integer = int(user_input.get())
    user_input.delete(0,END)
    label_1["text"] = f"{miles_integer} Miles"
    label_3["text"] = int(miles * 1.609344)


win = Tk()
win.title("Miles to Km Converter")
win.geometry("290x100")

user_input = Entry()
user_input.grid(column=1, row=0)

label_1 = Label(text="Miles", font=("Aerial", 12))
label_1.grid(column=2, row=0)

label_2 = Label(text="is equal to", font=("Aerial", 12))
label_2.grid(column=0, row=1)

label_3 = Label(text="0", font=("Aerial", 12))
label_3.grid(column=1, row=1)

label_4 = Label(text="Km", font=("Aerial", 12))
label_4.grid(column=2, row=1)

button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=3)

win.bind("<Return>", calculate)
win.mainloop()
