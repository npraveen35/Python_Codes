#!/usr/bin/env python
# Insertion sort is good for collections that are very small
# or nearly sorted. Otherwise it's not a good sorting algorithm.
# it moves data around too much. Each time an insertion is made,
# all elements in a greater position are shifted.
    
#V1 shifting, faster approach
def insertionSort(mylist):
    for i in range(1,len(mylist)): # unsorted portion L -> R
        curnum = mylist[i] # item which we'll move to sorted portion
        j = i
        while (j > 0 and mylist[j-1] > curnum): # this iterates in sorted portion R -> L
            mylist[j] = mylist[j-1]
            j = j -1
        mylist[j] = curnum

'''
#V2 swapping, slower compared to above

def insertionSort(mylist):
    for i in range(1,len(mylist)):
        for j in range (i-1, -1, -1):
            if mylist[j] > mylist[j+1]:
                mylist[j], mylist[j+1] = mylist[j+1], mylist[j]
            else:
                break
'''
a = [4,6,3,49, 8,1]
insertionSort(a)
print a
