import tkinter as tk
from frames.chat import Chat
from tkinter import ttk
import tkinter.font as font

COLOUR_LIGHT_BACKGROUND_1 = "#fff"
COLOUR_LIGHT_BACKGROUND_2 = "#f2f3f5"
COLOUR_LIGHT_BACKGROUND_3 = "#e3e5e8"

COLOUR_LIGHT_TEXT = "#aaa"

COLOUR_BUTTON_NORMAL = "#5fba7d"
COLOUR_BUTTON_ACTIVE = "#58c77c"
COLOUR_BUTTON_PRESSED = "#44e378"

# Messenger class which is our TK application
# Main application window
class Messenger(tk.Tk):
    def __init__(self, *args, **kwargs):
        # call super classes to start the process
        super().__init__(*args, **kwargs)

        # define starting size
        self.geometry("1200x500")

        # minimum window application size
        self.minsize(800, 500)
        # some column and row configurations (c 0, r 0), top left
        # with maximum size possible
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # chat frame that has the custom Chat class
        self.chat_frame = Chat(
            self,
            background=COLOUR_LIGHT_BACKGROUND_1,
            style="Messages.TFrame"
        )

        self.chat_frame.grid(row=0, column=0, sticky="NSEW")

# create root object, messenger
root = Messenger()

# styling
# increase font size
font.nametofont("TkDefaultFont").configure(size=14)

# create style database
style = ttk.Style(root)
# clam theme is more configurable than native themes, homogenous in other OS
style.theme_use("clam")

# frame BGC3
style.configure("Messages.TFrame", background=COLOUR_LIGHT_BACKGROUND_3)

# Frame BGC2
style.configure("Controls.TFrame", background=COLOUR_LIGHT_BACKGROUND_2)

# button styles
style.configure("SendButton.TButton", borderwidth=0, background=COLOUR_BUTTON_NORMAL)
style.map(
    "SendButton.TButton",
    background=[("pressed", COLOUR_BUTTON_PRESSED), ("active", COLOUR_BUTTON_ACTIVE)],
)

style.configure(
    "FetchButton.TButton", background=COLOUR_LIGHT_BACKGROUND_1, borderwidth=0
)

style.configure(
    "Time.TLabel",
    padding=5,
    background=COLOUR_LIGHT_BACKGROUND_1,
    foreground=COLOUR_LIGHT_TEXT,
    font=8
)

style.configure("Avatar.TLabel", background=COLOUR_LIGHT_BACKGROUND_3)
style.configure("Message.TLabel", background=COLOUR_LIGHT_BACKGROUND_2)

# start root object
root.mainloop()
