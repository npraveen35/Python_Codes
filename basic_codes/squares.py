#!/usr/bin/python
# Reads number from user and prints the perfect squares within the limit.
# V1
'''
def squares(limit):
    for i in range(1,limit):
        i = i ** 2
        if i < limit: # NOTE:Without if, output will reach upto square of (limit-1)
            print (i)

N=int(input("Enter Number:"))
squares(N)
'''

'''
# V2 Using Lambda,Map,Filter function

N=int(input("Enter Number:"))

sq = lambda i: i**2 # square function
pr_sq = map(sq, range(1,N+1)) # list of perfect squares
my_list = filter(lambda x: x <= N, pr_sq)  # get a list of perfect squares within the limit
print my_list
'''

# V3 - Optmised code of V2 

N=int(input("Enter Number:"))

pr_sq = map(lambda i: i**2, range(1,N+1))
#print pr_sq # prints square of 1 upto square of N
#my_list_sq = filter(lambda i: i < N, pr_sq)
#print my_list_sq
print (list(filter(lambda i: i <= N, pr_sq)))
