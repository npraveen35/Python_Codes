#!/usr/bin/python
# V1 checks for word

def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return text == reverse(text)

my_str = raw_input('Enter text:')

if is_palindrome(my_str.lower()):
    print my_str, "is PALINDROME"
else:
    print my_str, 'is NOT A PALINDROME'

# V2 check the statement
text = "Rise to vote, sir."
original_text=''.join(t for t in text if t.isalnum()) # joins the each character continuously eliminating special char
#print original_text

def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return text == text[::-1]

if is_palindrome(original_text.lower()):
    print 'Yes, its palindrome'
else:
    print 'No, its not palindrome'
