# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 12:35:41 2024

@author: 김윤서
"""

import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rd

x = np.random.rand(20)
print(x)

x = np.random.uniform(low = -3, high = 5, size = 20)
print(x)

x = list()
for i in range(5000):
    x.append(np.random.randint(1,7)) # 1, 2, 3, 4, 5, 6
    
x = np.array(x)

plt.figure()
# bins = [1,2,3,4,5,6,7]
# intervals : [1,2), [2,3), [3,4), [4,5), [5,6), [6,7)
plt.hist(x, bins = [i for i in range(1,8)], rwidth = 0.5, align = 'left')
plt.show()


#%%

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

N = 50000

# CDF inversion
r = rd.rand(N)
x = -np.log(1.-r)

# ref.
xref = rd.exponential(scale = 1., size = N)

M = 50
plt.figure()
plt.hist(x, bins = M, density = True, alpha = 0.5)
plt.hist(xref, bins = M, density = True, alpha = 0.5)

xp = np.linspace(0., 5., 100)
pdf = np.exp(-xp)
plt.plot(xp, pdf, 'k--')

plt.show()