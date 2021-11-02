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
        self.text3 = tk.StringVar()

        self.text1.set("Hangman")
        self.text2.set("Letter:")
        self.text3.set("Guess:")

        button = tk.Button(self, text="Go to the start page",
                        command=lambda: controller.show_frame("UserScreen"))
        button.pack()

        self.label1 = tk.Label(self, textvariable=self.text1)
        self.label2 = tk.Label(self, textvariable=self.text2)
        self.label3 = tk.Label(self, textvariable=self.text3)
        
        self.label1.pack()
        self.label2.pack()

        entryl = tk.Entry(self, width=1)

        entryl.pack()

        self.label3.pack()

        entryg = tk.Entry(self, width=50)

        entryg.pack()

    def load_game(self):
        pass
    def update_screen(self):
        pass