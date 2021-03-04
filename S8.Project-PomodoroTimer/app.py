#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 2 13:48 2021
Milestone Project: Pomodoro Timer
app.py
Basically main

@author: lavarius
"""
import tkinter as tk
from tkinter import ttk
from collections import deque # for rotating items in a list
from frames import Timer, Settings

# controller
class PomodoroTimer(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Pomodoro Timer")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        # creating amount of time each timer lasts for
        self.pomodoro = tk.StringVar(value=25)
        self.long_break = tk.StringVar(value=15)
        self.short_break = tk.StringVar(value=5)

        # control time and timings, timer moved from timer class
        self.timer_order = ["Pomodoro", "Short Break", "Pomodoro", "Short Break", "Pomodoro", "long Break"]
        # Create a deck with this list, keeping it unchanged, Rearranging with deck instead of a list
        self.timer_schedule = deque(self.timer_order) # rotate elements from one end to another

        container = ttk.Frame(self)
        container.grid()
        container.columnconfigure(0, weight=1)

        # timer_frame = Timer(container, self)
        # timer_frame.grid(row=0, column=0, sticky="NESW")

        settings_frame = Settings(container, self)  
        settings_frame.grid(row=0, column=0, sticky="NESW")

app = PomodoroTimer()
app.mainloop()