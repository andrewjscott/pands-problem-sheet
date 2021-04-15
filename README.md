# Programming and Scripting Problem Sheets
## Andrew Scott - Student ID: G00398249

This code was written in Python 3.8.3 using Visual Studio Code version 1.55.2.

Python packages not part of the Python Standard Library that were installed and used are:   
numpy==1.18.5   
matplotlib==3.2.2

These can be installed by downloading the requirements.txt file and running pip3 install -r requirements.txt.
The requirements.txt file was generated using pipreqs 0.4.10.

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
First, the input() method[1] is used in order to ask the user to enter both a weight and a height. The numbers entered by the user are then assigned to variables called weight and height. 

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
First the user is asked to input a string which is stored to a variable. Each character in a string has a corresponding numerical value, with the first character 0, second character 1, etc. Slicing a string is done by using square brackets followed by the number corresponding to the start point, end point, and steps of the slicing with each number separated by colons, i.e. [slicing start point:slicing end point:steps taken while slicing][5].

If the slicing start and end points are left blank, python assumes these values to correspond to the beginning and end of the string
If no value is used to specify the size of the step, python continues with steps as a value of 1 by default. A minus value for steps means the string is sliced in reverse. So in this code, the values for the start and end point are left blank to include the entire string, while
the steps is set to -2, which starts the slicing in reverse and only includes every second letter. 

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

This code was later altered to include error detection to ensure the user only enters a positive integer. If they enter anything else an error message is output and they are asked to input a positive integer again. The code to do this was found on stackoverflow as an answer by a user named Padraic Cunningham[9]. This code includes a loop that first determines if the user input is an integer. if it is, it then checks if it is positive by seeing if the integer is less than 0. If the number is less than 0 the user is asked to enter a number again. If the user enters something other than an integer, an additional block of code kicks in to tell the user that they have not entered an integer and to try again. This will repeat and only end once the user enters a positive integer. Further research shows that the 'try except' aspect of this code is used to test for error detection[10].


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
To easily work with dates in python, the "datetime" module was imported[11]. A list containing the two days of the weekend (Saturday and Sunday) was then created. A variable "date" was assigned information about the current date using the method "datetime.datetime.now()". This variable will then be updated to reflect the date whenever the program is run. 

The datetime method ".strftime()" can now be used with the variable "date", and by passing the directive "%A" as an argument, the full word of the current day of the week is returned. The day that is returned is then compared with the previously created list, and if it matches a value in that list (i.e. the returned day is either "Saturday" or "Sunday") then the message "It is the weekend, yay!" is returned to the user. If the returned day is neither Saturday nor Sunday it is by default a weekday, so the returned message is instead "Yes, unfortunately today is a weekday.".


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
The first step was to research methods for calculating square roots. While the task suggests using the Newton method for calculating square roots, I found the additional calculus and formulae associated with the method both distracting and overwhelming. This initial research did reveal that the Newton method is closely related to the Babylonian method for calculating square roots, however, and finding this method easier to read and follow I used the Babylonian method in this code[12][13]. For this code I have written it as new_guess = (initial_guess + (x/initial_guess))/2, initial_guess being an initial guess of the square root to plug into the formula, and x being the number entered by the user that we want to find the square root of. This formula is then repeated with the answer from the previous iteration used in place of the initial guess, becoming new_guess, and this process repeats until the answers are almost identical. 

The function for calculating a square root contains two initial variables. 

The first, initial_guess, is the initial guess. The formula requires an initial guess for the square root's value. Rather than have the user 
enter a value, a formula of the number that we want to find the square root of divided by 2 is used as the initial guess. This 
is not the most efficient in terms of finding the square root in the fewest iterations of the loop, as a guess closer to 
the square root will solve faster. However, this formula for an initial guess should be good enough for our purposes and 
saves the user from having to enter anything other than the number the want the square root of. As the function iterates, 
the value for initial_guess is replaced by the answer of that loop, new_guess.

