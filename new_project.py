import customtkinter as ctk
import hashlib
import mysql.connector as mc
import tkinter
from tkinter import *
from PIL import ImageTk, Image

# ctk.set_appearance_mode('light')

class quiz:
    def __init__(self):
        # window1 widgets : Login / Home
        #insert image
        self.img1 = ctk.CTkImage(Image.open("bgimage.png"), size=(500,500))
        self.imglabel1 = ctk.CTkLabel(root, image=self.img1)

        self.img2 = ctk.CTkImage(Image.open("quiz_logo.png"), size=(150,150))
        self.imglabel2 = ctk.CTkLabel(root, image=self.img2)

        #create frame for login
        self.frame = ctk.CTkFrame(root, width=320, height=400, fg_color='transparent') #fg_color='white'

        #login form
        self.Home = ctk.CTkButton(root, text="Home", text_color='#4D9AD4', font=('rockwell',15), fg_color='transparent',
                                  hover_color='#C7E2FF', width=70, corner_radius=0, command=self.home)
        self.AboutUs = ctk.CTkButton(root, text="About Us", text_color='#4D9AD4', font=('rockwell', 15),fg_color='transparent',
                                    hover_color='#C7E2FF', width=80, corner_radius=0, command=self.about_us)
        self.ContactUs = ctk.CTkButton(root, text="Contact Us", text_color='#4D9AD4', font=('rockwell', 15),fg_color='transparent',
                                        hover_color='#C7E2FF', width=80, corner_radius=0, command=self.contact_us)
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

#---------------------------------------------------------------------------------------------------------------------------------------------------------------
        #window 2 widgets : Sign Up
        #insert image : use same widgets for logo and background image
        #create frame for signup
        # self.SignUpFrame = ctk.CTkFrame(root, width=320, height=400, fg_color='transparent')
        #use same frame for signup also
        # Sign Up form
        self.Home = ctk.CTkButton(root, text="Home", text_color='#4D9AD4', font=('rockwell', 15), fg_color='transparent',
                                  hover_color='#C7E2FF', width=70, corner_radius=0, command=self.home)
        self.AboutUs = ctk.CTkButton(root, text="About Us", text_color='#4D9AD4', font=('rockwell', 15), fg_color='transparent',
                                     hover_color='#C7E2FF', width=80, corner_radius=0, command=self.about_us)
        self.ContactUs = ctk.CTkButton(root, text="Contact Us", text_color='#4D9AD4', font=('rockwell', 15), fg_color='transparent',
                                       hover_color='#C7E2FF', width=80, corner_radius=0, command=self.contact_us)
        self.signupLabel = ctk.CTkLabel(self.frame, text="Sign Up",text_color='#4D9AD4', font=('rockwell',30,'bold'))



    def window1(self):
        self.imglabel2.place(relx=0.1,rely=0.06,anchor='center')
        self.Home.place(relx=0.2, rely=0.06,anchor='center')
        self.AboutUs.place(relx=0.3, rely=0.06,anchor='center')
        self.ContactUs.place(relx=0.4,rely=0.06,anchor='center')
        # self.label.pack()
        self.imglabel1.place(relx=0.5, rely=0.1)
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

    def home(self):
        print("Home Botton Clicked")

    def about_us(self):
        self.clear_window1()
        print("About Us Button Clicked")

    def contact_us(self):
        self.clear_window1()
        print("Contact Us Button Clicked")

    def forgotusername(self):
        self.clear_window1()
        print("Forgot Username Clicked")

    def forgotpassword(self):
        self.clear_window1()
        print("Forgot Password Clicked")

    def login(self):
        self.clear_window1()
        print("Login Clicked")

    def Signup(self):
        self.clear_window1()
        self.window2()
        print("Sign Up Clicked")

    def clear_window1(self):
        # self.usernameEntry.delete(0, END)
        # self.passwordEntry.delete(0, END)
        self.imglabel2.place_forget()
        self.Home.place_forget()
        self.AboutUs.place_forget()
        self.ContactUs.place_forget()
        self.imglabel1.place_forget()
        self.frame.place_forget()
        self.loginLabel.place_forget()
        self.usernameEntry.place_forget()
        self.forgotUsername.place_forget()
        self.passwordEntry.place_forget()
        self.forgotPass.place_forget()
        self.loginButton.place_forget()
        self.noAccount.place_forget()
        self.signupButton.place_forget()

#----------------------------------------------------------------------------------------------------------------------------

    def window2(self):
        self.imglabel2.place(relx=0.1, rely=0.06, anchor='center')
        self.Home.place(relx=0.2, rely=0.06, anchor='center')
        self.AboutUs.place(relx=0.3, rely=0.06, anchor='center')
        self.ContactUs.place(relx=0.4, rely=0.06, anchor='center')
        self.imglabel1.place(relx=0.5, rely=0.1)
        self.frame.place(relx=0.3, rely=0.5, anchor='center')
        self.signupLabel.place(relx=0.5,rely=0.1,anchor='center')

if __name__ == "__main__":
    dbPass = 'mokshada'
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
