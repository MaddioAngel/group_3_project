import json

class Hangman:
    def __init__(self, sentence):
        self.guessed = False
        self.compled_part = list()
        self.sentence = sentence.lower()
        self.tries = 6
        self.letters_guessed = list()
        self.guessed_words = list()

        self.start_game()
    
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
        print(completed_part)
        print(self.compled_part)
        print(sentence)

    def start_game(self):
        while(self.tries > 0 and not self.guessed):
            print(self.display_hangman(self.tries))
            self.print_completed()
            guess = input("guess a letter or word: ").lower()
            if len(guess) == 1 and guess.isalpha():
                if guess in self.letters_guessed:
                    print("you already tried", guess, "!")
                elif guess not in self.sentence:
                    print(guess, "isn't in the word :(")
                    self.tries -= 1
                    self.letters_guessed.append(guess)
                else:
                    print("Nice one,", guess, "is in the word!")
                    self.letters_guessed.append(guess)
                    self.updated_completed_part(guess)
                    if self.compled_part == self.sentence:
                        self.guessed = True   
                         
            elif len(guess) == len(self.sentence) and guess.isalpha():
                if guess in self.guessed_words:
                    print("You already tried ", guess, "!")
                elif guess != self.sentence:
                    print(guess, " ist nicht das Wort :(")
                    self.tries -= 1
                    self.guessed_words.append(guess)
                else:
                    self.guessed = True
                    self.compled_part = self.sentence  
            else:
                print("invalid input")
        print(self.display_hangman(self.tries))
        if self.guessed:
            print("Good Job, you guessed the word! \'" + self.sentence + "\'")  
        elif self.tries == 0:
            print("I'm sorry, but you ran out of tries. The phrase was \'" + self.sentence + "\'. Maybe next time!")

    def print_completed(self):
        done = False
        for i in range(len(self.sentence)):
            if self.sentence[i] == " ":
                print(" ", end=" ")
            elif self.sentence[i] in self.letters_guessed:
                print(self.sentence[i], end=" ")
            else:
                print("_", end=" ")
        print("")

    def display_hangman(self, tries):
        stages = [  """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      
                   |
                   |
                   |
                   -
                   """
        ]
        return stages[tries]
            
if __name__ == "__main__":
    Hangman("Do you like jazz")