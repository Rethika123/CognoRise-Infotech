import tkinter as tk
from tkinter import messagebox
import time

# Function to start the countdown
def start_timer():
    try:
        hours = int(entry_hours.get())
        minutes = int(entry_minutes.get())
        seconds = int(entry_seconds.get())
        total_seconds = hours * 3600 + minutes * 60 + seconds
        while total_seconds > 0:
            hrs, remainder = divmod(total_seconds, 3600)
            mins, secs = divmod(remainder, 60)
            time_str = "{:02}:{:02}:{:02}".format(hrs, mins, secs)
            label_timer.config(text=time_str)
            root.update()
            time.sleep(1)
            total_seconds -= 1
        label_timer.config(text="00:00:00")
        messagebox.showinfo("Time's up!", "Countdown completed!")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers for hours, minutes, and seconds.")

# Create the main window
root = tk.Tk()
root.title("Countdown Timer")

# Create and place the widgets
tk.Label(root, text="Hours:").grid(row=0, column=0, padx=10, pady=10)
entry_hours = tk.Entry(root, width=5)
entry_hours.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Minutes:").grid(row=1, column=0, padx=10, pady=10)
entry_minutes = tk.Entry(root, width=5)
entry_minutes.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Seconds:").grid(row=2, column=0, padx=10, pady=10)
entry_seconds = tk.Entry(root, width=5)
entry_seconds.grid(row=2, column=1, padx=10, pady=10)

button_start = tk.Button(root, text="Start", command=start_timer, font=('Arial', 16))
button_start.grid(row=3, columnspan=2, padx=10, pady=10)

label_timer = tk.Label(root, text="00:00:00", font=('Arial', 48))
label_timer.grid(row=4, columnspan=2, padx=10, pady=10)

# Start the GUI event loop
root.mainloop()
