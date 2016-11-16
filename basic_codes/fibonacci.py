#!/usr/bin/python
#V1 Displays the first n elements of fibonacci series

def fib(n):
    a,b=0,1
    i =1
    while i<=n:
        print a,
        a,b=b,a+b
        i+=1

n = input('enter number:')
fib(n)


#V2 Displays the fibonacci numbers within limit
'''
def fibon(lim):
    a, b = 0, 1
    while b <=lim:
        print (b)
        a,b = b,a+b

n = input('enter number:')
fibon(n)
'''
