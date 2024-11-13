### Introduction to Computational Thinking and Programming for CFD
#### Module 13251
##### Dr. rer. nat. Marten Klein
###### Numerical Fluid and Gas Dynamics, BTU Cottbus-Senftenberg


### Ex01
#### Goals
* Introduction to the Python programming language
* Executing and editing Python programs
* Importing and using Python modules such as numpy and matplotlib
#### Tasks
1. Install a Python distribution and Spyder on your system (see Moodle for hints).
2. Introduction to Python
  * A Python program is given by a human-readable source le ((script )), e.g.,
my_program.py. The compilation and execution of this script is handled by the
Python interpreter (shell and kernel). There is no need to manually compile the
source le. This is done on-the-y by the interpreter.
  * Take a look at the Minimal Python handout (available on Moodle) and type the
commands into Spyder's Python shell. Hit enter submit a command.
3. Numerical data operations and plotting: Using the numpy and matplotlib.pyplot mo-
dules
(a) Create a new Python source le (e.g. myplot.py) and open it with Spyder. Load
numpy and matplotlib.pyplot.
(b) Create an array x with linearly increasing values [0.0, 0.1, 0.2, . . . 1.0]. The size N of
the array should be N = 11.
(c) Modify N such that the step size is x = xi+1 􀀀 xi = 0:025.
(d) Plot the following three functions:
f1(x) = 1 - 2x, f2(x) = (x - 0.4)^2; f3(x) = sin(2*pi*x)
Note: The sine function can be found in numpy.
(e) Plot the functions. The gure should contain:
 * title "Figure 1"
 * y-axis limits ylow = -1.2 and yhi = 1.2
 * x-axis label "x" and y-axis label "y"
 * grid lines
 * legend with labels "f1", "f2", "f3"
(f) Additional task: Plot f3(x) only over the range 0 <= x <= 0.5.
#### Hints and remarks
 * Basic Python commands can be found in the Minimal Python handout in Moodle.
 * Detailed help and examples for numpy and matplotlib can be found online:
numpy.org matplotlib.org pythontutor.com . . . (see Moodle)


### Ex 02
#### Goals
 * Taylor series
 * Functions, recursion
 * Loops, branches
 * Increment operator
 * Algorithm for the sum
#### Tasks
1. Algorithm for the sum.
(a) Develop and implement an algorithm that computes the following sum:
(b) Compare the result with Gauss' product 0.5 * d * N * (N + 1).
(c) Print out repr(x) for the result of case (a) and (b), respectively. Are there differences? Why or why not?
2. What is the denition of the Taylor series of a function f(x) around a point x0?
3. We consider the function f(x) = exp (-2x - 1) over the interval -1 <= x<= 4.
(a) Expand the Taylor series TN(x; x0) of f(x) around x0 = -0.5 up to of 4th order, that is, give T4(x;-0.5) explicitly.
(b) Implement T4(x;-0.5) in a Python function.
(c) Plot the numpy-based reference function f(x) together with your approximation
T4(x;-0.5). Where does the largest and where the smallest error occur?
4. Now consider the general case for arbitrary order N.
(a) Determine analytically the Taylor series of TN(x;-0.5).
(b) Implement a recursive function for the factorial n! = n * (n - 1) * ... * 1.
(c) Implement TN(x;􀀀0:5) in a Python function, passing N as the second parameter of the function.
(d) Plot the reference function f(x), the approximation T4(x;-0.5), and TN(x;-0.5) for various integer values of N. What do you observe for increasing N?
5. Determine numerically the order N for which the error between f(x) and TN(x;-0.5) at x = 4 is less than 10^(-8).
#### Hints and remarks
* Standard libraries
''' python
import numpy as np
import matplotlib.pyplot as pl
'''
* Define a function
''' python
def myfunc(x):
val = 3*(x-1.)**(1./3.)
return val
'''
* Call a function
''' python
x = myfunc(1.0)
print( x )
'''
* Save / show a plot
''' python
# generate data
x = np.linspace(1., 2., 4)
y = myfunc(x)
# plot
pl.plot(x, y)
pl.savefig('myfig.png') # save figure
pl.show() # display figure
'''
