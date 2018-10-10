import MySQLdb,datetime
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
    def addUser(self):
        #athenticate(usercontact,password);
        try:
            cursor=self.db.cursor()
            sql="INSERT INTO users (name,contact,password,account) VALUES ('antony','0704273214','antonykaigi',1000)";
            cursor.execute(sql);
            self.db.commit()
            print("User added successfully");
        except ():
            print "Error adding the user";
    #2.Deleting a users params (contact)
    def deleteUser(self):
        try:
            cursor=self.db.cursor()
            sql="DELETE FROM users where contact='0704273214'"
            cursor.execute(sql)
            self.db.commit()
            print "User deleted successfully"
        except():
            print "Error in deleting user"


    #----------------------------------book management --------------------------------------------
    #1.Adding new books params(id,bookname,author,category,copiesbought,copiesavailable)
    def addBook(self):
        try:
            cursor=self.db.cursor()
            sql="INSERT INTO Inventory (id,bookname,author,category,copiesbought,copiesavailable) VALUES('james','Fall','johnny','Romance',1,1)"
            cursor.execute(sql);
            self.db.commit()
            print "Book added successfully"
        except():
            print "Book Not added"
    #2.Deleting books
    def deleteBook(self):
        try:
            cursor=self.db.cursor()
            sql="DELETE FROM Inventory where id='awfA'"
            cursor.execute(sql)
            self.db.commit()
            print "Book deleted successfully"
        except():
            print "Error in deleting Book"


    #--------------------------------Borrowing management----------------------------------------
    #1.borrowing books params(idofthebook,userscontact,password,dateborrowed,state)
    def borrow(self):
        #athenticate(usercontact,password);
        try:
            #getting the number of coppies of available books to check if the book is available
            cursor=self.db.cursor()
            sql1="SELECT CopiesAvailable FROM Inventory WHERE id='james'"
            cursor.execute(sql1);
            p_available=cursor.fetchall()
            #check if the books are available at the time if not available notify the user he/she cannot borrow them
            if(p_available[0][0]!=0):

                #getting the current date
                d=datetime.datetime.now();
                date=str(d.year)+"-"+str(d.month)+"-"+str(d.day);
                cursor=self.db.cursor()
                #adding the record of the borrowed book to table BorrowedBooks
                sql="INSERT INTO BorrowedBooks (id,name,dateborrowed,state) VALUES('james','antony','%s','False')"%(date);
                cursor.execute(sql);
                self.db.commit()

                available=p_available[0][0]-1;
                sql2="UPDATE Inventory set CopiesAvailable=%d"%(available);
                cursor.execute(sql2);
                self.db.commit()
            else:
                print "The book is not available at this time"
        except():
            print "Error Borrowing Book"

    #2.returnig the book params (bookid,username,password,dateofreturn)
    def BookReturn(self):
            #athenticate(usercontact,password);
        try:
            sql="SELECT * FROM BorrowedBooks where id='jkshdf'"
            cursor=self.db.cursor();
            cursor.execute(sql);
            r=cursor.fetchall()
            if(len(r)!=0):
                print "Yes the record exist"
            else:
                print "There is no borrowed book by such details"
        except():
            print "Error returnig Book"


l=LibRecords();
#l.addUser();
#l.deleteUser();
#l.addBook();
#l.deleteBook();
#l.borrow()
#l.BookReturn()
