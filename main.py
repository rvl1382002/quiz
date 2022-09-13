import hashlib
from tkinter import *
import tkinter.font as font
import mysql.connector as mc

# window1=Home window,
# window2=login window,
# window3=signup window
# window4=leaderboard window
# window5=dashboard window


class quiz:
    def __init__(self):
        #Window1 widgets
        self.heading = Label(tk, text="This is heading", font=("Rockwell", 40, "bold"))
        self.signupButton = Button(tk, text="SIGNUP", height=3, width=15, font=myFont, bg="#07AD31", fg="white",activebackground="white", command=self.signup)
        self.logButton = Button(tk, text="LOGIN", height=3, width=15, font=myFont, bg="#07AD31", fg="white",activebackground="white", command=self.login)
        self.leadButton = Button(tk, text="LEADERBOARD", height=3, width=15, font=myFont, bg="#07AD31", fg="white",activebackground="white", command=self.leaderboard)

        #Window2 widgets
        self.heading2 = Label(tk, text="Login", font=("Rockwell", 40, "bold"))
        self.userNameText = Label(tk, text="Username: ", font=("Rockwell", 15))
        self.userNameEntry = Entry(tk)
        self.passText = Label(tk, text="Password: ", font=("Rockwell", 15))
        self.passEntry = Entry(tk, show="*")
        self.submit = Button(tk, text="LOGIN", height=1, width=8, font=myFont, bg="#07AD31", fg="white",activebackground="white", command=self.checkLogin)
        self.invalidLogin = Label(tk, text="Invalid username or password", font=("Rockwell", 15))

        #Window3widgets
    #-------------------------------------------------------------------------------------------------------------------
    def window1(self):
        self.heading.place(relx=0.5, rely=0.1, anchor="center")
        self.signupButton.place(relx=0.5, rely=0.4, anchor="center")
        self.logButton.place(relx=0.5, rely=0.53, anchor="center")
        self.leadButton.place(relx=0.5, rely=0.6, anchor="n")

    def signup(self):
        self.clearWindow1()
        print("Signup clicked")
        #self.window3

    def login(self):
        self.clearWindow1()
        print("Login clicked")
        self.window2()

    def leaderboard(self):
        self.clearWindow1()
        print("Leaderboard clicked")
        #self.window4

    def clearWindow1(self):
        self.heading.place_forget()
        self.signupButton.place_forget()
        self.logButton.place_forget()
        self.leadButton.place_forget()

    #-------------------------------------------------------------------------------------------------------------------
    def window2(self):
        self.heading2.place(relx=0.5, rely=0.1, anchor="center")
        self.userNameText.place(relx=0.4, rely=0.4, anchor="e")
        self.userNameEntry.place(relx=0.41, rely=0.4, anchor="w")
        self.passText.place(relx=0.4, rely=0.5, anchor="e")
        self.passEntry.place(relx=0.41, rely=0.5, anchor="w")
        self.submit.place(relx=0.5, rely=0.6, anchor="center")

    def clearWindow2(self):
        self.heading2.place_forget()
        self.userNameText.place_forget()
        self.userNameEntry.place_forget()
        self.passText.place_forget()
        self.passEntry.place_forget()
        self.submit.place_forget()
        self.invalidLogin.place_forget()


    def checkLogin(self):
        enteredUsername = self.userNameEntry.get()
        enteredPass = self.passEntry.get()
        user.execute("SELECT PASSWORD FROM USERS WHERE USERNAME={}".format('username'))
        pasHash=user.fetchone()
        if pasHash[0]==hashlib.sha256(enteredPass.encode()).hexdigest():
            print("Login successful")
            self.clearWindow2()
            #window5
        else:
            self.invalidLogin.place(relx=0.5, rely=0.3, anchor='center')

if __name__=='__main__':
    try:
        mycon = mc.connect(host="localhost", user="root", password="Ridd_hish", database="quiz")
        user = mycon.cursor()
    except:
        print("Error connecting to the database...!\nPlease try again after sometime.")
        print("We are sorry for the inconvenience")
        exit()
    tk=Tk()
    tk.title("Title")
    myFont = font.Font(family='Rockwell')
    tk.geometry('1200x700')
    ob=quiz()
    ob.window1()
    print("Window1 called")
    tk.mainloop()
