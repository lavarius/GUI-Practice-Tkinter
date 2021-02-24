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

# configure column sizing aswindow changes
root.columnconfigure(0,  weight=1)

# Create TkStringVar
user_name = tk.StringVar()

# Frame to customize orientation of widgets
input_frame = ttk.Frame(root, padding=(20, 10, 20, 0))
# Grid Geoemetry
input_frame.grid(row=0, column=0, sticky="EW")

# Create entry field for the main window, label 
name_label = ttk.Label(input_frame, text="Name: ") # pass container with Label
# Label in window, .pack() layout algorithm puts element into the window
name_label.grid(row=0, column= 0, padx=(10, 10)) 

# Entry field
name_entry = ttk.Entry(input_frame, width=15, textvariable=user_name)
# textvariable must have a tk string var
name_entry.grid(row=0, column= 1)
name_entry.focus() # focus to this entry field when window is opened

# Button widgets
#   Button frame for widget formation
buttons_frame = ttk.Frame(root, padding=(20,10))
buttons_frame.grid(row=1, column=0, sticky="EW") # stick east and west

# size changing buttons using tuples
buttons_frame.columnconfigure(0,  weight=1)
buttons_frame.columnconfigure(1,  weight=1)

greet_button = ttk.Button(buttons_frame, text="Greet", command=greet)
greet_button.grid(row=0, column= 0, sticky="EW")

# quit buttonn
quit_button = ttk.Button(buttons_frame, text="Quit", command=root.destroy)
#pack into the window
quit_button.grid(row=0, column= 1, sticky="EW")

root.mainloop() # starts running window and pauses the program here
