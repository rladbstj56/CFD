# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 17:50:34 2024

@author: 김윤서
"""

import numpy as np
import matplotlib.pyplot as plt

h = 1.e-2

xStart = -5.
xEnd = 5.
N = int((xEnd - xStart) / h) + 1

x = np.linspace(xStart, xEnd, N)
dx = x[1] - x[0]

def g(x):
    mu = 0.3
    sigma = 1.2
    
    return 1/np.sqrt(2*np.pi*sigma**2)*np.exp(-(x-mu)**2/(2*sigma**2))

y = g(x)

def g1cal(x):
    mu = 0.3
    sigma = 1.2
    return -(x-mu)/sigma**2*g(x)

y1cal = g1cal(x)

def g1(y,dx):
    tmp = np.zeros_like(y)
    tmp[1:-1] = (y[2:] - y[0:-2])/(2*dx)
    return tmp

y1 = g1(y,dx)

def g2cal(x):
    mu = 0.3
    sigma = 1.2
    return ((x-mu)**2/sigma**4-1/sigma**2)*g(x)

y2cal = g2cal(x)

def g2(y,dx):
    tmp = np.zeros_like(y)
    tmp[1:-1] = (y[2:] - 2*y[1:-1] + y[0:-2])/(dx**2)
    return tmp

y2 = g2(y,dx)

"""
plt.subplot(3,1,1)
plt.plot(x,y)
plt.title("y = g(x)")
plt.grid()

plt.subplot(3,1,2)
plt.plot(x,y1,label = 'y1')
plt.plot(x,y1cal,label = 'y1_cal', linestyle = '--')
plt.title("y = g1(x)")
plt.legend()
plt.grid()

plt.subplot(3,1,3)
plt.plot(x,y2,label = 'y2')
plt.plot(x,y2cal,label = 'y2_cal', linestyle = '--')
plt.title("y = g2(x)") 
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()   
"""

"""
plt.figure()
plt.plot(x,y, label = 'y')
plt.plot(x,y1,label = 'y1')
plt.plot(x,y1cal,label = 'y1_cal', linestyle = '--')
plt.plot(x,y2,label = 'y2')
plt.plot(x,y2cal,label = 'y2_cal', linestyle = '--')
plt.legend()
plt.grid()
plt.show()
"""



#%%

err1 = np.abs(y1 - y1cal)
err2 = np.abs(y2 - y2cal)

plt.figure()
plt.semilogy(x, err1, label = 'Error 1')
plt.semilogy(x, err2, label = 'Error 2')
plt.legend()
plt.grid()
plt.show()

#%%

h_values = [1e-2, 1e-3, 1e-4, 1e-5, 1e-6, 1e-7]

for h in h_values:
    x = np.arange(xStart, xEnd+h, h)
    dx = x[1] - x[0]

    y_ = g(x)
    y1_ = g1(y_, dx)
    y1cal_ = g1cal(x)

    err1_ = np.abs(y1_ - y1cal_)
    
    max_error = np.max(err1_)
    
    if(max_error < 1.e-3) :
        print(f"h = {h}, Max error = {max_error}")
    
    
# the smallest h when the maximum error max(err1) is smaller than 1e-3
# is 1e-7
    

