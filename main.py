from screen_helper import screen_helper
from database import *

if __name__ == "__main__":
    create_user_table()
    create_word_table()
    create_shop_table()
    create_high_score_table()
    app = screen_helper() 
    app.resizable(False, False)
    app.mainloop()
