
Aryan N <aryannangarath407@gmail.com>
Apr 18, 2023, 2:29 PM (1 day ago)
to me

from tkinter import*
from PIL import  ImageTk,Image
import mysql.connector as mysc
from tkinter import messagebox
global root
root=Tk()
root.title('LIBRARY MANAGEMENT')
root.geometry("1700x800")
root.config(bg="white")
mylabel=Label(fr,text="MY LIBRARY",font=("impact",30,"bold"),bg="white")
mylabel.place(x=200,y=30)


#label for user id
user_id_label = Label(fr,text="ENTER USER ID",font=("times new roman",18),bg="white")
user_id_label.place(x=50,y=150)

#enter for user id
global user_id
user_id= Entry(fr,font=("times new roman",15),bg="lightgray",width="18")
user_id.place(x=340,y=150)

#label for password
password_label = Label(fr,text="ENTER PASSWORD",font=("times new roman",18),bg="white")
password_label.place(x=50,y=210)

#entry for password
global password
password= Entry(fr,font=("times new roman",15),bg="lightgray",width="18",show='*')
password.place(x=340,y=210)

#creating a login button
login_button = Button(fr,text="LOGIN",bg="green",fg="black",font=("times new roman",15),width="15",command=login)
login_button.place(x=200,y=280)



root.mainloop()
