from tkinter import *


'''
the logic of the hangman game
function:
updated_completed_part - updates the completed part of the the word (addes the '_' to the shown word)

'''
class Hangman:
    '''
    guessed - keeps track of whether the user has guessed the word
    sentence - the actural word/phrase
    compled_part - keeps track of the completed part of the word
    tries - keeps track of the number of tries the user has left
    letters_guessed
    '''
    def __init__(self, sentence):
        self.guessed = False
        self.compled_part = list()
        self.sentence = sentence.upper()
        self.tries = 11
        self.letters_guessed = list()
        self.guessed_words = list()
    
    def updated_completed_part(self, letter): 
        '''
        splits the completed_part of the word into a list
        splits the actual word into a list
        
        makes sure that the letter in completed_part is the same as the letter in the actual word

        check where the letter is in the actual word
        then adds it to the completed_part
        '''
        completed_part = list(self.compled_part)
        sentence = list(self.sentence)
        length = len(sentence)
        special_char = ".\"!@#$%^&*()-+?=,<>/;:[]{\}|\'"
        if len(completed_part) == 0:
            completed_part = [None] * length
            for i in range(length):
                if " " in sentence[i]:
                    completed_part[i] = " "
                elif self.sentence[i] in special_char:
                    completed_part[i] = self.sentence[i]
                else:
                    completed_part[i] = "_"
        for i in range(length):
            if letter in sentence[i]:
                    completed_part[i] = letter
        self.compled_part = "".join(completed_part)

    def guess_letter(self, guess):
        '''
        checks to see if letter is in the word
        if it is, it adds it to the letters_guessed list
        if it is not, it subtracts a try
        if already guessed, return 1 to let game screen know

        '''
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
        '''
        checks to see if phrase is the word
        if it is, it adds it to the letters_guessed list
        if it is not, it subtracts a try
        if already guessed, return 1 to let game screen know
        '''
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
        '''
        updated the completed part of the word
        and returns it as a string so the game screen can display it
        '''
        string = ''
        special_char = "\"!@#$%^&*()-+?=,<>/;:[]{\}|\'"
        done = False
        new_line = 0
        for i in range(len(self.sentence)):
            if self.sentence[i] == " ":
                string += "  "
                new_line += 1
                if new_line == 5:
                    string += "\n"
                    new_line = 0
            elif self.sentence[i] in ".":
                string += " .\n"
                new_line = 0
            elif self.sentence[i] in self.letters_guessed:
                string += self.sentence[i] + " "
            elif self.sentence[i] in special_char:
                string += self.sentence[i] + " "
            else:
                string += "_ "
        return string
            