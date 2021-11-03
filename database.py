import sqlite3
from os.path import exists

def connect_to_database():
    file_exists = exists("database.db")
    if not file_exists:
        open("database.db", "w")
    return sqlite3.connect("database.db")

def create_user_table():
    try:
        con = connect_to_database()
        con.cursor()
        con.execute('''CREATE TABLE USERS
        (ID INTEGER PRIMARY KEY,
        NAME           TEXT    NOT NULL,
        PASSWORD       TEXT    NOT NULL,
        MONEY          REAL    NOT NULL,
        SCORE          INT      ) ;''')
        con.commit()
        con.close()
    except sqlite3.OperationalError:
        print("Table already exists")

def create_shop_table():
    try:
        con = connect_to_database()
        con.cursor()
        con.execute('''CREATE TABLE SHOP
        (NAME           TEXT    NOT NULL,
        PRICE          REAL    NOT NULL,
        TYPE           TEXT    NOT NULL) ;''')
        con.commit()
        con.close()
    except sqlite3.OperationalError:
        print("Table already exists")

def add_user_data(user,password):
    user = user.lower()
    con = connect_to_database()
    con.cursor()

    if check_if_user_exists(user):
        sql_user_data = (user,password,15,0)
        sql = 'INSERT INTO USERS(NAME,PASSWORD,MONEY,SCORE)VALUES(?,?,?,?)'
        con.execute(sql, sql_user_data)
        con.commit()
    con.close()

def add_to_store():
    con = connect_to_database()
    con.cursor()
    con.close()

def print_user_data():
    print("items in the user database")
    con = connect_to_database()
    for row in con.execute('SELECT * FROM USERS'):
        print(row)

def check_if_user_exists(user):
    con = connect_to_database()
    name = (user.lower(),)
    data = con.execute("SELECT NAME FROM USERS WHERE NAME = ?",name)
    try:
        is_in_user = data.fetchone()[0]
    except:
        is_in_user = None
    con.close()

    if not is_in_user == None:
        return False
    else:
        return True

def check_user_password(user,entered_password):
    con = connect_to_database()
    name = (user.lower(),)
    data = con.execute("SELECT PASSWORD FROM USERS WHERE NAME = ?",name)
    try: 
        password = data.fetchone()[0]
    except:
        password = None
    con.close()
    if not password == None:
        if entered_password == password:
            return True
        else:
            return False

def get_user_data(user):
    con = connect_to_database()
    name = (user.lower(),)
    data = con.execute("SELECT NAME,MONEY,SCORE FROM USERS WHERE NAME = ?",name)
    # try:
    user_data = data.fetchone()
    name, money, score = user_data
    con.close()
    return name, money, score

def update_user_data(user,money,score):
    con = connect_to_database()
    name = user.lower()
    con.execute("UPDATE USERS SET MONEY = ?, SCORE = ? WHERE NAME = ?",(money,score,name))
    con.commit()
    con.close()

def delete_user_data(user):
    con = connect_to_database()
    name = (user.lower(),)
    con.execute("DELETE FROM USERS WHERE NAME = ?",name)
    con.commit()
    con.close()


print_user_data()