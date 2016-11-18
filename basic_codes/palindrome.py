#!/usr/bin/python
#V1
str = raw_input('Enter your string:')

def palindrome_check(my_str):
    rev_str = my_str[::-1]
    if my_str == rev_str:
        print my_str, "is PALINDROME"
    else:
        print my_str, 'is NOT A PALINDROME'

palindrome_check(str)

#V2
'''
def palindrome(str):
    return str == str[::-1]
'''
