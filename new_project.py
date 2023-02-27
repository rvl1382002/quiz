import customtkinter as ctk
import hashlib
import mysql.connector as mc
import tkinter
from tkinter import *
from PIL import ImageTk, Image

ctk.set_appearance_mode('light')

class quiz:
    def __init__(self):
        # window1 widgets : Login / Home
        self.frame1 = ctk.CTkFrame(root, width=5000, height=80, fg_color='#C7E2FF')

        #insert image
        self.img1 = ctk.CTkImage(Image.open("bgimage.png"), size=(500,500))
        self.imglabel1 = ctk.CTkLabel(root, text='', image=self.img1)

        self.img2 = ctk.CTkImage(Image.open("quiz_logo.png"), size=(150,150))
        self.imglabel2 = ctk.CTkLabel(self.frame1, text='', image=self.img2)

        #theme button
        self.theme_value=ctk.StringVar(value="light")
        self.theme = ctk.CTkSwitch(root, text="Dark Theme", command = self.switch_theme, variable= self.theme_value,onvalue="dark",offvalue="light")
        self.theme.place(relx=0.8,rely=0.05)

        #create frame for login
        self.loginFrame = ctk.CTkFrame(root, width=320, height=400, fg_color='transparent')

        #login form
        self.homeButton = ctk.CTkButton(self.frame1, text="Home", text_color='#4D9AD4', font=('rockwell',15), fg_color='transparent',
                                       hover_color='#C7E2FF', width=70, corner_radius=0, command=self.Home)
        self.aboutUsButton = ctk.CTkButton(self.frame1, text="About Us", text_color='#4D9AD4', font=('rockwell', 15),fg_color='transparent',
                                            hover_color='#C7E2FF', width=80, corner_radius=0, command=self.aboutUs)
        self.contactUsButton = ctk.CTkButton(self.frame1, text="Contact Us", text_color='#4D9AD4', font=('rockwell', 15),fg_color='transparent',
                                             hover_color='#C7E2FF', width=80, corner_radius=0, command=self.contactUs)
        self.loginLabel = ctk.CTkLabel(self.loginFrame, text="Login",text_color='#4D9AD4', font=('rockwell',30,'bold')) #, fg_color=("white", "gray75"))
        self.usernameEntry = ctk.CTkEntry(self.loginFrame, width=250, placeholder_text=u'\U0001F464'+'   Username',border_width=2, border_color='#55ABEB',
                                         corner_radius=60, placeholder_text_color='#55ABEB')
        self.forgotUsername = ctk.CTkButton(self.loginFrame, text='Forgot username?', font=('rockwell', 14), fg_color='transparent',
                                            text_color='#55ABEB', hover_color='#C7E2FF', command=self.forgotusername)
        self.passwordEntry = ctk.CTkEntry(self.loginFrame, show='*', width=250, placeholder_text=u'\U0001F512' + '   Password',
                                          border_color='#55ABEB',placeholder_text_color='#55ABEB', corner_radius=60)
        self.forgotPass = ctk.CTkButton(self.loginFrame, text='Forgot password?', font=('rockwell', 14), fg_color='transparent',
                                        text_color='#55ABEB', hover_color='#C7E2FF', command=self.forgotpassword)
        self.loginButton1 = ctk.CTkButton(self.loginFrame, text='Login', font=('rockwell', 20, 'bold'), fg_color='#55ABEB',text_color='white',
                                         width=250, corner_radius=0, command=self.checkLogin) #, hover_color='White')
        self.noAccount = ctk.CTkLabel(self.loginFrame, text="Don't have an account?", text_color =('black','white'), font=('rockwell',14), )
        self.signupButton = ctk.CTkButton(self.loginFrame, text='Sign Up', font=('rockwell', 15, 'bold'),fg_color='transparent',text_color='#55ABEB',
                                          width=70, hover_color='#C7E2FF', corner_radius=0, command=self.Signup)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------
        #window 2 widgets : Sign Up

        #insert image : use same widgets for logo and background image
        #create frame for signup
        self.signUpFrame = ctk.CTkFrame(root, width=320, height=480, fg_color='transparent')
        # Sign Up form
        # self.homeButton = ctk.CTkButton(root, text="Home", text_color='#4D9AD4', font=('rockwell', 15), fg_color='transparent',
        #                           hover_color='#C7E2FF', width=70, corner_radius=0, command=self.Home)
        # self.aboutUsButton = ctk.CTkButton(root, text="About Us", text_color='#4D9AD4', font=('rockwell', 15), fg_color='transparent',
        #                              hover_color='#C7E2FF', width=80, corner_radius=0, command=self.aboutUs)
        # self.contactUsButton = ctk.CTkButton(root, text="Contact Us", text_color='#4D9AD4', font=('rockwell', 15), fg_color='transparent',
        #                               hover_color='#C7E2FF', width=80, corner_radius=0, command=self.contactUs)
        self.signupLabel = ctk.CTkLabel(self.signUpFrame, text="Sign Up",text_color='#4D9AD4', font=('rockwell',30,'bold'))
        self.nameEntry = ctk.CTkEntry(self.signUpFrame, width=250, placeholder_text=u'\U0001F464' + '   Enter your name here',border_width=2, border_color='#55ABEB',
                                          corner_radius=60, placeholder_text_color='#55ABEB')
        self.emailEntry = ctk.CTkEntry(self.signUpFrame, width=250, placeholder_text='@   Enter valid email id', border_width=2, border_color='#55ABEB',
                                       corner_radius=60, placeholder_text_color='#55ABEB')
        self.signupUsernameEntry = ctk.CTkEntry(self.signUpFrame, width=250, placeholder_text=u'\U0001F464' + '   Username',border_width=2, border_color='#55ABEB',
                                          corner_radius=60, placeholder_text_color='#55ABEB')
        self.signupPassEntry = ctk.CTkEntry(self.signUpFrame, show='*', width=250, placeholder_text=u'\U0001F512' + '   Password',
                                          border_color='#55ABEB', placeholder_text_color='#55ABEB', corner_radius=60)
        self.reenterpassEntry = ctk.CTkEntry(self.signUpFrame, show='*', width=250,placeholder_text=u'\U0001F512' + '   Re-Enter Password',
                                          border_color='#55ABEB', placeholder_text_color='#55ABEB', corner_radius=60)
        self.submitsignup = ctk.CTkButton(self.signUpFrame, text="Submit", text_color='white', font=('rockwell',20,'bold'), fg_color='#55ABEB',
                                        width=250, corner_radius=0, command=self.SubmitSignUp)
        self.haveAccount = ctk.CTkLabel(self.signUpFrame, text="Already have an account?", text_color=('black','white'), font=('rockwell', 14))
        self.loginButton2 = ctk.CTkButton(self.signUpFrame, text='Login', font=('rockwell', 15, 'bold'),fg_color='transparent',text_color='#55ABEB',
                                          width=70, hover_color='#C7E2FF', corner_radius=0, command=self.login)

