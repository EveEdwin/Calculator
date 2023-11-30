'''
import tkinter as tk

# Function to update the entry field when a button is clicked
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, str(current) + str(number))

# Function to perform calculations
def calculate():
    current = entry.get()
    try:
        result = eval(current)  # Using eval to evaluate the expression entered
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to clear the entry field
def clear():
    entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Entry field to display input and output
entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define buttons
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', 'C', '=', '+')
]

# Create and position buttons in a grid
row_num = 1
for row in buttons:
    col_num = 0
    for label in row:
        if label == '=':
            btn = tk.Button(root, text=label, padx=40, pady=20, command=calculate)
        elif label == 'C':
            btn = tk.Button(root, text=label, padx=40, pady=20, command=clear)
        else:
            btn = tk.Button(root, text=label, padx=40, pady=20, command=lambda label=label: button_click(label))
        btn.grid(row=row_num, column=col_num)
        col_num += 1
    row_num += 1

# Run the application
root.mainloop()
'''

import tkinter as tk

# Function to update the entry field when a button is clicked
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, str(current) + str(number))

# Function to perform calculations
def calculate():
    current = entry.get()
    try:
        result = eval(current)  # Using eval to evaluate the expression entered
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to clear the entry field
def clear():
    entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Entry field to display input and output
entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define buttons
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', 'C', '=', '+')
]

# Create and position buttons in a grid
row_num = 1
for row in buttons:
    col_num = 0
    for label in row:
        if label == '=':
            btn = tk.Button(root, text=label, padx=40, pady=20, command=calculate)
        elif label == 'C':
            btn = tk.Button(root, text=label, padx=40, pady=20, command=clear)
        else:
            btn = tk.Button(root, text=label, padx=40, pady=20, command=lambda label=label: button_click(label))
        btn.grid(row=row_num, column=col_num)
        col_num += 1
    row_num += 1

# Run the application
root.mainloop()
