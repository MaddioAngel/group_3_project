import tkinter as tk                # python 3
from tkinter import font as tkfont  # python 3

from sign_in_gui import StartPage, Login, Register
from user_screen_giu import UserScreen
from game_gui import Game_Screen, Phrase_Screen
from shop_gui import ShopScreen


class screen_helper(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, Login, Register, UserScreen, Game_Screen, ShopScreen, Phrase_Screen):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

    def get_screen_object(self, frame_name):
        frame = self.frames[frame_name]
        return frame

