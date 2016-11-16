#!/usr/bin/python

m = n = 10
print '*' * 50 #string will be printed n many times.
for i in range(1, m+1):
    for j in range(1, n+1):
        print "%4d" %(j*i),  #1
    print ''                 #2 
print '*' * 50

'''
Output resembles as below:
**************************************************
   1    2    3    4    5    6    7    8    9   10
   2    4    6    8   10   12   14   16   18   20
   3    6    9   12   15   18   21   24   27   30
   4    8   12   16   20   24   28   32   36   40
   5   10   15   20   25   30   35   40   45   50
   6   12   18   24   30   36   42   48   54   60
   7   14   21   28   35   42   49   56   63   70
   8   16   24   32   40   48   56   64   72   80
   9   18   27   36   45   54   63   72   81   90
  10   20   30   40   50   60   70   80   90  100
**************************************************

NOTE: In Python 3, print statements changes as below:
1. print("%4d" % (i * n), end=' ')
2. print()

In print function call if you pass another argument called end and pass a space string, 
it will print in the same line with space delimiter. The default value for end is 'n'.
'''
