# Structure this script entirely on your own.
# See Chapter 8: Strings Exercise 12 for guidance
# Please do provide function calls that test/demonstrate your function

#Inputs

def rotate_word(s, int):
	"""Returns and encrypted string by rotating the letters of the original string (s) by a set integer (int). 

	Rotating the letters means to shift each letter through the alphabet, wrapping 
	around to the beginning if necessary. For example, 'A' is shifted by 3 to 'D'.
	"""
	s_encrypt = ''
	int = int%26										#Forces high and negative int numbers to be between 0 and 26								

	for char in s:
		char_value = ord(char)							#Isolate single character and find its int value.
		char_value_encrypt = char_value + int 			#Rotate the int value to encrypte it.

		#Forces encrypting by looping through the alphabet 
		if char_value > 96 and char_value < 123:		#Uppercase letters
			if char_value_encrypt > 122:
				char_value_encrypt = 96 + char_value_encrypt - 122
		elif char_value > 64 and char_value < 91:		#Lowercase letters
			if char_value_encrypt > 90:
				char_value_encrypt = 64 + char_value_encrypt - 90

		char_encrypt = chr(char_value_encrypt)			#Convert int value back to character.
		s_encrypt = s_encrypt + char_encrypt			#Re-combine charcter to encrypted word.
	return s_encrypt

def main():
	print rotate_word('cheer', 7) 	#jolly
	print rotate_word('melon', -10) #cubed

if __name__ == '__main__':
	main()