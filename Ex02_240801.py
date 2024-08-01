# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 19:42:51 2024

@author: 김윤서
"""

import numpy as np
import matplotlib.pyplot as plt

# 1

d = 2.e-4
N = 100
sigma = 0.0

for i in range(0,N+1):
    sigma += i*d
    

def Gauss(d,N):
    return 0.5*d*N*(N+1)
gauss = Gauss(d,N)

print(repr(sigma),sigma)
print(repr(gauss),gauss)

# 2
"""
 The Taylor Series of a function f(x) represents the function
as a infinite sum of its derivatives evaluated at a point x0,
provided that f(x) can be differentiated infinitely many times 
around that point. 
"""

# 3

def Taylor4(x):
    T = np.zeros_like(x)
    for i in range(0,5):
        T += (-2)**i * (x+0.5)**i / np.math.factorial(i)
    return T

x = np.linspace(-1,4,1000)

def f(x):
    return np.exp(-2*x-1)

F = f(x)
T = Taylor4(x)

plt.figure()
plt.plot(x,T,label='Taylor Series4')
plt.plot(x,F,label='Reference function')
plt.legend()
plt.grid()
plt.show()

# 4

def fact(n):
    if (n==0) or (n==1):
        return 1
    else:
        return n*fact(n-1)
    
def TN(x,N):
    x0 = -0.5
    Taylor = 0.0
    for i in range(0,N+1):
        Taylor += (-2)**i * (x-x0)**i / fact(i)
    return Taylor

N1 = np.linspace(0,20,10).astype(int)
plt.figure()
for i in N1:
    taylor = TN(x, i)
    L = f" N = {i} "
    plt.plot(x,taylor,label = L)
plt.legend()
plt.grid()
plt.show()


# 5

x_point = 4
target_error = 1e-8

N2 = np.linspace(0,100,101).astype(int) 

error = np.zeros_like(N2).astype(float)


f_x_point = f(x_point)

for i in N2:
    Taylor_approx = TN(x_point, i)
    error[i] = np.abs(Taylor_approx - f_x_point)
    if (error[i]<= 1.e-8):
        print(error[i], i)
    
plt.figure()
plt.plot(N2, error, label = "Error")
plt.yscale('log') # Logarithmic scale for better visualization
plt.xlabel("N")
plt.ylabel("Error")
plt.grid()
plt.legend()
plt.title(f"Error between f(4) and TN(x; x0 = {x_point})")
plt.show()

