import tkinter as tk                # python 3
from tkinter import font as tkfont  # python 3
from tkinter import *
from tkinter import messagebox
from string import ascii_uppercase
from game_logic import Hangman
import random
import game_data
from database import *
from tkinter import ttk
class Hign_Score_Screen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg="lightcyan3")

        button = tk.Button(self, text="Main Menu", font=("Georgia", 10, "bold"), bg = "skyblue4", fg = "white", padx=24,
                           command=lambda: self.back_to_sign_in())
        
        self.games = ["EASY_WORDS", "HARD_WORDS", "ANIMALS", "COUNTRIES", "MOVIE_QUOTES"]
        self.count = 0
        self.game = tk.StringVar()
        self.game.set(self.games[self.count])
        button.pack(side="top", pady = 10)
        self.label1 = tk.Label(self, textvariable=self.game, font=("Aharoni", 20), bg = "lightcyan3", fg = "black", padx=24).pack()
        tk.Button(self,text="Next", font=("Georgia", 10), bg = "skyblue4", fg = "white", command=lambda: self.next()).place(x=440, y=360)           #Next Button
        tk.Button(self,text="Back", font=("Georgia", 10), bg = "skyblue4", fg = "white", command=lambda: self.back()).place(x=365, y=360)           #Back Button
        self.scores = tk.Frame(self, bg = "lightcyan3")
        self.scores.pack()
        tk.Label(self.scores, textvariable="", bg = "lightcyan3").pack()
        self.label1 = tk.StringVar()
        self.label2 = tk.StringVar()
        self.label3 = tk.StringVar()
        self.label4 = tk.StringVar()
        self.label5 = tk.StringVar()
        self.label6 = tk.StringVar()
        self.label7 = tk.StringVar()
        self.label8 = tk.StringVar()
        self.label9 = tk.StringVar()
        self.label10 = tk.StringVar()
        self.label_list = [self.label1, self.label2, self.label3, self.label4, self.label5, 
                           self.label6, self.label7, self.label8, self.label9, self.label10]
        for l in self.label_list:
            l.set("")
            tk.Label(self.scores, textvariable=l, font=("Aharoni", 12), bg = "lightcyan3", fg = "black", padx=24,).pack()
        self.update_data()

    def update_data(self):
        mode = self.games[self.count]
        scores = get_high_score_data(mode)
        score_list = []
        for s in range(len(scores)):
            temp_str = f"{s+1}. {scores[s][0]}:{scores[s][1]}"
            score_list.append(temp_str)

        if len(score_list) != 10:
            for i in range(10):
                try:
                    if score_list[i]:
                        pass
                except IndexError:
                    score_list.append(f"{i+1}. ")

        for s in range(len(score_list)):
            self.label_list[s].set(score_list[s])
    
    def next(self):
        if self.count == len(self.games)-1:
            return
        else:
            self.count += 1
        self.game.set(self.games[self.count])
        self.update_data()

    def back(self):
        if self.count == 0:
            return
        else:
            self.count -= 1
        self.game.set(self.games[self.count])
        self.update_data()

    def back_to_sign_in(self):
        self.controller.show_frame("StartPage")



        




