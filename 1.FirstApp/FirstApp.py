# App Widget 
# Author: Mark Bartolo
# Date: 2021.02.23 Tuesday
import tkinter as tk
from tkinter import ttk # widgets, native looking windows

def greet():
    print(f"Hello, {user_name.get() or 'Unnamed World'}!")

# Create the main window
root= tk.Tk() #creating a TK object, main window of application | container
# title for the root window
root.title("Greeter App")

# Create TkStringVar
user_name = tk.StringVar()

# Frame to customize orientation of widgets
input_frame = ttk.Frame(root, padding=(20, 10, 20, 0))
input_frame.pack(fill="both")

# Create entry field for the main window, label 
name_label = ttk.Label(input_frame, text="Name: ") # pass container with Label
# Label in window, .pack() layout algorithm puts element into the window
name_label.pack(side = "left", padx=(10, 10)) 

# Entry field
name_entry = ttk.Entry(input_frame, width=15, textvariable=user_name)
# textvariable must have a tk string var
name_entry.pack(side="left")
name_entry.focus() # focus to this entry field when window is opened

# Button widgets
#   Button frame for widget formation
buttons_frame = ttk.Frame(root, padding=(20,10))
buttons_frame.pack(fill="both")

greet_button = ttk.Button(buttons_frame, text="Greet", command=greet)
greet_button.pack(side="left", fill="x", expand=True)

# quit buttonn
quit_button = ttk.Button(buttons_frame, text="Quit", command=root.destroy)
#pack into the window
quit_button.pack(side="left", fill="x", expand=True)

root.mainloop() # starts running