#---------------------------------------------------------------------------------------------------------------------------------------------
        #window 3 widgets : dashboard

        # self.dashboardHomeButton = ctk.CTkButton(root, text="Home", text_color='#4D9AD4', font=('rockwell', 15), fg_color='transparent',
        #                                  hover_color='#C7E2FF', width=70, corner_radius=0, command=self.Home)
        self.leaderboardButton = ctk.CTkButton(root, text="Leaderboard", text_color='#4D9AD4', font=('rockwell', 15), fg_color='transparent',
                                            hover_color='#C7E2FF', width=100, corner_radius=0, command=self.LeaderBoard)
        self.helpbutton = ctk.CTkButton(root, text="Help", text_color='#4D9AD4', font=('rockwell', 15), fg_color='transparent',
                                        hover_color='#C7E2FF', width=50, corner_radius=0, command=self.Help)
        self.dashboardFrame2 = ctk.CTkFrame(root, width=900, height=480, fg_color='white')
        self.dashboardName = ctk.CTkLabel(self.dashboardFrame2, text='Name: ', font=('rockwell', 15))
        self.dashboardUsername = ctk.CTkLabel(self.dashboardFrame2, text='Username: ', font=('rockwell', 15))
        self.dashboardEmail = ctk.CTkLabel(self.dashboardFrame2, text='Email: ', font=('rockwell', 15))


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def switch_theme(self):
        print("Theme change",self.theme_value.get())
        ctk.set_appearance_mode(self.theme_value.get())

    def window1(self):
        self.frame1.place(relx=0.1, rely=0.05, anchor='center')
        self.imglabel2.place(relx=0.49999,rely=0.5,anchor='center')
        self.homeButton.place(relx=0.53, rely=0.5,anchor='center')
        self.aboutUsButton.place(relx=0.56, rely=0.5,anchor='center')
        self.contactUsButton.place(relx=0.59,rely=0.5,anchor='center')
        # self.label.pack()
        self.imglabel1.place(relx=0.5, rely=0.13)
        self.loginFrame.place(relx=0.3,rely=0.5,anchor='center')
        self.loginLabel.place(relx=0.5,rely=0.1,anchor='center')
        self.usernameEntry.place(relx=0.5, rely=0.3, anchor='center')
        self.forgotUsername.place(relx=0.51,rely=0.38,anchor='e')
        self.passwordEntry.place(relx=0.5, rely=0.5,anchor='center')
        self.forgotPass.place(relx=0.51, rely=0.58,anchor='e')
        self.loginButton1.place(relx=0.5, rely=0.7,anchor='center')
        self.noAccount.place(relx=0.6, rely=0.9, anchor='e')
        self.signupButton.place(relx=0.6,rely=0.9, anchor='w')

    def Home(self):
        self.clearWindow2()
        self.window1()
        print("Home Botton Clicked")

    def aboutUs(self):
        self.clearWindow1()
        print("About Us Button Clicked")

    def contactUs(self):
        self.clearWindow1()
        print("Contact Us Button Clicked")

    def forgotusername(self):
        self.clearWindow1()
        print("Forgot Username Clicked")

    def forgotpassword(self):
        self.clearWindow1()
        print("Forgot Password Clicked")

    def checkLogin(self):
        self.clearWindow1()
        self.window3()
        print("Login Clicked")

    def Signup(self):
        self.clearWindow1()
        self.window2()
        print("Sign Up Clicked")

    def clearWindow1(self):
        # self.usernameEntry.delete(0, END)
        # self.passwordEntry.delete(0, END)
        self.frame1.place_forget()
        self.imglabel2.place_forget()
        # self.homeButton.place_forget()
        # self.aboutUsButton.place_forget()
        # self.contactUsButton.place_forget()
        self.imglabel1.place_forget()
        self.loginFrame.place_forget()
        # self.loginLabel.place_forget()
        # self.usernameEntry.place_forget()
        # self.forgotUsername.place_forget()
        # self.passwordEntry.place_forget()
        # self.forgotPass.place_forget()
        # self.loginButton1.place_forget()
        # self.noAccount.place_forget()
        # self.signupButton.place_forget()

