#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 2 13:48 2021
Milestone Project: Pomodoro Timer
@author: lavarius
"""
import tkinter as tk
from tkinter import ttk
from collections import deque # for rotating items in a list
class PomodoroTimer(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Pomodoro Timer")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        container = ttk.Frame(self)
        container.grid()
        container.columnconfigure(0, weight=1)

        timer_frame = Timer(container)
        timer_frame.grid(row=0, column=0, sticky="NESW")

class Timer(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.current_time = tk.StringVar(value="00:10")
        # List describing timers
        self.timer_order = ["Pomodoro", "Short Break", "Pomodoro", "Short Break", "Pomodoro", "long Break"]
        # Create a deck with this list, keeping it unchanged
        # Rearranging with deck instead of a list
        self.timer_schedule = deque(self.timer_order) # rotate elements from one end to another
        # creating a label to show which timer we are on
        self.current_timer_label = tk.StringVar(value=self.timer_schedule[0])
        self.timer_running = True

        timer_description = ttk.Label(
            self,
            textvariable=self.current_timer_label
        )

        timer_description.grid(row=0, column=0, sticky="W", padx=(10,0), pady=(10,0))


        # creat another inner frame for this Label
        timer_frame = ttk.Frame(self, height="100")
        timer_frame.grid(pady=(10,0), sticky="NSEW")

        # create label
        timer_counter = ttk.Label(
            timer_frame, # inside timer frame
            textvariable=self.current_time
        )
        #timer_counter.grid() # place in row 0 col 0 of timer frame
        timer_counter.place(relx=0.5, rely=0.5, anchor="center") # pack and grid, position elements relative to elements
                                # place to absolutely position elements
        self.decrement_time() # call this every second

    def decrement_time(self):
        # start off with current time
        current_time = self.current_time.get() # str of value self.current_time

        # there is an easier way to do this using divmod (built in function in python)
        if self.timer_running and current_time != "00:00":
            minutes, seconds = current_time.split(":")

            if int(seconds) > 0:
                seconds = int(seconds) - 1
                minutes = int(minutes)
            else:
                seconds = 59
                minutes = int(minutes) - 1
            
            self.current_time.set(f"{minutes:02d}:{seconds:02d}")
            # call after method() of the frame
            self.after(1000, self.decrement_time) # every 1s, call function
        elif self.timer_running and current_time == "00:00":
            # assume we are on the first setting "Pomodoro"
            self.timer_schedule.rotate(-1) # takes first value and moves it to the end
            next_up = self.timer_schedule[0]
            # update timer type label
            self.current_timer_label.set(next_up)

            if next_up == "Pomodoro":
                self.current_time.set("25:00")
            elif next_up == "Short Break":
                self.current_time.set("05:00")
            elif next_up == "Long Break":
                self.current_time.set("15:00")
                
            self.after(1000, self.decrement_time)


app = PomodoroTimer()
app.mainloop()