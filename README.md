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
(b) Create an array x with linearly increasing values [0:0; 0:1; 0:2; : : : 1:0]. The size N of
the array should be N = 11.
(c) Modify N such that the step size is x = xi+1 􀀀 xi = 0:025.
(d) Plot the following three functions:
f1(x) = 1 - 2x; f2(x) = (x 􀀀 0:4)2; f3(x) = sin(2x)
Note: The sine function can be found in numpy.
(e) Plot the functions. The gure should contain:
 title Figure 1
 y-axis limits ylow = 􀀀1:2 and yhi = 1:2
 x-axis label x and y-axis label y
 grid lines
 legend with labels f1, f2, f3
(f) Additional task: Plot f3(x) only over the range 0  x  0:5.
#### Hints and remarks
 Basic Python commands can be found in the Minimal Python handout in Moodle.
 Detailed help and examples for numpy and matplotlib can be found online:
numpy.org matplotlib.org pythontutor.com . . . (see Moodle)
