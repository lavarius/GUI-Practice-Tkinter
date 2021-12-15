import tkinter as tk
from frames.chat import Chat


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
        self.chat_frame = Chat(self)

        self.chat_frame.grid(row=0, column=0, sticky="NSEW")

root = Messenger()
root.mainloop()
