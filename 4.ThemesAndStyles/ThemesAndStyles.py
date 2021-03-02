#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 2 13:48 2021
@author: lavarius
Themes and styles with Tkinter
"""
import tkinter as tk
from tkinter import ttk
#import tkinter.font as font
#from windows import set_dpi_awarenes
#set_dpi_awareness

def greet(*args):
    print(f"Hello, {user_name.get()}!")

root = tk.Tk()
root.resizable(False, False)
root.title("Greeter")
# Initialize Style Database
style = ttk.Style(root)
style.configure("CustomEntryStyle.TEntry", font=15)
#font.nametofont("CustomEntryStyle.Tentry").configure(size=13)
# get themes available in your computer, may not be available elsewhere
print(style.theme_names())
#print(style.theme_use("calm"))
# can download and use different available themes

main = ttk.Frame(root, padding=(40,20))
main.grid()

user_name = tk.StringVar()

name_label = ttk.Label(main, text="Name: ")
name_label.grid(row=0, column=0, padx=(0x10))
name_entry = ttk.Entry(main, width = 15, textvariable=user_name)
# create a custom Style
name_entry["style"] = "CustomEntryStyle.TEntry"
name_entry.grid(row=0, column=1, padx=10)
name_entry.focus()

print(name_label.winfo_class()) # check the style used
style.configure("TLabel", font=("Helvetica", 20))
greet_button = ttk.Button(main, text="Greet", command=greet)
greet_button.grid(row=0, column=2, sticky="EW", padx=10)

root.mainloop()
