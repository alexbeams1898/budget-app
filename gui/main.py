import tkinter as tk
from tkinter import *
from gui.pages import Home, Login, NewUser

from server.app import app


class MainGui(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Multi-Page Application")
        self.geometry("400x300")

        # Container to hold the frames
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        # Dictionary to hold references to each page
        self.frames = {}

        # Create and store pages
        for PageClass in (Home, Login, NewUser):
            page_name = PageClass.__name__
            frame = PageClass(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Show the initial page
        self.show_frame("Login")

    def show_frame(self, page_name):
        """Show a frame for the given page name."""
        frame = self.frames[page_name]
        frame.tkraise()  # Bring the frame to the front

def run_gui():
    app = MainGui()
    app.mainloop()