The second, is tolerance. This means the program will loop until the current answer for initial_guess/new_guess minus the previous answer for initial_guess/new_guess is within the tolerance level. When this happens, we should be returned a pretty good approximation of the square root. 

For taking the user input, code from the solution for the collatz task was reused for error detection, as this task also requires the user input to only be a positive number. The only change is converting the user input to a float. The sqrt function previously written is then called, and the output is returned and rounded to 1 decimal place.


## Weekly Task 6 - numberOfEs
> Write a program that reads in a text file and outputs the number of e's it contains.  
> The program should take the filename from an argument on the command line.
> 
> $ python es.py moby-dick.txt   
> 116960 

### Solution
This task requires the filename to be taken as an argument from the command line, which can be done by importing the sys module and using sys.argv[14]. As the program itself is in position 0, the line sys.argv[1] takes the next argument, i.e. the filename entered by the user, and stores it too a variable called filename.

The task was ambiguous as to whether the program should count only the symbol 'e', i.e. only the lower case e, or if it should count all instances or the letter e, which would include lower case e and upper case E. As such, two functions have been included to cover both cases. The first counts instances of 'e' while the second counts instances of 'E'. The function imports the file called by the user and the count method is used to count the number of instances of either 'e' or 'E'[15][16]. The returned values are converted to strings to be output to the user.

If statements are used when returning the values to the user for grammatical purposes. Should either character only appear once, the singular 'time' is used, otherwise the sentence with say the character appear "x times". The variable total is the sum of the amount of lowercase e's and uppercase E's, which is also returned to the user.


## Weekly Task 7 - plotTask
> Write a program called plottask.py that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.
>
> Some marks will be given for making the plot look nice.

### Solution
First, matlibplot and numpy are imported. When first trying to import matlibplot and numpy, Visual Studio Code threw up an error, pylint(import-error). By searching for a solution it was discovered this was due to the default python interpreter in Visual Studio Code being regular python 3, and the problem was solved by changing this to Anaconda's python 3[17]. Matlibplot allows for the creation of plots within python[18], whereas numpy is used to create an array which will be used to define the parameters of the plot's x-axis[19]. The task outline asks for a range of [0, 4] which is what is used. A step of 0.5 within this range is also used to allow extra points on the plot than the default 1 step. I feel this makes the graph easier to read. More points would be too cluttered, whereas fewer points would be too sparse. 

The y-axis plots are defined by the results of the three functions being plotted, so each gets their own variable. The results of each function are then plotted, with each getting their own unique line type, colour, and marker to differentiate each one. This would hopefully allow colourblind users who find the colours difficult to differentiate still be able to read the graph using the different markers and line types. This was done by using shortcuts as arguments after the arguments for the x and y points when calling matlibplot's plot module[20]. For example, 'b-o' creates a blue straight line with a circle marking each value. Labels are added to each line within the plot, as well as the axis, a title, and a legend in order to let the user know what the plot is doing. In order to make the plot more readable and user friendly, a grid was added, and the tick values on the y-axis were changed from the default 10 to 5 by adapting a line of code found on StackOverflow[21]. The resulting plot is then saved. Originally, saving the plot was the last line of code, but this resulted in the plot being saved as a blank image. After looking this issue up, it seems that the image should be saved first before being shown otherwise it will end up as a blank image[22].

