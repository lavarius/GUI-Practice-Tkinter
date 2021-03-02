#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 20:19:18 2021
Milestone Project: Distance Converter
@author: lavarius
"""
import tkinter as tk
# import font package to change local and global font
import tkinter.font as font
from tkinter import ttk
# from windows import set_dpi_awareness

# might want to set static window size, set to non resizable

# set_dpi_awarenes()

# Creating our own class and inherit from tk and is copy of tk.Tk()
class DistanceConverter(tk.Tk):
    def __init__(self, *args, **kwargs):
        # define a super class, any initialization to be performed
        super().__init__(*args, **kwargs)

        self.title("Distance Converter") # self. <- made into object property
        # -- Frame --
        frame = MetresToFeet(self, padding=(30,15))
        frame.grid()
        #ttk.Label(self, text="Hello, World!").pack()

        # create key bindings to operate window with keyboard
        self.bind("<Return>", frame.calculate_feet) # only one field
        self.bind("<KP_Enter>", frame.calculate_feet) # on numpad keyboard enter
        #metres_input.bind() # can bind to only input if preferred

# -- Frame Class --
class MetresToFeet(ttk.Frame):
    def __init__(self, container, **kwargs):
        super().__init__(container)
        # text variable for input
        self.metres_value = tk.StringVar()
        self.feet_value = tk.StringVar(value="Feet shown here") # sticky value
        # -- Widgets --
        # create widgets
        # label and buttons
        metres_label = ttk.Label(self, text="Metres: ")
        metres_input = ttk.Entry(self, width=10, textvariable=self.metres_value, font=("Helvetica", 15))
        feet_label = ttk.Label(self, text="Feet: ")
        feet_display = ttk.Label(self,  textvariable=self.feet_value)
        calc_button = ttk.Button(self, text="Calculate", command=self.calculate_feet)

        # -- Layout -- 
        # place all elements in the main frame by using grid
        # top most element, metres label and 
        # Below are Children of the Frame
        metres_label.grid(column=0, row=0, sticky = "W") # stick left
        metres_input.grid(column=1, row=0, sticky="EW") # span the column
        metres_input.focus()
        feet_label.grid(column=0, row=1, sticky = "W") # stick left
        feet_display.grid(column=1, row=1, sticky="EW") # span the column
        calc_button.grid(column=0, row=2, columnspan=2, sticky="EW" )
        # Widget Info Window, padx and pady on all children
        for child in self.winfo_children():
            child.grid_configure(padx=15, pady=15)
            
    # fn to calculate feet at button press
    def calculate_feet(self, *args):
        try:
            metres = float(self.metres_value.get())
            feet = metres*3.28084
            #print(f"{metres} metres is equal to {feet:.3f} feet.")
            self.feet_value.set(f"{feet:.3f}")
        except ValueError: # avoid crashing our program if value isn't provided
            pass

root = DistanceConverter()
# adjustable width for column

font.nametofont("TkDefaultFont").configure(size=15) # extracts from tkinter the default font

root.columnconfigure(0, weight=1)

root.mainloop()
