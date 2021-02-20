# A program that tells the user if today is a weekday or if it's a weekend
# Author: Andrew Scott

# Imports a module that allows you to work with current dates and times
import datetime

# A list that cointains all weekend days. 
weekend = ["Saturday", "Sunday"]

# Uses a method in the datetime module to import the current date information and stores it to a variable
date = datetime.datetime.now()

# ("%A") is a directive within the datetime module that extracts the current day of the week from the date. 
# This day is then compared with the previous list
# If the day extracted matches a day in the weekend list, the programs prints that it is currently a weekend 
if date.strftime("%A") in weekend:
    print("It is the weekend, yay!")

# Since any day that does not fall on a weekend is automatically a weekday, we do not need a list of weekdays to compare the 
# extracted day with. Therefore, we can just state that is the extracted day is not found on the weekend list, today is a weekday
else:
    print("Yes, unfortunately today is a weekday.")