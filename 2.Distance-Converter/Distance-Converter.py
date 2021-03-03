#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 20:19:18 2021
Milestone Project: Distance Converter
@author: lavarius
Note: might want to set static window size, set to non resizable
"""
import tkinter as tk
# import font package to change local and global font
import tkinter.font as font
from tkinter import ttk
# from windows import set_dpi_awareness
# set_dpi_awarenes()

# Creating our own class and inherit from tk and is copy of tk.Tk()
class DistanceConverter(tk.Tk):
    def __init__(self, *args, **kwargs):
        # define a super class, any initialization to be performed
        super().__init__(*args, **kwargs)

        self.title("Distance Converter") # self. <- made into object property

        # -- Frame --
        self.frames = dict() # Store Frames as Dictionary
        
        # container frame to be inside the Two Frames:
        # MetresToFeet and FeetToMetres Frame
        container = ttk.Frame(self)
        container.grid(padx=60, pady=50, sticky="EW")

        # Construct frames out of the classes
        for FrameClass in (MetresToFeet, FeetToMetres):
            frame = FrameClass(container, self)
            self.frames[FrameClass] = frame
            frame.grid(row=0, column=0, sticky="NSEW")

        # create key bindings to operate window with keyboard
        # initiate the first frame to work with
        self.show_frame(MetresToFeet)
        #metres_input.bind() # can bind to only input if preferred

    # -- Show Frames --
    def show_frame(self, container):
        frame = self.frames[container]
        # need to assign key bindings here
        self.bind("<Return>", frame.calculate)
        self.bind("<KP_Enter>", frame.calculate) # on numpad keyboard enter
        frame.tkraise() # raise the frame

# -- Frame Class --
class MetresToFeet(ttk.Frame):
    def __init__(self, container, controller, **kwargs):
        super().__init__(container)
        # text variable for input
        self.metres_value = tk.StringVar()
        self.feet_value = tk.StringVar(value="Feet shown here") # sticky value
        
        # -- Widgets | Labels and Buttons--
        metres_label = ttk.Label(self, text="Metres: ")
        metres_input = ttk.Entry(self, width=10, textvariable=self.metres_value, font=("Helvetica", 15))
        feet_label = ttk.Label(self, text="Feet: ")
        feet_display = ttk.Label(self,  textvariable=self.feet_value)
        calc_button = ttk.Button(self, text="Calculate", command=self.calculate)
        switch_page_button = ttk.Button(
            self,
            text="Switch to feet conversion",
            command=lambda: controller.show_frame(FeetToMetres)
        )

        # -- Layout | Children of the Frame using Grid -- 
        metres_label.grid(column=0, row=0, sticky = "W") # stick left
        metres_input.grid(column=1, row=0, sticky="EW") # span the column
        metres_input.focus()
        feet_label.grid(column=0, row=1, sticky = "W") # stick left
        feet_display.grid(column=1, row=1, sticky="EW") # span the column
        calc_button.grid(column=0, row=2, columnspan=2, sticky="EW" )
        switch_page_button.grid(column=0, row=3, columnspan=2, sticky="EW")
        # Widget Info Window, padx and pady on all children
        for child in self.winfo_children():
            child.grid_configure(padx=10, pady=10)
            
    # fn to calculate feet at button press
    def calculate(self, *args):
        try:
            metres = float(self.metres_value.get())
            feet = metres*3.28084
            #print(f"{metres} metres is equal to {feet:.3f} feet.")
            self.feet_value.set(f"{feet:.3f}")
        except ValueError: # avoid crashing our program if value isn't provided
            pass

class FeetToMetres(ttk.Frame):
    def __init__(self, container, controller, **kwargs):
        super().__init__(container)
        # text variable for input
        self.feet_value = tk.StringVar()
        self.metres_value = tk.StringVar(value="Metres shown here") # sticky value
        # -- Widgets | Labels and Buttons--
        feet_label = ttk.Label(self, text="Feet: ")
        feet_input = ttk.Entry(self, width=10, textvariable=self.feet_value, font=("Helvetica", 15))
        metres_label = ttk.Label(self, text="Metres: ")
        metres_display = ttk.Label(self,  textvariable=self.metres_value)
        calc_button = ttk.Button(self, text="Calculate", command=self.calculate)
        switch_page_button = ttk.Button(
            self,
            text="Switch to metres conversion",
            command=lambda: controller.show_frame(MetresToFeet)
        )

        # -- Layout | Children of the Frame using Grid -- 
        feet_label.grid(column=0, row=0, sticky = "W") # stick left
        feet_input.grid(column=1, row=0, sticky="EW") # span the column
        feet_input.focus()
        metres_label.grid(column=0, row=1, sticky = "W") # stick left
        metres_display.grid(column=1, row=1, sticky="EW") # span the column
        calc_button.grid(column=0, row=2, columnspan=2, sticky="EW" )
        switch_page_button.grid(column=0, row=3, columnspan=2, sticky="EW")
        
        # Widget Info Window, padx and pady on all Children
        for child in self.winfo_children():
            child.grid_configure(padx=10, pady=10)
            
    # fn to calculate feet at button press
    def calculate(self, *args):
        try:
            feet = float(self.feet_value.get())
            metres = feet/3.28084
            #print(f"{metres} metres is equal to {feet:.3f} feet.")
            self.metres_value.set(f"{metres:.3f}")
        except ValueError: # avoid crashing our program if value isn't provided
            pass
root = DistanceConverter()
# adjustable width for column

font.nametofont("TkDefaultFont").configure(size=15) # extracts from tkinter the default font

root.columnconfigure(0, weight=1)

root.mainloop()
