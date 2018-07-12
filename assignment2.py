# Assignment 2

'''

Libraries and Functions always come in handy to developers by allowing reusability of existing code. 
There are certain well known inherent libraries that you have access to after installing python. By 
using these libraries and functions in them, write a program (in Python 3) to guess a randomly generated 
number between 1 and 10.

For Example: 

Guess the number: 4
Wrong, try again! 

Guess the number: 8
Correct! 

Hint: Figure out which library the "randint" function belongs to.

'''

# Solution to Assignment 2

import random

random_1to10 = random.randint(1, 10)
# print('Generated random number is ',random_1to10)

while True:
    if (int(input('Guess the number: ')) == random_1to10):
        print('Correct!'),
        break
    else:
        print('Wrong, try again!\n')
