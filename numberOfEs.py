# Reads in a text file and outputs the number of e's that file contains
# Author: Andrew Scott

# The system module imported to allow the user to enter an argument from the command line
import sys

# The filename entered by the user in the command line is read and referenced by the variable filename
filename = sys.argv[1]

# Function that counts the number of times the letter "e" appears 
def countLetter():
    with open(filename) as f:
        importFile = f.read()              # File is imported as a string and stored with the variable importFile
        count = importFile.count("e")      # The count method is used to tally up th enumber of times e appears
    return count                           # The number of e's found is stored in the variable count and then returned

# The function to count the number of e's is called and the returned value stored to a new variable
eCount = str(countLetter())

# Outputs the number of e's in the entered file
# An if loop used in case the file only contains one e, then the printed sentence is altered to print "time" instead of "times"
if eCount == 1:
    print("The letter 'e' appears {} time in this file".format(eCount))
else:
    print("The letter 'e' appears {} times in this file".format(eCount))