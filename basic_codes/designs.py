#!/usr/bin/python

n = int(input("Enter number of rows:"))
p = m = n

print '-'* 35
print " DESIGN 1 "
print '-'* 35

while n >= 1:
    print '*' * n
    n -=1


print '-'* 35
print " DESIGN 2 "
print '-'* 35
i = 1
while i <= m:
    print '*' * i
    i +=1

print '-'* 35
print " DESIGN 3 "
print '-'* 35
r = p
while r >= 1:
    rows = '*' * r
    spaces = ' ' * (p-r) 
    print spaces, rows
    r -=1

z = 1
while z <= m:
    rows = '*' * z
    spaces = ' ' * (m -z)
    print spaces, rows
    z +=1

'''
Enter number of rows:10
-----------------------------------
 DESIGN 1
-----------------------------------
**********
*********
********
*******
******
*****
****
***
**
*
-----------------------------------
 DESIGN 2
-----------------------------------
*
**
***
****
*****
******
*******
********
*********
**********
-----------------------------------
 DESIGN 3
-----------------------------------
 **********
  *********
   ********
    *******
     ******
      *****
       ****
        ***
         **
          *
          *
         **
        ***
       ****
      *****
     ******
    *******
   ********
  *********
 **********
'''

# V2 SIMPLE AND COMPACT CODE FOR PATTERNS
#!/usr/bin/python

def pascalTriangle(n):
    # LEFT INDENTED TRIANGLES
    # ActualTriangle
    print('\n{0:*^16}\n'.format('Pattern1'))
    for i in range(1,n+1):
        print '*' * i

    print('\n{0:*^16}\n'.format('Pattern2'))
    # InvertedTriangle
    for i in range(n,0,-1):
        print '*' * i

    # RIGHT INDENTED TRIANGLES
    # ActualTriangle
    print('\n{0:*^16}\n'.format('Pattern3'))
    for i in range(1, n+1):
        x = ' ' * (n-i)
        y = '*' * i
        print x + y

    # InvertedTriangle
    print('\n{0:*^16}\n'.format('Pattern4'))
    for i in range(n, 0, -1):
        x = ' ' * (n-i)
        y = '*' * i
        print x + y

pascalTriangle(6)

[praveen@myworld python_works]$ python pascalTriangle.py

****Pattern1****

*
**
***
****
*****
******

****Pattern2****

******
*****
****
***
**
*

****Pattern3****

     *
    **
   ***
  ****
 *****
******

****Pattern4****

******
 *****
  ****
   ***
    **
     *
