#1
#(a)

import numpy as np
import matplotlib.pyplot as pl

# 이미 정해진 값으로 list 생성
A = [[11,12, 13], [21, 22, 23]]

A2D = np.array(A)
print(A2D)

#(b)
A2D[1, 2] = 99 # a23 <- 99
print(A2D)

#(c)
#nonexisting = A2D[4, 4]
#print(nonexisting)

#exception has occured: IndexError
#index 4 is out of bounds for axis 0 wth size 2

#%%

import numpy as np
import matplotlib.pyplot as pl

#2
#(a)
x = np.linspace(0, 4, 50)
y = np.linspace(-1, 1, 30)
X, Y = np.meshgrid(x, y)

#(b)
#pl.scatter(X, Y, color='b')
pl.show()


#%%
import numpy as np
import matplotlib.pyplot as pl

#(c)&(d)
nx = int(input("Enter the number of cells in the x direction : "))
ny = int(input("Enter the number of cells in the y direction : "))


x = np.linspace(0, 4, nx)
y = np.linspace(-1, 1, ny)
X, Y = np.meshgrid(x, y)
pl.scatter(X, Y, color = 'green', alpha = 0.5)
pl.show()

np.savetxt("Ex03_input_x", X, delimiter = ',')
np.savetxt("Ex03_input_y", Y, delimiter = ',')

# %%

import numpy as np
import matplotlib.pyplot as pl

#3
#(a)

x = np.linspace(0, 4, 5)
y = np.linspace(-1, 1, 10)

X, Y = np.meshgrid(x, y)
np.savetxt("Ex03_equix", X, delimiter = ',')
np.savetxt("Ex03_equiy", Y, delimiter = ',')

print("It's X\n", X)
print("It's Y\n", Y)

def stretching_function(xi, a=0.99):
    #Arg is grid coordinate that runs between 0 and 1
    b = 0.5 * np.log((1+a)/(1-a))
    return np.tanh(b*(xi-0.5))/np.tanh(b/2.)

# generate grid for [0,1] for y coordinate
xi = np.linspace(0., 1., len(y))

y = stretching_function(xi)

x2d, y2d = np.meshgrid(x, y)

pl.scatter(x2d, y2d, color = 'r')
#pl.show() # equi plot이랑 같이 보여주기 위해서

x2d_equi = np.loadtxt("Ex03_equix", delimiter = ',')
y2d_equi = np.loadtxt("Ex03_equiy", delimiter = ',')

pl.scatter(x2d_equi, y2d_equi, color = 'b')
pl.show()

# %%


import numpy as np
import matplotlib.pyplot as pl

#4

from numpy import random as rnd

# (a)
def scalar(x, y):
    return np.sin(2*np.pi*x)*np.cos(8*np.pi*y)*np.exp(-4*y**2)

# (b)
# high resolution structured Cartesian
unit = np.linspace(0, 1, 200)
x1d = y1d = unit
x2d, y2d = np.meshgrid(x1d, y1d)

# (c)
# get scalar for high resolution grid
z2d = scalar(x2d, y2d)
# pl.contourf(x2d, y2d, z2d, 256)

# (d)
# low resolution unstructured random
points = rnd.random_sample((100, 2)) # row : 100, column : 2
x_pts = points[:,0]
y_pts = points[:,1]
xpts2d, ypts2d = np.meshgrid(x_pts, y_pts)

pl.scatter(x_pts, y_pts, color = 'k', s = 3) # color : black, size : 3

# (e)
# get scalar for low resolution unstructured points
z_pts = scalar(x_pts, y_pts)
# 여기부터는 contourf 만들려고 그냥 2차원으로 만들어봄
zpts2d = scalar(xpts2d, ypts2d)
pl.contourf(xpts2d, ypts2d, zpts2d, 256)

pl.show()

# %%
