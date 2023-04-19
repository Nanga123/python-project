from tkinter import *
from tkinter import messagebox
import sqlite3

user_list = []



def init():
    conn = sqlite3.connect("Database.db")
    cur = conn.cursor()

    if cur.execute("""SELECT * FROM sqlite_master WHERE type='table'""").fetchall() == []:
        cur.execute("""CREATE TABLE Users(Name text, Username text, Password text);""")

    conn.commit()
    conn.close()
    init_login('start')


def init_login(From):
    global tb_username
    global tb_password
    global login_win

    if From == 'signup':
        signup_win.destroy()
    elif From == 'main':
        main_win.destroy()

    login_win = Tk()
    login_win.title("Login page")
    login_win.geometry('1700x800')
    login_win.config(bg='light yellow')

    lbl_login = Label(text="LOGIN",font=("impact",35,"bold"),bg="light yellow",fg='black')
    lbl_login.place(relx=0.5,rely=0.25,anchor='center')

    lbl_username = Label(text="ENTER USER ID",font=("times new roman",20),bg="light yellow",fg='black')
    lbl_username.place(relx=0.43,rely=0.35,anchor='center')

    tb_username = Entry(font=("times new roman",17),bg="lightgray",width="18",fg='black')
    tb_username.place(relx=0.57,rely=0.35,anchor='center')

    lbl_password = Label(text="ENTER PASSWORD",font=("times new roman",20),bg="light yellow",fg='black')
    lbl_password.place(relx=0.43,rely=0.40,anchor='center')

    tb_password =Entry(font=("times new roman",17),bg="lightgray",width="18",show='*',fg='black')
    tb_password.place(relx=0.57,rely=0.40,anchor='center')

    btn_login = Button(text="LOGIN",font=("times new roman",18),width="15",fg='blue',command=login)
    btn_login.place(relx=0.5,rely=0.52,anchor='center')

    lbl_signup = Label( text="Do not have an account?",font=("times new roman",20),bg="light yellow",fg='red')
    lbl_signup.place(relx=0.43,rely=0.66,anchor='center')

    btn_signup = Button(text="Sign up",font=("times new roman",18),width="15",fg='red', command=lambda: init_signup('login'))
    btn_signup.place(relx=0.57,rely=0.66,anchor='center')

    login_win.mainloop()


def init_signup(From):
    global signup_win
    global tb_name
    global tb_username
    global tb_password
    global tb_reenterpass


    if From == 'login':
        login_win.destroy()
    elif From == 'main':
        main_win.destroy()

    signup_win = Tk()

    signup_win.title("Sign-up Page")
    signup_win.geometry('1700x800')
    signup_win.config(bg='light yellow')

    lbl_createacnt = Label(signup_win,text="Sign up",font=("impact",35,"bold"),bg="light yellow",fg='black')
    lbl_createacnt.place(relx=0.5,rely=0.25,anchor='center')


    lbl_name = Label(signup_win, text='Enter Name:',font=("times new roman",20),bg="light yellow",fg='black')
    lbl_name.place(relx=0.43,rely=0.35,anchor='center')

    tb_name = Entry(signup_win,font=("times new roman",17),bg="lightgray",width="18",fg='black')
    tb_name.place(relx=0.57,rely=0.35,anchor='center')


    lbl_username = Label(signup_win, text='Enter Username:',font=("times new roman",20),bg="light yellow",fg='black')
    lbl_username.place(relx=0.43,rely=0.40,anchor='center')

    tb_username = Entry(signup_win,font=("times new roman",17),bg="lightgray",width="18",fg='black')
    tb_username.place(relx=0.57,rely=0.40,anchor='center')

    lbl_password = Label(signup_win, text='Enter Password:',font=("times new roman",20),bg="light yellow",fg='black')
    lbl_password.place(relx=0.43,rely=0.45,anchor='center')

    tb_password = Entry(signup_win, show='*',font=("times new roman",17),bg="lightgray",width="18",fg='black')
    tb_password.place(relx=0.57,rely=0.45,anchor='center')

    lbl_reenterpass = Label(signup_win, text='Re-enter password:',font=("times new roman",20),bg="light yellow",fg='black')
    lbl_reenterpass.place(relx=0.43,rely=0.50,anchor='center')

    tb_reenterpass = Entry(signup_win, show='*',font=("times new roman",17),bg="lightgray",width="18",fg='black')
    tb_reenterpass.place(relx=0.57,rely=0.50,anchor='center')



    btn_signup = Button(signup_win, text='Sign Up',font=("times new roman",18),width="15",fg='red',command=signup)
    btn_signup.place(relx=0.5,rely=0.66,anchor='center')

    lbl_login = Label(signup_win, text="Already have an account?",font=("times new roman",20),bg="light yellow",fg='black')
    lbl_login.place(relx=0.43,rely=0.75,anchor='center')


    btn_login = Button(signup_win, text="Go back to login page",font=("times new roman",18),width="15",fg='blue', command=lambda: init_login('signup'))
    btn_login.place(relx=0.57,rely=0.75,anchor='center')

    signup_win.mainloop()


