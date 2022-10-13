from tkinter import *

FONT = ("Arial", 22, "normal")
ITEM_PADDING = 10

window = Tk()
window.title("C to F Temp Converter")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)

# Input Celsius
c_input = Entry(width=10)
c_input.insert(END, string="0")
c_input.grid(row=0, column=1)

# Display "Celsius"
cel_label = Label(text="°C", font=FONT, pady=ITEM_PADDING, padx=ITEM_PADDING)
cel_label.grid(row=0, column=2)

# Display "is equal to"
eq = Label(text="is equal to", font=FONT, padx=ITEM_PADDING, pady=ITEM_PADDING)
eq.grid(row=1, column=0)


# Calculate & display output
def calculate():
    f_output = (float(c_input.get()) * (9 / 5)) + 32
    fahr.config(text=f_output)


fahr = Label(text="0", font=FONT, pady=ITEM_PADDING, padx=ITEM_PADDING)
fahr.grid(row=1, column=1)

# Display "Fahrenheit"
fahr_label = Label(text="°F", font=FONT, padx=ITEM_PADDING, pady=ITEM_PADDING)
fahr_label.grid(column=2, row=1)

# "Calculate" button
button = Button(text="Calculate", command=calculate, pady=ITEM_PADDING, padx=ITEM_PADDING)
button.grid(row=2, column=1)

window.mainloop()
