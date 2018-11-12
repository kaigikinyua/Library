import MySQLdb,datetime,random
class LibRecords:
    #---------------------------database Connection----------------------------------
#constructor that connects to the database
    def __init__(self):
        try:
            self.db=MySQLdb.connect("localhost","root","root","Library")
            print "Connection success"
        except():
            print "Error connecting to the database"

    #-------------------------------user management--------------------------------
    #1.adding a new user params(username,contact,password,accountbalance)
    def dispalyUsers(self):
        cursor=self.db.cursor()
        sql="SELECT * FROM users"
        cursor.execute(sql)
        r=cursor.fetchall()
        return r
    def addUser(self,uname,contact,password):
        #athenticate(usercontact,password);
        try:
            cursor=self.db.cursor()
            sql0="SELECT * FROM users where contact='%s'"%(contact)
            cursor.execute(sql0)
            r=cursor.fetchall()
            if(len(r)==0):
                sql="INSERT INTO users (name,contact,password,account) VALUES ('%s','%s','%s',1000)"%(uname,contact,password);
                cursor.execute(sql);
                self.db.commit()
                return True
            else:
                return "Exist"
        except ():
            return False
    #2.Deleting a users params (contact)
    def deleteUser(self,uname,contact):
        try:
            cursor=self.db.cursor()
            sql0="SELECT * FROM users where name='%s' and contact='%s'"%(uname,contact)
            cursor.execute(sql0)
            r=cursor.fetchall()
            if(len(r)>1):
                return "Many"
            elif(len(r)==0):
                return "None"
            else:
                sql="DELETE FROM users where name='%s' and contact='%s'"%(uname,contact)
                cursor.execute(sql)
                self.db.commit()
                return True
        except():
            return False


#----------------------------------book management --------------------------------------------
    #1.Adding new books params(id,bookname,author,category,copiesbought,copiesavailable)
    def addBook(self,bookname,author,category,copies):
        try:
            cursor=self.db.cursor()
            rand=random.randint(1,1000000)
            check="SELECT * FROM Inventory WHERE id='%s'"%(rand)
            cursor.execute(check)
            r=cursor.fetchall()
            while (len(r)>0):
                cursor=self.db.cursor()
                rand=random.randint(1,1000000)
                check="SELECT * FROM Inventory WHERE id='%s'"%(rand)
                cursor.execute(check)
                r=cursor.fetchall()
                if(len(r)==0):
                    break;
            sql="INSERT INTO Inventory (id,bookname,author,category,copiesbought,copiesavailable) VALUES('%s','%s','%s','%s',%d,%d)"%(str(rand),bookname,author,category,int(copies),int(copies))
            cursor.execute(sql);
            self.db.commit()
            return True
        except():
            return False
    #2.Deleting books
