import tkinter as tk                # python 3
from tkinter import font as tkfont  # python 3
import json
import os
from tkinter import *
from tkinter import messagebox
from string import ascii_uppercase
from game_logic import Hangman
import random
import word_generation

word_list = ["Python"]

class Game_Screen(tk.Frame):
    def __init__(self, parent, controller):
        global word_list
        self.hangman = None
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.imgLabel = Label(self)
        self.lblWord=StringVar()
        self.photos = [PhotoImage(file="hangman_images/hang11.png"),PhotoImage(file="hangman_images/hang10.png")
         ,PhotoImage(file="hangman_images/hang9.png"),PhotoImage(file="hangman_images/hang8.png")
         ,PhotoImage(file="hangman_images/hang7.png"),PhotoImage(file="hangman_images/hang6.png")
         ,PhotoImage(file="hangman_images/hang5.png"),PhotoImage(file="hangman_images/hang4.png")
         ,PhotoImage(file="hangman_images/hang3.png"),PhotoImage(file="hangman_images/hang2.png")
         ,PhotoImage(file="hangman_images/hang1.png"),PhotoImage(file="hangman_images/hang0.png")]
        self.new_game()

    def new_game(self):
        global word_list
        self.hangman = Hangman(random.choice(word_list).upper())
        self.imgLabel.config(image=self.photos[self.hangman.tries])
        self.imgLabel.place_slaves()
        self.lblWord.set(self.hangman.string_completed())


        tk.Button(self, text="Back", command=lambda: self.controller.show_frame("UserScreen")).grid(row = 0, column = 0)
        self.imgLabel.grid(row=1,column=0,columnspan=3, padx=10, pady=40)
        Label(self, textvariable=self.lblWord).grid(row=1,column=3,columnspan=6, padx=10)
        n=0
        for c in ascii_uppercase:
            Button(self, text=c, command=lambda c=c: self.guess(c), width=5).grid(row=2+n//9, column=n%9, sticky = 'WE')
            n+=1
        Button(self, text="Phrase", command=lambda: self.controller.show_frame("Phrase_Screen")).grid(row=3, column=8,sticky="NSWE")
        Button(self, text="New", command=lambda: self.new_game()).grid(row=4, column=8,sticky="NSWE")


    def guess(self,letter):
        if(self.hangman.tries > 0):
            self.hangman.guess_letter(letter.upper())
            self.lblWord.set(self.hangman.string_completed())
            self.imgLabel.config(image=self.photos[self.hangman.tries])
            print(self.hangman.tries)
            if(self.hangman.guessed):
                messagebox.showinfo("Hangman", "You win!")
                self.new_game()
            if(self.hangman.tries == 0):
                messagebox.showwarning("Hangman", "Game Over")
                self.lblWord.set(self.hangman.sentence)

class Phrase_Screen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

