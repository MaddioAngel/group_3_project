import tkinter as tk
from database import *
import user_data
import game_data
import screens

'''
user screen giu shows different gamemodes the uaer can choose from and the high score button
'''
class UserScreen(tk.Frame):
    '''
    this is the main function that runs the user screen
    has the high score button and log out 
    '''
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.name = ""
        self.points = 0
        self.controller = controller
        self.config(bg="lightcyan3")                                   
        self.text1 = tk.StringVar()
        self.text2 = tk.StringVar()
        self.text1.set("")
        self.text2.set("")
        tk.Button(self, text="Log Out", font=("Georgia", 10, "bold"), bg = "skyblue4", fg = "white", width=10,         
                        command=lambda: self.return_to_sign_in()).place(x=440, y=300)
        self.label1 = tk.Label(self, textvariable=self.text1, font=("arial black",10), bg = "lightcyan3", fg ="black").pack()       
        self.label3 = tk.Label(self, textvariable=self.text2, font=("arial black",10), bg = "lightcyan3", fg ="black").pack()
        self.label4 = tk.Label(self, bg = "lightcyan3", pady=10).pack()  
        self.games = tk.Frame(self, bg = "lightcyan3", pady=10)
        self.games.pack()
        tk.Button(self, text="High Scores",  font=("Georgia", 10, "bold"), bg = "skyblue4", fg = "white", width=10, command=lambda: self.got_to_high_score()).place(x=305, y=300)

    def get_user_info(self):
        '''
        updates the user info when the user logs in
        '''
        global user_data
        self.name, self.points, self.unlocked = get_user_data(user_data.user_name)
        unlocked_list = self.unlocked.split(" ")
        self.buttons = []
        for game_mode in unlocked_list:
            self.buttons.append(tk.Button(self.games,text=game_mode, width=18, height=1, font=("Elephant", 10), bg = "white", fg = "black", command=lambda mode=game_mode: self.change_to_game_screen(mode)))
        for button in self.buttons:
            button.pack()
        data_user = f"User: {self.name}"
        data_points = f"Points: {self.points}"
        self.text1.set(data_user) 
        self.text2.set(data_points)

    def change_to_game_screen(self, mode):
        '''
        moves to the game screen
        '''
        global game_data
        global screens
        game_data.game_mode = mode
        screens.screen_data["Game_Screen"].new_game()
        self.controller.show_frame("Game_Screen")
        self.clear()

    def return_to_sign_in(self):
        '''
        return to the start page
        '''
        self.controller.show_frame("StartPage")
        self.clear()

    def got_to_high_score(self):
        '''
        '''
        global screens
        screens.screen_data["Hign_Score_Screen"].update_data()
        self.controller.show_frame("Hign_Score_Screen")
        self.clear()

    def clear(self):
        '''
        clears the user data so if a other user logs in it will update
        '''
        for button in self.buttons:
            button.destroy()
        self.buttons = []
