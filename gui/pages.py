
import tkinter as tk
from tkinter import ttk
from tkinter import *

import server.db as db

db.create_db()


class Home(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        ttk.Button(self, text="Go to Page 2",
                   command=lambda: controller.show_frame("Login"))
        self.grid(column=0, row=0, sticky=(N, W, E, S))

        val = IntVar()
        val_entry = ttk.Entry(self, width=7, textvariable=val)
        val_entry.grid(column=2, row=1, sticky=(W, E))

        db_val = IntVar()
        ttk.Label(self, textvariable=db_val).grid(
            column=2, row=2, sticky=(W, E))
        ttk.Label(self, text="value").grid(column=3, row=2, sticky=W)

        ttk.Button(self, text="Get", command=lambda: self.get_val(
            val)).grid(column=3, row=3, sticky=W)
        ttk.Button(self, text="Set", command=lambda: self.set_val(
            db_val)).grid(column=4, row=3, sticky=W)

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5)

        val_entry.focus()

    def set_val(self, val):
        print(val)
        db.set_db_val(val.get())

    def get_val(self, db_val):
        print(db.get_db_val())
        db_val.set(db.get_db_val())


class Login(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        # ttk.Button(self, text="Go to Page 2",
        #            command=lambda: controller.show_frame("Home"))
        self.grid(column=0, row=0, sticky=(N, W, E, S))

        ttk.Label(self, text="Username").grid(column=2, row=1, sticky=W)

        username = StringVar()
        username_entry = ttk.Entry(self, width=7, textvariable=username)
        username_entry.grid(column=2, row=2, sticky=(W, E))

        ttk.Button(self, text="New User", command=lambda: controller.show_frame(
            "NewUser")).grid(column=4, row=3, sticky=W)
        ttk.Button(self, text="Login", command=lambda: self.login(
            username)).grid(column=5, row=3, sticky=W)

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5)

        username_entry.focus()

    def login(self, username):
        user_data = db.get_user(username.get())
        print(user_data)


class NewUser(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        # ttk.Button(self, text="Go to Page 2",
        #            command=lambda: controller.show_frame("Home"))
        self.grid(column=0, row=0, sticky=(N, W, E, S))

        ttk.Label(self, text="Enter a name for the new user:").grid(
            column=2, row=1, sticky=W)

        username = StringVar()
        username_entry = ttk.Entry(self, width=7, textvariable=username)
        username_entry.grid(column=2, row=2, sticky=(W, E))

        ttk.Button(self, text="Add", command=lambda: self.add_new_user(
            username.get())).grid(column=4, row=4, sticky=W)
        ttk.Button(self, text="Cancel", command=lambda: controller.show_frame(
            "Login")).grid(column=5, row=4, sticky=W)

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5)

        username_entry.focus()

    def add_new_user(self, username):
        db.add_user(username)
        self.controller.show_frame("Login")
