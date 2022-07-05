from tkinter import *

# Creating a new window and configurations
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=300)


miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

converted_label = Label(text="")
converted_label.grid(column=1, row=1)


# Buttons
def calculate():
    # Gets text in entry
    km = float(entry.get())*1.60934
    converted_label.config(text=f"{km}")


# calls action() when pressed
button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

# Entries
entry = Entry(width=30)
# Add some text to begin with
entry.insert(END, string="0")
entry.grid(column=1, row=0)



window.mainloop()
