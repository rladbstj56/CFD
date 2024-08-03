# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 15:21:18 2024

@author: 김윤서
"""

import numpy as np
import matplotlib.pyplot as plt

b = 8./3.
r = 28.
s = 10.

x0 = -8.
y0 = -1.
z0 = 33.


def integrate_lorenz(x0, y0, z0, dt, N):
    x = np.zeros(N) # x[0] ~ x[N-1]
    y = np.zeros(N)
    z = np.zeros(N)
    
    x[0] = x0
    y[0] = y0
    z[0] = z0
    
    for i in range(0, N-1):
        x[i+1] = x[i] + dt * (s*(y[i]-x[i]))
        y[i+1] = y[i] + dt * ((r-z[i])*x[i]-y[i])
        z[i+1] = z[i] + dt * (x[i]*y[i]-b*z[i])

    return x, y, z

dt = 1.e-3
N = int(40 / dt)

x, y, z = integrate_lorenz(x0, y0, z0, dt, N)


plt.subplot(3,1,1)
plt.plot(x,z)
plt.xlabel('x')
plt.ylabel('z')
plt.title('x vs z')
plt.grid()

plt.subplot(3,1,2)
plt.plot(y,z)
plt.xlabel('y')
plt.ylabel('z')
plt.title('y vs z')
plt.grid()

plt.subplot(3,1,3)
plt.plot(x+y,x-y)
plt.xlabel('x+y')
plt.ylabel('x-y')
plt.title('x+y vs x-y')
plt.grid()

plt.tight_layout()
plt.show()


#%%

fig = plt.figure()
ax3d = fig.add_subplot(111, projection='3d')
ax3d.plot(x+y, x-y, z, lw=0.5) # line width = 0.5
ax3d.set_xlabel('x+y')
ax3d.set_ylabel('x-y')
ax3d.set_zlabel('z')
ax3d.set_title('Lorenz 3D plot')
plt.show()
