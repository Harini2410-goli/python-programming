import tkinter as tk

# Function to update the display when a button is clicked
def button_click(value):
    current = display.get()
    display.delete(0, tk.END)  # Clear the display
    display.insert(tk.END, current + value)  # Append the new value

# Function to evaluate the expression and show the result
def calculate():
    try:
        result = str(eval(display.get()))  # Evaluate the expression
        display.delete(0, tk.END)
        display.insert(tk.END, result)  # Display the result
    except Exception:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")  # Display error for invalid expressions

# Function to clear the display
def clear_display():
    display.delete(0, tk.END)  # Clear the display

# Creating the main window
root = tk.Tk()
root.title("Simple Calculator")

# Display Entry
display = tk.Entry(root, width=20, font=("Arial", 18), borderwidth=2, relief="solid")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button Layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0)
]

# Creating buttons and placing them on the grid
for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14), command=calculate)
    elif text == 'C':
        button = tk.Button(root, text=text, width=20, height=2, font=("Arial", 14), command=clear_display)
        button.grid(row=row, column=col, columnspan=4, padx=5, pady=5)
        continue
    else:
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14), command=lambda t=text: button_click(t))
    button.grid(row=row, column=col, padx=5, pady=5)

# Start the main loop
root.mainloop()
