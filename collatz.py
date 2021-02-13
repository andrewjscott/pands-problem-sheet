# Asks the user to input a positive integer. If the integer is even it is divided by two and if it is odd the 
# number is multiplied by 3 and one is added to it. value of this calculation is an output and the calculation
# is repeated on the new value until the number is 1, whereupon the program will end

# Author: Andrew Scott

#Tells the user to enter a positive integers which is stored to a variable called number
number = int(input("Please enter a positive integer: "))
# Returns an error message if the user enters a negative integer and asks them to enter a new integer
if number <= 0: 
    number = int(input("That is not a positive integer. Please enter a positive integer: "))

# Creates a list with the first item in the list being the integer entered by the user
numbers = [number]

# Creates a loop where even numbers are divided by 2 and added to the list, while odd numbers are multiplied by 3 and 1 added
# Loop continues until the value is 1
while number != 1:
    if number % 2 == 0:
        number = int(number / 2)
        numbers.append(number)
    else:
        number = int((number * 3) + 1)
        numbers.append(number)

# Prints the list containing the initial number and all subsequent calculated values
print(numbers)