#!/usr/bin/env python3
#v1 COUNTS NUMBER OF WORDS IN A SENTENCE:
def count_words(str):
    return len(str.split(' ')) #splits the str with space & creates list

sentence = "An Apple a day keeps a Doctor away !!"
print (count_words(sentence)) #Output is 9
