'''Write a simple program to simulate the operation of the grep command on Unix. 
Ask the user to enter a regular expression and count the number of lines that 
matched the regular expression:
$ python grep.py
'''

import re

count = 0                                                   # variables

user_input = input('Enter a regular expression: ')          #get user input
regex = str(user_input)
fname = 'mbox-short.txt'
fhand = open(fname)

for line in fhand:
    line = line.rstrip()

    if re.findall(regex, line) != []:
        count +=1
print(fname, ' has ', str(count))