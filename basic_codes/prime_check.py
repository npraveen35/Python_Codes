#!/usr/bin/python
n = int(raw_input('enter your number:'))
i = 2
if (n == 1) | (n == 0):
    print n,'is not PRIME\n'

else:
    while i <= n-1:
        if n % i == 0:
            print "NOT A PRIME." #COMPOSITE NUMBER
            exit()
        i=i+1
    print 'Number is PRIME'
