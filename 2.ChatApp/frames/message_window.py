import tkinter as tk
from tkinter import ttk
import datetime
from PIL import Image, ImageTk

TARGET_SIZE = (56, 56)

class MessageWindow(tk.Canvas):
	def __init__(self, container, *args, **kwargs):
		super().__init__(container, *args, **kwargs, highlightthickness=0)

		self.message_frame = ttk.Frame(self)
		self.message_frame.columnconfigure(0, weight=1) # take up available space

		# Canvas.create_window, now on self
		self.scrollable_window = self.create_window(0, 0, window=self.message_frame, anchor="nw")


		def configure_scroll_region(event):
			"""
				configure a scrollabe region that takes in an event
			"""
			self.configure(scrollregion=self.bbox("all"))

		def configure_window_size(event):
			"""
				Limit the width of canvas 
			"""
			#self.scrollable_window, not an tkinter widget, it's an ID, 
			self.itemconfig(self.scrollable_window, width=self.winfo_width())

		# Change window size by passing in the function
		self.bind("<Configure>", configure_window_size)

		# configure by passing function
		self.message_frame.bind("<Configure>", configure_scroll_region)

		# configure scrollbar
		scrollbar = ttk.Scrollbar(container, orient="vertical", command=self.yview)
		scrollbar.grid(row=0, column=1, sticky="NS")

		self.configure(yscrollcommand=scrollbar.set)

		# move the canvas down to the very bottom of scrollable area, contents always on the same place when opening up the application
		self.yview_moveto(1.0)

	def update_message_widgets(self, messages, message_labels):
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
		container = ttk.Frame(self.message_frame)
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