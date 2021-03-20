# Reads in a text file and outputs the number of e's that file contains
# Author: Andrew Scott

# The system module imported to allow the user to enter an argument from the command line
import sys

# The filename entered by the user in the command line is read and referenced by the variable filename
# If the file is in the same location as the program, simply enter the filename in the command line 
# when running the code eg $ python numberOfEs.py moby-dick.txt 
# If the filename has spaces, use inverted commas eg $ python es.py "moby dick.txt"
# If the file is in a different location to this program, use the entire path for the file
# eg $ python es.py C:\Users\UserName\Documents\moby-dick.txt

filename = sys.argv[1]

# Function that counts the number of times the letter "e" appears 
def countLetterLower():
    with open(filename) as f:
        importFile = f.read()              # File is imported as a string and stored with the variable importFile
        count = importFile.count("e")      # The count method is used to tally up the number of times e appears
    return count                           # The number of e's found is stored in the variable count and then returned

# As the question was ambiguous as to whether the program should just count lower case e's or both lower and upper,
# I've decided to include a second function that will count upper case E's also
def countLetterUpper():
    with open(filename) as f:
        importFile = f.read()
        count = importFile.count("E")
    return count

# The function to count the number of e's is called and the returned value stored to a new variable as a string
lowerCount = str(countLetterLower())
upperCount = str(countLetterUpper())
total = str(countLetterLower() + countLetterUpper())

# Outputs the number of e's in the entered file
# An if loop used in case the file only contains one e, then the printed sentence is altered to print "time" instead of "times"
if lowerCount == "1" and upperCount == "1":
    print("A lower case 'e' appears", lowerCount, "time, and an upper case 'E' appears", upperCount, "time.")
elif lowerCount == "1":
    print("A lower case 'e' appears", lowerCount, "time, and an upper case 'E' appears", upperCount, "times.")
elif upperCount == "1":
    print("A lower case 'e' appears", lowerCount, "times, and an upper case 'E' appears", upperCount, "time.")
else:
    print("A lower case 'e' appears", lowerCount, "times, and an upper case 'E' appears", upperCount, "times.")

print("This gives a total of", total, "es and Es combined")

