# Asks the user to enter a number and the output is an approximation of its square root
# Author: Andrew Scott

# A function that calculates the square root via the Newton Raphson method
# The variable t is the tolerance level. This means the program will loop until the current answer 
# minus the previous answer is within the tolerance level. Abs is used so the answer being plus or minus
# isn't important as long as it's within the tolerance level. 
# When this happens the loop ends and we assume we have found a good approximation of the square root

# The variable g is the initial guess of the square root needed to use in the formula. The formula works by taking the
# initial guess, plugging it in the formula, then replacing the guess with the answer for the next iteration (newG). This repeats 
# until the answers are within the tolerance level. For our purposes the initial guess will be just the number we want to find
# the square root of divided by 2. 

# As per https://hackernoon.com/calculating-the-square-root-of-a-number-using-the-newton-raphson-method-a-how-to-guide-yr4e32zo, 
# # one way of writing the Newton Raphon formula is x_i := (x_i + n / x_i) / 2, where x_i is the initial guess 
# of the square root (the variable g below) and x is the number we want to finf the square root of.

def sqrt(x):
    t = 0.00001
    g = x / 2

    while True:
        newG = (g + (x/g)) / 2
        if abs(g - newG) < t:
            return newG
        g = newG

# Asks the user to enter a positive integer. If they enter something else an error is shown and they are asked to enter again
number = float(input("Please enter a positive number: "))
while number <= 0:
    print("\nYou have not entered a positive number")
    number = float(input("\nPlease enter a positive number: "))

# Calls the function to calculate the squre root of the number the user entered, then in a new variable rounds that answer to 2
# decimal places
root = sqrt(number)
roundRoot = round(root, 2)

# Outputs the number entered by the user and the answer calculated by the function
print("The square root of", number, "is approx.", str(roundRoot))
