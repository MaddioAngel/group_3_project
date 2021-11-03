from screen_helper import screen_helper
from database import *

if __name__ == "__main__":
    create_user_table()
    app = screen_helper() 
    app.resizable(False, False)
    app.mainloop()

