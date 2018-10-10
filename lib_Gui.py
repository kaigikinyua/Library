from Tkinter import *
class Gui():
    def __init__(self):
        root=Tk()
        root.title("Library Management System ")
        frame=Frame(root)
        l=Label(frame,text="Username")
        self.username=Entry(frame,width=30)
        l1=Label(frame,text="Password")
        self.password=Entry(frame,width=30)
        button=Button(frame,text="Login",background="green",command=self.login)
        l.pack()
        self.username.pack()
        l1.pack()
        self.password.pack()
        button.pack()
        frame.pack()
        root.mainloop()
    def login(self):
        uname=self.username.get()
        password=self.password.get()
        
g=Gui()
