import tkinter as tk
from tkinter import messagebox
import subprocess
import threading

def run_dd(source, output, bs):
    try:
        command = ["dd", f"if={source}", f"of={output}", f"bs={bs}"]
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        messagebox.showinfo("Success", "File recovery completed successfully!")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"An error occurred: {e.stderr}")

def start_recovery():
    source = source_entry.get()
    output = output_entry.get()
    bs = bs_entry.get()

    if not source or not output or not bs:
        messagebox.showwarning("Input Error", "Please fill in all fields.")
        return

    threading.Thread(target=run_dd, args=(source, output, bs)).start()

# Create the main window
root = tk.Tk()
root.title("File Recovery using dd")

# Source Disk Input
tk.Label(root, text="Source Disk:").grid(row=0, column=0, padx=10, pady=10)
source_entry = tk.Entry(root)
source_entry.grid(row=0, column=1, padx=10, pady=10)

# Output File Path Input
tk.Label(root, text="Output File Path:").grid(row=1, column=0, padx=10, pady=10)
output_entry = tk.Entry(root)
output_entry.grid(row=1, column=1, padx=10, pady=10)

# Block Size Input
tk.Label(root, text="Block Size (bs):").grid(row=2, column=0, padx=10, pady=10)
bs_entry = tk.Entry(root)
bs_entry.grid(row=2, column=1, padx=10, pady=10)

# Start Button
start_button = tk.Button(root, text="Start Recovery", command=start_recovery)
start_button.grid(row=3, column=0, columnspan=2, pady=10)

# Start the Tkinter event loop
root.mainloop()
