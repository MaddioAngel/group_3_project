import tkinter as tk                # python 3
from tkinter import font as tkfont  # python 3
import json
import os
from user_screen_giu import *
from database import *
import user_data

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the start page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Login",
                            command=lambda: controller.show_frame("Login"))
        button2 = tk.Button(self, text="Register",
                            command=lambda: controller.show_frame("Register"))
        button1.pack()
        button2.pack()


class Login(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()
        tk.Label(self,text="Please enter details below to login").pack()
        tk.Label(self,text="").pack()
    
        global username_verify
        global password_verify
    
        username_verify = tk.StringVar()
        password_verify = tk.StringVar()
    
        global username_login_entry
        global password_login_entry
    
        tk.Label(self,text="Username * ").pack()
        username_login_entry = tk.Entry(self,textvariable=username_verify)
        username_login_entry.pack()
        tk.Label(self,text="").pack()
        tk.Label(self,text="Password * ").pack()
        password_login_entry = tk.Entry(self,textvariable=password_verify, show= '*')
        password_login_entry.pack()
        tk.Label(self,text="").pack()
        tk.Button(self,text="Login", width=10, height=1, command = self.login_verify).pack()
        self.text = tk.StringVar()
        self.text.set("")
        self.good_label = tk.Label(self,textvariable=self.text).pack()
  
    # Implementing event on login button 
    def login_verify(self):
        global user_data
        username1 = username_verify.get()
        password1 = password_verify.get()
        username_login_entry.delete(0, tk.END)
        password_login_entry.delete(0, tk.END)

        if username1 == "" or password1 == "":
            tk.Label(self, text="Please enter username and password").pack()
            return

        if not check_if_user_exists(username1):
            if check_user_password(username1, password1):
                self.controller.show_frame("UserScreen")
                UserScreen_object = self.controller.get_screen_object("UserScreen")
                user_data.user_name = username1
                UserScreen_object.get_user_info()
                return 
            else:
                self.password_not_recognised()
                return
        self.user_not_found()


        # with open('user_data.json', 'r') as read_file:
        #     user_data_json = json.load(read_file)
        # users_list = user_data_json["users"]
        # for user in users_list:
        #     name = list(user.keys())[0]
        #     if username1 == name:
        #         if password1 == user[name]["password"]:
        #             self.controller.show_frame("UserScreen")
        #             UserScreen_object = self.controller.get_screen_object("UserScreen")
        #             user_data.user_dict = dict(user)
        #             UserScreen_object.get_user_info()
        #             return 
        #         else:
        #             self.password_not_recognised()
        #             return
        # self.user_not_found()
        
    # Designing popup for login invalid password
    def password_not_recognised(self):
        global password_not_recog_screen
        password_not_recog_screen = tk.Toplevel(self.controller)
        password_not_recog_screen.title("Success")
        password_not_recog_screen.geometry("150x100")
        tk.Label(password_not_recog_screen, text="Invalid Password ").pack()
        tk.Button(password_not_recog_screen, text="OK", command=self.delete_password_not_recognised).pack()
    # Designing popup for user not found
    def user_not_found(self):
        global user_not_found_screen
        user_not_found_screen = tk.Toplevel(self.controller)
        user_not_found_screen.title("Success")
        user_not_found_screen.geometry("150x100")
        tk.Label(user_not_found_screen, text="User Not Found").pack()
        tk.Button(user_not_found_screen, text="OK", command=self.delete_user_not_found_screen).pack()
    
    def delete_password_not_recognised(self):
        password_not_recog_screen.destroy()
    
    def delete_user_not_found_screen(self):
        user_not_found_screen.destroy()
    
class Register(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

        global username
        global password
        global username_entry
        global password_entry
        username = tk.StringVar()
        password = tk.StringVar()
        
        tk.Label(self,text="Please enter details below", bg="blue").pack()
        tk.Label(self,text="").pack()
        username_lable = tk.Label(self,text="Username * ")
        username_lable.pack()
        username_entry = tk.Entry(self,textvariable=username)
        username_entry.pack()

        password_lable = tk.Label(self,text="Password * ")
        password_lable.pack()
        password_entry = tk.Entry(self,textvariable=password, show='*')
        password_entry.pack()
        self.text = tk.StringVar()
        self.text.set("")
        tk.Button(self,text="Register", width=10, height=1, bg="blue", command = self.register_user).pack()
        self.good_label = tk.Label(self,textvariable=self.text).pack()

    def register_user(self):
        username_info = username.get()
        password_info = password.get()

        if username_info == "" or password_info == "":
            self.text.set("Unable to Register")
            # self.good_label = tk.Label(self,text="Unable to Register", fg="red", font=("calibri", 13)).pack()
        else:
            if check_if_user_exists(username_info):
                add_user_data(username_info, password_info)
                #reset for next register
                username_entry.delete(0, tk.END)
                password_entry.delete(0, tk.END)
                self.text.set("Registration Success")
                # self.good_label = tk.Label(self,text="Registration Success", fg="green", font=("calibri", 13)).pack()
            else:
                self.text.set("Username already exists")
                # self.good_label = tk.Label(self,text="Username already exists", fg="red", font=("calibri", 13)).pack()
