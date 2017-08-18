#!/usr/bin/python
#V1

def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return text == reverse(text)

my_str = raw_input('Enter text:')

if is_palindrome(my_str.lower()):
    print my_str, "is PALINDROME"
else:
    print my_str, 'is NOT A PALINDROME'

#V2
