# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 20:44:31 2024

@author: 김윤서
"""

import numpy as np
import matplotlib.pyplot as plt

I = np.log(2)
h = 0.01

def f(x):
    return 1./(1+x)


def lowersum(h):
    lower = 0.0
    N = int((1-0)/h)+1 # 전체 index: 0~N-1
    
    for i in range(N-1): # 그 중 index 0부터 N-2까지
        lower += f(i*h)*h
    
    return lower


def uppersum(h):
    upper = 0.0
    N = int((1-0)/h)+1
    
    for i in range(1,N):
        upper += f(i*h)*h
        
    return upper
    

def trapezoidal(h):
    trape = 0.0
    N = int((1-0)/h)+1
    
    for i in range(N-1):
        trape += (f(i*h)+f((i+1)*h))*h/2
        
    return trape


def error(x):
    return np.abs(I - x)


"""
lower = lowersum(h)
upper = uppersum(h)
trape = trapezoidal(h)

err_lower = error(lower)
err_upper = error(upper)
err_trape = error(trape)

print(f"Error lower : {err_lower}, upper : {err_upper}, trape : {err_trape}")

"""



#%%


# h_values = np.logspace(-16,-1,16)
h_values = np.logspace(-6,0,7)

err_lower = np.zeros(len(h_values))
err_upper = np.zeros(len(h_values))
err_trape = np.zeros(len(h_values))

for ind, h in enumerate(h_values): # ind = index, h = value

    lower = lowersum(h)
    upper = uppersum(h)
    trape = trapezoidal(h)
    
    err_lower[ind] = error(lower)
    err_upper[ind] = error(upper)
    err_trape[ind] = error(trape)
    

plt.figure()
 
plt.loglog(h_values,err_lower, label = 'Error_Lowersum')
plt.loglog(h_values,err_upper, linestyle = '--', label = 'Error_uppersum')
plt.loglog(h_values,err_trape, label = 'Error_trapezoidal')

plt.xlabel('h')
plt.ylabel('Error')
plt.legend()
plt.grid()
plt.show()
    

#%%

