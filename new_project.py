import customtkinter as ctk
import hashlib
import mysql.connector as mc
import re
from tkinter import messagebox
from tkinter import *
from PIL import ImageTk, Image


ctk.set_appearance_mode('light')

def isUserName(u):
	for i in u:
		if not i.isalnum() and i!="_":
			return False
	return True

def isEmail(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.fullmatch(regex,email):
        return True
    else:
        return False

def usernameExists(u):#incomplete
    user.execute("SELECT USERNAME FROM USERS")
    existingUsernames=user.fetchall()
    if u in [j for i in existingUsernames for j in i]:
        return True
    else:
        return False

def emailExists(u):
    user.execute('SELECT EMAIL FROM USERS')
    existingEmail = user.fetchall()
    if u in [j for i in existingEmail for j in i]:
        return True
    else:
        return False


class quiz:
    def __init__(self):
        # window1 widgets : Login / Home
        #frame for home, aboutUs and contactUs button
        self.frame1 = ctk.CTkFrame(root, width=5000, height=80, fg_color='#C7E2FF')

        #insert image
        self.img1 = ctk.CTkImage(Image.open("bgimage.png"), size=(500,500))
        self.imglabel1 = ctk.CTkLabel(root, text='', image=self.img1)

        self.img2 = ctk.CTkImage(Image.open("quiz_logo.png"), size=(150,150))
        self.imglabel2 = ctk.CTkLabel(self.frame1, text='', image=self.img2)

        #theme button
        self.theme_value=ctk.StringVar(value="light")
        self.theme = ctk.CTkSwitch(self.frame1, text="Dark Theme",text_color='#3166A6', command = self.switch_theme, variable= self.theme_value,onvalue="dark",offvalue="light")
        self.theme.place(relx=0.63,rely=0.4)

        #create frame for login
        self.loginFrame = ctk.CTkFrame(root, width=320, height=400)

        #login form
        self.homeButton = ctk.CTkButton(self.frame1, text="Home", text_color='#3166A6', font=('rockwell',15,'bold'), fg_color='transparent',
                                       hover_color='#AED3FF', width=70, corner_radius=0, command=self.Home)
        self.aboutUsButton = ctk.CTkButton(self.frame1, text="About Us", text_color='#3166A6', font=('rockwell', 15,'bold'),fg_color='transparent',
                                            hover_color='#AED3FF', width=80, corner_radius=0, command=self.aboutUs)
        self.contactUsButton = ctk.CTkButton(self.frame1, text="Contact Us", text_color='#3166A6', font=('rockwell', 15, 'bold'),fg_color='transparent',
                                             hover_color='#AED3FF', width=80, corner_radius=0, command=self.contactUs)
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
        self.invalidLogin = ctk.CTkLabel(self.loginFrame, text='Invalid username or password!', font=('rockwell',15), text_color='red')

#---------------------------------------------------------------------------------------------------------------------------------------------------------------
        #window 2 widgets : Sign Up

        #insert image : use same widgets for logo and background image
        #create frame for signup
        self.signUpFrame = ctk.CTkFrame(root, width=320, height=480)
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
                                        width=250, corner_radius=0, command=self.register)
        self.invalidUsername = ctk.CTkLabel(self.signUpFrame, text='Invalid username!', font=('rockwell', 15),
                                         text_color='red')
        self.usernameExists = ctk.CTkLabel(self.signUpFrame, text='Username already Exists!', font=('rockwell', 15),
                                            text_color='red')
        self.invalidPassword = ctk.CTkLabel(self.signUpFrame, text='Invalid password!', font=('rockwell', 15),
                                            text_color='red')
        self.invalidEmail = ctk.CTkLabel(self.signUpFrame, text='Invalid Email id!', font=('rockwell', 15),
                                            text_color='red')
        self.emailExists = ctk.CTkLabel(self.signUpFrame, text='Email already Exists!', font=('rockwell', 15),
                                            text_color='red')
        self.fillDetails = ctk.CTkLabel(self.signUpFrame, text='Please enter all the details!', font=('rockwell', 15),
                                            text_color='red')

        self.haveAccount = ctk.CTkLabel(self.signUpFrame, text="Already have an account?", text_color=('black','white'), font=('rockwell', 14))
        self.loginButton2 = ctk.CTkButton(self.signUpFrame, text='Login', font=('rockwell', 15, 'bold'),fg_color='transparent',text_color='#55ABEB',
                                          width=70, hover_color='#C7E2FF', corner_radius=0, command=self.login)