#----------------------------------------------------------------------------------------------------------------------------

    def window2(self):
        self.frame1.place(relx=0.1, rely=0.05, anchor='center')
        self.imglabel2.place(relx=0.49999, rely=0.5, anchor='center')
        self.homeButton.place(relx=0.53, rely=0.5, anchor='center')
        self.aboutUsButton.place(relx=0.56, rely=0.5, anchor='center')
        self.contactUsButton.place(relx=0.59, rely=0.5, anchor='center')
        self.imglabel1.place(relx=0.5, rely=0.15)
        self.signUpFrame.place(relx=0.3, rely=0.52, anchor='center')
        self.signupLabel.place(relx=0.5,rely=0.13,anchor='center')
        self.nameEntry.place(relx=0.5,rely=0.3,anchor='center')
        self.emailEntry.place(relx=0.5,rely=0.4,anchor='center')
        self.signupUsernameEntry.place(relx=0.5,rely=0.5,anchor='center')
        self.signupPassEntry.place(relx=0.5,rely=0.6,anchor='center')
        self.reenterpassEntry.place(relx=0.5,rely=0.7,anchor='center')
        self.submitsignup.place(relx=0.5,rely=0.82,anchor='center')
        self.haveAccount.place(relx=0.68,rely=0.93,anchor='e')
        self.loginButton2.place(relx=0.9,rely=0.93,anchor='e')

    def SubmitSignUp(self):
        self.clearWindow2()
        self.window3()
        print("Submit Buttom Clicked")

    def login(self):
        self.clearWindow2()
        self.window1()
        print("Login Clicked")

    def clearWindow2(self):
        # self.imglabel2.place_forget()
        # self.homeButton.place_forget()
        # self.aboutUsButton.place_forget()
        # self.contactUsButton.place_forget()
        self.frame1.place_forget()
        self.imglabel1.place_forget()
        self.signUpFrame.place_forget()
#---------------------------------------------------------------------------------------------------------------------------------------

    def window3(self):
        # self.frame1.place(relx=0.1, rely=0.05, anchor='center')
        # self.imglabel2.place(relx=0.49999, rely=0.5, anchor='center')
        # self.homeButton.place(relx=0.53, rely=0.5, anchor='center')
        # self.leaderboardButton.place(relx=0.4, rely=0.06, anchor='center')
        # self.helpbutton.place(relx=0.6, rely=0.06,anchor='center')
        self.dashboardFrame2.place(relx=0.5, rely=0.53, anchor='center')
        self.dashboardName.place(relx=0.1,rely=0.1,anchor='e')
        self.dashboardUsername.place(relx=0.1, rely=0.2, anchor='e')
        self.dashboardEmail.place(relx=0.1, rely=0.3, anchor='e')

    def LeaderBoard(self):
        print("Leaderboard Button Clicked")

    def Help(self):
        print("Help Button Clicked")


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
