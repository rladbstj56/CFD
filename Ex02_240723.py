#1
#(a)

import numpy as np

def sigma(a,b):
    val = 0
    for i in range(a,b+1): # b+1 is exclusive (a, ,b)
        val += i
    return val

N = 100
d = 2.e-4
sum = sigma(0,N) * d
print(sum)

#%%

#(b)
def gauss(gd,gn):
    return 0.5 * gd * gn * (gn+1)

GP = gauss(d,N)
print(GP)

if sum > GP :
    print("Sum is bigger ", sum)
elif sum == GP :
    print("They are same ", sum)
else :
    print("Gauss' product is bigger ", GP)
    
#(c)
print(repr(sum))
print(repr(GP))
#내 결과는 똑같이 나오는데
#차이가 있어야하는거 아닌가

#2
# What is the definition of the Taylor series of a function f(x) around a point x0?
# The Taylor series of a function f(x) around a point x0 is an infinite series that represents f(x) as a sum of its derivatives at x0.

#%%

#3
def f(x):
    return np.exp(-2*x-1)

#(a)
import math # factorial function
def taylorsigma(a,b,x,x0):
    taylorsum = 0
    for i in range (a,b+1):
        taylorsum += 1/math.factorial(i)*(-1)**i*(x-x0)**i
    return taylorsum
    
x0 = -0.5

def taylorf(x):
    return taylorsigma(0,4,x,x0)

x_values = [i for i in range(-1,4)] # x값 범위
y_values = [taylorf(x) for x in x_values]

import matplotlib.pyplot as pl

pl.plot(x_values, y_values, label='y=f(x)')
pl.legend()
pl.xlim(-5,8)
pl.grid() #격자
pl.show()

#(b)

#(c)

#%%

#4
