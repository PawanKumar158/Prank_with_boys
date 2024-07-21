import tkinter as tk
from tkinter import messagebox
import random

def fake_error_message():
    messages = [
        "Error: Disk read failure. Please insert a floppy disk to continue.",
        "Critical Error: Unexpected system shutdown. Reboot required.",
        "Fatal Error: Blue screen of death. Please contact IT support.",
        "Alert: Malware detected. Immediate action required.",
        "Warning: Low memory. Please close some applications.",
        "Error: Network connection lost. Check your internet settings.",
        "Critical Error: System overheating. Shutdown imminent.",
        "Error: Unrecognized USB device. Please remove the device.",
        "Fatal Error: Application has crashed. Please restart the program.",
        "Warning: Unauthorized access attempt detected."
    ]
    
    # Randomly select an error message
    selected_message = random.choice(messages)
    
    # Create the root window
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    
    # Show the fake error message
    messagebox.showerror("Error", selected_message)
    
    # Destroy the root window after showing the message
    root.destroy()

if __name__ == "__main__":
    fake_error_message()
