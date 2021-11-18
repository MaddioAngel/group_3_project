import tkinter as tk                # python 3
from tkinter import font as tkfont  # python 3
import json
import os
from database import *
import user_data
import game_data
import screens


class UserScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.name = ""
        self.money = 0

        self.controller = controller
        self.text1 = tk.StringVar()
        self.text3 = tk.StringVar()
        self.text1.set("")

        self.text3.set("")
        button = tk.Button(self, text="Go to the start page",
                        command=lambda: self.return_to_sign_in())
        button.pack()
        self.label1 = tk.Label(self, textvariable=self.text1).pack()
        self.label3 = tk.Label(self, textvariable=self.text3).pack()
        self.games = tk.Frame(self)
        self.games.pack()

        tk.Button(self,text="Shop", width=10, height=1, command=lambda: controller.show_frame("ShopScreen")).pack()
        
    def get_user_info(self):
        global user_data
        self.name, self.money, self.points, self.unlocked = get_user_data(user_data.user_name)
        unlocked_list = self.unlocked.split(" ")
        self.buttons = []

        for game_mode in unlocked_list:
            self.buttons.append(tk.Button(self.games,text=game_mode, width=10, height=1, command=lambda mode=game_mode: self.change_to_game_screen(mode)))
        for button in self.buttons:
            button.pack()
        data_user = f"User: {self.name}"
        data_money = f"Money: {self.money}"
        self.text1.set(data_user) 
        self.text3.set(data_money)

    def change_to_game_screen(self, mode):
        global game_data
        global screens
        game_data.game_mode = mode
        screens.screen_data["Game_Screen"].new_game()
        self.controller.show_frame("Game_Screen")
        self.clear()

    def return_to_sign_in(self):
        self.controller.show_frame("StartPage")
        self.clear()

    def clear(self):
        for button in self.buttons:
            button.destroy()
        self.buttons = []
