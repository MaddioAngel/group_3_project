import tkinter as tk                # python 3
from tkinter import font as tkfont  # python 3
import json
import os

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
  
    # Implementing event on login button 
    
    def login_verify(self):
        username1 = username_verify.get()
        password1 = password_verify.get()
        username_login_entry.delete(0, tk.END)
        password_login_entry.delete(0, tk.END)
    
        with open('user_data.json', 'r') as read_file:
            user_data_json = json.load(read_file)
        users_list = user_data_json["users"]
        for user in users_list:
            if username1 in user.keys():
                if password1 in user.values():
                    self.controller.show_frame("UserScreen")
                    return
                else:
                    self.password_not_recognised()
                    return
        self.user_not_found()
    
    # Designing popup for login success
    
    def login_sucess(self):
        global login_success_screen
        login_success_screen = tk.Toplevel(self.controller)
        login_success_screen.title("Success")
        login_success_screen.geometry("150x100")
        tk.Label(login_success_screen, text="Login Success").pack()
        tk.Button(login_success_screen, text="OK", command=self.delete_login_success).pack()
    
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
    
    # Deleting popups
    
    def delete_login_success(self):
        login_success_screen.destroy()
    
    
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
        tk.Label(self,text="").pack()
        tk.Button(self,text="Register", width=10, height=1, bg="blue", command = self.register_user).pack()

    def register_user(self):
    
        username_info = username.get()
        password_info = password.get()
        user_dict = {username_info:password_info}
        dict_ = {"users":[user_dict]}
        if not os.path.exists('user_data.json'):
            file_ = open('user_data.json', 'w')
            file_.write(json.dumps(dict_))
            file_.close()
        else:
            with open('user_data.json','r+') as file:
                    # First we load existing data into a dict.
                    file_data = json.load(file)
                    # Join new_data with file_data inside emp_details
                    file_data["users"].append(user_dict)
                    # Sets file's current position at offset.
                    file.seek(0)
                    # convert back to json.
                    json.dump(file_data, file, indent = 4)
        #reset for next register
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
    
        tk.Label(self,text="Registration Success", fg="green", font=("calibri", 13)).pack()
