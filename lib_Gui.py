from Tkinter import *
import tkMessageBox
from lib_dbase import *
from PIL import Image,ImageTk
class Gui():
#-----admin login-----------------------------------------------------------------
    def __init__(self):
        self.root=Tk()
        self.root.title("Library Management System ")
        photo=PhotoImage(file=".//pictures//lib.png")
        bg=Label(self.root,image=photo)
        bg.pack()
        frame=Frame(self.root)
        login=Label(frame,text="-----Login------",font="red")
        login.pack()
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
        mainpage.configure(bg="lightblue")
        mainpage.title("Library Management System");
        photo=PhotoImage(file=".//pictures//shellfc.png")
        lphoto=Label(mainpage,image=photo)
        lphoto.pack(side=TOP)

        #Edditing the mainpage
    #Bottom Frame
        BottomFrame=Frame(mainpage)
      #borrow Frame(LEFT)
        borrowF=Frame(BottomFrame)
        #userdetails
        rframe=Frame(borrowF,highlightbackground="lightgreen",highlightthickness=3)
        lborrow=Label(rframe,text="Borrow Book")
        lborrow.pack(side=TOP)
        luname=Label(rframe,text="Username");lcontact=Label(rframe,text="User Contact");
        self.Euname=Entry(rframe,width=30);self.Econtact=Entry(rframe,width=30);
        luname.pack();self.Euname.pack();lcontact.pack();self.Econtact.pack()
        b=Button(rframe,text="Borrow",bg="lightgreen",fg="white")
        b.pack(side=BOTTOM)
        rframe.pack(side=LEFT)
        ##############
        #pictures and animation
        lframe=Frame(borrowF,highlightbackground="lightgreen",highlightthickness=1)
        picture=PhotoImage(file=".//pictures//ui.png")
        lphoto=Label(lframe,image=picture)
        lphoto.pack()
        lframe.pack(side=RIGHT)

        borrowF.pack(side=LEFT)

      #return Frame(right)
        returnFrame=Frame(BottomFrame,highlightbackground="lightgreen",highlightthickness=3)
        #userDetails
        lrFrame=Frame(returnFrame)
        lreturnFrame=Label(lrFrame,text="Return Book")
        lreturnFrame.pack(side=TOP)
        luname=Label(lrFrame,text="Username");lbook=Label(lrFrame,text="Book")
        self.runame=Entry(lrFrame,width=30);self.rbook=Entry(lrFrame,width=30);
        luname.pack();self.runame.pack();lbook.pack();self.rbook.pack()
        b2=Button(lrFrame,text="Return",bg="lightgreen",fg="white")
        b2.pack()
        lrFrame.pack(side=RIGHT)
        #annimation and Results
        rrframe=Frame(returnFrame)
        image=PhotoImage(file=".//pictures//si.png")
        limage=Label(rrframe,image=image)
        limage.pack(side=TOP)
        rrframe.pack(side=LEFT)
        returnFrame.pack(side=RIGHT)

        BottomFrame.pack()
        mainpage.mainloop()
#-----user management page-------------------------------------------------------
#---add some pictures men that thing is too blank
"""   def borrowBook(self):
        window=Tk()
        window.title("LMS--Borrow Books")
        l=LibRecords()
        r=l.displayBooks()
        books=[];i=0;
#display the books the user wants
#should be easily selectable and added to users wishlist
#should not be more than 3 books
        books=[];j=0;
        for item in range(len(r)):
            books+=[r[j][1]+" "+r[j][2]+" "+r[j][3]];j+=1;
        self.list=Listbox(window);i=0;
        for item in books:
            self.list.insert(i,item);i+=1;
        self.list.pack()
        mylist=Button(window,text="Borrow",bg="green",command=self.enventBorrow)
        mylist.pack()
        window.mainloop()
    #event handler for the Listbox
    def enventBorrow(self):
        a=self.list.curselection()
        print a
        for i in a:
            print self.list.get(i)"""
g=Gui()
