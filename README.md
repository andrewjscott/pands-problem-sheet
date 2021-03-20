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
First, the input() method[1] is used in order to ask the user to enter both a weight and a height. The numbers entered by the user
are then assigned to variables called weight and height. 

To calculate the BMI, I used the following line of code: bmi = float(weight)/((float(height)/100)**2)
Python takes user inputs to be string types, so in order to perform calculations on them float is used to convert the variables
to floating point numbers[2]. Further, the height entered by the user has to be converted from cm to m, which is done by dividing
the user's entered value for height by 100. The "/" operator is used for division, while the ** operator is used for exponentiation[3].
The calculated value is assigned to the variable BMI. 

The BMI value calculated is returned to the user, and for it to be printed the value must be converted back to a string again,
which is done using the str() method. The round() method is used to restrict the calculated value to two decimal places, as per
the example result of '20.06' in the task outline.

After reading about the string isX methods in the book "Automate the Boring Stuff with Python" (2015, p. 130)[4], the code was edited to
include the method isDecimal() along with a while and if statement. This is to ensure that the user enters a valid whole number,
and if the enter something that is not a whole number, the code will inform the user of their error and ask them to enter a number
again. This will repeat until the user enters a valid whole number. 

## Weekly Task 2 - secondString
>  Write a program that takes asks a user to input a string and outputs every second letter in reverse order.   
>
> $ python secondstring.py   
> Please enter a sentence: The quick brown fox jumps over the lazy dog.   
>
> .o zletrv pu o wr cu h   

### Solution
First the user is asked to input a string which is stored to a variable. Each character in a string has a corresponding numberical value, with the first character 0, second character 1, etc. Slicing a string is done by using square brackets followed by the number corresponding to the start point, end point, and steps of the slicing with each number seperated by colons, ie [slicing start point:slicing end point:steps taken while slicing][5].

If the slicing start and end points are left blank, python assumes these values to correspond to the beginning and end of the string
If the steps is left out copletely pythons continues with steps as a value of 1 by default. A minus value for steps means the string is sliced in reverse. So in this code, the values for the start and end point are left blank to include the entire string, while
the steps is set to -2, which starts the slicing in reverse and only insludes every second letter. 

Using slicing in this manner, the user entered string can be manipulated and output in the manner requested in the task outline. 

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
The first step was to take input from the user for the starting integer. 

To keep track of each step in the collatz process, a list was created with the first entry being the number entered by the user.
A while loop is used so the calculations will continue until the value is equal to 0[6]. The task requires different calculations based on if the entered number is odd or even. A number is even if it leaves no remainder when divided by 2, so this was used to identify even numbers.

An if statement is then used so different calculations can be made depending on if the number is even or odd[7]. If the 
number is determined to be even, it is divided by 2 and the result is added to the list alongside the initial entered number. This result is now the number that will be used in calculations. 

As a number that is not even is by default an odd number, an else statement will suffice after the if statement determines whether
the number is even or not. If there is a remainder after the number is divided by 2, then the line of code following the if statement is ignored, and instead the code after the else statement is used, where the number is first multiplied by three, then 1 added to that answer. This result is then added to the list[8]. This process is repeated until the result is 1. When this happens the loop ends and all the numbers that have been added to the list are output.

Printing a list does mean the output is slightly different that the output in the task outline ([10, 5, 16, 8, 4, 2, 1] vs 10 5 16 8 4 2 1). However, I feel using a list is the neatest method to solve this problem, so decided to use it despite the aesthetic differences in the output. 

This code was later altered to include error detection to ensure the user only enters a positive integer. If they enter anything else an error message is ouput and they are asked to input a positive integer again. The code to do this was found on stackoverflow as an answer by a user named Padraic Cunningham[9]. This code includes a loop that first determines if the user input is an integer. if it is, it then checks if it is positive by seeing if the integer is less than 0. If the number is less than 0 the user is asked to enter a number again. If the user enters something other than an integer, a seperate block of code kicks in to tell the user that they have not entered an integer and to try again. This will repeat and only end once the user enters a positive integer. Further research shows that the 'try except' aspect of this code is used to test for error detection[10].


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
To easily work with dates in python, the "datetime" module was imported[11]. A list containing the two days of the weekend (Saturday and Sunday) was then created. A variable "date" was assigned information about the current date using the method "datetime.datetime.now()". This variable will then be updated to relect the date whenever the program is run. 

