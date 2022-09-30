import hashlib #for password
from tkinter import *
import tkinter.font as font
from tkinter import messagebox
import mysql.connector as mc
import re #for valid email
import time
import smtplib
import random

# window1=Home window
# window2=login window
# window3=signup window
# window4=leaderboard window
# window5=dashboard window
# window6=quiz window
# window7=admin login
# window8=Forgot Credentials and email verification
#window9 = change password

def sendMail(email):
    otp=str(random.randint(100000,999999))
    try:
        server=smtplib.SMTP("smtp.gmail.com",587)
        server.ehlo()
        server.starttls()
        server.login("root.rvl@gmail.com","")
        server.sendmail('root.rvl@gmail.com', email, "Subject:[No reply]\nOTP for email verification is "+otp)
        server.close()
    except:
        print("Unable to reach the server")

def verifyOTP():
    print("under process")

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
        # Window1 widgets
        self.heading = Label(tk, text="This is heading", font=("Rockwell", 40, "bold"))
        self.signupButton = Button(tk, text="SIGNUP", height=3, width=15, font=myFont, bg="#07AD31", fg="white",
                                   activebackground="white", command=self.signup)
        self.logButton = Button(tk, text="LOGIN", height=3, width=15, font=myFont, bg="#07AD31", fg="white",
                                activebackground="white", command=self.login)
        self.leadButton = Button(tk, text="LEADERBOARD", height=3, width=15, font=myFont, bg="#07AD31", fg="white",
                                 activebackground="white", command=self.leaderboard)
        # self.adminLoginButton = Button(tk, text="ADMIN LOGIN", height=2, width=12, font=myFont,bg="#07AD31",fg="white", activebackground="white", command=self.adminLogin)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        # Window2 widgets: Login
        self.heading2 = Label(tk, text="Login", font=("Rockwell", 40, "bold"))
        self.userNameText = Label(tk, text="Username: ", font=("Rockwell", 15))
        self.userNameEntry = Entry(tk,width=30)
        self.passText = Label(tk, text="Password: ", font=("Rockwell", 15))
        self.passEntry = Entry(tk, show="*",width=30)
        self.submit = Button(tk, text="LOGIN", height=1, width=8, font=myFont, bg="#07AD31", fg="white",
                             activebackground="white", command=self.checkLogin)
        self.invalidLogin = Label(tk, text="Invalid username or password", font=("Rockwell", 15))
        self.forgotUserPassButton = Button(tk, text="Forgot Username/Password", height=1, width=25, font=myFont2, bg="white", fg="black", activeforeground="blue", command=self.forgotUserPass)
        self.NoAccountText = Label(tk, text="Don't have an account?", font=myFont3)
        self.signupButton2 = Button(tk, text="SIGNUP", height=1, width=8, font=myFont, bg="#07AD31", fg="white",
                                   activebackground="white", command=self.signup)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # Window3 widgets: Signup
        self.heading3 = Label(tk, text="Create a New account", font=("Rockwell", 40, 'bold'))
        self.NameText = Label(tk, text='Name: ', font=('Rockwell', 18))
        self.NameEntry = Entry(tk, width=40)
        self.EmailText = Label(tk, text='Email: ', font=('Rockwell', 18))
        self.EmailEntry = Entry(tk, width=40)
        self.invalidEmail = Label(tk, text="Invalid Email id!", font=('Rockwell',15))
        self.ExistEmail = Label(tk, text="Email already Exist", font=('Rockwell',15))
        self.userNameText2 = Label(tk, text="Username: ", font=("Rockwell", 18))
        self.userNameEntry2 = Entry(tk, width=40)
        self.invalidUsername = Label(tk,text="Invalid username!", font=('Rockwell',15))
        self.ExistUsername = Label(tk, text="Username already exist", font=('rockwell',15))
        self.passText2 = Label(tk, text="Password: ", font=("Rockwell", 18))
        self.passEntry2 = Entry(tk, show="*", width=40)
        self.confirmPassText = Label(tk, text='Confirm Password: ', font=('Rockwell', 18))
        self.confirmPassEntry = Entry(tk, show='*', width=40)
        self.invalidPassword = Label(tk, text="Password doesn't match!", font=("Rockwell", 15))
        self.submitButton = Button(tk, text="SUBMIT", height=1, width=8, font=myFont, bg="#07AD31", fg="white",
                                   activebackground="white", command=self.register)
        self.HaveAccountText = Label(tk, text="Already have an account?", font=myFont3)
        self.loginButton2 = Button(tk, text="LOGIN", height=1, width=8, font=myFont, bg="#07AD31", fg="white",
                                    activebackground="white", command=self.login)

        self.registeredMessage = Label(tk, text='Registered Succesfully!', font=("Rockwell", 22))

        # Window4 widgets
        # window 4 widgets here

        # Window5 widgets : dashboard
        # using widgets name username email from window3
        self.changePassButton = Button(tk, text='Change Password', height=1, width=15, font=myFont,bg="#07AD31", fg="white",
                                    activebackground="white", command=self.window9)

        # Window6 widgets
        # window 6 widgets here

        #Window7 widgets
        #Window 7 widgets here

        # Window 8 widgets : forget username and password
        self.verifyEmailText = Label(tk, text="Verify your email id")
        self.enterUserMailText = Label(tk, text="Enter Username or E-mail id")
        self.otpText = Label(tk, text="Enter the OTP sent to your registered email id")
        self.otpEntry = Entry(tk,width=6, font=("Rockwell",15))
        self.userMailEntry = Entry(tk, width=40)
        self.submitForgotCreds = Button(tk, text="Get e-mail",height=1,width=12, font=myFont,bg="#07AD31", fg="white",
                                   activebackground="white", command=sendMail)
        self.verifyOTPButton = Button(tk, text="Verify OTP",height=1,width=12, font=myFont,bg="#07AD31", fg="white",
                                   activebackground="white", command=verifyOTP)

        #window9 widgets : change password
        self.heading9 = Label(tk, text='Change Password', font=('Rockwell',40,'bold'))
        self.currentPassText = Label(tk, text='Current Password: ', font=('Rockwell', 18))
        self.currentPassEntry = Entry(tk,show="*",width=40)
        self.invalidCurrentPass = Label(tk,text="Invalid Current Password!", font=('Rockwell',15))
        self.submitChangePassButton = Button(tk, text="Submit",height=1,width=12, font=myFont,bg="#07AD31", fg="white",
                                   activebackground="white", command=self.changePass)
        # using window3 passtext2 and confirmpass

    # -------------------------------------------------------------------------------------------------------------------
    def window1(self):
        self.heading.place(relx=0.5, rely=0.1, anchor="center")
        self.signupButton.place(relx=0.5, rely=0.4, anchor="center")
        self.logButton.place(relx=0.5, rely=0.53, anchor="center")
        self.leadButton.place(relx=0.5, rely=0.6, anchor="n")

    def signup(self):
        self.clearWindow1()
        self.clearWindow2()
        print("Signup clicked")
        self.window3()

    def login(self):
        self.clearWindow1()
        self.clearWindow3()
        print("Login clicked")
        self.window2()

    def leaderboard(self):
        self.clearWindow1()
        print("Leaderboard clicked")
        # self.window4

    def clearWindow1(self):
        self.heading.place_forget()
        self.signupButton.place_forget()
        self.logButton.place_forget()
        self.leadButton.place_forget()

    # -------------------------------------------------------------------------------------------------------------------
    def window2(self):
        self.heading2.place(relx=0.5, rely=0.1, anchor="center")
        self.userNameText.place(relx=0.4, rely=0.4, anchor="e")
        self.userNameEntry.place(relx=0.41, rely=0.4, anchor="w")
        self.passText.place(relx=0.4, rely=0.5, anchor="e")
        self.passEntry.place(relx=0.41, rely=0.5, anchor="w")
        self.submit.place(relx=0.5, rely=0.64, anchor="center")
        self.forgotUserPassButton.place(relx=0.44, rely=0.58, anchor="w")
        self.NoAccountText.place(relx= 0.5, rely=0.73, anchor='center')
        self.signupButton2.place(relx=0.5, rely=0.78, anchor='center')

    def clearWindow2(self):
        self.heading2.place_forget()
        self.userNameText.place_forget()
        self.userNameEntry.place_forget()
        self.passText.place_forget()
        self.passEntry.place_forget()
        self.submit.place_forget()
        self.invalidLogin.place_forget()
        self.forgotUserPassButton.place_forget()
        self.NoAccountText.place_forget()
        self.signupButton2.place_forget()

    def checkLogin(self):
        self.enteredUsername = self.userNameEntry.get()
        enteredPass = self.passEntry.get()
        user.execute("SELECT PASSWORD FROM USERS WHERE USERNAME='{}'".format(self.enteredUsername))
        pasHash = user.fetchone()
        if pasHash!=None and pasHash[0] == hashlib.sha256(enteredPass.encode()).hexdigest():
            print("Login successful")
            self.clearWindow2()
            self.window5()
        else:
            self.invalidLogin.place(relx=0.5, rely=0.3, anchor='center')

    def forgotUserPass(self):
        self.clearWindow2()
        self.userName=self.userNameEntry.get()
        self.window8(self.userName)
        print("Forgot UserPass Clicked")

    def mailForOTP(self):
        print("Send e-mail clicked")

    # --------------------------------------------------------------------------------------------------------------------------------
    def window3(self):
        self.heading3.place(relx=0.5, rely=0.1, anchor='center')
        self.NameText.place(relx=0.4, rely=0.3, anchor='e')
        self.NameEntry.place(relx=0.41, rely=0.3, anchor='w')
        self.EmailText.place(relx=0.4, rely=0.38, anchor='e')
        self.EmailEntry.place(relx=0.41, rely=0.38, anchor='w')
        self.userNameText2.place(relx=0.4, rely=0.46, anchor='e')
        self.userNameEntry2.place(relx=0.41, rely=0.46, anchor='w')
        self.passText2.place(relx=0.4, rely=0.54, anchor='e')
        self.passEntry2.place(relx=0.41, rely=0.54, anchor='w')
        self.confirmPassText.place(relx=0.4, rely=0.62, anchor='e')
        self.confirmPassEntry.place(relx=0.41, rely=0.62, anchor='w')
        self.submitButton.place(relx=0.5, rely=0.7, anchor='center')
        self.HaveAccountText.place(relx=0.5, rely=0.8, anchor='center')
        self.loginButton2.place(relx=0.5, rely=0.87, anchor='center')

    def clearWindow3(self):
        self.passEntry2.delete(0,END)
        self.confirmPassEntry.delete(0,END)
        self.heading3.place_forget()
        self.NameText.place_forget()
        self.NameEntry.place_forget()
        self.EmailText.place_forget()
        self.EmailEntry.place_forget()
        self.userNameText2.place_forget()
        self.userNameEntry2.place_forget()
        self.passText2.place_forget()
        self.passEntry2.place_forget()
        self.confirmPassText.place_forget()
        self.confirmPassEntry.place_forget()
        self.submitButton.place_forget()
        self.HaveAccountText.place_forget()
        self.loginButton2.place_forget()
        self.invalidPassword.place_forget()
        self.invalidEmail.place_forget()
        self.invalidUsername.place_forget()
        self.ExistEmail.place_forget()
        self.ExistUsername.place_forget()


    def register(self):
        self.invalidUsername.place_forget()
        self.invalidEmail.place_forget()
        self.ExistEmail.place_forget()
        self.ExistUsername.place_forget()
        self.invalidPassword.place_forget()

        enteredName=self.NameEntry.get()
        self.enteredUsername=self.userNameEntry2.get()
        enteredEmail=self.EmailEntry.get()
        enteredPassword=self.passEntry2.get()
        enteredConfirmpassword=self.confirmPassEntry.get()

        if not isUserName(self.enteredUsername):
            self.invalidUsername.place(relx=0.5, rely=0.2, anchor='center')
        elif not isEmail(enteredEmail):
            self.invalidEmail.place(relx=0.5,rely=0.2,anchor='center')
        elif usernameExists(self.enteredUsername):
            self.ExistUsername.place(relx=0.5,rely=0.2,anchor='center')
        elif emailExists(enteredEmail):
            self.ExistEmail.place(relx=0.5,rely=0.2,anchor='center')
        elif enteredPassword != enteredConfirmpassword:
            self.invalidPassword.place(relx=0.5, rely=0.2,anchor='center')
        else:
            self.clearWindow3()
            print("Button Clicked")
            #window5
            passHash = hashlib.sha256(enteredPassword.encode()).hexdigest()
            user.execute("INSERT INTO USERS VALUES('{}','{}','{}','{}')".format(enteredName, enteredEmail,self.enteredUsername, passHash))
            mycon.commit()
            messagebox.showinfo("Congrats!","Registered Successfully")
            # self.registeredMessage.place(relx=0.5, rely=0.4, anchor='center')
            # time.sleep(3)
            # self.registeredMessage.place_forget()
            self.window5()

