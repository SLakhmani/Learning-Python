from tkinter import *


def calculate_clicked():  # Event listener
    # Error Label
    error_label = Label(text="Invalid Input!", font=("Arial", 12))
    error_label.grid(column=2, row=0)

    try:
        error_label.config(foreground="white")
        miles = float(input_box.get())
        km = miles * 1.689
        output_box.delete(0, END)
        output_box.insert(index=0, string=str(round(km, 2)))
    except ValueError:
        error_label.config(foreground="red")
        output_box.delete(0, END)
        output_box.insert(index=0, string="Error")


# Window
window = Tk()
window.title("Miles To Km Converter")
window.minsize(width=330, height=100)
window.config(padx=15, pady=5)

# Miles Entry
input_box = Entry(width=10, font=("Arial", 15))
input_box.insert(END, string="0")
input_box.grid(column=0, row=0)

# Miles Label
miles_label = Label(text="Miles", font=("Arial", 15))
miles_label.grid(column=1, row=0)
miles_label.config(padx=10, pady=10)

# Button
calculate = Button(text="Convert", command=calculate_clicked)
calculate.grid(column=0, row=1)

# Km Output
output_box = Entry(width=10, font=("Arial", 15))
output_box.insert(END, string="0")
output_box.grid(column=0, row=2)

# Km Label
km_label = Label(text="Kms", font=("Arial", 15))
km_label.grid(column=1, row=2)
km_label.config(padx=10, pady=10)

window.mainloop()  # Always at the end
