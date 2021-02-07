# Asks the user to input a string, and returns outputs every second letter in reverse order
# Author: Andrew Scott

"""

First the user is asked to input a string which is stored to a variable
Each character in a string has a corresponding numberical value, with the first character 0, second character 1, etc
Slicing a string is done by using square brackets followed by the number corresponding to the 
start point, end point, and steps of the slicing with each number seperated by colons
ie [slicing start point:slicing end point:steps taken while slicing]
If the slicing start and end points are left blank, python assumes these values to correspond to the beginning and end of the string
If the steps is left out copletely pythons continues with steps as a value of 1 by default
A minus value for steps means the string is sliced in reverse
So in this code, the values for the start and end point are left blank to include the entire string, while
the steps is set to -2, which starts the slicing in reverse and only insludes every second letter

"""
string = input("Please enter a string: ")
reverseString = string[::-2]

print(reverseString)