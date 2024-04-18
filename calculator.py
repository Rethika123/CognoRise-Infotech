import tkinter as tk

def add():
    try:
        result.set(float(num1.get()) + float(num2.get()))
    except ValueError:
        result.set("Error")

def subtract():
    try:
        result.set(float(num1.get()) - float(num2.get()))
    except ValueError:
        result.set("Error")

def multiply():
    try:
        result.set(float(num1.get()) * float(num2.get()))
    except ValueError:
        result.set("Error")

def divide():
    try:
        if float(num2.get()) == 0:
            result.set("Error: Cannot divide by zero")
        else:
            result.set(float(num1.get()) / float(num2.get()))
    except ValueError:
        result.set("Error")

# Create main window
root = tk.Tk()
root.title("Simple Calculator")

# Create entry fields for numbers
num1_label = tk.Label(root, text="Enter first number:")
num1_label.grid(row=0, column=0)
num1 = tk.Entry(root)
num1.grid(row=0, column=1)

num2_label = tk.Label(root, text="Enter second number:")
num2_label.grid(row=1, column=0)
num2 = tk.Entry(root)
num2.grid(row=1, column=1)

# Create buttons for operations
add_button = tk.Button(root, text="Add", command=add)
add_button.grid(row=2, column=0)

subtract_button = tk.Button(root, text="Subtract", command=subtract)
subtract_button.grid(row=2, column=1)

multiply_button = tk.Button(root, text="Multiply", command=multiply)
multiply_button.grid(row=3, column=0)

divide_button = tk.Button(root, text="Divide", command=divide)
divide_button.grid(row=3, column=1)

# Display result
result = tk.StringVar()
result_label = tk.Label(root, textvariable=result)
result_label.grid(row=4, columnspan=2)

# Run the main event loop
root.mainloop()
