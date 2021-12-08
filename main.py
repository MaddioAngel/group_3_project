from screen_helper import screen_helper
from database import *
# import ctypes
# ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

if __name__ == "__main__":
    create_user_table()
    create_word_table()
    create_high_score_table()
    app = screen_helper() 
    app.minsize(600, 400)
    app.resizable(False, False)
    app.title("Hangman")
    app.mainloop()
 