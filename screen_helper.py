import tkinter as tk
from tkinter import font as tkfont
from sign_in_gui import StartPage, Login, Register
from user_screen_giu import UserScreen
from game_gui import Game_Screen, Phrase_Screen
from high_score_gui import Hign_Score_Screen
import screens

class screen_helper(tk.Tk):
    '''
    keeps track of all the screens it can access them all
    '''
    def __init__(self, *args, **kwargs):
        global screens
        tk.Tk.__init__(self, *args, **kwargs)
        
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (StartPage, Login, Register, UserScreen, Game_Screen, Phrase_Screen, Hign_Score_Screen):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        screens.screen_data = self.frames
        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''
        switchs the screen to the one specified
        '''
        frame = self.frames[page_name]
        frame.tkraise()

    def get_screen_object(self, frame_name):
        '''
        returns the screen object
        '''
        frame = self.frames[frame_name]
        return frame

