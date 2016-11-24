#!/usr/bin/env python

# In this example , you have to take number of students as input , then ask marks for three subjects
# as 'Physics', 'Maths', 'History', if the total marks for any student is less 120 then print he failed,
# or else say passed.


# NUMBER OF STUDENTS
no_stud = input("Enter number of students:")

students = [] # list of students

marks = {} # dict of {student_name: total marks}

subjects = ["Physics", "Maths", "History"]

for n_s in range(1, no_stud+1):
    total = 0 # total marks of all subjects 
    stud_name=str(raw_input ("\nEnter name of Student%d:" % n_s))
    students.append(stud_name)
    print "\n For %s student \n" % stud_name
    for s in subjects:
        total += int(input("Enter marks for %s:" % s ) )
    marks[stud_name] = total

print '\n'
for key, val in marks.iteritems():
    if val < 120:
        print "%s Fail :( Total Marks scored = %d" %(key,val)

    else:
        print "%s Pass :) Total Marks scored = %d" %(key,val)