#---------------------------------------------------------------------------------------------------------------------------------------------

        #window 3 widgets : dashboard
        # Using name, username, and email from signup window i.e. window2
        # self.dashboardHomeButton = ctk.CTkButton(root, text="Home", text_color='#4D9AD4', font=('rockwell', 15), fg_color='transparent',
        #                                  hover_color='#C7E2FF', width=70, corner_radius=0, command=self.Home)
        self.leaderboardButton = ctk.CTkButton(self.frame1, text="Leaderboard", text_color='#3166A6', font=('rockwell', 15,'bold'), fg_color='transparent',
                                            hover_color='#AED3FF', width=100, corner_radius=0, command=self.LeaderBoard)
        self.helpbutton = ctk.CTkButton(self.frame1, text="Help", text_color='#3166A6', font=('rockwell', 15,'bold'), fg_color='transparent',
                                        hover_color='#AED3FF', width=50, corner_radius=0, command=self.Help)
        self.dashboardFrame = ctk.CTkFrame(root, width=900, height=480)
        self.dashboardName = ctk.CTkLabel(self.dashboardFrame, text='Name: ',text_color=('#4489BD','#4FA0DB'), font=('rockwell', 15))
        self.dashboardUsername = ctk.CTkLabel(self.dashboardFrame, text='Username: ',text_color=('#4489BD','#4FA0DB'), font=('rockwell', 15))
        self.dashboardEmail = ctk.CTkLabel(self.dashboardFrame, text='Email: ', text_color=('#4489BD','#4FA0DB'), font=('rockwell', 15))
        self.changePass = ctk.CTkButton(self.dashboardFrame, text='Change Password', text_color="white", font=('rockwell',16,'bold'),fg_color='#55ABEB',
                                        width=180, corner_radius=0, command=self.changePassword)
        self.logoutButton = ctk.CTkButton(self.frame1, text='Logout', text_color="#3166A6", font=('rockwell',16,'bold'),fg_color='transparent',
                                        hover_color='#AED3FF',width=100, corner_radius=0, command=self.logout)
        self.giveQuizButton = ctk.CTkButton(self.dashboardFrame, text='Give Quiz', text_color='white', font=('rockwell',16,'bold'),fg_color='#55ABEB',
                                            width=100, corner_radius=0, command=self.giveQuiz)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------

        # Window 4 Widgets: About Us
        self.aboutBgimage = ctk.CTkImage(Image.open("aboutUs_bgimage.png"), size=(500, 500))
        self.aboutBgimageLabel = ctk.CTkLabel(root, text='', image=self.aboutBgimage)
        self.aboutUsFrame = ctk.CTkFrame(root, width=320, height=400, fg_color='transparent')
        self.aboutLable = ctk.CTkLabel(self.aboutUsFrame, text="About Us", text_color='#4D9AD4', font=('rockwell', 35, 'bold'))
        self.aboutLable2 = ctk.CTkLabel(self.aboutUsFrame, text="Developed and Designed by: \n\n Riddhish V. Lichade \n Mokshada E. Jawale "
                                                                "\n\n Computer Engineering Student \n Dr. Babasaheb Ambedkar \n Technological University, Lonere.",
                                        text_color='#3166A6', font=('rockwell', 17))


