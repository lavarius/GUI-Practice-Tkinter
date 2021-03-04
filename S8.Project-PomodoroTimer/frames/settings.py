
import tkinter as tk
from tkinter import ttk

class Settings(ttk.Frame):
    def __init__(self, parent, controller, show_timer):
        super().__init__(parent)
        # similar to the timer frame, has a parent and a controller, getting different values
        
        # additional configurations, to tighten up the look
        self.columnconfigure(0, weight=1)
        self.rowconfigure(2, weight=1)

        # settings container frame
        settings_container = ttk.Frame(
            self,
            padding = "30 15 30 15",
        )

        settings_container.grid(row=0, column=0, sticky="EW", padx=10, pady=10)

        settings_container.columnconfigure(0, weight=1)
        settings_container.rowconfigure(1, weight=1)

        # Variables will have a label and spin box
        pomodoro_label = ttk.Label(
            settings_container,
            text="Pomodoro: "
        )
        pomodoro_label.grid(row=0, column=0, sticky="W")

        pomodoro_input = tk.Spinbox(
            settings_container,
            from_=0,
            to=120,
            increment = 1,
            justify="center",
            textvariable=controller.pomodoro,
            width=10
        )
        pomodoro_input.grid(row=0, column=1, sticky="EW")
        pomodoro_input.focus()

        # long break
        long_break_label = ttk.Label(
            settings_container,
            text="Long Break Time: "
        )
        long_break_label.grid(row=1, column=0, sticky="W")

        long_break_input = tk.Spinbox(
            settings_container,
            from_=0,
            to=60,
            increment = 1,
            justify="center",
            textvariable=controller.long_break,
            width=10
        )
        long_break_input.grid(row=1, column=1, sticky="EW")

        # short break timer
        short_break_label = ttk.Label(
            settings_container,
            text="Short Break Time: "
        )
        short_break_label.grid(row=2, column=0, sticky="W")

        short_break_input = tk.Spinbox(
            settings_container,
            from_=0,
            to=30,
            increment = 1,
            justify="center",
            textvariable=controller.short_break,
            width=10
        )
        short_break_input.grid(row=2, column=1, sticky="EW")

        # Breathing Room
        for child in settings_container.winfo_children():
            child.grid_configure(padx=5, pady=5)

        # Back Button
        button_container = ttk.Frame(self)
        button_container.grid(sticky="EW", padx=10) # placed in next row
        button_container.columnconfigure(0, weight=1) # configure the column 0 to take up all the available space

        timer_button = ttk.Button(
            button_container,
            text="<- Back",
            command=show_timer, # call fn from lambda function
            cursor="hand2"
        )
        timer_button.grid(column=0, row=0, sticky="EW", padx=2)
