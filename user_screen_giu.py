import tkinter as tk                # python 3
from tkinter import font as tkfont  # python 3
import json
import os
import user_data


class UserScreen(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.text1 = tk.StringVar()
        self.text2 = tk.StringVar()

        self.text1.set("")
        self.text2.set("")
        button = tk.Button(self, text="Go to the start page",
                        command=lambda: controller.show_frame("StartPage"))
        button.pack()
        self.label1 = tk.Label(self, textvariable=self.text1).pack()
        self.label2 = tk.Label(self, textvariable=self.text2).pack()
        tk.Button(self,text="Hangman", width=10, height=1, command=lambda: controller.show_frame("Game_Screen")).pack()
    

    def get_user_info(self):
        name = list(user_data.user_dict.keys())[0]
        points = user_data.user_dict[name]["points"]
        data_user = f"User: {name}"
        data_points = f"Points: {points}"

        self.text1.set(data_user) 
        self.text2.set(data_points) 
