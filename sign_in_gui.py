import tkinter as tk
from user_screen_giu import *
from database import *
import user_data


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg="lightcyan3")
        label = tk.Label(self, text="Hangman", font=('Jokerman',50), fg = "skyblue4", bg = "lightcyan3")
        label.pack(side="top", fill="x", pady=60)
        button1 = tk.Button(self, text="Login", font=("Georgia", 10, "bold"), bg = "skyblue4", fg = "white", padx=26,
                            command=lambda: controller.show_frame("Login"))
        button2 = tk.Button(self, text="Register",  font=("Georgia", 10, "bold"), bg = "skyblue4", fg = "white", padx=18,
                            command=lambda: controller.show_frame("Register"))
        button3 = tk.Button(self, text="High Scores",  font=("Georgia", 10, "bold"), bg = "skyblue4", fg = "white", padx=7,
                            command=lambda: controller.show_frame("Hign_Score_Screen"))
        button1.pack(side="top", pady=5)
        button2.pack(side="top", pady=5)
        button3.pack(side="top", pady=5)

class Login(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg="lightcyan3")
        tk.Button(self, text="Main Menu", font=("Georgia", 10, "bold"), bg = "skyblue4", fg = "white", width=10,
                           command=lambda: controller.show_frame("StartPage")).place(x=440, y=300)
        tk.Label(self,text="Enter details below to login", font=("arial black",12), bg = "lightcyan3", fg ="black", pady=20).pack()
        global username_verify
        global password_verify
        username_verify = tk.StringVar()
        password_verify = tk.StringVar()
        global username_login_entry
        global password_login_entry
        tk.Label(self,text="Username * ", font=("Georgia",10, "bold"), bg = "lightcyan3", fg ="skyblue4").pack(side="top", pady=2)
        username_login_entry = tk.Entry(self,textvariable=username_verify)
        username_login_entry.pack(side="top", pady=2)
        tk.Label(self,text=" ", font=("Georgia",10), bg = "lightcyan3", fg="skyblue4").pack(side="top", pady=2)
        tk.Label(self,text="Password * ", font=("Georgia",10, "bold"), bg = "lightcyan3", fg="skyblue4").pack(side="top", pady=2)
        password_login_entry = tk.Entry(self,textvariable=password_verify, show= '*')
        password_login_entry.pack(side="top", pady=2)
        tk.Button(self,text="Login", font=("Georgia", 10, "bold"), bg = "skyblue4", fg = "white", width=10, height=1, command = self.login_verify).place(x=305, y=300)
        self.text = tk.StringVar()

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

    def password_not_recognised(self):
        global password_not_recog_screen
        password_not_recog_screen = tk.Toplevel(self.controller)
        password_not_recog_screen.title("Success")
        password_not_recog_screen.geometry("150x100")
        tk.Label(password_not_recog_screen, text="Invalid Password ").pack()
        tk.Button(password_not_recog_screen, text="OK", command=self.delete_password_not_recognised).pack()

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
        self.config(bg="lightcyan3")
        button = tk.Button(self, text="Main Menu", font=("Georgia", 10), bg = "skyblue4", fg = "white", padx=24,
                           command=lambda: controller.show_frame("StartPage"))
        button.pack(side="top", pady = 10)
        global username
        global password
        global username_entry
        global password_entry
        username = tk.StringVar()
        password = tk.StringVar()
        tk.Label(self,text="Create a Username and Password", font=("arial black",10), bg = "lightcyan3", fg ="skyblue4", pady=20).pack()
        username_lable = tk.Label(self,text="Enter a Username * ", font=("arial black",10), bg = "lightcyan3", fg ="skyblue4").pack(side="top", pady=2)
        username_entry = tk.Entry(self,textvariable=username)
        username_entry.pack(side="top", pady=2)
        tk.Label(self,text=" ", font=("arial black",10), bg = "lightcyan3", fg="skyblue4").pack(side="top", pady=2)
        password_lable = tk.Label(self,text="Enter a Password * ", font=("arial black",10), bg = "lightcyan3", fg ="skyblue4").pack(side="top", pady=2)
        password_entry = tk.Entry(self,textvariable=password, show='*')
        password_entry.pack(side="top", pady=2)
        self.text = tk.StringVar()
        self.text.set("")
        tk.Button(self,text="Register", font=("Georgia", 10), bg = "skyblue4", fg = "white", command = self.register_user).pack(side="top", pady=10)
        self.confirmation = tk.Label(self,textvariable=self.text, font=("arial black",10), bg = "lightcyan3", fg ="skyblue4").pack()

    def register_user(self):
        username_info = username.get()
        password_info = password.get()

        if username_info == "" or password_info == "":
            self.text.set("Unable to Register")
        else:
            if check_if_user_exists(username_info):
                add_user_data(username_info, password_info)
                username_entry.delete(0, tk.END)
                password_entry.delete(0, tk.END)
                self.text.set("Registration Success")
            else:
                self.text.set("Username already exists")
