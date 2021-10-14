import tkinter as tk                # python 3
from tkinter import font as tkfont  # python 3
import json
import os
import user_data

class Game_Screen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.text1 = tk.StringVar()
        self.text2 = tk.StringVar()

        self.text1.set("Hangman")
        self.text2.set("YaY")
        button = tk.Button(self, text="Go to the start page",
                        command=lambda: controller.show_frame("UserScreen"))
        button.pack()

        self.label1 = tk.Label(self, textvariable=self.text1)
        self.label2 = tk.Label(self, textvariable=self.text2)
        
        self.label1.pack()
        self.label2.pack()

    def load_game(self):
        pass
    def update_screen(self):
        pass