![alt text](https://raw.githubusercontent.com/andrewjscott/pands-problem-sheet/main/taskPlot.png "Plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4]")

#### Acknowledgements
It should be noted that the majority of the ideas and concepts covered here came from a fantastic lecture series called Programming and Scripting by Andrew Beatty. The references below are in many cases supplemental to that series and are offered as a text-based alternative that covers similar content. 

#### References
1. W3schools.com. 2021. Python User Input. [online] Available at: <https://www.w3schools.com/python/python_user_input.asp> [Accessed 15 March 2021].
2. W3schools.com. 2021. Python Data Types. [online] Available at: <https://www.w3schools.com/python/python_datatypes.asp> [Accessed 15 March 2021].
3. W3schools.com. 2021. Python Arithmetic Operators. [online] Available at: <https://www.w3schools.com/python/python_operators.asp> [Accessed 15 March 2021].
4. Sweigart, A., 2015. Automate the boring stuff with Python: practical programming for total beginners. No Starch Press.
5. educative.io. 2021. String Slicing. [online] Available at: <https://www.educative.io/courses/learn-python-3-from-scratch/mE73nLqKGA3> [Accessed 16 March 2021].
6. Sturtz, J. 2021. Python "while" Loops (Indefinite Iteration). [online] Available at: <https://realpython.com/python-while-loop/> [Accessed 16 March 2021].
7. Sturtz, J. 2021. Conditional Statements in Python. [online] Available at: <https://realpython.com/python-conditional-statements/> [Accessed 16 March 2021].
8. W3schools.com. 2021. Python Lists. [online] Available at: <https://www.w3schools.com/python/python_lists.asp> [Accessed 16 March 2021]
9. Cunningham, P. 2014. Check if input is positive integer. [online] Available at: <https://stackoverflow.com/questions/26198131/check-if-input-is-positive-integer> [Accessed 16 March 2021].
10. W3schools.com. 2021. Python Try Except. [online] Available at: <https://www.w3schools.com/python/python_try_except.asp> [Accessed 17
 March 2021]
11. W3schools.com. 2021. Python Datetime. [online] Available at: <https://www.w3schools.com/python/python_datetime.asp> [Accessed 18 March 2021]
12. Dellajustina, F.J. and Martins, L.C., 2014. The Hidden Geometry of the Babylonian Square Root Method. Applied Mathematics, 5(19), p.2982.
13. Brent. 2009. Square roots with pencil and paper: the Babylonian method. [online] Available at: <https://mathlesstraveled.com/2009/05/18/square-roots-with-pencil-and-paper-the-babylonian-method/> [Accessed 20 March 2021]
14. geeksforgeeks.com. 2019. How to use sys.argv in Python. [online] Available at: <https://www.geeksforgeeks.org/how-to-use-sys-argv-in-python/> [Accessed 20 March 2021]
15. Ndlovu, V. 2021. Working With Files in Python. [online] Available at: <https://realpython.com/working-with-files-in-python/> [Accessed 16 March 2021].
16. W3schools.com. 2021. Python String count() Method. [online] Available at: <https://www.w3schools.com/python/ref_string_count.asp> [Accessed 20 March 2021]
17. FewSteps. 2021. Fixed Pylint (import-error) Unable to import - How to fix Unable to import '' pylint(import-error). [online] Available at: <https://www.youtube.com/watch?v=BhNDn-FkKiU> [Accessed 21 March 2021]
18. W3schools.com. 2021. Matplotlib Tutorial. [online] Available at: <https://www.w3schools.com/python/matplotlib_intro.asp> [Accessed 21 March 2021]
19. W3schools.com. 2021. NumPy Introduction. [online] Available at: <https://www.w3schools.com/python/numpy_intro.asp> [Accessed 21 March 2021]
20. W3schools.com. 2021. Matplotlib Markers. [online] Available at: <https://www.w3schools.com/python/matplotlib_markers.asp> [Accessed 21 March 2021]
21. unutbu. 2012. Changing the “tick frequency” on x or y axis in matplotlib?. [online] Available at: <https://stackoverflow.com/questions/12608788/changing-the-tick-frequency-on-x-or-y-axis-in-matplotlib/12608937> [Accessed 21 March 2021]
22. ProgrammerSought. 2021.  Matplotlib solves a blank when saving a picture using plt.savefig. [online] Available at: <https://www.programmersought.com/article/6223231972/> [Accessed 29 March 2021]