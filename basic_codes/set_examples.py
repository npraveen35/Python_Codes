#!/usr/bin/env python
list1 = [ 1,2,3,4,5,6]
list2 = [1,2,6,8,9,11,23,64]

# Get uncommon elements from the above 2 lists
print (set(list1) ^ set(list2))
# {64, 3, 4, 5, 8, 9, 11, 23}

# Difference l1 - l2 
print (set(list1) - set(list2))
# {3, 4, 5}

# Difference l2 - l1
print (set(list2) - set(list1))
# {64, 8, 9, 11, 23}

# Get Common elements
print (set(list1) & set (list2))
# {1, 2, 6}

# Get Union of all elements removing dups
print (set(list1) | set (list2))
#{64, 1, 2, 3, 4, 5, 6, 8, 9, 11, 23}


