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
        Inventory=Button(managementFrame,text="Books",bg="red",fg="white")
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
        bor=Tk()
        bor.title("User management")
        main=Frame(bor)
        bor=Frame(main)
        l1=Label(bor,text="Users")
        l1.pack()
        self.borrowedList=Listbox()
        l=LibRecords()
        r=l.dispalyUsers()
        users=[]
        for i in range(len(r)):
            users+=[r[i][0]+" "+r[i][1]+" "+r[i][2]]
        j=0
        for item in users:
            self.borrowedList.insert(j,item)
            j+=1
        self.borrowedList.pack()
        main.pack()
        bor.mainloop()
    #* add delete,insert funtionalities
g=Gui()
