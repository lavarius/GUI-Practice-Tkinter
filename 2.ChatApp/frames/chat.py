import tkinter as tk
from tkinter import ttk
import requests
# import files
from frames.message_window import MessageWindow

# default sample message, if server was offline
messages = [{"message": "Hello, world", "date": 15498487}]

# empty list, creating empty labels for each message, to only show new messages with new labels
message_labels = []


class Chat(ttk.Frame):
    def __init__(self, container, background, **kwargs):
        # super class call
        super().__init__(container, **kwargs)

        # column and row configuration
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # a message frame to put into our messages
        #self.messages_frame = ttk.Frame(self)
        self.message_window = MessageWindow(self, background=background) # create a message object instead, not a frame but now a Canvas
        # place messages_frame using grid, entire cell with some top&bottom padding
        self.message_window.grid(row=0, column=0, sticky="NSEW", pady=5)

        # add a button frame for 'input_frame'
        input_frame = ttk.Frame(self, style="Controls.TFrame", padding=10) # frame to contain button
        # placed inside of self, which is the Chat object

        # On row 1, adding something else in row 0 later
        input_frame.grid(row=1, column=0, sticky="EW")

        # create a container for posting messages
        self.message_input = tk.Text(input_frame, height=3)
        self.message_input.pack(expand=True, fill="both", side="left", padx=(0, 10))

        message_submit = ttk.Button(
            input_frame,
            text="Send",
            style="SendButton.TButton",
            command=self.post_message

        )
        message_submit.pack() #automatic put on side as top

        # Create the button for getting messages
        message_fetch = ttk.Button(
            input_frame,
            text="Fetch",
            style="FetchButton.TButton",
            command=self.get_messages
        )
        message_fetch.pack()
        # note can use grid() and pack() in the same application but not the same container
        # since we use pack() on the input_frame, all other widgets must use pack() as well
        # however, anything else inside self, must use grid since self uses grid()
        #self.update_message_widgets()
        self.message_window.update_message_widgets(messages, message_labels)

    def post_message(self):
        """
            need content and send request

        """
        #Test
        #body = "message body"
        body = self.message_input.get("1.0", "end").strip()

        # send message to server
        requests.post("http://167.99.63.70/message", json={"message": body})

        # delete the message input that was typed previously
        self.message_input.delete("1.0", "end")

        # refresh messages
        self.get_messages()

    def get_messages(self):
        """
            Makes a request to the server 
        """
        global messages # to store messages and access in other methods
        # get data, as object as .json
        messages = requests.get("http://167.99.63.70/messages").json()
        #print(messages)
        # update the method of printing out messages
        self.message_window.update_message_widgets(messages, message_labels)

        # after 150 ms, move to bottom of scrollable frame
        self.after(150, lambda: self.message_window.yview_moveto(1.0))

    