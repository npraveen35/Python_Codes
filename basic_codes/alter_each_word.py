#!/usr/bin/python
mystr = raw_input("enter your string:")
# SPLIT THE SENTENCE INTO A LIST OF WORDS
mylist = mystr.split()
print '\n*PIG LATIN SENTENCE*\n'
for word in mylist:
    # ALTER EACH WORD
    altered_str = word[1::] + word[0] + 'AY'
    print altered_str,
    
# EXAMPLE OUTPUT
'''
C:\Python27\python.exe C:/Users/nagegowd/PycharmProjects/PracticeCodes/alter_str_word.py
enter your string:I SLEPT MOST OF THE NIGHT

*PIG LATIN SENTENCE*

IAY LEPTSAY OSTMAY FOAY HETAY IGHTNAY
'''
