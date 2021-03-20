# Asks the user to enter a number and the output is an approximation of its square root
# Author: Andrew Scott

# A function that calculates the square root via the Babylonian method.
# The variable t is the tolerance level. This means the program will loop until the current answer 
# minus the previous answer is within the tolerance level. Abs is used so the answer being plus or minus
# isn't important as long as it's within the tolerance level. 
# When this happens the loop ends and we assume we have found a good approximation of the square root

# The variable g is the initial guess of the square root needed to use in the formula. The formula works by taking the
# initial guess, plugging it in the formula, then replacing the guess with the answer for the next iteration (newG). This repeats 
# until the answers are within the tolerance level. For our purposes the initial guess will be just the number we want to find
# the square root of divided by 2. 

# While the task suggests using the Newton method for calculating square roots, I found the additional calculus and formulae 
# associated with the method both distracting and overwhelming. This initial research did reveal that the Newton method is closely 
# related to the Babylonian method for calculating square roots, however, and finding this method easier to read and follow
# I used the Babylonian method in this code
# See: https://www.researchgate.net/publication/276498146_The_Hidden_Geometry_of_the_Babylonian_Square_Root_Method
# https://mathlesstraveled.com/2009/05/18/square-roots-with-pencil-and-paper-the-babylonian-method/

def sqrt(x):
    g = x / 2
    t = 0.00001

    while True:
        newG = (g + (x/g)) / 2
        if abs(g - newG) < t:
            return newG
        g = newG

# Asks the user to enter a positive integer. If they enter something else an error is shown and they are asked to enter again
# This section of code was mostly apated from a response on stackoverflow in order to return 
# an error should the user enter anything other than a positive number: 
# https://stackoverflow.com/questions/26198131/check-if-input-is-positive-integer
while True:
    val = input("Enter a positive integer: ")
    try:
        number = float(val)
        if number <= 0:  # if not a positive int print message and ask for input again
            print("Sorry, input must be a positive integer. Please try again.")
            continue
        break
    except ValueError:
        print("That's not an integer. Please try again.")  


# Calls the function to calculate the squre root of the number the user entered, then in a new variable rounds that answer to 2
# decimal places
root = sqrt(number)
roundRoot = round(root, 1)

# Outputs the number entered by the user and the answer calculated by the function
print("The square root of", number, "is approx.", str(roundRoot))
