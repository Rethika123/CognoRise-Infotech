import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length, use_upper, use_lower, use_digits, use_special):
    character_pool = ''
    if use_upper:
        character_pool += string.ascii_uppercase
    if use_lower:
        character_pool += string.ascii_lowercase
    if use_digits:
        character_pool += string.digits
    if use_special:
        character_pool += string.punctuation

    if not character_pool:
        messagebox.showwarning("Input Error", "Select at least one character type!")
        return None

    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

def create_app():
    def generate():
        try:
            length = int(length_entry.get())
            use_upper = upper_var.get()
            use_lower = lower_var.get()
            use_digits = digits_var.get()
            use_special = special_var.get()

            password = generate_password(length, use_upper, use_lower, use_digits, use_special)
            if password:
                result_label.config(text=password)
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid length!")

    # Create the main window
    root = tk.Tk()
    root.title("Password Generator")
    root.geometry("400x300")
    root.configure(bg="#87CEEB")  # Sky blue background color

    # Style definitions
    label_bg = "#61afef"
    label_fg = "#282c34"
    entry_bg = "#98c379"
    entry_fg = "#282c34"
    button_bg = "#e06c75"
    button_fg = "#282c34"
    check_bg = "#87CEEB"  # Match checkbutton background to sky blue
    check_fg = "#282c34"

    # Length label and entry
    tk.Label(root, text="Password Length:", bg=label_bg, fg=label_fg).grid(row=0, column=0, pady=5, padx=5)
    length_entry = tk.Entry(root, bg=entry_bg, fg=entry_fg)
    length_entry.grid(row=0, column=1, pady=5, padx=5)

    # Checkbuttons for character types
    upper_var = tk.BooleanVar()
    lower_var = tk.BooleanVar()
    digits_var = tk.BooleanVar()
    special_var = tk.BooleanVar()

    tk.Checkbutton(root, text="Include Uppercase Letters", variable=upper_var, bg=check_bg, fg=check_fg).grid(row=1, column=0, columnspan=2, pady=5, padx=5)
    tk.Checkbutton(root, text="Include Lowercase Letters", variable=lower_var, bg=check_bg, fg=check_fg).grid(row=2, column=0, columnspan=2, pady=5, padx=5)
    tk.Checkbutton(root, text="Include Digits", variable=digits_var, bg=check_bg, fg=check_fg).grid(row=3, column=0, columnspan=2, pady=5, padx=5)
    tk.Checkbutton(root, text="Include Special Characters", variable=special_var, bg=check_bg, fg=check_fg).grid(row=4, column=0, columnspan=2, pady=5, padx=5)

    # Generate button
    tk.Button(root, text="Generate Password", command=generate, bg=button_bg, fg=button_fg).grid(row=5, column=0, columnspan=2, pady=10, padx=5)

    # Result label
    result_label = tk.Label(root, text="", font=("Helvetica", 12), bg="#87CEEB", fg="#282c34")
    result_label.grid(row=6, column=0, columnspan=2, pady=5, padx=5)

    # Run the application
    root.mainloop()

if __name__ == "__main__":
    create_app()