#-----------------------------------------------------------------------------------------------------------------------------------------------------------
        # Window 5 Widgets: Contact Us
        self.contactBgimage = ctk.CTkImage(Image.open("contactUs_bgimage.png"), size=(500, 500))
        self.contactBgimageLabel = ctk.CTkLabel(root, text='', image=self.contactBgimage)
        self.contactUsFrame = ctk.CTkFrame(root, width=320, height=400, fg_color='transparent')
        self.contactLabel = ctk.CTkLabel(self.contactUsFrame, text="Contact Us", text_color='#4D9AD4', font=('rockwell', 35, 'bold'))
        self.contactName = ctk.CTkEntry(self.contactUsFrame, width=250, placeholder_text=u'\U0001F464' + '   Name',border_width=2, border_color='#55ABEB',
                                        placeholder_text_color='#55ABEB')
        self.contactEmail = ctk.CTkEntry(self.contactUsFrame, width=250, placeholder_text='@   Email', border_width=2, border_color='#55ABEB',
                                        placeholder_text_color='#55ABEB')
        self.contactMsg = ctk.CTkEntry(self.contactUsFrame, width=250,height=100, placeholder_text=u'\U0001F4AC' + '   Message', border_width=2, border_color='#55ABEB',
                                       placeholder_text_color='#55ABEB')
        self.contactSubmitButton = ctk.CTkButton(self.contactUsFrame, text="Submit", text_color='white', font=('rockwell',20,'bold'), fg_color='#55ABEB',
                                                width=250, corner_radius=0, command=self.submitMsg)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        #window 6 Widgets: forgot username and password
        # create upper frame
        # self.upperRecoveryFrame = ctk.CTkFrame(root, width=5000, height=80, fg_color='#C7E2FF')
        self.recoverUsernameLabel = ctk.CTkLabel(self.frame1, text='Recover Username', font=('Calibri', 32, 'bold'), text_color='#254D7D')
        self.recoverPasswordLabel = ctk.CTkLabel(self.frame1, text='Recover Password', font=('Calibri', 32, 'bold'), text_color='#254D7D')

        #insert bgimage
        self.forgetCredsBgimage = ctk.CTkImage(Image.open("forgetCredsBgimage.png"), size=(500, 500))
        self.imglabel3 = ctk.CTkLabel(root, text='', image=self.forgetCredsBgimage)

        #create frame
        self.forgetCredsFrame = ctk.CTkFrame(root, width=470, height=380)

        self.provideDetailsLabel = ctk.CTkLabel(root, text="Provide Account Details", text_color=('black', 'white'), font=('Rockwell', 20))

        self.label = ctk.CTkLabel(self.forgetCredsFrame, text="Enter your registered email to recover your username.",
                                  text_color=('#356EB3','#4FA0DB'), font=('Rockwell', 18)) #Enter your email and we'll send you a link to reset your password.
        self.label = ctk.CTkLabel(self.forgetCredsFrame, text="Enter your registered email to reset your Password.",
                                  text_color=('#356EB3', '#4FA0DB'), font=('Rockwell', 18))
        self.forgetCredsEmailLabel = ctk.CTkLabel(self.forgetCredsFrame, text='Email: ', text_color=('#356EB3','#4FA0DB'), font=('Rockwell',20))
        self.forgetCredsEmailEntry = ctk.CTkEntry(self.forgetCredsFrame, width=270, height=30,  placeholder_text='@   Enter valid email id',
                                       border_width=2, border_color='#356EB3',corner_radius=60, placeholder_text_color='#55ABEB')
        self.getOtpButton = ctk.CTkButton(self.forgetCredsFrame, text="Get OTP", text_color='white', font=('rockwell',15), fg_color='#2A568C',
                                                width=150, corner_radius=0) #, command=self.getOtp
        self.validEmailMsg = ctk.CTkLabel(self.forgetCredsFrame, text='Enter valid email.', text_color='red', font=('Rockwell',15))
        self.otpSentMsg = ctk.CTkLabel(self.forgetCredsFrame, text='OTP has been sent to your registered email address.', text_color='red', font=('Rockwell',15))
        self.otpText = ctk.CTkLabel(self.forgetCredsFrame, text="Enter the OTP sent to your registered email id:", text_color=('#356EB3','#4FA0DB'), font=('Rockwell',20))
        self.otpEntry = ctk.CTkEntry(self.forgetCredsFrame, show='*',width=270, height=30,  placeholder_text='Enter otp', border_width=2, border_color='#356EB3',
                                     corner_radius=60, placeholder_text_color='#55ABEB')
        self.continueButton = ctk.CTkButton(self.forgetCredsFrame, text="Continue", text_color='white', font=('rockwell',15), fg_color='#2A568C',
                                                width=150, corner_radius=0)
        self.resendOtpButton = ctk.CTkButton(self.forgetCredsFrame, text="Resend OTP", text_color='white', font=('rockwell',15), fg_color='#2A568C',
                                                width=150, corner_radius=0)


        # self.verifyEmailText = ctk.CTkLabel(self.forgetUserPassFrame, text="Verify your email id")
        # self.enterUserMailText = ctk.CTkLabel(self.forgetUserPassFrame, text="Enter Username or E-mail id")
        # self.otpText = ctk.CTkLabel(self.forgetUserPassFrame, text="Enter the OTP sent to your registered email id")
        # self.otpEntry = ctk.CTkEntry(self.forgetUserPassFrame, width=6, font=("Rockwell", 15))
        # self.userMailEntry = ctk.CTkEntry(self.forgetUserPassFrame, width=40)
        # self.submitForgotCreds = ctk.CTkButton(self.forgetUserPassFrame, text="Get e-mail", height=1, width=12, font=("Rockwell", 15), bg="#07AD31", fg="white",
        #                                 activebackground="white") #, command=sendMail)
        # self.verifyOTPButton = ctk.CTkButton(self.forgetUserPassFrame, text="Verify OTP", height=1, width=12, font=("Rockwell", 15), bg="#07AD31", fg="white",
        #                               activebackground="white") #, command=verifyOTP)


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
        self.clearWindow3()
        self.clearWindow4()
        self.clearWindow5()
        self.window1()
        print("Home Botton Clicked")

    def aboutUs(self):
        self.clearWindow1()
        self.clearWindow2()
        self.clearWindow5()
        self.window4()
        print("About Us Button Clicked")

    def contactUs(self):
        self.clearWindow1()
        self.clearWindow2()
        self.clearWindow4()
        self.window5()
        print("Contact Us Button Clicked")

    def forgotusername(self):
        self.clearWindow1()
        self.window6()
        print("Forgot Username Clicked")

    def forgotpassword(self):
        self.clearWindow1()
        self.window6()
        print("Forgot Password Clicked")

    def checkLogin(self):
        self.enteredUsername = self.usernameEntry.get()
        enteredPass = self.passwordEntry.get()
        user.execute("SELECT PASSWORD FROM USERS WHERE USERNAME='{}'".format(self.enteredUsername))
        pasHash = user.fetchone()
        if pasHash != None and pasHash[0] == hashlib.sha256(enteredPass.encode()).hexdigest():
            print("Login successful")
            self.clearWindow1()
            self.window3()
        else:
            self.invalidLogin.place(relx=0.5, rely=0.18, anchor='center')

    def Signup(self):
        self.clearWindow1()
        self.window2()
        print("Sign Up Clicked")

    def clearWindow1(self):
        self.usernameEntry.delete(0, END)
        self.passwordEntry.delete(0, END)
        self.frame1.place_forget()
        # self.imglabel2.place_forget()
        self.homeButton.place_forget()
        self.aboutUsButton.place_forget()
        self.contactUsButton.place_forget()
        self.imglabel1.place_forget()
        self.loginFrame.place_forget()
        self.invalidLogin.place_forget()

