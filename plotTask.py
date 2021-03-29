# Displays a plot of the functions f(x)=x, g(x)=x ** 2 and h(x)=x ** 3 in the range [0, 4] on the one set of axes
# Author: Andrew Scott

import matplotlib.pyplot as plt
import numpy as np

# Sets the range of the x axis from 0-4 using numpy, but added as a float to allow for plot points every 0.5 steps
# I chose 0.5 as the range is quite small, so having half steps helps make the graph clearer in my opinion
xPoints = np.arange(0.0, 4.0, 0.5)

# Sets the plot points for each function on the y-axis in relation to the x-axis values
yPoints1 = xPoints
yPoints2 = xPoints ** 2
yPoints3 = xPoints ** 3

# Plots the values, with shortcuts to differentiate each function, with labels added for the legend
# 'b-o' = a blue straight line with a circle marking each value
# 'r--^' = a red dashed line with a triangle marking each value
# 'g:s' = a green dotted line with a square making each value
plt.plot(xPoints, yPoints1, 'b-o', label='f(x) = x')
plt.plot(xPoints, yPoints2, 'r--^', label='g(x) =  x**2')
plt.plot(xPoints, yPoints3, 'g:s', label='h(x) = x**3')

# The graph was showing the y-axis values in steps of 10 by default which I felt was too large, so I changed it to 5 with this line
# Code adapted from an answer found at: https://stackoverflow.com/questions/12608788/changing-the-tick-frequency-on-x-or-y-axis-in-matplotlib/12608937
plt.yticks(np.arange(0, max(yPoints3)+1, 5.0))

# Labelling the graph to explain what it's showing
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Plotting the Functions f(x)=x, g(x)=x**2, and h(x)=x**3")
plt.legend()

# Adds a grid to help easier see the values of each line
plt.grid()

# Saves the plot as a png image
plt.savefig('taskPlot.png')

plt.show()
