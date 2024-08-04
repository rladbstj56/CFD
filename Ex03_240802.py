# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 11:19:41 2024

@author: 김윤서
"""

#import numpy as np
#import matplotlib.pyplot as plt

# 1

"""
A = np.array([[11,12,13],[21,22,23]])    
print(A)

A[1,2] = 99
A[0][1] = 100
print(A)
"""

"""
A[5,5] = 5
if I try to print the nonexisting element such as a66,
'indexerror' occurs.
"""

#%%

# 2

"""
x = np.linspace(0,4,50)
y = np.linspace(-1,1,30)
xv, yv = np.meshgrid(x,y)

#plt.figure(1)
#plt.scatter(xv,yv)
#plt.show()

np.savetxt('Ex03_grid_x.csv',xv)
np.savetxt('Ex03_grid_y.csv',yv)
"""

"""
xn = int(input("Enter the number of X cells : "))
yn = int(input("Enter the number of Y cells : "))
xStart = int(input("Enter the start point of x : "))
xEnd = int(input("Enter the end point of x : "))
yStart = int(input("Enter the start point of y : "))
yEnd = int(input("Enter the end point of y : "))

x_enter = np.linspace(xStart,xEnd,xn)
y_enter = np.linspace(yStart,yEnd,yn)

plt.figure()
xv_enter, yv_enter = np.meshgrid(x_enter,y_enter)
plt.scatter(xv_enter,yv_enter)
plt.show()
"""

#%%

# 3

"""

y = np.linspace(-1, 1, 10)

def stretched(x):
    a = 0.99
    b = 1/2*np.log((1+a)/(1-a))
    
    return np.tanh(b*(x-1/2))/np.tanh(b/2)

xi = np.linspace(0., 1., len(y))

x = np.linspace(0.,4.,5)
y = stretched(xi)
    
xv_stretched, yv_stretched = np.meshgrid(x,y)

#plt.figure()
#plt.scatter(xv_stretched,yv_stretched)
#plt.show()


x_load = np.loadtxt('Ex03_grid_x.csv')
y_load = np.loadtxt('Ex03_grid_y.csv')
xv_load, yv_load = np.meshgrid(x_load, y_load)

plt.figure()
plt.scatter(xv_load, yv_load, color = 'green', label = 'load')
plt.scatter(xv_stretched, yv_stretched, color = 'orange', label = 'stretched')
plt.legend()
plt.show()

"""

#%%

# 4

import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rnd
from scipy.interpolate import griddata

def f(x,y):
    return np.sin(2*np.pi*x)*np.cos(8*np.pi*y)*np.exp(-4*y**2)

# high resolution

x1d = np.linspace(0,1,200)
y1d = np.linspace(0,1,200)
x2d, y2d = np.meshgrid(x1d,y1d)

z2d = f(x2d,y2d)

plt.figure()
plt.contourf(x2d,y2d,z2d,256)
plt.show()


# low resolution
# 1차원 배열 (2차원 그리드 아님)

points = rnd.random_sample((100,2)) # x 100개 y 100개
x1d_points = points[:,0]
y1d_points = points[:,1]

plt.figure()
plt.contourf(x2d, y2d, z2d, 256)
plt.scatter(x1d_points, y1d_points, color = 'k', marker = 'o')
plt.show()


z1d_points = f(x1d_points, y1d_points)

# interpolate the low-resolution data(1d) to the high-resolution grid(2d)
z_near = griddata((x1d_points,y1d_points),z1d_points,(x2d,y2d), method = 'nearest')
z_lin = griddata((x1d_points,y1d_points),z1d_points,(x2d,y2d), method = 'linear')
z_cub = griddata((x1d_points,y1d_points),z1d_points,(x2d,y2d), method = 'cubic')

plt.subplot(2,2,1)
plt.contourf(x2d, y2d, z2d, 256)
plt.title('Z2D')

plt.subplot(2,2,2)
plt.contourf(x2d, y2d, z_near, 256)
plt.title('nearest')

plt.subplot(2,2,3)
plt.contourf(x2d, y2d, z_lin, 256)
plt.title('linear')

plt.subplot(2,2,4)
plt.contourf(x2d, y2d, z_cub, 256)
plt.title('cubic')

plt.tight_layout()
plt.show()
#%%

