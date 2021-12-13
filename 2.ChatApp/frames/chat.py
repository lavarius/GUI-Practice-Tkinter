import tkinter as tk
from tkinter import ttk
import requests

# default sample message, if server was offline
messages = [{"message": "Hello, world", "date": 15498487}]

# empty list, creating empty labels for each message, to only show new messages with new labels
message_labels = []


class Chat(ttk.Frame):
    def __init__(self, container, **kwargs):
        # super class call
        super().__init__(container, **kwargs)

        # column and row configuration
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # a message frame to put into our messages
        self.messages_frame = ttk.Frame(self)
        # place messages_frame using grid, entire cell with some top&bottom padding
        self.messages_frame.grid(row=0, column=0, sticky="NSEW", pady=5)

        # add a button frame for 'input_frame'
        input_frame = ttk.Frame(self, padding=10) # frame to contain button
        # placed inside of self, which is the Chat object

        # On row 1, adding something else in row 0 later
        input_frame.grid(row=1, column=0, sticky="EW")

        # Create the button for getting messages
        message_fetch = ttk.Button(
            input_frame,
            text="Fetch",
            command=self.get_messages
        )
        message_fetch.pack()
        # note can use grid() and pack() in the same application but not the same container
        # since we use pack() on the input_frame, all other widgets must use pack() as well
        # however, anything else inside self, must use grid since self uses grid()

    def get_messages(self):
        """
            Makes a request to the server 
        """
        global messages # to store messages and access in other methods
        # get data, as object as .json
        messages = requests.get("http://167.99.63.70/messages").json()
        #print(messages)
        # update the method of printing out messages
        self.update_message_widgets()

    def update_message_widgets(self):
        # determine what existing labels we already have?
        existing_labels = [message["text"] for message in message_labels]

        for message in messages:

            # check for existing message labels to remove duplicates
            if message["message"] not in existing_labels:

                message_label = ttk.Label(
                    self.messages_frame, # inside messages frame
                    text=message["message"], #obtain 'message' property
                    anchor="w",
                    justify="left" # label to left and text to left instead of center (default)
                )

                # place into container using grid
                message_label.grid(sticky="NSEW")

                # storing the list of message_labels
                message_labels.append(message_label)
