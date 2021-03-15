# Programming and Scripting Problem Sheets
## Andrew Scott - Student ID: G00398249

## Table of contents


## Weekly Task 1 - bmi
> 1. Write a program that calculates somebody's Body Mass Index (BMI). Call the file bmi.py
> - The inputs are the person's height in centimetres and weight in kilograms.
> - The output is their weight divided by their height in metres squared.
>
>$ python bmi.py  
>Enter weight: 65  
>Enter height: 180
>
>BMI is 20.06.

### Solution
First, the input() method is used in order to ask the user to enter both a weight and a height. The numbers entered by the user
are then assigned to variables called weight and height. 

To calculate the BMI, I used the following line of code: bmi = float(weight)/((float(height)/100)**2)
Python takes user inputs to be string types, so in order to perform calculations on them float is used to convert the variables
to floating point numbers. Further, the height entered by the user has to be converted from cm to m, which is done by dividing
the user's entered value for height by 100. The "/" operator is used for division, while the ** operator is used for exponentiation.
The calculated value is assigned to the variable BMI. 

The BMI value calculated is returned to the user, and for it to be printed the value must be converted back to a string again,
which is done using the str() method. The round() method is used to restrict the calculated value to two decimal places, as per
the example result of '20.06' in the task outline.

After reading about the string isX methods in the book "Automate the Boring Stuff with Python" (2015, p. 130), the code was edited to
include the method isDecimal() along with a while and if statement. This is to ensure that the user enters a valid whole number,
and if the enter something that is not a whole number, the code will inform the user of their error and ask them to enter a number
again. This will repeat until the user enters a valid whole number. 

#### References
1. W3schools.com. 2021. Python User Input. [online] Available at: <https://www.w3schools.com/python/python_user_input.asp> [Accessed 15 March 2021].
2. W3schools.com. 2021. Python Data Types. [online] Available at: <https://www.w3schools.com/python/python_datatypes.asp> [Accessed 15 March 2021].
3. W3schools.com. 2021. Python Arithmetic Operators. [online] Available at: <https://www.w3schools.com/python/python_operators.asp> [Accessed 15 March 2021].
4. Sweigart, A., 2015. Automate the boring stuff with Python: practical programming for total beginners. No Starch Press.


## Weekly Task 2 - secondString
>  Write a program that takes asks a user to input a string and outputs every second letter in reverse order.   
>
> $ python secondstring.py   
> Please enter a sentence: The quick brown fox jumps over the lazy dog.   
>
> .o zletrv pu o wr cu h   

### Solution

## Weekly Task 3 - collatz
> Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation.   
> At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.   
> Have the program end if the current value is one.
>
> $ python collatz.py   
> Please enter a positive integer: 10    
>
> 10 5 16 8 4 2 1    

### Solution

## Weekly Task 4 - weekday
> Write a program that outputs whether or not today is a weekday.   
> (You will need to search the web to find how you work out what day it is)   
> An example of running this program on a Thursday is given below.   
>
> $ python weekday.py   
>
> Yes, unfortunately today is a weekday.   
> 
> An example of running it on a Saturday is as follows:   
> 
> $ python weekday.py   
>
> It is the weekend, yay! 

### Solution

## Weekly Task 5 - squareRoot
> Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.
>
> You should create a function called <tt>sqrt</tt> that does this.
>  
> I am asking you to create your own sqrt function and not to use the built in functions x ** .5 or math.sqrt(x).
>
> This is to demonstrate that you can research and code a process (If you really needed the square root you would use one of the above methods).
>
> I suggest that you look at the newton method at estimating square roots.
>
> This is a more difficult task than some of the others, but will be marked equally, so only do as much work on this as you feel comfortable.
> 
> $ python squareroot.py   
> Please enter a positive number: 14.5   
> The square root of 14.5 is approx. 3.8.   

### Solution

## Weekly Task 6 - numberOfEs
> Write a program that reads in a text file and outputs the number of e's it contains.  
> The program should take the filename from an argument on the command line.
> 
> $ python es.py moby-dick.txt   
> 116960 

### Solution

## Weekly Task 7 - plotTask
> Write a program called plottask.py that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.
>
> Some marks will be given for making the plot look nice.

### Solution