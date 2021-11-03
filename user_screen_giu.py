import tkinter as tk                # python 3
from tkinter import font as tkfont  # python 3
import json
import os
from database import *
import user_data


class UserScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.name = ""
        self.money = 0
        self.points = 0 

        self.controller = controller
        self.text1 = tk.StringVar()
        self.text2 = tk.StringVar()
        self.text3 = tk.StringVar()
        self.text1.set("")
        self.text2.set("")
        self.text3.set("")
        button = tk.Button(self, text="Go to the start page",
                        command=lambda: controller.show_frame("StartPage"))
        button.pack()
        self.label1 = tk.Label(self, textvariable=self.text1).pack()
        self.label2 = tk.Label(self, textvariable=self.text2).pack()
        self.label3 = tk.Label(self, textvariable=self.text3).pack()

        tk.Button(self,text="Hangman", width=10, height=1, command=lambda: controller.show_frame("Game_Screen")).pack()
        tk.Button(self,text="Shop", width=10, height=1, command=lambda: controller.show_frame("ShopScreen")).pack()
        tk.Button(self,text="Add money", width=10, height=1, command=self.update_data).pack()
    def get_user_info(self):
        global user_data
        self.name, self.money, self.points = get_user_data(user_data.user_name)
        
        data_user = f"User: {self.name}"
        data_money = f"Money: {self.money}"
        data_points = f"Points: {self.points}"

        self.text1.set(data_user) 
        self.text2.set(data_points) 
        self.text3.set(data_money)

    def update_data(self):
        self.money = int(self.money) + 10
        data_user = f"User: {self.name}"
        data_money = f"Money: {self.money}"
        data_points = f"Points: {self.points}"

        self.text1.set(data_user) 
        self.text2.set(data_points) 
        self.text3.set(data_money)
        update_user_data(str(self.name), float(self.money), int(self.points))




