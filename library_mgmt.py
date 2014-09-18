Student_list = ['StudentlistRecords(USN, Student name,Branch,semester)',155069,'Pravin','EC',4 , 155072,'Sahna','CS',4]
class Student_Record(object):

	def __init__(self):
		print"Welcome!! Library Management System"

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
		Student_list.extend((a,b,c,d))

	def  Display_studentlist(self):
		 for i in range(len(Student_list)):
			print Student_list[i]
		 print "\n"	

mylistb = ['Bookslist(Book no. Book name, Author name)',1,'Java  Balagurusamy',2,'Python  HeadFirst',3,'Cpp Comer']
class Book:
	   
	def create_book(self,number,book_name_aut):
		 mylistb.extend((number,book_name_aut))    
				
	def Display_Books(self):
	 	j=len(mylistb)
	 	for index in range(j):
	 	    print mylistb[index]	
	 	print '\n'

print "//**********************************//"
s1 = Student_Record()
b1 = Book()
print "\nMAIN MENU:\n"
#print "1.Admin\n2.Student\n3.Exit"
while True:
		print "\n1.Admin\n2.Student\n3.Exit"
		n=raw_input("Enter your choice:")
		if n == '1':
				print "ADMIN MENU"
				admin = raw_input("enter username:")
				password = raw_input("\nenter password:")
				if admin!='Admin' or password!='Admin':
   	    				print "Unauthorised Access!"
       					exit()
	
				else:
			 			while True:
	   							print "\nAdmin Particulars\n1.Display Student list\n2.View Book Details\n3.Delete Student Record\n4.Add Books\n5.Exit\n"
 	 							m=raw_input("enter your choice:")
 	  							if m == '1':
 			 							s1.Display_studentlist()

 			 					elif m =='2':
 			 							b1.Display_Books()


 			 					elif m =='3':
 										j = input('enter usn of student to be removed:')
 										p = Student_list.index(j)
 										for indx in range (0,4):
 												Student_list.pop(p)
  										print"Record deleted"	
				

  								elif m =='4':
  									    number = input('\nenter book no.:')
  									    book_name_aut = raw_input("Enter book name and author name(in a single line): ")
  									    b1.create_book(number, book_name_aut)

  								else:
  								    	break	    


		elif n =='2': 			     	    	
	    		print "***Student MENU***"
	    		s1.Student_details()
	    		b1.Display_Books()
	    		number=input('Select any 1 book  from the above list\n enter the book number:')
	    		num = mylistb.index(number)
	    		print "Book issued is:" 
	    		print (mylistb[num],mylistb[num+1])
	    		for i in range(0,2):
	 					mylistb.remove(mylistb[num])
 	     	     	
 		else:
     			exit()   	











