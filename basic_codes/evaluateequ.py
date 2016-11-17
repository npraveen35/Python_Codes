#!/usr/bin/python

# This code evaluates 1/x + 1/(x+1) + 1/(x+2).....+ 1/n
x = 1
n = 10
s = 0.0
while x <= n:
    s += (1.0/x)
    x +=1

print ("sum of series is %.4f" % s)

# Given below is the Output:
# sum of series is 2.9290