#----------------------------------------------------------------------------------------------------------------------------

    def window2(self):
        self.frame1.place(relx=0.1, rely=0.05, anchor='center')
        self.imglabel2.place(relx=0.49999, rely=0.5, anchor='center')
        self.homeButton.place(relx=0.53, rely=0.5, anchor='center')
        self.aboutUsButton.place(relx=0.56, rely=0.5, anchor='center')
        self.contactUsButton.place(relx=0.59, rely=0.5, anchor='center')
        self.imglabel1.place(relx=0.5, rely=0.15)
        self.signUpFrame.place(relx=0.3, rely=0.55, anchor='center')
        self.signupLabel.place(relx=0.5,rely=0.13,anchor='center')
        self.nameEntry.place(relx=0.5,rely=0.3,anchor='center')
        self.emailEntry.place(relx=0.5,rely=0.4,anchor='center')
        self.signupUsernameEntry.place(relx=0.5,rely=0.5,anchor='center')
        self.signupPassEntry.place(relx=0.5,rely=0.6,anchor='center')
        self.reenterpassEntry.place(relx=0.5,rely=0.7,anchor='center')
        self.submitsignup.place(relx=0.5,rely=0.82,anchor='center')
        self.haveAccount.place(relx=0.68,rely=0.93,anchor='e')
        self.loginButton2.place(relx=0.9,rely=0.93,anchor='e')

    def register(self):

        self.invalidUsername.place_forget()
        self.invalidEmail.place_forget()
        self.emailExists.place_forget()
        self.usernameExists.place_forget()
        self.invalidPassword.place_forget()
        self.fillDetails.place_forget()

        enteredName = self.nameEntry.get()
        self.enteredUsername = self.signupUsernameEntry.get()
        enteredEmail = self.emailEntry.get()
        enteredPassword = self.signupPassEntry.get()
        enteredConfirmpassword = self.reenterpassEntry.get()
        print(len(enteredName))
        if len(enteredName)==0 or len(enteredEmail)==0 or len(self.enteredUsername)==0 or len(enteredPassword)==0:
            self.fillDetails.place(relx=0.5, rely=0.2, anchor='center')
        elif not (self.enteredUsername):
            self.invalidUsername.place(relx=0.5, rely=0.2, anchor='center')
        elif not isEmail(enteredEmail):
            self.invalidEmail.place(relx=0.5, rely=0.2, anchor='center')
        elif usernameExists(self.enteredUsername):
            self.usernameExists.place(relx=0.5, rely=0.2, anchor='center')
        elif emailExists(enteredEmail):
            self.emailExists.place(relx=0.5, rely=0.2, anchor='center')
        elif enteredPassword != enteredConfirmpassword:
            self.invalidPassword.place(relx=0.5, rely=0.2, anchor='center')
        else:
            self.clearWindow2()
            print("Button Clicked")
            # window3
            passHash = hashlib.sha256(enteredPassword.encode()).hexdigest()
            user.execute(
                "INSERT INTO USERS VALUES('{}','{}','{}','{}')".format(enteredName, enteredEmail, self.enteredUsername,
                                                                       passHash))
            mycon.commit()
            messagebox.showinfo("Congrats!", "Registered Successfully")
            # self.registeredMessage.place(relx=0.5, rely=0.4, anchor='center')
            # time.sleep(3)
            # self.registeredMessage.place_forget()
            self.window3()
            print("Submit Buttom Clicked")

    def login(self):
        self.clearWindow2()
        self.window1()
        print("Login Clicked")

    def clearWindow2(self):
        # self.imglabel2.place_forget()
        self.homeButton.place_forget()
        self.aboutUsButton.place_forget()
        self.contactUsButton.place_forget()
        self.frame1.place_forget()
        self.imglabel1.place_forget()
        self.signUpFrame.place_forget()
