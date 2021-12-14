import sqlite3
from os.path import exists
import os
import json

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
        SCORE          TEXT    NOT NULL,    
        UNLOCKED       TEXT    NOT NULL) ;''')
        con.commit()
        con.close()
    except sqlite3.OperationalError:
        print("User Table already exists")

def create_word_table():
    try:
        con = connect_to_database()
        con.cursor()
        con.execute('''CREATE TABLE EASY_WORDS
        (ID INTEGER PRIMARY KEY,
        WORD           TEXT    NOT NULL,
        SCORE          INT      ) ;''')
        con.execute('''CREATE TABLE HARD_WORDS
        (ID INTEGER PRIMARY KEY,
        WORD           TEXT    NOT NULL,
        SCORE          INT      ) ;''')
        con.execute('''CREATE TABLE WORD_OF_THE_DAY
        (ID INTEGER PRIMARY KEY,
        WORD           TEXT    NOT NULL,
        SCORE          INT      ) ;''')
        con.execute('''CREATE TABLE MOVIE_QUOTES
        (ID INTEGER PRIMARY KEY,
        WORD           TEXT    NOT NULL,
        SCORE          INT      ) ;''')
        con.execute('''CREATE TABLE ANIMALS
        (ID INTEGER PRIMARY KEY,
        WORD           TEXT    NOT NULL,
        SCORE          INT      ) ;''')
        con.execute('''CREATE TABLE COUNTRIES
        (ID INTEGER PRIMARY KEY,
        WORD           TEXT    NOT NULL,
        SCORE          INT      ) ;''')
        con.commit()
        con.close()
        adding_words_from_files()
        print("Word Table create for the first time and words added")
    except sqlite3.OperationalError:
        print("Word Table already exists")

def create_high_score_table():
    try:
        con = connect_to_database()
        con.cursor()
        con.execute('''CREATE TABLE HIGH_SCORE
        (ID INTEGER PRIMARY KEY,
        GAME_MODE      TEXT    NOT NULL,
        NAME           TEXT    NOT NULL,
        SCORE          INT      ) ;''')
        con.commit()
        con.close()
    except sqlite3.OperationalError:
        print("High Score Table already exists")

def add_user_data(user,password):
    user = user.lower()
    con = connect_to_database()
    con.cursor()
    score_dict = {"EASY_WORDS":0,"HARD_WORDS":0,"MOVIE_QUOTES":0,"ANIMALS":0,"COUNTRIES":0}
    json_score = json.dumps(score_dict)
    sql_user_data = (user,password,json_score, "EASY_WORDS HARD_WORDS MOVIE_QUOTES ANIMALS COUNTRIES")
    sql = 'INSERT INTO USERS(NAME,PASSWORD,SCORE,UNLOCKED)VALUES(?,?,?,?)'
    con.execute(sql, sql_user_data)
    con.commit()
    con.close()

def add_word_data(database,word,score):
    con = connect_to_database()
    con.cursor()
    sql_user_data = (word,score)
    sql = f'INSERT INTO {database}(WORD,SCORE)VALUES(?,?)'
    con.execute(sql, sql_user_data)
    con.commit()
    con.close()

def adding_words_from_files():
    directory = './words'
    for filename in os.listdir(directory):
        file_ = open(directory+"/"+filename, "r")
        lines = file_.readlines()
        # Strips the newline character
        for word in lines:
            score = len(word)
            add_word_data(filename, word.strip(), score)

def add_high_score(game_mode,user,score):
    con = connect_to_database()
    if not check_if_highscore_exists(game_mode, score):
        con.cursor()
        sql_user_data = (game_mode,user,score)
        sql = f'INSERT INTO HIGH_SCORE(GAME_MODE,NAME,SCORE)VALUES(?,?,?)'
        con.execute(sql, sql_user_data)
        con.commit()
        con.close()
        return True
    else:
        return False

def print_user_data():
    print("items in the user database")
    con = connect_to_database()
    for row in con.execute('SELECT * FROM USERS'):
        print(row)

def print_word_data(database):
    print(f"items in the {database} database")
    con = connect_to_database()
    for row in con.execute(f'SELECT * FROM {database}'):
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

def check_if_highscore_exists(game_mode,score):
    con = connect_to_database()
    check_items = (game_mode,score)
    data = con.execute("SELECT * FROM HIGH_SCORE WHERE GAME_MODE = ? AND SCORE = ?", check_items)
    try:
        is_in_highscore = data.fetchone()
    except:
        is_in_highscore = None
    con.close()
    if not is_in_highscore == None:
        return True
    else:
        return False

def check_top_scores(game_mode, user, points):
    top_10 = get_high_score_data(game_mode)
    for i in top_10:
        if  i[1] == points:
            if i[0] == user:
                return True
            else:
                return False
    return False

def get_user_data(user):
    con = connect_to_database()
    name = (user.lower(),)
    data = con.execute("SELECT NAME,SCORE,UNLOCKED FROM USERS WHERE NAME = ?",name)
    user_data = data.fetchone()
    name, score, unlocked = user_data
    con.close()
    return name, score, unlocked

def get_random_word_data(database):
    con = connect_to_database()
    data = con.execute(f"SELECT WORD,SCORE FROM {database} ORDER BY RANDOM() LIMIT 1;")
    word_data = data.fetchone()
    word, score = word_data
    con.close()
    return word, score

def get_high_score_data(game_mode):
    con = connect_to_database()
    data = con.execute(f"SELECT NAME,SCORE FROM HIGH_SCORE WHERE GAME_MODE = '{game_mode}' ORDER BY SCORE DESC LIMIT 10;")
    high_score_data = data.fetchall()
    con.close()
    return high_score_data

def update__user_data_score(user, game_mode, score):
    user = user.lower()
    con = connect_to_database()
    data = get_user_data(user)
    scores = json.loads(data[1])
    scores[game_mode] = score
    scores = json.dumps(scores)
    con.execute("UPDATE USERS SET SCORE=? WHERE NAME=?", (scores, user,))
    con.commit()
    con.close()

def delete_user_data(user):
    con = connect_to_database()
    name = (user.lower(),)
    con.execute("DELETE FROM USERS WHERE NAME = ?",name)
    con.commit()
    con.close()

def clear_high_score_data(game_mode):
    con = connect_to_database()
    con.execute(f"DELETE FROM HIGH_SCORE WHERE GAME_MODE = '{game_mode}'")
    con.commit()
    con.close()
