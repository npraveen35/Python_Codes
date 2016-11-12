#!/usr/bin/python
#V1
'''
num = int(raw_input('enter a number:'))
f=1
for i in range(1, num+1):
    f *=i
print "Factorial of %d is %d" %(num,f)
'''

#V2

def fact (n):
    if n==0:
        return 1
    else:
        return (n*fact(n-1))
num = int(raw_input('enter a number:'))
print "Factorial is ", fact(num)
