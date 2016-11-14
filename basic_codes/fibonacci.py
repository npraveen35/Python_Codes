#!/usr/bin/python
#V1
def fib(n):
    a,b=0,1
    i =1
    while i<=n:
        print a,
        a,b=b,a+b
        i+=1

n = input('enter number:')
fib(n)
