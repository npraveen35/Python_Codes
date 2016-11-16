#!/usr/bin/python

# Evaluate POWER SERIES: e**x = 1 + x + x**2/2! + x**3/3! +....+ x**n/n! and 0<x<1
x = input("Enter the value of x(0<x<1):")
n = 100
sum = 1.0
i = 1
term = 0.0

# Factorial
def fact(n):
    if n == 0:
        return 1
    else:
        return (n*fact(n-1))

# pow(x,i) and fact(i)
while i <= n:
    term = pow(x,i)/fact(i)
    sum += term
    i +=1

print sum
