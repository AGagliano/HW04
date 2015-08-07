#!/usr/bin/env python
# HW04_ex08_05

# The following program counts the number of times the letter a appears in a 
# string:

#     word = 'banana'
#     count = 0
#     for letter in word:
#         if letter == 'a':
#             count = count + 1
#     print count

# Encapsulate this code in a function named "count", and generalize it so that 
# it accepts the string and the letter as arguments.

################################################################################
# Imports


# Body

#Counts the number of times a letter (l) appears in a string (s).
def count(s, l):
	count = 0
	for char in s:
		if char == l:
			count += 1
	print count 


################################################################################
def main():

    count('strawberry', 'r')
    count('pants', 'z')
    count('Ischool', 'i')
    

if __name__ == '__main__':
    main()