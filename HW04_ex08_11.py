#!/usr/bin/env python
# HW04_ex08_11

# The following functions are all intended to check whether a string contains 
# any lowercase letters, but at least some of them are wrong. For each function, 
# describe what the function actually does (assuming that the parameter is a
# string).

# Do not merely paste the output as a counterexample into the documentation 
# string, explain what is wrong.

################################################################################
# Body

def any_lowercase1(s):
    """The function tests if the first character in the string is lower case or not. 
    Since True or False is returned in both if/else cases, only the 
    first character in the string is tested, as opposed to all the characters.
    """
    for c in s:
        if c.islower():
            return True
        else:
            return False

def any_lowercase2(s):
    """The if statement tests if the string 'c' is lowercase, which is always true. 
    The function should instead test the character c (indexed character within the string s).
    """
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

def any_lowercase3(s):
    """The function will loop through all the characters c in s, and will
    ony return whether or not the last character is lower case or not, 
    because the return is after the for loop.
    """
    for c in s:
        flag = c.islower()
    return flag

def any_lowercase4(s):
    """Nothing is wrong. If a character is lowercase, flag will update to True, 
    and will remain True throughout the remainder of the for loop. 
    """
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

def any_lowercase5(s):
    """The function checks through all charcters in s and returns False upon the 
    first instance of an uppercase letter, as opposed to checking through all 
    the letters.
    """
    for c in s:
        if not c.islower():
            return False
    return True

################################################################################
def main():

    print any_lowercase1('Blueberry')
    print any_lowercase2('CHIP')
    print any_lowercase3('chocolatE')
    print any_lowercase4('IT WORKS')
    print any_lowercase5('piTa')

if __name__ == '__main__':
    main()