import json
from tkinter import *

class Hangman:
    def __init__(self, sentence):
        self.guessed = False
        self.compled_part = list()
        self.sentence = sentence.upper()
        self.tries = 11
        self.letters_guessed = list()
        self.guessed_words = list()
    
    def updated_completed_part(self, letter): 
        completed_part = list(self.compled_part)
        sentence = list(self.sentence)
        length = len(sentence)
        if len(completed_part) == 0:
            completed_part = [None] * length
            for i in range(length):
                if " " in sentence[i]:
                    completed_part[i] = " "
                else:
                    completed_part[i] = "_"
        for i in range(length):
            if letter in sentence[i]:
                    completed_part[i] = letter
        self.compled_part = "".join(completed_part)

    def over(self) -> bool:
        return self.guessed or self.tries == 0

    def guess_letter(self, guess):
        if len(guess) == 1 and guess.isalpha():
            if guess in self.letters_guessed:
                print("you already tried", guess, "!")
                return 1
            elif guess not in self.sentence:
                print(guess, "isn't in the word :(")
                self.tries -= 1
                self.letters_guessed.append(guess)
                return 2
            else:
                print("Nice one,", guess, "is in the word!")
                self.letters_guessed.append(guess)
                self.updated_completed_part(guess)
                if self.compled_part == self.sentence:
                    self.guessed = True 
                return 0
        else:
            return 2 
    
    def guess_phrase(self, guess):
        if len(guess) == len(self.sentence):
            if guess in self.guessed_words:
                print("You already tried ", guess, "!")
                return False
            elif guess != self.sentence:
                print(guess, " is not the word :(")
                self.tries -= 1
                self.guessed_words.append(guess)
            else:
                self.guessed = True
                self.compled_part = self.sentence
            return True
        else:
            return False

    def string_completed(self) -> str:
        string = ''
        done = False
        for i in range(len(self.sentence)):
            if self.sentence[i] == " ":
                string += "  "
            elif self.sentence[i] in self.letters_guessed:
                string += self.sentence[i] + " "
            else:
                string += "_ "
        return string
            