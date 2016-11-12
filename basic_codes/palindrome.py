my_str = raw_input('Enter your string:')
rev_str = my_str[::-1]
if my_str == rev_str:
    print my_str, "is PALINDROME"
else:
    print my_str, 'is NOT A PALINDROME'
