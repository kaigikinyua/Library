from Tkinter import *
import tkMessageBox
from lib_dbase import *
from PIL import Image,ImageTk
class Gui():
#-----admin login-------------------------------------------------------------------------
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
#----mainpage------------------------------------------------------------------------------
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
        rframe=Frame(borrowF,highlightbackground="lightgreen",highlightthickness=1)
        lborrow=Label(rframe,text="Borrow Book")
        lborrow.pack(side=TOP)
        luname=Label(rframe,text="Username");lcontact=Label(rframe,text="User Contact");
        self.Euname=Entry(rframe,width=30);self.Econtact=Entry(rframe,width=30);
        luname.pack();self.Euname.pack();lcontact.pack();self.Econtact.pack()


        #dispalys books that are p_available
        books=[];i=0;l=LibRecords();
        r=l.displayBooks()
        for item in range(len(r)):
            books+=[r[i][0]+" - "+r[i][1]+" - "+r[i][2]+" - "+r[i][3]]
            i+=1
        self.bookList=Listbox(rframe,width=60);j=0;
        for item in books:
            self.bookList.insert(j,item)
        self.bookList.pack()


        b=Button(rframe,text="Borrow",bg="green",fg="white",command=self.enventBorrow)
        b.pack(side=BOTTOM)
        rframe.pack(side=LEFT)
        ##############
        #pictures and animation
        lframe=Frame(borrowF,highlightbackground="lightblue",highlightthickness=1)
        picture=PhotoImage(file=".//pictures//ui.png")
        lphoto=Label(lframe,image=picture)
        lphoto.pack()
        lframe.pack(side=RIGHT)

        borrowF.pack(side=LEFT)

      #*return Frame(right) have a search engine -- remove the userDetails and add the search engine please
        returnFrame=Frame(BottomFrame,highlightbackground="lightblue",highlightthickness=1)
        #userDetails
        lrFrame=Frame(returnFrame)
        lreturnFrame=Label(lrFrame,text="Return Book")
        lreturnFrame.pack(side=TOP)
        search=Label(lrFrame,text="Search Record By user contact");
        self.search=Entry(lrFrame,width=30);
        searchButton=Button(lrFrame,bg="blue",text="Search")
        #add a command for search
        search.pack();self.search.pack();searchButton.pack()


        l=LibRecords()
        r=l.displayBorrowed();borrowed=[];e=0;
        for item in range(len(r)):
            borrowed+=[r[e][0]+" "+r[e][1]+" "+str(r[e][2])]
            e+=1
        self.borrowed=Listbox(lrFrame,width=30);q=0;
        for item in borrowed:
                self.borrowed.insert(j,item)
                q+=1
        self.borrowed.pack()

        b2=Button(lrFrame,text="Return",bg="green",fg="white",command=self.returnBook)
        #add a command for the return should have a security check if the record is true
    #update the Inventory records
    #check for penalties
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
        #lib _ records

        managementFrame=Frame(mainpage)
        lManagement=Label(managementFrame,text="Management")
        lManagement.pack()
        borrowedRecords=Button(managementFrame,text="Users",bg="red",fg="white",command=self.borrowedRecords)
        borrowedRecords.pack(side=LEFT)
        Inventory=Button(managementFrame,text="Books",bg="red",fg="white",command=self.bookRecords)
        Inventory.pack(side=RIGHT)
        managementFrame.pack()
        mainpage.mainloop()

