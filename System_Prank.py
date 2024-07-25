import tkinter as tk
from tkinter import messagebox
import random
import time

def fake_error_messages():
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
    
    # Create the root window
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    
    for _ in range(10):
        # Randomly select an error message
        selected_message = random.choice(messages)
        
        # Show the fake error message
        messagebox.showerror("Error", selected_message)
        
        # Wait for 2 seconds before showing the next message
        time.sleep(2)
    
    # Destroy the root window after showing all messages
    root.destroy()

if __name__ == "__main__":
    fake_error_messages()
