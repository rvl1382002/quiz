import hashlib
from tkinter import *
import tkinter.font as font
import mysql.connector as mc


# window1=Home window
# window2=login window
# window3=signup window #moksha
# window4=leaderboard window
# window5=dashboard window #moksha
# window6=quiz window #moksha
# window7=admin login
# window8=Forgot Credentials

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

        # Window2 widgets: Login
        self.heading2 = Label(tk, text="Login", font=("Rockwell", 40, "bold"))
        self.userNameText = Label(tk, text="Username: ", font=("Rockwell", 15))
        self.userNameEntry = Entry(tk)
        self.passText = Label(tk, text="Password: ", font=("Rockwell", 15))
        self.passEntry = Entry(tk, show="*")
        self.submit = Button(tk, text="LOGIN", height=1, width=8, font=myFont, bg="#07AD31", fg="white",
                             activebackground="white", command=self.checkLogin)
        self.invalidLogin = Label(tk, text="Invalid username or password", font=("Rockwell", 15))
        self.forgotUserPassButton = Button(tk, text="Forgot Username/Password", height=1, width=25, font=myFont2, bg="white", fg="black", activeforeground="blue", command=self.forgotUserPass)

        # Window3 widgets: Signup
        self.heading3 = Label(tk, text="Create a New account", font=("Rockwell", 40, 'bold'))
        self.NameText = Label(tk, text='Name: ', font=('Rockwell', 18))
        self.NameEntry = Entry(tk, width=40)
        self.EmailText = Label(tk, text='Email: ', font=('Rockwell', 18))
        self.EmailEntry = Entry(tk, width=40)
        self.userNameText = Label(tk, text="Username: ", font=("Rockwell", 18))
        self.userNameEntry = Entry(tk, width=40)
        self.passText = Label(tk, text="Password: ", font=("Rockwell", 18))
        self.passEntry = Entry(tk, show="*", width=40)
        self.confirmPassText = Label(tk, text='Confirm Password: ', font=('Rockwell', 18))
        self.confirmPassEntry = Entry(tk, show='*', width=40)
        self.submitButton = Button(tk, text="SUBMIT", height=1, width=8, font=myFont, bg="#07AD31", fg="white",
                                   activebackground="white", command=self.register)

        # Window4 widgets
        # window 4 widgets here

        # Window5 widgets
        # window 5 widgets here

        # Window6 widgets
        # window 6 widgets here

        #Window7 widgets
        #Window 7 widgets here

        # Window 8 widgets
        self.enterUserMailText = Label(tk, text="Enter Username or E-mail id")
        self.userMailEntry = Entry(tk, width=40)
        self.submitForgotCreds = Button(tk, text="Get e-mail",height=1,width=12, font=myFont,bg="#07AD31", fg="white",
                                   activebackground="white", command=self.mailForOTP)

    # -------------------------------------------------------------------------------------------------------------------
    def window1(self):
        self.heading.place(relx=0.5, rely=0.1, anchor="center")
        self.signupButton.place(relx=0.5, rely=0.4, anchor="center")
        self.logButton.place(relx=0.5, rely=0.53, anchor="center")
        self.leadButton.place(relx=0.5, rely=0.6, anchor="n")

    def signup(self):
        self.clearWindow1()
        print("Signup clicked")
        self.window3()

    def login(self):
        self.clearWindow1()
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

    def clearWindow2(self):
        self.heading2.place_forget()
        self.userNameText.place_forget()
        self.userNameEntry.place_forget()
        self.passText.place_forget()
        self.passEntry.place_forget()
        self.submit.place_forget()
        self.invalidLogin.place_forget()
        self.forgotUserPassButton.place_forget()

    def checkLogin(self):
        enteredUsername = self.userNameEntry.get()
        enteredPass = self.passEntry.get()
        user.execute("SELECT PASSWORD FROM USERS WHERE USERNAME={}".format('username'))
        pasHash = user.fetchone()
        if pasHash[0] == hashlib.sha256(enteredPass.encode()).hexdigest():
            print("Login successful")
            self.clearWindow2()
            # window5
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
        self.NameText.place(relx=0.4, rely=0.4, anchor='e')
        self.NameEntry.place(relx=0.41, rely=0.4, anchor='w')
        self.EmailText.place(relx=0.4, rely=0.5, anchor='e')
        self.EmailEntry.place(relx=0.41, rely=0.5, anchor='w')
        self.userNameText.place(relx=0.4, rely=0.6, anchor='e')
        self.userNameEntry.place(relx=0.41, rely=0.6, anchor='w')
        self.passText.place(relx=0.4, rely=0.7, anchor='e')
        self.passEntry.place(relx=0.41, rely=0.7, anchor='w')
        self.confirmPassText.place(relx=0.4, rely=0.8, anchor='e')
        self.confirmPassEntry.place(relx=0.41, rely=0.8, anchor='w')
        self.submitButton.place(relx=0.5, rely=0.9, anchor='center')

    def clearWindow3(self):
        self.heading3.place_forget()
        self.NameText.place_forget()
        self.NameEntry.place_forget()
        self.EmailText.place_forget()
        self.EmailEntry.place_forget()
        self.userNameText.place_forget()
        self.userNameEntry.place_forget()
        self.passText.place_forget()
        self.passEntry.place_forget()
        self.confirmPassText.place_forget()
        self.confirmPassEntry.place_forget()
        self.submitButton.place_forget()

    def register(self):
        self.clearWindow3()
        print("Button Clicked")

    #Window 8-----------------------------------------------------------------------------------------------------------
    def window8(self,username):
        self.enterUserMailText.place(relx=0.5,rely=0.35,anchor="center")
        self.userMailEntry.place(relx=0.5,rely=0.4,anchor="center")
        self.userMailEntry.insert(END,username)
        self.submitForgotCreds.place(relx=0.5,rely=0.5,anchor="center")

if __name__ == '__main__':
    dbPass = "Ridd_hish"  # change this as per your machine
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
    tk.geometry('1200x700')
    ob = quiz()
    ob.window1()
    tk.mainloop()
