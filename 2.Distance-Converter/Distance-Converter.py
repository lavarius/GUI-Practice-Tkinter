#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 20:19:18 2021
Milestone Project: Distance Converter
@author: mdbart
"""
import tkinter as tk
from tkinter import ttk
# from windows import set_dpi_awareness

# set_dpi_awarenes()

root = tk.Tk()
root.title("Distance Converter")

# adjustable width for column
#root.columnconfigure(0, weight=1)

# frame
main = ttk.Frame(root, padding=(30,15))
main.grid() # col 0 and ro 0

# create widgets
# label and buttons
metres_label = ttk.Label(main, text="Metres: ")
metres_input = ttk.Entry(main, width=10)
feet_label = ttk.Label(main, text="Feet: ")
feet_display = ttk.Label(main, text="Feet shown here")
calc_button = ttk.Button(main, text="Calculate")

# place all elements in the main frame by using grid
# top most element, metres label and 
metres_label.grid(column=0, row=0, sticky = "W", padx=5, pady=5) # stick left
metres_input.grid(column=1, row=0, sticky="EW", padx=5, pady=5) # span the column
metres_input.focus()

feet_label.grid(column=0, row=1, sticky = "W", padx=5, pady=5) # stick left
feet_display.grid(column=1, row=1, sticky="EW", padx=5, pady=5) # span the column

calc_button.grid(column=0, row=2, columnspan=2, sticky="EW", padx=5, pady=5)

root.mainloop()
