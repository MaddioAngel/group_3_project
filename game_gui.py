import tkinter as tk                # python 3
from tkinter import font as tkfont  # python 3
import json
import os
from tkinter import *
from tkinter import messagebox
from string import ascii_uppercase
import random
import word_generation

word_list = ["Python"]

class Game_Screen(tk.Frame):
    def __init__(self, parent, controller):
        global word_list
        global number_of_guesses
        number_of_guesses = 0

        self.photos = [PhotoImage(file="hangman_images/hang0.png"),PhotoImage(file="hangman_images/hang1.png")
         ,PhotoImage(file="hangman_images/hang2.png"),PhotoImage(file="hangman_images/hang3.png")
         ,PhotoImage(file="hangman_images/hang4.png"),PhotoImage(file="hangman_images/hang5.png")
         ,PhotoImage(file="hangman_images/hang6.png"),PhotoImage(file="hangman_images/hang7.png")
         ,PhotoImage(file="hangman_images/hang8.png"),PhotoImage(file="hangman_images/hang9.png")
         ,PhotoImage(file="hangman_images/hang10.png"),PhotoImage(file="hangman_images/hang11.png")]
        tk.Frame.__init__(self, parent)
        self.controller = controller
        tk.Button(self, text="Go to the start page",command=lambda: controller.show_frame("UserScreen")).grid()
        self.imgLabel = Label(self)
        self.imgLabel.grid(row=0,column=0,columnspan=3, padx=10, pady=40)
        self.imgLabel.config(image=self.photos[0])
        self.lblWord=StringVar()
        Label(self, textvariable=self.lblWord).grid(row=0,column=3,columnspan=6, padx=10)
        
        n=0
        for c in ascii_uppercase:
            Button(self, text=c, command=lambda c=c: self.guess(c), width=4).grid(row=1+n//9, column=n%9)
            n+=1
        Button(self, text="New\nGame", command=lambda: self.new_game()).grid(row=3, column=8,sticky="NSWE")
        self.new_game()

    def new_game(self):
        global word_with_spaces
        global number_of_guesses
        global word
        number_of_guesses = 0
        self.imgLabel.config(image=self.photos[0])
        self.imgLabel.place_slaves()
        word = random.choice(word_list).upper()
        word_with_spaces = " ".join(word)
        self.lblWord.set(" ".join("_" * len(word)))


    def guess(self,letter):
        global number_of_guesses
        global word_with_spaces
        print(word_with_spaces)

        letter = letter.upper()
        if number_of_guesses < 11:
            txt = list(word_with_spaces)
            guessed = list(self.lblWord.get())
            if word_with_spaces.count(letter) > 0:
                for i in range(len(txt)):
                    if txt[i] == letter:
                        guessed[i] = letter
                    self.lblWord.set("".join(guessed))
                    if self.lblWord.get() == word_with_spaces:
                        messagebox.showinfo("Hangman", "You win!")

                        self.new_game()
            else:
                number_of_guesses += 1
                self.imgLabel.config(image=self.photos[number_of_guesses])
                if number_of_guesses == 11:
                    messagebox.showwarning("Hangman", "Game Over")
                    self.lblWord.set(word_with_spaces.replace(" ",""))
        else:
            pass
