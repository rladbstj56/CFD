# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 10:45:35 2024

@author: 김윤서
"""

import numpy as np
import matplotlib.pyplot as plt

# Ex 08

# 1

rand1 = np.random.rand(20)
#print(rand1)

rand2 = np.random.rand(20)*8 - 3
#print(rand2)

# 2

rand3 = np.random.randint(1,7,5000)
#print(rand3)

"""
plt.figure()
plt.hist(rand3, bins = [i for i in range(1,8)], rwidth = 0.5, align = 'left')
plt.title('random histogram 1<=x<=6')
plt.show()
"""

def mean(x):
    return sum(x)/len(x)

def std(x):
    return np.sqrt(sum((x-mean(x))**2)/len(x))

mean_value = mean(rand3)
#print("mean : ", mean_value)
std_value = std(rand3)
#print("std : ", std_value)
    

# 3

x0, a, c = 1, 2, 3
N = 30
m_list = (5, 7, 8, 10, 11)
n = 1
plt.figure()
for m in m_list :
    x = x0
    xa = [x0]
    for i in range(N-1):
        x = (a*x + c)%m
        xa.append(x)
        
    # Normalize by m to obtain random numbers in [0,1)
    xa_normalized = [num / m for num in xa]
    
    plt.subplot(3,2,n)
    plt.hist(xa, bins = [ i for i in range(m+1)], color = 'green')
    n += 1
plt.show()


#%%

# 4

"""
N = 50000
exp = np.random.exponential(1.0,N) # scale = 1.0
plt.subplot(2,1,1)
plt.plot(exp)
plt.subplot(2,1,2)
plt.hist(exp, bins = 100, density = True)
plt.show()


sample_r = np.random.rand(N)
c = -np.log(1-sample_r)

plt.figure()
plt.hist(c, bins = 30, density = True) # PDF = probability density function
plt.show()

#%%

"""
# 5

