import tkinter as tk
from tkinter import messagebox

def fake_error_message():
    # Create the root window
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    
    # Show the fake error message
    messagebox.showerror("Error", "An unexpected error has occurred. Please contact support.")
    
    # Destroy the root window after showing the message
    root.destroy()

if __name__ == "__main__":
    fake_error_message()
