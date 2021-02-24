# App Widget 
# Author: Mark Bartolo
# Date: 2021.02.23 Tuesday
import tkinter as tk
from tkinter import ttk # widgets, native looking windows

def greet():
    print(f"Hello, {user_name.get() or 'Unnamed World'}!")

# Create the main window
root= tk.Tk() #creating a TK object, main window of application | container

# Create TkStringVar
user_name = tk.StringVar()
# Create entry field for the main window

# label 
name_label = ttk.Label(root, text="Name: ").pack(side = "left", padx=(10, 10)) 
# pass container with Label
# Label in window
# .pack() layout algorithm puts element into the window


# Entry field
name_entry = ttk.Entry(root, width=15, textvariable=user_name)
# textvariable must have a tk string var
name_entry.pack(side="left")
name_entry.focus() # focus to this entry field when window is opened

# Button widgets
greet_button = ttk.Button(root, text="Greet", command=greet)

# pack into the window
# oriented to the left
# fill property reserves space
# expand, fills extra space by expanding
greet_button.pack(side="left", fill="both", expand=True)

# quit buttonn
quit_button = ttk.Button(root, text="Quit", command=root.destroy)
#pack into the window
quit_button.pack(side="left", fill="x")

root.mainloop() # starts running
