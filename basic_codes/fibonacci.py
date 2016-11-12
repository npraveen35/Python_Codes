#!/usr/bin/python
#V1

n = input('enter number:')
a,b=0,1
i =1
while i<=n:
    print a,
    a,b=b,a+b
    i+=1
