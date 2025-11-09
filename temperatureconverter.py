from tkinter import *

def fahrenheit_to_celsius():
    f = float(entry_f.get())
    c = (f - 32) * 5 / 9
    entry_c.delete(0, END)
    entry_c.insert(0, str(c))

def celsius_to_fahrenheit():
    c = float(entry_c.get())
    f = (c * 9 / 5) + 32
    entry_f.delete(0, END)
    entry_f.insert(0, str(f))

window = Tk()
window.title("Temperature Converter")

label_f = Label(window, text="Fahrenheit")
label_c = Label(window, text="Celsius")

entry_f = Entry(window)
entry_f.insert(0, "32.0")
entry_c = Entry(window)
entry_c.insert(0, "0.0")

button_to_c = Button(window, text=">>>>", command=fahrenheit_to_celsius)
button_to_f = Button(window, text="<<<<", command=celsius_to_fahrenheit)

label_f.grid(row=0, column=0)
label_c.grid(row=0, column=1)
entry_f.grid(row=1, column=0)
entry_c.grid(row=1, column=1)
button_to_c.grid(row=2, column=0)
button_to_f.grid(row=2, column=1)

window.mainloop()
