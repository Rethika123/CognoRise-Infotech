import tkinter as tk

# Define the main calculator class
class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Simple Calculator")
        master.configure(bg="sky blue")

        # Create an entry widget for the display
        self.display = tk.Entry(master, width=16, font=("Arial", 24), bd=10, insertwidth=2, bg="white", justify='right')
        self.display.grid(row=0, column=0, columnspan=4)

        # Define the buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        # Create buttons using a loop
        row_val = 1
        col_val = 0
        for button in buttons:
            self.create_button(button).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # Add the Clear button at the bottom
        self.create_button('C').grid(row=row_val, column=0, columnspan=4, sticky='nsew')

        # Configure grid row and column weights for resizing
        for i in range(5):
            master.grid_rowconfigure(i, weight=1)
            master.grid_columnconfigure(i, weight=1)

    def create_button(self, value):
        return tk.Button(self.master, text=value, width=5, height=2, font=("Arial", 18), bd=5, command=lambda: self.click(value))

    def click(self, value):
        current_text = self.display.get()
        if value == '=':
            try:
                result = str(eval(current_text))
                self.display.delete(0, tk.END)
                self.display.insert(0, result)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        elif value == 'C':
            self.display.delete(0, tk.END)
        else:
            self.display.insert(tk.END, value)

# Main loop
if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
