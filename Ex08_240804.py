# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 13:07:58 2024

@author: 김윤서
"""

import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rnd

N = 20

rand1 = rnd.rand(N)
# print(rand1)
mean1 = np.mean(rand1)
std1 = np.std(rand1)
# print(mean1,std1)

rand2 = rnd.rand(20)*8-3
# print(rand2)
mean2 = np.mean(rand2)
std2 = np.std(rand2)
# print(mean2,std2)


#%%

N = 5000

dice = rnd.randint(1,7,N) # 1~6까지 N개 

"""
plt.figure()
# bins는 히스토그램 구간의 경계
# range(1,8) :  1부터 7까지 
# 히스토그램 1,2,3,4,5,6,7 구간에 대해 그려짐
# bins = [1,2,3,4,5,6,7]
# intervals : [1,2), [2,3), [3,4), [4,5), [5,6), [6,7)
plt.hist(dice, bins = [i for i in range(1,8)], rwidth = 0.5, align = 'left')
plt.show()
"""

mean = np.mean(dice)
std = np.std(dice)

# print(mean, std)


#%%

N = 20

x0 = 1
a = 2
c = 3
m = 5

x = np.zeros(N)
x[0] = x0


seed_list = [[1,2,3,5], [5,-1,37,7], [100,3,-1,9], [30,-2, 10, 11]]

"""
plt.figure()
ind = 1

for l in seed_list:
    x0 = l[0]
    a = l[1]
    c = l[2]
    m = l[3]
    x[0] = x0
    
    for i in range(N-1):
        x[i+1] = (a*x[i]+c)%m
     
    xn = [num/m for num in x]
    print(x)
    print(xn)
    
    plt.subplot(4,1,ind)
    # [0,1), [1,2), ,,, [m-1,m)
    plt.hist(x, bins = [ i for i in range(m+1)], color = 'green')
    plt.title(f"x0 = {x0}, a = {a}, c = {c}, m = {m}")

    ind += 1
    
plt.tight_layout()
plt.show()
"""


#%%


N = 50000

x = rnd.exponential(1,N)
x_val = np.linspace(0, max(x), N)

p = np.exp(-x_val)

plt.figure()
# random sampled histogram
plt.hist(x, bins = 100, density = True, alpha = 0.7, color = 'green' )
# PDF of Exponential Distribution
plt.plot(x_val, p, 'r--', lw=2, label = 'p(x)')

plt.xlabel('x')
plt.ylabel('probability density')
plt.title('PDF of Exponential Distribution and Sampled Histogram')
plt.legend()
plt.grid()
plt.show()

#%%

N = 1000

r = rnd.rand(N)

x = -np.log(1-r)
x_val = np.linspace(0, np.max(x), N)

p = np.exp(-x_val)

plt.figure()
# PDF of generated xi
plt.hist(x, bins = 100, density = True, alpha = 0.7, color = 'green', edgecolor = 'black')
# reference PDF p(x)
plt.plot(x_val, p, 'r--', lw = 2)

plt.xlabel('x')
plt.ylabel('probability density')
plt.title('PDF of Generated Exponential Sample and Reference PDF')
plt.grid()
plt.show()


#%%

N = 6

tEnd = 20
dt = 1.e-2
steps = int(tEnd/dt) # 20000

e = rnd.rand(N) - 0.5
n = rnd.rand(N) - 0.5
c = rnd.rand(N) - 0.5
x0 = rnd.randint(1,100)
y0 = rnd.randint(1,100)
z0 = rnd.randint(1,100)

initial = np.array([[x0+ei,y0+ni,z0+ci] for ei,ni,ci in zip(e,n,c)])
ind = 1

for ini in initial: # 10번 반복
    x0,y0,z0 = ini

    s = 10.
    r = 28.
    b = 8./3.
    
    x = np.zeros(steps)
    y = np.zeros(steps)
    z = np.zeros(steps)
    
    x[0] = x0
    y[0] = y0
    z[0] = z0
    
    for i in range(steps-1):
        x[i+1] = x[i] + dt*(s*(y[i]-x[i]))
        y[i+1] = y[i] + dt*(x[i]*(r-z[i])-y[i])
        z[i+1] = z[i] + dt*(x[i]*y[i]-b*z[i])                      
    
    plt.subplot(3,2,ind)
    ind += 1
    plt.plot(x,y,'r-',lw=1,alpha=0.5,label='x vs y')
    plt.plot(x,z,'b-',lw=1,alpha=0.5,label='x vs z')
    plt.grid()
    plt.legend()

plt.tight_layout()
plt.show()