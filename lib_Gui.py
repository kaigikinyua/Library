from Tkinter import *
import tkMessageBox
from lib_dbase import *
class Gui():
#-----admin login-----------------------------------------------------------------
    def __init__(self):
        self.root=Tk()
        self.root.title("Library Management System ")
        frame=Frame(self.root)
        l=Label(frame,text="Username")
        self.username=Entry(frame,width=30)
        l1=Label(frame,text="Password")
        self.password=Entry(frame,show="*",width=30)
        button=Button(frame,text="Login",background="green",command=self.login)
        l.pack()
        self.username.pack()
        l1.pack()
        self.password.pack()
        button.pack()
        frame.pack()
        self.root.mainloop()
    #-----checks details entered into the login are correct
    def login(self):
        uname=self.username.get()
        password=self.password.get()
        l=LibRecords();
        r=l.adminDetails(uname,password)
        if(r==TRUE):
            self.root.destroy()
            #showerror,showwarning,showinfo
            #tkMessageBox.showinfo("Login Sucess","Hello")
            self.mainpage();
        else:
            tkMessageBox.showwarning("Acess Denied","Wrong Username or Password")
#----mainpage--------------------------------------------------------------------
    def mainpage(self):
        mainpage=Tk()
        mainpage.title("Library Management System");
        menuframe=Frame(mainpage,background="yellow")
        mUsers=Button(menuframe,text="Users",command=self.userMangementPage)
        mBooks=Button(menuframe,text="Books",command=self.bookManageMent)
        borrow=Button(menuframe,text="Borrow")
        rBook=Button(menuframe,text="Return")
        mUsers.pack()
        mBooks.pack()
        borrow.pack()
        rBook.pack()
        menuframe.pack(side=LEFT)
        mainpage.mainloop()
#-----user management page-------------------------------------------------------
#---add some pictures men that thing is too blank
    def userMangementPage(self):
        self.userm=Tk()
        self.userm.title("LSM--User Management")
        frame=Frame(self.userm)
        frameL=Frame(self.userm)
        addUser=Button(frame,text="ADD User",background="GREEN",command=self.addUser)
        deleteUser=Button(frame,text="Delete User",background="RED",command=self.deleteUser)
        lname=Label(frameL,text="Username")
        lcontact=Label(frameL,text="Contact")
        lpass=Label(frameL,text="Password")
        self.name=Entry(frameL,width=30)
        self.contact=Entry(frameL,width=30)
        self.password=Entry(frameL,width=30,show="*")
        addUser.pack(side=RIGHT)
        deleteUser.pack(side=LEFT)
        frame.pack(side=BOTTOM)
        lname.pack()
        self.name.pack()
        lcontact.pack()
        self.contact.pack()
        lpass.pack()
        self.password.pack()
        frameL.pack(side=TOP)
        self.userm.mainloop()
    #adding a new user params(username,password,contact)
    def addUser(self):
        uname=self.name.get()
        contact=self.contact.get()
        password=self.password.get()
        l=LibRecords()
        r=l.addUser(uname,contact,password)
        if(r==True):
            tkMessageBox.showinfo("User Added","User "+uname+" has been Added successfully")
            self.userm.destroy()
        else:
            tkMessageBox.showerror("Failed","Error while adding user\nPlease contact the System admin")
    #adding a new user params(username,password,contact)
    def deleteUser(self):
        uname=self.name.get()
        contact=self.contact.get()
        password=self.password.get()
        l=LibRecords()
        r=l.deleteUser(uname,contact,password)
        if(r==True):
            tkMessageBox.showinfo("Deleted User",uname+" has been deleted")
        else:
            tkMessageBox.showerror("Error","Error in deleting "+uname)
#-------Book management----------------------------------------------------------
    def bookManageMent(self):
        bookp=Tk()
        bookp.title("LMS---Book Management")
        frame=Frame(bookp)
        lBook=Label(frame,text="Book Name")
        lauthor=Label(frame,text="Author Name")
#!!---category should be a dropdown
        lcategory=Label(frame,text="Category")
        lcopies=Label(frame,text="Copies")
        self.Book=Entry(frame,width=30)
        self.author=Entry(frame,width=30)
        self.category=Entry(frame,width=30)
        self.copies=Entry(frame,width=30)
        lBook.pack();self.Book.pack()
        lauthor.pack();self.author.pack()
        lcategory.pack();self.category.pack()
        lcopies.pack();self.copies.pack()
        frame.pack(side=TOP)
        bFrame=Frame(bookp)
#!!command------
        add=Button(bFrame,text="Add",background='green',command=self.addBook)
        delete=Button(bFrame,text="Delete",background='red')
        add.pack(side=RIGHT)
        delete.pack(side=LEFT)
        bFrame.pack(side=BOTTOM)
        book.mainloop()
    #method for adding books
    def addBook(self):
        l=LibRecords()
        bookname=self.Book.get();author=self.author.get();category=self.category.get();copies=self.copies.get();
        r=l.addBook(bookname,author,category,copies)
        if(r==True):
            tkMessageBox.showinfo("Entry Sucess","The Book "+bookname+" has been added successfully")
        else:
            tkMessageBox.showerror("Error ","There was an Error while adding "+bookname)
#------Borrow Books -----------------------------------------------------------------
g=Gui()
