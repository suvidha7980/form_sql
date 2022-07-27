from tkinter import *
from tkinter import messagebox as msgbx
import mysql.connector
window = Tk()
window.title("Registration Form")
window.geometry('400x400')
window.config()

def register():
    conn=mysql.connector.connect(host='127.0.0.1',port='3306',user='root',password='root',database='demo2')
    mycursor=conn.cursor()
    fname=a1.get()
    lname=b1.get()
    email=c1.get()
    contact=e1.get()
    mycursor.execute("insert into register values(%s,%s,%s,%s)",(fname,lname,email,contact))
    msgbx.showinfo("Registration","Submitted")
    conn.commit()

d= Label(window, text="Registration form",font=("bold", 15)).grid(row = 0,column = 0)
a = Label(window ,text = "First Name:",padx=10,pady=10,font=("bold", 15)).grid(row = 1,column = 0)
b = Label(window ,text = "Last Name:",padx=10,pady=10,font=("bold", 15)).grid(row = 2,column = 0)
c = Label(window ,text = "Email Id:",padx=10,pady=10,font=("bold", 15)).grid(row = 3,column = 0)
e = Label(window ,text = "Phone No.:",padx=10,pady=10,font=("bold", 15)).grid(row = 4,column = 0)
btn1  = Button(window ,text="Submit",command=register,width=15, bg= 'blue',fg='white',pady=10,).grid(row=5,column=1)

a1 = Entry(window)
a1.grid(row = 1,column = 1)
b1 = Entry(window)
b1.grid(row = 2,column = 1)
c1 = Entry(window)
c1.grid(row = 3,column = 1)
e1 = Entry(window)
e1.grid(row = 4,column = 1)
window.mainloop()
4