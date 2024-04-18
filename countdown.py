import tkinter as tk
from tkinter import messagebox
import time

def start_countdown():
    try:
        total_seconds = int(hours_entry.get()) * 3600 + int(minutes_entry.get()) * 60 + int(seconds_entry.get())
        if total_seconds <= 0:
            raise ValueError("Invalid time")

        while total_seconds:
            hours = total_seconds // 3600
            minutes = (total_seconds % 3600) // 60
            seconds = total_seconds % 60
            time_str = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
            countdown_label.config(text=time_str)
            root.update()
            time.sleep(1)
            total_seconds -= 1

        messagebox.showinfo("Countdown Timer", "Time's up!")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid time")

# Create main window
root = tk.Tk()
root.title("Countdown Timer")

# Create entry fields for hours, minutes, and seconds
hours_label = tk.Label(root, text="Hours:")
hours_label.grid(row=0, column=0)
hours_entry = tk.Entry(root)
hours_entry.grid(row=0, column=1)

minutes_label = tk.Label(root, text="Minutes:")
minutes_label.grid(row=1, column=0)
minutes_entry = tk.Entry(root)
minutes_entry.grid(row=1, column=1)

seconds_label = tk.Label(root, text="Seconds:")
seconds_label.grid(row=2, column=0)
seconds_entry = tk.Entry(root)
seconds_entry.grid(row=2, column=1)

# Create button to start countdown
start_button = tk.Button(root, text="Start Countdown", command=start_countdown)
start_button.grid(row=3, columnspan=2)

# Create label to display countdown
countdown_label = tk.Label(root, text="", font=("Helvetica", 24))
countdown_label.grid(row=4, columnspan=2)

# Run the main event loop
root.mainloop()