#-----------------------------------------------------------------------------------------------------------------------
    #window 5
    def window5(self):
        self.NameText.place(relx=0.25,rely=0.2,anchor='w')
        self.userNameText2.place(relx=0.25,rely=0.28,anchor='w')
        self.EmailText.place(relx=0.25,rely=0.36,anchor='w')
        self.changePassButton.place(relx=0.45,rely=0.44,anchor='center')
        user.execute("SELECT NAME,EMAIL FROM USERS WHERE USERNAME='{}'".format(self.enteredUsername))
        self.userData = user.fetchone()
        #widgets
        self.getName = Label(tk, text=self.userData[0], font=myFont)
        self.getUsername = Label(tk, text=self.enteredUsername, font=myFont)
        self.getEmail = Label(tk, text=self.userData[1], font=myFont)

        self.getName.place(relx=0.37,rely=0.2,anchor='w')
        self.getUsername.place(relx=0.37, rely=0.28, anchor='w')
        self.getEmail.place(relx=0.37,rely=0.36,anchor='w')

    def clearwindow5(self):
        self.NameText.place_forget()
        self.userNameText2.place_forget()
        self.EmailText.place_forget()
        self.changePassButton.place_forget()
        self.getName.place_forget()
        self.getUsername.place_forget()
        self.getEmail.place_forget()

    #Window 8-----------------------------------------------------------------------------------------------------------
    def window8(self,x):
        #x=1 represents verify email after registration; x=2 represents forgot username/password
        if x==1:
            self.verifyEmailText.place(relx=0.5,rely=1,anchor="center")
        else:
            self.userMailEntry.place(relx=0.5,rely=0.35,anchor="center")#continue here-------------------------------------------------------------------------
        self.enterUserMailText.place(relx=0.5,rely=0.35,anchor="center")
        self.userMailEntry.place(relx=0.5,rely=0.4,anchor="center")
        self.userMailEntry.insert(END,username)
        self.submitForgotCreds.place(relx=0.5,rely=0.5,anchor="center")

    def clearWindow8(self):
        self.verifyEmailText.place_forget()
        self.enterUserMailText.place_forget()
        self.otpText.place_forget()
        self.otpEntry.place_forget()
        self.userMailEntry.place_forget()
        self.submitForgotCreds.place_forget()
        self.verifyOTPButton.place_forget()