The datetime method ".strftime()" can now be used with the variable "date", and by passing the directive "%A" as an argument, the full word of the current day of the week is returned. The day that is returned is then compared with the previously created list, and if it matches a value in that list (ie the returned day is either "Saturday" or "Sunday") then the message "It is the weekend, yay!" is returned to the user. If the returned day is neither Saturday nor Sunday it is by default a weekday, so the returned message is instead "Yes, unfortunately today is a weekday.".

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
The first step was to research methods for calculating square roots. While the task suggests using the Newton method for calculating square roots, I found the additional calculus and formulae associated with the method both distracting and overwhelming. This initial research did reveal that the Newton method is closely related to the Babylonian method for calculating square roots, however, and finding this method easier to read and follow I used the Babylonian method in this code[12][13]. For this code I have written it as newG = (g + (x/g)) / 2, g being an initial guess, and x being the number entered by the user that we want to find the square root of. This formula is then repeated with the answer from the previous itteration used in place of the initial guess, and this process repeats until the answers are almost identical. 

The function for calculating a square root contains two initial variables. 

The first, g, is the initial guess. The formula requires an initial guess for the square root's value. Rather than have the user 
enter a value, a formula of the number that we want to find the square root of divided by 2 is used as the initial guess. This 
is not the most efficient in terms of finding the square root in the fewest itterations of the loop, as a guess closer to 
the square root will solve faster. However, this formula for an initial guess should be good enough for our purposes and 
saves the user from having to enter anything other than the number the want the square root of. As the function itterates, 
the value for g is replaced by the answer of that loop, newG.

The second, t, is the tolerance. This means the program will loop until the current answer for g/newG minus the previous answer for g/newG is within the tolerance level. When this happens, we should be returned a pretty good approximation of the square root. 

For taking the user input, code from the solution for the collatz task was reused for error detection, as this task also requires the user input to only be a positive number. The only change is converting the user input to a float. The sqrt function previously written is then called, and the output is returned and rounded to 1 decimal place.

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


#### References
1. W3schools.com. 2021. Python User Input. [online] Available at: <https://www.w3schools.com/python/python_user_input.asp> [Accessed 15 March 2021].
2. W3schools.com. 2021. Python Data Types. [online] Available at: <https://www.w3schools.com/python/python_datatypes.asp> [Accessed 15 March 2021].
3. W3schools.com. 2021. Python Arithmetic Operators. [online] Available at: <https://www.w3schools.com/python/python_operators.asp> [Accessed 15 March 2021].
4. Sweigart, A., 2015. Automate the boring stuff with Python: practical programming for total beginners. No Starch Press.
5. educative.io. 2021. String Slicing. [online] Available at: <https://www.educative.io/courses/learn-python-3-from-scratch/mE73nLqKGA3> [Accessed 16 March 2021].
6. realpython.com. 2021. Python "while" Loops (Indefinite Iteration). [online] Available at: <https://realpython.com/python-while-loop/> [Accessed 16 March 2021].
7. realpython.com. 2021. Conditional Statements in Python. [online] Available at: <https://realpython.com/python-conditional-statements/> [Accessed 16 March 2021].
8. W3schools.com. 2021. Python Lists. [online] Available at: <https://www.w3schools.com/python/python_lists.asp> [Accessed 16 March 2021]
9. stackoverflow.com. 2021. Check if input is positive integer. [online] Available at: <https://stackoverflow.com/questions/26198131/check-if-input-is-positive-integer> [Accessed 16 March 2021].
10. W3schools.com. 2021. Python Try Except. [online] Available at: <https://www.w3schools.com/python/python_try_except.asp> [Accessed 17
 March 2021]
 11. W3schools.com. 2021. Python Datetime. [online] Available at: <https://www.w3schools.com/python/python_datetime.asp> [Accessed 18 March 2021]
 12. Dellajustina, F.J. and Martins, L.C., 2014. The Hidden Geometry of the Babylonian Square Root Method. Applied Mathematics, 5(19), p.2982.
 13. Brent. 2009. Square roots with pencil and paper: the Babylonian method. [online] Available at: <https://mathlesstraveled.com/2009/05/18/square-roots-with-pencil-and-paper-the-babylonian-method/> [Accessed 20 March 2021]

