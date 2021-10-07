import tkinter as tk                # python 3
from tkinter import font as tkfont  # python 3
import json
import os

class UserScreen(tk.Frame):

    def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller
            button = tk.Button(self, text="Go to the start page",
                            command=lambda: controller.show_frame("StartPage"))
            button.pack()
            tk.Label(self,text="Adding more in a sec").pack()