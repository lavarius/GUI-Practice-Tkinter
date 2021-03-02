#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 20:19:18 2021
Milestone Project: Distance Converter
@author: mdbart
"""
import tkinter as tk
# import font package to change local and global font
import tkinter.font as font
from tkinter import ttk
# from windows import set_dpi_awareness

# might want to set static window size, set to non resizable

# set_dpi_awarenes()

root = tk.Tk()
root.title("Distance Converter")
# adjustable width for column
#root.columnconfigure(0, weight=1)

font.nametofont("TkDefaultFont").configure(size=15) # extracts from tkinter the default font

# text variable for input
metres_value = tk.StringVar()
feet_value = tk.StringVar(value="Feet shown here") # sticky value
# fn to calculate feet at button press
def calculate_feet(*args):
    try:
        #pass
        metres = float(metres_value.get())
        feet = metres*3.28084
        #print(f"{metres} metres is equal to {feet:.3f} feet.")
        feet_value.set(f"{feet:.3f}")
    except ValueError: # avoid crashing our program if value isn't provided
        pass


# frame
main = ttk.Frame(root, padding=(30,15))
main.grid() # col 0 and ro 0

# create widgets
# label and buttons
metres_label = ttk.Label(main, text="Metres: ")
metres_input = ttk.Entry(main, width=10, textvariable=metres_value, font=("Helvetica", 15))
feet_label = ttk.Label(main, text="Feet: ")
feet_display = ttk.Label(main,  textvariable=feet_value)
calc_button = ttk.Button(main, text="Calculate", command=calculate_feet)

# place all elements in the main frame by using grid
# top most element, metres label and 
# can use children to change the padding easily
metres_label.grid(column=0, row=0, sticky = "W", padx=15, pady=15) # stick left
metres_input.grid(column=1, row=0, sticky="EW", padx=15, pady=15) # span the column
metres_input.focus()

feet_label.grid(column=0, row=1, sticky = "W", padx=15, pady=15) # stick left
feet_display.grid(column=1, row=1, sticky="EW", padx=15, pady=15) # span the column

calc_button.grid(column=0, row=2, columnspan=2, sticky="EW", padx=15, pady=15)

# create key bindings to operate window with keyboard
root.bind("<Return>", calculate_feet) # only one field
    # same command as the button
root.bind("<KP_Enter>", calculate_feet) # on numpad keyboard enter
#metres_input.bind() # can bind to only input if preferred

root.mainloop()