#-------------------------------------------------------------------------------------------------------------------------
    def window9(self):
        self.clearwindow5()
        self.heading9.place(relx=0.5, rely=0.1,anchor='center')
        self.currentPassText.place(relx=0.4, rely=0.25,anchor='e')
        self.currentPassEntry.place(relx=0.41, rely=0.25,anchor='w')
        self.passText2.place(relx=0.4, rely=0.35, anchor='e')
        self.passEntry2.place(relx=0.41, rely=0.35, anchor='w')
        self.confirmPassText.place(relx=0.4, rely=0.45, anchor='e')
        self.confirmPassEntry.place(relx=0.41, rely=0.45, anchor='w')
        self.submitChangePassButton.place(relx=0.5,rely=0.6,anchor='center')

    def changePass(self):
        self.invalidCurrentPass.place_forget()
        self.invalidPassword.place_forget()

        enteredCurrentPass = self.currentPassEntry.get()
        enteredPassword2 = self.passEntry2.get()
        enteredConfirmpassword2 = self.confirmPassEntry.get()
        user.execute("SELECT PASSWORD FROM USERS WHERE USERNAME='{}'".format(self.enteredUsername))
        currentpass = user.fetchone()[0]
        if hashlib.sha256(enteredCurrentPass.encode()).hexdigest() != currentpass:
            self.invalidCurrentPass.place(relx=0.5, rely=0.2, anchor='center')
        elif enteredPassword2 != enteredConfirmpassword2:
            self.invalidPassword.place(relx=0.5, rely=0.2, anchor='center')
        else:
            user.execute("UPDATE USERS SET PASSWORD='{}' WHERE USERNAME='{}'".format(hashlib.sha256(enteredPassword2.encode()).hexdigest(), self.enteredUsername))
            mycon.commit()
            self.clearwindow9()

    def clearwindow9(self):
        self.heading9.place_forget()
        self.currentPassText.place_forget()
        self.currentPassEntry.place_forget()
        self.passText2.place_forget()
        self.passEntry2.place_forget()
        self.confirmPassText.place_forget()
        self.confirmPassEntry.place_forget()
        self.submitChangePassButton.place_forget()

if __name__ == '__main__':
    dbPass = "mokshada"  # change this as per your machine
    dbName = "quiz"  # change if database name is different on your machine
    try:
        mycon = mc.connect(host="localhost", user="root", password=dbPass, database=dbName)
        user = mycon.cursor()

    except:
        print("Error connecting to the database...!\nPlease try again after sometime.")
        print("We are sorry for the inconvenience")
        exit()
    tk = Tk()
    tk.title("Title")
    myFont = font.Font(family='Rockwell')
    myFont2 = font.Font(family='Rockwell', size=8) #Used for forgot username/password button
    myFont3 = font.Font(family='Rockwell', size=10) #Used for account
    tk.geometry('1200x700')
    ob = quiz()
    ob.window1()
    tk.mainloop()