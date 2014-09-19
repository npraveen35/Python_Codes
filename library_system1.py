import MySQLdb

class connect_database():
	
	def __init__(self):
		db = MySQLdb.connect("localhost","root","1CLOUD","Librarysystem_project" )
		cursor = db.cursor()

	def connection(sql):
		cursor.execute(sql)
		db.commit()
		db.close()

studentdetails_list = [ ]
class student (connect_database):

	def Student_details(self):
		print " Please enter your curiculum details below\n"
		b=raw_input("Enter your name :")
		print ("your name is " +b)
		a=raw_input("Enter your USN :")
		print ("Your USN is",int(a))
		c=raw_input("Enter your branch :")		
		print ("your  baranch is " +c)
		d=raw_input("Enter your current semester :")
		print ("you are in the semester",int(d))
		studentdetails_list.extend((a,b,c,d))

	def add_student(studentdetails_list):
		sql1 = """INSERT INTO Students_list(USN,Student_name,Branch,Sem )VALUES (studentdetails_list)"""

	def  Display_studentlist(self):
		sql1 = """SELECT *FROM	Students_list """
		
        
bookdetails_list = [ ]
class book (connect_database):
	
	def create_book(self):
		number = raw_input("enter Bookno:")
		book_name = raw_input("enter Book_name:")
		author_name = raw_input("enter author_name")
		bookdetails_list.extend((number,book_name,author_name))

	def add_book(bookdetails_list):
		sql1 ="""INSERT INTO Booklist(USN,Student_name,Branch,Sem ) VALUES (bookdetails_list) """	  
				
	def Display_Books(self):
		sql1 = """SELECT *FROM Booklist """ 
		