#---------------------------------------------------------------------------------------------------------------------------------------

    def window3(self):
        self.frame1.place(relx=0.1, rely=0.05, anchor='center')
        # self.imglabel2.place(relx=0.49999, rely=0.5, anchor='center')
        self.homeButton.place(relx=0.53, rely=0.5, anchor='center')
        self.leaderboardButton.place(relx=0.57, rely=0.5, anchor='center')
        self.helpbutton.place(relx=0.61, rely=0.5,anchor='center')
        self.logoutButton.place(relx=0.675, rely=0.5, anchor='center')
        self.dashboardFrame.place(relx=0.5, rely=0.53, anchor='center')
        self.dashboardName.place(relx=0.15,rely=0.1,anchor='e')
        self.dashboardUsername.place(relx=0.15, rely=0.2, anchor='e')
        self.dashboardEmail.place(relx=0.15, rely=0.3, anchor='e')

        username=self.enteredUsername
        user.execute("SELECT NAME,EMAIL FROM USERS WHERE USERNAME='{}'".format(self.enteredUsername))
        self.userData = user.fetchone()
        self.nameLabel = ctk.CTkLabel(self.dashboardFrame, text=self.userData[0], font=('rockwell', 15))
        self.usernameLabel = ctk.CTkLabel(self.dashboardFrame, text=self.enteredUsername, font=('rockwell', 15))
        self.emailLabel = ctk.CTkLabel(self.dashboardFrame, text=self.userData[1], font=('rockwell', 15))
        self.nameLabel.place(relx=0.18, rely=0.1, anchor='w')
        self.usernameLabel.place(relx=0.18, rely=0.2, anchor='w')
        self.emailLabel.place(relx=0.18, rely=0.3, anchor='w')

        admin.execute("SHOW TABLES")
        subjects = [j.capitalize() for i in admin.fetchall() for j in i]
        print(subjects)
        self.sub_list = StringVar()
        self.sub_list.set('Select any subject')
        self.display_sub = ctk.CTkOptionMenu(self.dashboardFrame,values=subjects, variable=self.sub_list, font=('rockwell',14))

        self.giveQuizButton.place(relx=0.9, rely=0.2, anchor='center')
        self.display_sub.place(relx=0.9, rely=0.1, anchor='center')

        self.changePass.place(relx=0.1, rely=0.9, anchor='center')

    def LeaderBoard(self):
        self.clearWindow3()
        print("Leaderboard Button Clicked")

    def Help(self):
        self.clearWindow3()
        print("Help Button Clicked")

    def changePassword(self):
        self.clearWindow3()
        print("Change Password Button Clicked")

    def logout(self):
        self.clearWindow3()
        self.clearWindow4()
        self.clearWindow5()
        self.window1()
        print('Logout Button Clicked')

    def giveQuiz(self):
        self.clearWindow3()
        print("Give quiz Button Clicked")

    def clearWindow3(self):
        self.frame1.place_forget()
        self.homeButton.place_forget()
        self.leaderboardButton.place_forget()
        self.helpbutton.place_forget()
        self.logoutButton.place_forget()
        self.dashboardFrame.place_forget()