#little logical bug-------------------
    #delete a certain book from the database
    def deleteBook(self,id,bookname,author,category):
        try:
            cursor=self.db.cursor()
            check="SELECT Copiesbought,CopiesAvailable from Inventory where id='%s'"%(id)
            cursor.execute(check)
            r=cursor.fetchall()
            if(r[0][0]==r[0][1] and len(r)==1):
                sql="DELETE FROM Inventory where id='%s'"%(id)
                cursor.execute(sql)
                self.db.commit()
                return True
            elif(len(r)>1):
                return "Id"
            elif(len(r)==0):
                return "No Book"
            elif(r[0][0]!=r[0][1]):
                return "Borrowed"
            else:
                return "Error"
        except():
            return False
    #displaying all the books
    def displayBooks(self):
        cursor=self.db.cursor()
        sql="SELECT * FROM Inventory where CopiesAvailable>1"
        cursor.execute(sql)
        r=cursor.fetchall()
        return r

    def displayInventory(self):
        cursor=self.db.cursor()
        sql="SELECT * FROM Inventory"
        cursor.execute(sql)
        r=cursor.fetchall()
        return r

    def displayBorrowed(self):
        cursor=self.db.cursor()
        sql="SELECT * FROM BorrowedBooks where state=False";
        cursor.execute(sql)
        r=cursor.fetchall()
        if(len(r)!=0):
            return r
        else:
            return False
    #--------------------------------Borrowing management----------------------------------------
    #1.borrowing books params(idofthebook,userscontact,password,dateborrowed,state)
    def borrow(self,id,contact):
        #athenticate(usercontact,password);
        try:
            #getting the number of coppies of available books to check if the book is available
            cursor=self.db.cursor()
            sqlC="SELECT * from users where contact='%s'"%(contact)
            cursor.execute(sqlC)
            r=cursor.fetchall()
            sqlL="SELECT * from BorrowedBooks where name='%s' and state='False'"%(contact)
            cursor.execute(sqlL)
            l=cursor.fetchall()
            if(len(r)==1 and len(l)<3):
                sql1="SELECT CopiesAvailable FROM Inventory WHERE id='%s'"%(id)
                cursor.execute(sql1);
                p_available=cursor.fetchall()
                #check if the books are available at the time if not available notify the user he/she cannot borrow them
                if(p_available[0][0]!=0):
                    #getting the current date
                    d=datetime.datetime.now();
                    date=str(d.year)+"-"+str(d.month)+"-"+str(d.day);
                    cursor=self.db.cursor()
                    #adding the record of the borrowed book to table BorrowedBooks
                    sql="INSERT INTO BorrowedBooks (id,name,dateborrowed,state) VALUES('%s','%s','%s','False')"%(id,contact,date);
                    cursor.execute(sql);
                    self.db.commit()

                    available=p_available[0][0]-1;
                    sql2="UPDATE Inventory set CopiesAvailable=%d where id='%s'"%(available,id);
                    cursor.execute(sql2);
                    self.db.commit()
                    return True
                else:
                    return "Not available"
            elif(len(r)==0):
                return "No"
            elif(len(r)>1):
                return "Many"
            elif(len(l)>=3):
                return "Limit"
            else:
                False
        except():
            return False

    #2.returnig the book params (bookid,username,password,dateofreturn)
    def BookReturn(self,bookid,contact):
            #athenticate(usercontact,password);
        try:
            sql="SELECT * FROM BorrowedBooks where id='%s' and name='%s'"%(bookid,contact)
            cursor=self.db.cursor();
            cursor.execute(sql);
            r=cursor.fetchall()
            if(len(r)==1):
                Return=datetime.datetime.now()
                dReturn=datetime.date(Return.year,Return.month,Return.day)
            
                sql1="UPDATE BorrowedBooks set state='True' where id='%s' and name='%s'"%(bookid,contact)
                cursor.execute(sql1)
                self.db.commit()
                sql2="SELECT CopiesAvailable FROM Inventory where id='%s'"%(bookid)
                cursor.execute(sql2)
                c=cursor.fetchall()
                d=c[0][0]+1
                print c[0][0]
                #patch for checking copiesavailable !> than copiesbought
                sql3="UPDATE Inventory set CopiesAvailable=%d where id='%s'"%(d,bookid)
                cursor.execute(sql3)
                self.db.commit()
                if(dReturn>(r[0][2]+datetime.timedelta(days=3))):
                    return "Penalty "+str(dReturn-(r[0][2]+datetime.timedelta(days=3)))
                return True
            elif(len(r)>1):
                return "Too many records"
            else:
                return "No record"
        except():
            return False
#--------------------------admin---------------------------------------------
    #login for admin params(name,password)
    def adminDetails(self,name,password):
        cursor=self.db.cursor()
        #sequrity breach add password to query
        sql="SELECT * FROM admin where admin_name='%s'"%(name);
        cursor.execute(sql)
        r=cursor.fetchall()
        if(len(r)==1):
            return True
        else:
            return False
#-------sequrity patches -----
    #patch for borrowing books
    #def s_borrow(self):
#l=LibRecords();
#l.addUser();
#l.deleteUser();
#l.addBook();
#l.deleteBook();
#l.borrow()
#l.BookReturn()
