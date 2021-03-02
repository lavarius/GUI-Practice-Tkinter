#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 02 10:22 AM 2021
OOP with Tkinter
Milestone Project: Distance Converter with Object Oriented Programming
@author: lavarius
"""
import tkinter as tk
# import font package to change local and global font
import tkinter.font as font
from tkinter import ttk
# ----- Windows imports ----
# use an if statement posssibly?
#from windows import set_dpi_awareness
#set_dpi_awarenes()
# --------------------------

# Creating our own class and inherit from tk and is copy of tk.Tk()
class HelloWorld(tk.Tk):
    def __init__(self):
        # define a super class, any initialization to be performed
        super().__init__()

        self.title("Distance Converter")
        UserInputFrame(self).pack()
        #ttk.Label(self, text="Hello, World!").pack()

# clone of ttk.Frame()
class UserInputFrame(ttk.Frame):
    def __init__(self, container): # argument for container
        super().__init__(container)

        self.user_input = tk.StringVar()
        label = ttk.Label(self, text="Enter your name:")
        entry = ttk.Entry(self, textvariable=self.user_input)
        button = ttk.Button(self, text="Greet", command=self.greet)

        label.pack(side="left")
        entry.pack(side="left")
        button.pack(side="left")

    def greet(self):
        print(f"Hello, {self.user_input.get()}!")

root = HelloWorld()

root.mainloop()
