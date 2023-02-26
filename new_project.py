import customtkinter as ctk
import hashlib
import mysql.connector as mc
import tkinter
from tkinter import *
from PIL import ImageTk, Image

# ctk.set_appearance_mode('light')

class quiz:
    def __init__(self):
        # window1 widgets
        #insert image
        self.img1 = ctk.CTkImage(Image.open("background_image.png"), size=(1100,600))
        self.label = ctk.CTkLabel(root, image=self.img1)

        #create frame for login
        self.frame = ctk.CTkFrame(root, width=320, height=400, fg_color='white') # fg_color='transparent')

        #login form
        self.loginLabel = ctk.CTkLabel(self.frame, text="Login",text_color='#4D9AD4', font=('rockwell',30,'bold')) #, fg_color=("white", "gray75"))
        self.usernameEntry = ctk.CTkEntry(self.frame, width=250, placeholder_text=u'\U0001F464'+'   Username',border_width=2, border_color='#55ABEB',
                                          corner_radius=60, placeholder_text_color='#55ABEB')
        self.forgotUsername = ctk.CTkButton(self.frame, text='Forgot username?', font=('rockwell', 14), fg_color='transparent',
                                            text_color='#55ABEB', hover_color='#C7E2FF', command=self.forgotusername)
        self.passwordEntry = ctk.CTkEntry(self.frame, show='*', width=250, placeholder_text=u'\U0001F512' + '   Password',
                                          border_color='#55ABEB',placeholder_text_color='#55ABEB', corner_radius=60)
        self.forgotPass = ctk.CTkButton(self.frame, text='Forgot password?', font=('rockwell', 14), fg_color='transparent',
                                        text_color='#55ABEB', hover_color='#C7E2FF', command=self.forgotpassword)
        self.loginButton = ctk.CTkButton(self.frame, text='Login', font=('rockwell', 20, 'bold'), fg_color='#55ABEB',text_color='white',
                                         width=250, corner_radius=0, command=self.login) #, hover_color='White')

        self.noAccount = ctk.CTkLabel(self.frame, text="Don't have an account?", text_color='black', font=('rockwell',14))
        self.signupButton = ctk.CTkButton(self.frame, text='Sign Up', font=('rockwell', 15, 'bold'),fg_color='transparent',text_color='#55ABEB',
                                          width=70, hover_color='#C7E2FF', corner_radius=0, command=self.Signup)

    def window1(self):
        # self.label.pack()
        self.label.place(relx=0.0, rely=0.0)
        # self.label.pack()
        self.frame.place(relx=0.3,rely=0.5,anchor='center')
        self.loginLabel.place(relx=0.5,rely=0.1,anchor='center')
        self.usernameEntry.place(relx=0.5, rely=0.3, anchor='center')
        self.forgotUsername.place(relx=0.51,rely=0.38,anchor='e')
        self.passwordEntry.place(relx=0.5, rely=0.5,anchor='center')
        self.forgotPass.place(relx=0.51, rely=0.58,anchor='e')
        self.loginButton.place(relx=0.5, rely=0.7,anchor='center')
        self.noAccount.place(relx=0.6, rely=0.9, anchor='e')
        self.signupButton.place(relx=0.6,rely=0.9, anchor='w')

    def forgotusername(self):
        print("Forgot Username Clicked")

    def forgotpassword(self):
        print("Forgot Password Clicked")

    def login(self):
        print("Login Clicked")
    def Signup(self):
        print("Sign Up Clicked")

if __name__ == "__main__":
    dbPass = 'Ridd_hish'
    try:
        mycon = mc.connect(host='localhost', user='root', password=dbPass, database='quiz')
        user = mycon.cursor()
        # print(mycon)
    except:
        print("Error connecting to the database...!\nPlease try again after sometime.")
        print("We are sorry for the inconvenience")
        exit()

    root = ctk.CTk()
    root.title('Login')
    root.geometry('1100x600')
    ob = quiz()
    ob.window1()
    root.mainloop()
