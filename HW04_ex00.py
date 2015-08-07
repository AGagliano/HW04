#!/usr/bin/env python
# HW04_ex00

# Create a program that does the following:
#     - creates a random integer from 1 - 25
#     - asks the user to guess what the number is
#     - validates input is a number
#     - tells the user if they guess correctly
#         - if not: tells them too high/low
#     - only lets the user guess five times
#         - then ends the program
################################################################################
# Imports

import random

# Body

#Chooses a random integer between 1 and 25, inclusive of 1 and 25
r = random.randint(1, 25) 	

#Allows user 5 attempts to guess the random number.
for n in range(5):	
	#Asks user to guess a number
	g = raw_input('Take a gander at a number somewhere between 1 and 25:\n')
	#Tries to convert the string g to an integer, yells at user if input was not an integer.
	try:
		g = int(g)
	except ValueError:
		print ('Just an integer...make it easy on yourself!')
	#Tests if user guessed the random number, and gives hints suggesting higher or lower guesses if they didn't.
	else: 
		if g == r:
			print 'Yay you nailed it!'
			break				#breaks from for loop when user succeeds
		elif g < r:
			print "Hint: reach for the sky"
		else:
			print "Hint: reach for the ground"
else:
	print "Sorry, but we only let you test your luck 5 times!"


################################################################################
def main():


    print("Hello World!") # Remove this and replace with your function calls
    

if __name__ == '__main__':
    main()