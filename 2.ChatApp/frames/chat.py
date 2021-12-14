import tkinter as tk
from tkinter import ttk
import requests
import datetime
from PIL import Image, ImageTk

TARGET_SIZE = (56,56)

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
        self.update_message_widgets()

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
        # a tuple, in list comprehension
        existing_labels = [
            (message["text"], time["text"]) for message, time in message_labels]

        for message in messages:
            # message time variable, accompanied with new frame and container
            message_time = datetime.datetime.fromtimestamp(message["date"]).strftime(
                "%d-%m-%Y %H:%M:%S"
            )
            # check for existing message labels to remove duplicates
            if (message["message"], message_time) not in existing_labels:
                self._create_message_container(message["message"], message_time, message_labels)

    def _create_message_container(self, message_content, message_time, message_labels):
        """
            Creates the message container and is responsible for calling the next method for creating the message contents
        """
        container = ttk.Frame(self.messages_frame)
        container.columnconfigure(1, weight=1)
        container.grid(sticky="EW", padx=(10, 50), pady=10)

        # call a method to create message content
        self._create_message_bubble(container, message_content, message_time, message_labels)

    def _create_message_bubble(self, container, message_content, message_time, message_labels):
        """
            Creates the message content
        """
        # create avatar image bubble
        avatar_image = Image.open("./assets/avatar_g.jpg")
        resized_img = avatar_image.resize(TARGET_SIZE)
        # convert to imageTk image
        avatar_photo = ImageTk.PhotoImage(resized_img)
        avatar_label = ttk.Label(
            container,
            image=avatar_photo
        )
        # save this image somewhere so it doesn't get trashed
        avatar_label.image = avatar_photo #creates image property inside avatar label as a custom property assigned as avatar_photo
        avatar_label.grid(
            row=0,
            column=0,
            rowspan=2, # span time label (row 0) and messsage label (row 1)
            sticky="NEW",
            padx=(0, 10),
            pady=(5,0)
        )


        time_label = ttk.Label(
            container,
            text=message_time
        )
        time_label.grid(row=0, column=1, sticky="NEW")


        message_label = ttk.Label(
            #self.messages_frame, # inside messages frame
            container,
            #text=message["message"], #obtain 'message' property
            text=message_content,
            anchor="w",
            justify="left" # label to left and text to left instead of center (default)
        )

        # place into container using grid
        message_label.grid(row=1, column=1, sticky="NSEW")

        # storing the list of message_labels
        #message_labels.append(message_label)
        message_labels.append((message_label, time_label))