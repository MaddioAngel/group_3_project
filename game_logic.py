import json

class Hangman:
    def __init__(self, sentence):
        self.guessed = False
        self.compled_part = list()
        self.sentence = sentence.lower()
        self.tries = 6
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

    def game_state(self) -> str:
        return self.display_hangman(self.tries)  + "\n" + self.string_completed() + "\n"

    def guess(self):
        if(self.over() == False):
            type = input("input type of guess: ").lower()
            while(type != 'l' and type != 'p'):
                print("invalid input")
                type = input("input type of guess: ").lower()
            if(type == 'l'):
                guess = input("guess a letter: ").lower()
                while(self.guess_letter(guess) == False):
                    print("invalid input")
                    guess = input("guess a letter: ").lower()
                
            if(type == 'p'):
                guess = input("guess a phrase: ").lower()
                if(self.guess_phrase(guess) == False):
                    print("invalid input")
                    guess = input("guess a phrase: ").lower()

    def guess_letter(self, guess):
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
            if self.guessed:
                print(self.display_hangman(self.tries))
                print("Good Job, you guessed the word! \'" + self.sentence + "\'")  
            elif self.tries == 0:
                print(self.display_hangman(self.tries))
                print("I'm sorry, but you ran out of tries. The phrase was \'" + self.sentence + "\'. Maybe next time!")
            return True
        else:
            return False 
    
    def guess_phrase(self, guess):
        if len(guess) == len(self.sentence):
            if guess in self.guessed_words:
                print("You already tried ", guess, "!")
            elif guess != self.sentence:
                print(guess, " ist nicht das Wort :(")
                self.tries -= 1
                self.guessed_words.append(guess)
            else:
                self.guessed = True
                self.compled_part = self.sentence
            return True
        else:
            return False
             
    def end_game(self):
        if self.guessed:
                print(self.display_hangman(self.tries))
                print("Good Job, you guessed the phrase! \'" + self.sentence + "\'")  
        elif self.tries == 0:
            print(self.display_hangman(self.tries))
            print("I'm sorry, but you ran out of tries. The phrase was \'" + self.sentence + "\'. Maybe next time!")

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

    def display_hangman(self, tries) -> str:
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
    a = Hangman("Do you like jazz")
    while(a.over() == False):
        print(a.game_state())
        a.guess()
    a.end_game()