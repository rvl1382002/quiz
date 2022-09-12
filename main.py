# Author: Riddhish V. Lichade
# username: root_rvl

import hashlib
import tkinter
from tkinter import *
from tkinter.ttk import *
import tkinter.font as font
import mysql.connector as mc
try:
    mycon=mc.connect(host="localhost",user="root",password="Ridd_hish",database="quiz")
    user=mycon.cursor()
except:
    print("Error connecting to the database...!\nPlease try again.")
    print("We are sorry for the inconvenience")
    exit()

#Window1=1st window, window2=login window, window3=leaderboard window,
def clearWindow1():
    heading.place_forget()
    logButton.place_forget()
    leadButton.place_forget()

def window2():
    global userNameEntry
    global passEntry
    heading2 = Label(tk, text="Login", font=("Rockwell", 40, "bold"))
    heading2.place(relx=0.5, rely=0.1, anchor="center")

    userNameText = Label(tk, text="Username: ", font=("Rockwell", 15))
    userNameText.place(relx=0.4, rely=0.4, anchor="e")

    userNameEntry=Entry(tk)
    userNameEntry.place(relx=0.41 ,rely=0.4, anchor="w")

    passText = Label(tk, text="Password: ", font=("Rockwell", 15))
    passText.place(relx=0.4, rely=0.5, anchor="e")

    passEntry = Entry(tk,show="*")
    passEntry.place(relx=0.41, rely=0.5, anchor="w")

    submit=tkinter.Button(tk,text="LOGIN", height=1,width=8, font=myFont,bg="#07AD31",fg="white",activebackground="white", command=checkLogin)
    submit.place(relx=0.5,rely=0.6,anchor="center")

def checkLogin():
    print(userNameEntry.get())
    print(passEntry.get())
    #continue from here----------------------------------------------------------------------
    user.execute("SELECT PASSWORD FROM USERS WHERE USERNAME={}".format(userNameEntry))
    print("Login clicked")

def login():
    clearWindow1()
    window2()
    print("login clicked")

def leaderboard():
    clearWindow1()
    print("Leaderboard clicked")


tk=tkinter.Tk()
tk.title("Title")
myFont = font.Font(family='Rockwell')
tk.geometry('1200x700')

#Heading
heading=Label(tk,text="This is heading",font=("Rockwell",40,"bold"))
heading.place(relx=0.5,rely=0.1,anchor="center")

#Login Button
logButton=tkinter.Button(tk,text="LOGIN", height=3,width=15, font=myFont,bg="#07AD31",fg="white",activebackground="white", command=login)
logButton.place(relx=0.5,rely=0.5,anchor="center")

#Leaderboard button
leadButton=tkinter.Button(tk,text="LEADERBOARD", height=3, width = 15, font=myFont, bg="#07AD31",fg="white",activebackground="white", command=leaderboard)
leadButton.place(relx=0.5,rely=0.6,anchor="n")


tk.mainloop()
