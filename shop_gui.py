import tkinter as tk                # python 3
from tkinter import font as tkfont  # python 3
import os

class ShopScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        tk.Button(self, text="Go to the start page",command=lambda: controller.show_frame("UserScreen")).grid()