#eventhandler for the borrow button-------------------------------------------------------------
    def enventBorrow(self):
        a=self.bookList.curselection()
        #add security 1.user shoulnot borrow more than 1 book
        string=self.bookList.get(a);id="";
        for i in range(7):
            if (string[i]!='0' and string[i]!='1' and string[i]!='2' and string[i]!='3' and string[i]!='4' and string[i]!='5' and string[i]!='6' and string[i]!='7' and string[i]!='8'):
                if(string[i]!='9'):
                    break;
                else:
                    id+=string[i]
            else:
                id+=string[i]
        contact=self.Econtact.get()
        #*write a patch to ensure the contact is a member
        if(len(contact)!=0):
            l=LibRecords()
            r=l.borrow(id,contact)
        else:
            tkMessageBox.showerror("Empty Fields","Enter the username and Contact");
        if(r==True):
            tkMessageBox.showinfo("Sucess","The user by the contact\n"+contact+" has borrowed the book by the id\n"+id)
        elif(r==False):
            tkMessageBox.showerror("Error","Please contact your system admin")
        else:
            tkMessageBox.showwarning("Book Not available","The book is not available at this time")
    #resoponse
    def returnBook(self):
        a=self.borrowed.curselection()
        details=[];b="";
        for i in self.borrowed.get(a):
            if (i!=" " and i!="\n"):
                b+=i
            else:
                details+=[b]
                b=""
        for item in details:
            print item
        l=LibRecords()
        r=l.BookReturn(details[0],details[1])
        #error handling
        if(r==True):
            tkMessageBox.showinfo("Success","Sucessfully Returned the book\n"+details[1]+"\nwith contact details\n"+details[0])
        elif(r=="Too many records"):
            tkMessageBox.showwarning("Too Many Records","There are more than one of such records")
        elif(r=="No records"):
            tkMessageBox.showwarning("No details","No such records in the database")
        else:
            tkMessageBox.showerror("Unrecoverable Error","Please Contact the system admin")
    def borrowedRecords(self):
        self.bor=Tk()
        self.bor.title("User management")
        main=Frame(self.bor)
        bor=Frame(main)
        l1=Label(self.bor,text="Users")
        l1.pack()
        self.borrowedList=Listbox(self.bor,width=50)
        l=LibRecords()
        r=l.dispalyUsers()
        users=[];i=0;
        for e in range(len(r)):
            users+=[r[i][0]+" "+r[i][1]]
            i+=1
        j=0
        for item in users:
            self.borrowedList.insert(j,item)
            j+=1
        self.borrowedList.pack()

        ldelete=Label(main,text="Delete User")
        ldelete.pack()
        #add funtionalities to delete
        bDelete=Button(main,text="Delete",fg="white",bg="red",command=self.deleteUser)
        bDelete.pack()
        l2=Label(main,text="Add a user")
        l2.pack()
        luname=Label(main,text="Username")
        luname.pack()
        self.user=Entry(main,width=30)
        self.user.pack()
        lcontact=Label(main,text="Contact")
        lcontact.pack()
        self.con=Entry(main,width=30)
        self.con.pack()
        lp=Label(main,text="Password")
        self.password=Entry(main,width=30,show="%")
        lpc=Label(main,text="Confirm Password")
        self.lpc=Entry(main,width=30,show="%")
        lpc.pack()
        self.lpc.pack()
        lp.pack()
        self.password.pack()
        button=Button(main,bg="green",text="Add",fg="white",command=self.addUser)
        button.pack()
        main.pack()
        self.bor.mainloop()
    #* add delete,insert funtionalities
    def addUser(self):
        uname=self.user.get()
        contact=self.con.get()
        password=self.password.get()
        lcon=self.lpc.get()
        if(lcon==password):
            if(len(uname)!=0 and len(contact)!=0 and len(password)!=0):
                l=LibRecords()
                r=l.addUser(uname,contact,password)
                if(r==True):
                    tkMessageBox.showinfo("Sucess","User "+uname+" has been added sucessfully")
                elif(r=="Exist"):
                    tkMessageBox.showinfo("Existing user","There is a user already existing by the details\n"+uname+"\n"+contact)
                else:
                    tkMessageBox.showerror("Error ","Error in adding the user "+uname+"\nplease contact the system admin")
            else:
                tkMessageBox.showerror("Empty Fields","Please Fill in all the Fields")
        else:
            tkMessageBox.showwarning("Unmatching passwords","The passwords do not match \n Please Enter matching passwords")
    def deleteUser(self):
        a=self.borrowedList.curselection();details=[];b="";
        d=self.borrowedList.get(a)
        for i in d:
            if(i!=" " and i!="\n"):
                b+=i
            else:
                details+=[b]
                b=""
        details+=[b]
        l=LibRecords()
        r=l.deleteUser(details[0],details[1])
        if(r==True):
            tkMessageBox.showinfo("Success","User "+details[0]+" deleted sucessfully")
        elif(r=="None"):
            tkMessageBox.showerror("Error","No user by the name\n"+details[0]+"\n and contact\n"+details[1])
        elif(r=="Many"):
            tkMessageBox.showerror("Many Users by the name \n"+details[0]+"\nand Contact\n"+details[1])
        else:
            tkMessageBox.showerror("Error","Please Contact the system admin")
    def bookRecords(self):
        bGui=Tk()
        bGui.title("Book Records")
        mFrame=Frame(bGui)
        self.bookList=Listbox(mFrame,width=70)
        bList=[];i=0;
        l=LibRecords()
        r=l.displayInventory()
        for item in r:
            self.bookList.insert(i,item)
            i+=1
        self.bookList.pack()
        delete=Button(bGui,text="Delete Book",bg="red",fg="white",command=self.deleteBook)
        delete.pack()
        addBookF=Frame(mFrame)
        task=Label(addBookF,text="Add A Book",fg="red")
        task.pack()
        self.bookname=Entry(addBookF,width=30);l1=Label(addBookF,text="Book Name");
        self.author=Entry(addBookF,width=30);l2=Label(addBookF,text="Author");
        self.category=Entry(addBookF,width=30);l3=Label(addBookF,text="Category");
        self.copiesbought=Entry(addBookF,width=30);l4=Label(addBookF,text="Copies");
        l1.pack();self.bookname.pack();
        l2.pack();self.author.pack();
        l3.pack();self.category.pack();
        l4.pack();self.copiesbought.pack();
        add=Button(addBookF,text="Add",fg="white",bg="green",command=self.addBook)
        add.pack()
        addBookF.pack()
        mFrame.pack()
        bGui.mainloop()
    def addBook(self):
        bookName=self.bookname.get()
        author=self.author.get()
        category=self.category.get()
        copies=self.copiesbought.get()
        if(len(bookName)<1 or len(author)<1 or len(category)<1 or len(copies)<1):
            tkMessageBox.showwarning("Missing details","Please Fill in all the details")
        else:
            l=LibRecords()
            r=l.addBook(bookName,author,category,copies)
            if(r==True):
                tkMessageBox.showinfo("Sucess","Sucessfully added the book "+bookName)
            else:
                tkMessageBox.showerror("Error","Please Contact your system administrator")
    def deleteBook(self):
        self.confirm=Tk()
        l=Label(self.confirm,text="Administrator Password");
        l1=Label(self.confirm,text="Administrator Name");
        l1.pack()
        self.name=Entry(self.confirm,width=30)
        self.name.pack()
        l.pack()
        self.password=Entry(self.confirm,width=30)
        self.password.pack()
        b1=Button(self.confirm,text="Enter",command=self.execute)
        b1.pack()
        #a=self.bookList.curselection()
        #print self.bookList.get(a)
        self.confirm.mainloop()
    def execute(self):
        name=self.name.get();
        password=self.password.get();
        l=LibRecords()
        r=l.adminDetails(name,password)
        if(r==True):
            a=self.bookList.curselection()
            j=self.bookList.get(a)
            print j[0]
            deleteBook(bookname,author,category,copies)
            self.confirm.destroy()
        else:
            tkMessageBox.showerror("Access Denied","Please Enter the correct Admin Details")
g=Gui()
