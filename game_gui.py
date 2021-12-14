import tkinter as tk                # python 3
from tkinter import font as tkfont  # python 3
import json
import os
from tkinter import *
from tkinter import messagebox
from string import ascii_uppercase
from game_logic import Hangman
import random
import game_data
import user_data
from database import *
import screens


class Game_Screen(tk.Frame):
    def __init__(self, parent, controller):
        self.hangman = None
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg="lightcyan3")        
        self.imgLabel = Label(self)
        self.lblWord=StringVar()
        self.photos = [PhotoImage(file="hangman_images/hang11.png"),PhotoImage(file="hangman_images/hang10.png")
        ,PhotoImage(file="hangman_images/hang9.png"),PhotoImage(file="hangman_images/hang8.png")
        ,PhotoImage(file="hangman_images/hang7.png"),PhotoImage(file="hangman_images/hang6.png")
        ,PhotoImage(file="hangman_images/hang5.png"),PhotoImage(file="hangman_images/hang4.png")
        ,PhotoImage(file="hangman_images/hang3.png"),PhotoImage(file="hangman_images/hang2.png")
        ,PhotoImage(file="hangman_images/hang1.png"),PhotoImage(file="hangman_images/hang0.png")]

    def new_game(self):
        global game_data
        word = get_random_word_data(game_data.game_mode)
        self.hangman = Hangman(word[0])
        print(word)
        self.imgLabel.config(image=self.photos[self.hangman.tries], bg = "lightcyan3") 
        self.imgLabel.place_slaves()
        self.lblWord.set(self.hangman.string_completed())
        tk.Button(self, text="Menu", font=("Georgia", 10, "bold"), bg = "skyblue4", fg = "white", command=lambda: self.back_to_user(), width=10).grid(row = 0, column = 0, columnspan=2)
        self.imgLabel.grid(row=1, column=0, columnspan=3, padx=10, pady=40)
        Label(self, textvariable=self.lblWord, font=("Georgia", 14), bg = "lightcyan3", fg = "black", wraplength=450).grid(row=1, column=3, rowspan=3, columnspan=7)
        n=0
        for c in ascii_uppercase:
            Button(self, text=c, font=("Georgia", 10, "bold"), bg = "white", fg = "black", command=lambda c=c: self.guess(c), width=5).grid(row=5+n//9, column=n%9, sticky = 'WE', padx=2, pady=2)
            n+=1
        Button(self, text="Guess", font=("Georgia", 10, "bold"), bg = "skyblue4", fg = "white", command=lambda: self.guess_phrase(), width=10).grid(row=5, column=9,sticky="NSWE")
        Button(self, text="End Game", font=("Georgia", 10, "bold"), bg = "skyblue4", fg = "white", command=lambda: game_over_screen(), width=10).grid(row=7, column=9, sticky="NSWE")
        Button(self, text="New", font=("Georgia", 10, "bold"), bg = "skyblue4", fg = "white", command=lambda: self.start_new_game(), width=10).grid(row=6, column=9,sticky="NSWE")

    def guess(self,letter):
        global game_data
        global user_data
        if(self.hangman.tries > 0):
            return_value = self.hangman.guess_letter(letter.upper())
            if(return_value == 1):
                messagebox.showwarning("Hangman", "Invalid Guess")
            self.lblWord.set(self.hangman.string_completed())
            self.imgLabel.config(image=self.photos[self.hangman.tries])
            print(self.hangman.tries)
            if(return_value == 0):
                user = get_user_data(user_data.user_name)
                scores = json.loads(user[1])
                p = scores[game_data.game_mode]
                p += 1
                update__user_data_score(user_data.user_name, game_data.game_mode, p)
            if(self.hangman.guessed):
                messagebox.showinfo("Hangman", "You win!")
                self.lblWord.set(self.hangman.sentence)
                game_over_screen()
            if(self.hangman.tries == 0):
                messagebox.showwarning("Hangman", "Game Over")
                self.lblWord.set(self.hangman.sentence)
                game_over_screen()
                user = get_user_data(user_data.user_name)
                scores = json.loads(user[1])
                p = scores[game_data.game_mode]
                if p!=0:
                    add_high_score(game_data.game_mode, user_data.user_name, p)
                    if check_top_scores(game_data.game_mode, user_data.user_name, p):   
                        messagebox.showwarning("Hangman", "New High Score!")
                update__user_data_score(user_data.user_name, game_data.game_mode, 0)

    def guess_phrase(self):
        self.controller.show_frame("Phrase_Screen")
        self.controller.get_screen_object("Phrase_Screen").set_hangman(self.hangman)
        self.controller.get_screen_object("Phrase_Screen").set_img(self.imgLabel)
        self.controller.get_screen_object("Phrase_Screen").set_up_screen()
         
    def back_to_user(self):
        self.controller.get_screen_object("UserScreen").get_user_info()
        self.controller.show_frame("UserScreen")

    def start_new_game(self):
        global game_data
        global user_data
        user = get_user_data(user_data.user_name)
        scores = json.loads(user[1])
        p = scores[game_data.game_mode]
        if p!=0:
            add_high_score(game_data.game_mode, user_data.user_name, p)
            if check_top_scores(game_data.game_mode, user_data.user_name, p):   
                messagebox.showwarning("Hangman", "New High Score!")
        update__user_data_score(user_data.user_name, game_data.game_mode, 0)
        messagebox.showwarning("Hangman", "New High Score!")
        screens.screen_data["Game_Screen"].new_game()

    def end_game(self):
        update__user_data_score(user_data.user_name, game_data.game_mode, 0)
        self.back_to_user()

class Phrase_Screen(tk.Frame):
    def __init__(self, parent, controller):
        self.hangman = None
        self.imgLabel = None
        self.photos = [PhotoImage(file="hangman_images/hang11.png"),PhotoImage(file="hangman_images/hang10.png")
        ,PhotoImage(file="hangman_images/hang9.png"),PhotoImage(file="hangman_images/hang8.png")
        ,PhotoImage(file="hangman_images/hang7.png"),PhotoImage(file="hangman_images/hang6.png")
        ,PhotoImage(file="hangman_images/hang5.png"),PhotoImage(file="hangman_images/hang4.png")
        ,PhotoImage(file="hangman_images/hang3.png"),PhotoImage(file="hangman_images/hang2.png")
        ,PhotoImage(file="hangman_images/hang1.png"),PhotoImage(file="hangman_images/hang0.png")]
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg="lightcyan3")        
        self.lblWord=StringVar()
        self.gue=StringVar()
        tk.Label(self, textvariable=self.lblWord, font=("Georgia", 14, "bold"), bg = "lightcyan3", fg = "black").pack(pady = 50)
        self.guessing_bar = tk.Entry(self, textvariable=self.gue)
        self.guessing_bar.pack(pady = 10)
        tk.Button(self, text='Guess', command=lambda:self.guess(), font=("Georgia", 10, "bold"), bg = "skyblue4", fg = "white", width = 10, height=1).pack(pady=5)
        tk.Button(self, text="Back", command=lambda: self.controller.show_frame("Game_Screen"), font=("Georgia", 10, "bold"), bg = "skyblue4", fg = "white", width = 10).pack(pady=5)

    def set_hangman(self, hangman: Hangman):
        self.hangman = hangman
    def set_img(self, img):
        self.imgLabel = img
    def set_up_screen(self):
        self.lblWord.set(self.hangman.string_completed())
    def guess(self):
        if(self.hangman.guess_phrase(self.gue.get().upper()) is False and self.hangman.tries != 0):
            self.hangman.tries -= 1
            messagebox.showwarning("Hangman", "Not the Answer")
            self.guessing_bar.select_clear()
        else:
            self.imgLabel.config(image=self.photos[self.hangman.tries])
            if(self.hangman.guessed):
                user = get_user_data(user_data.user_name)
                scores = json.loads(user[1])
                p = scores[game_data.game_mode]
                p += 10
                update__user_data_score(user_data.user_name, game_data.game_mode, p)
                messagebox.showinfo("Hangman", "You win!")
                self.controller.get_screen_object("Game_Screen").lblWord.set(self.hangman.sentence)
                self.controller.show_frame("Game_Screen")
                self.guessing_bar.select_clear()
                game_over_screen()
                
            if(self.hangman.tries == 0):
                messagebox.showwarning("Hangman", "Game Over")
                self.controller.get_screen_object("Game_Screen").lblWord.set(self.hangman.sentence)
                self.controller.show_frame("Game_Screen")
                self.guessing_bar.select_clear()
                game_over_screen()

def game_over_screen():
    global user_data
    global game_data
    top= Toplevel(screens.screen_data["Game_Screen"])
    top.geometry("700x250")
    top.title("Game Over")
    all_data = get_user_data(user_data.user_name)
    scores = json.loads(all_data[1])
    p = scores[game_data.game_mode]
    Label(top, text="Game Over", font=("Georgia", 20, "bold"), fg = "skyblue4",).pack(pady=5)
    Label(top, text=f"Points Earned: {p}", font=("Georgia", 14, "bold"), fg = "black", pady=20).pack(pady=5)
    Button(top, text="New Game", command=lambda: [screens.screen_data["Game_Screen"].new_game(), top.destroy()], font=("Georgia", 10, "bold"), bg = "skyblue4", fg = "white").pack(pady=5)
    Button(top, text="Back to Main Menu", command=lambda: [screens.screen_data["Game_Screen"].end_game(), top.destroy()], font=("Georgia", 10, "bold"), bg = "skyblue4", fg = "white").pack(pady=5)
