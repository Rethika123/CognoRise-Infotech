import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError("Password length should be greater than zero")

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
    except ValueError as e:
        messagebox.showerror("Error", e)

# Create main window
root = tk.Tk()
root.title("Password Generator")

# Create entry field for password length
length_label = tk.Label(root, text="Password Length:")
length_label.grid(row=0, column=0)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1)

# Create button to generate password
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=1, columnspan=2)

# Create entry field to display generated password
password_label = tk.Label(root, text="Generated Password:")
password_label.grid(row=2, column=0)
password_entry = tk.Entry(root)
password_entry.grid(row=2, column=1)

# Run the main event loop
root.mainloop()