def init_main(From):
    global main_win
    global user_list

    if From == 'login':
        login_win.destroy()
    elif From == 'signup':
        signup_win.destroy()

    main_win = Tk()
    main_win.config(bg='light yellow')
    main_win.geometry('1700x800')

    lbl_name = Label(main_win, text=("Name:" + user_list[0]))
    lbl_name.grid(row=0, column=0)

    lbl_username = Label(main_win, text=("Username:" + user_list[1]))
    lbl_username.grid(row=1, column=0)



    btn_logout = Button(main_win, text="Logout", command=lambda: init_login('main'))
    btn_logout.grid(row=3, column=0)

    main_win.mainloop()


def login():
    global user_list
    global tb_username
    global tb_password

    conn = sqlite3.connect("Database.db")
    cur = conn.cursor()

    if tb_username.get() == '' or tb_password.get() == '':
        messagebox.showwarning("All fields are required", "Please enter all required fields")
        return ()
    else:
        cur.execute("SELECT rowid,* FROM Users WHERE USERNAME=?", (tb_username.get(),))
        temp_list = cur.fetchone()

    if temp_list == None:
        messagebox.showwarning("Invalid username", "Username does not exist")
        return ()
    elif tb_password.get() == temp_list[3]:
        user_list = list(temp_list)
        login_win.destroy
        init_main('login')
        return ()
    else:
        messagebox.showwarning("Wrong username or password", "Username and password don't match")
        return ()

    conn.commit()
    conn.close()


def signup():
    global user_list

    conn = sqlite3.connect("Database.db")
    cur = conn.cursor()

    if tb_name.get() == '' or tb_username.get() == '' or tb_password.get() == '' or tb_reenterpass.get() == '' :
        messagebox.showwarning("All fields are required", "Please enter all required fields")
        return ()
    elif len(tb_password.get()) < 8:
        messagebox.showwarning("Password is too short", "Password must be at least 8 characters long")
        return ()
    elif tb_password.get() != tb_reenterpass.get():
        messagebox.showwarning("Password does not match",
                               "Password entered in password textbox does not match password entered in re-enter password textbox")
        return ()

    else:
        cur.execute("SELECT rowid,* FROM Users WHERE Username=?", (tb_username.get(),))
        temp_list = cur.fetchone()

    if temp_list != None:
        messagebox.showwarning("Username already taken", "Please choose another username")
        return ()
    else:
        cur.execute("INSERT INTO Users VALUES (?,?,?)",
                    (tb_name.get(), tb_username.get(), tb_password.get()))
        conn.commit()

        cur.execute("SELECT rowid,* FROM Users WHERE Username=?", (tb_username.get(),))
        conn.commit()

        user_list = list(cur.fetchone())
        init_main('signup')

    conn.commit()
    conn.close()


init()