#--------------------------------------------------------------------------------------------------------------------------------------------------
    def window4(self):
        self.frame1.place(relx=0.1,rely=0.05,anchor='center')
        self.homeButton.place(relx=0.53, rely=0.5, anchor='center')
        self.contactUsButton.place(relx=0.59,rely=0.5,anchor='center')
        self.logoutButton.place(relx=0.675, rely=0.5, anchor='center')
        self.aboutBgimageLabel.place(relx=0.5, rely=0.13)
        self.aboutUsFrame.place(relx=0.3, rely=0.55, anchor='center')
        self.aboutLable.place(relx=0.5,rely=0.1,anchor='center')
        self.aboutLable2.place(relx=0.12,rely=0.4,anchor='w')

    def clearWindow4(self):
        self.frame1.place_forget()
        self.homeButton.place_forget()
        self.aboutBgimageLabel.place_forget()
        self.aboutUsFrame.place_forget()

#-------------------------------------------------------------------------------------------------------------------------------------------------------
    def window5(self):
        self.frame1.place(relx=0.1, rely=0.05, anchor='center')
        self.homeButton.place(relx=0.53, rely=0.5, anchor='center')
        self.aboutUsButton.place(relx=0.56, rely=0.5, anchor='center')
        self.contactUsFrame.place(relx=0.7,rely=0.55,anchor='center')
        self.logoutButton.place(relx=0.675, rely=0.5, anchor='center')
        self.contactBgimageLabel.place(relx=0.27,rely=0.55,anchor='center')
        self.contactLabel.place(relx=0.5,rely=0.1,anchor='center')
        self.contactName.place(relx=0.5,rely=0.3,anchor='center')
        self.contactEmail.place(relx=0.5,rely=0.4,anchor='center')
        self.contactMsg.place(relx=0.5,rely=0.45,anchor='n')
        self.contactSubmitButton.place(relx=0.5,rely=0.8,anchor='center')

    def submitMsg(self):
        print('Submit button clicked')

    def clearWindow5(self):
        self.frame1.place_forget()
        self.homeButton.place_forget()
        self.contactUsFrame.place_forget()
        self.contactBgimageLabel.place_forget()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def window6(self):
        self.frame1.place(relx=0.1, rely=0.1, anchor='center')
        self.recoverUsernameLabel.place(relx=0.55, rely=0.5, anchor='center')
        self.theme.place(relx=0.66, rely=0.4)
        self.imglabel3.place(relx=0.53, rely=0.17)
        # self.upperRecoveryFrame.place(relx=0.1, rely=0.1, anchor='center')
        self.provideDetailsLabel.place(relx=0.19, rely=0.23, anchor='center')
        self.forgetCredsFrame.place(relx=0.3, rely=0.58, anchor='center')
        self.label.place(relx=0.02, rely=0.03)
        self.forgetCredsEmailLabel.place(relx=0.13, rely=0.2, anchor='center')
        self.forgetCredsEmailEntry.place(relx=0.03, rely=0.3, anchor='w')
        self.getOtpButton.place(relx=0.6, rely=0.41, anchor='center')
        self.otpText.place(relx=0.03, rely=0.65, anchor='w')
        self.otpEntry.place(relx=0.03, rely=0.75, anchor='w')
        self.continueButton.place(relx=0.05, rely=0.85, anchor='w')
        self.resendOtpButton.place(relx=0.45, rely=0.85, anchor='w')




if __name__ == "__main__":
    dbPass = 'mokshada'
    try:
        mycon = mc.connect(host='localhost', user='root', password=dbPass, database='quiz')
        mycon2 = mc.connect(host="localhost", user="root", password=dbPass, database="quiz_admin")
        user = mycon.cursor()
        admin = mycon2.cursor()
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

