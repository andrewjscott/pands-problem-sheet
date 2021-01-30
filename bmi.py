# Asks the user to input their weight and height and returns their Body Mass Index (BMI) number
# Author: Andrew Scott

# Asks the user to input their weight and stores that value in a variable named weight
weight = input("Enter weight (in kg): " )
# Asks the user to input their height and stores that value in a variable named height
height = input("Enter height (in cm): ")

# BMI is defined as weight divided by height in meters squared, which this calculates and stores in a variable called bmi
# As the height input by the user is in cm, it must be divided by 10 to convert it to meters
# float() used to ensure the input values are seen by python as numbers that can return fractions instead of strings
bmi = float(weight)/((float(height)/100)**2)

# Outputs the calulated BMI value stored in the variable bmi
# round() is used to restrict the output to 2 decimal places to avoid overly long outputs
print("BMI is: " + str(round(bmi, 2)))