# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 12:38:26 2024

@author: 김윤서
"""

# Ex 06

import numpy as np
import matplotlib.pyplot as pl
from mpl_toolkits.mplot3d import Axes3D

b = 8./3.
r = 28.
s = 10.
x = -8.
y = -1.
z = 33.

tStart = 0
tEnd = 40.
dt = 1.0e-3
t = tStart

# animation
#myplot = pl.plot(x, y, 'o')
#pl.xlim([-10., 0.])
#pl.ylim([-5., 5.])

# initialize storage
xa = [x]
ya = [y]
za = [z]
ta = [t]

# do time loop
n = 0
while t < tEnd:
    
    # discretized ODE system (update step)
    xn = x + dt * s * (y-x)
    yn = y + dt * ( (r-z)*x - y )
    zn = z + dt * (x*y - b*z)
    
    # synchronize the slution
    x = xn
    y = yn
    z = zn
    
    t += dt # increment time
    n += 1  # increment time step counter
    
    #pl.plot(x, y, 'b.')
    
    # animation
    #pl.setp(myplot[0], xdata = x, ydata = y)
    #pl.pause(0.1)
    
    xa.append(x)
    ya.append(y)
    za.append(z)


np.savetxt('xdata.dat', xa)
np.savetxt('ydata.dat', ya)
np.savetxt('zdata.dat', za)
np.savetxt('tdata.dat', ta)

xb = np.loadtxt('xdata.dat')
yb = np.loadtxt('ydata.dat')
zb = np.loadtxt('zdata.dat')
tb = np.loadtxt('tdata.dat')

xa = np.array(xa)
ya = np.array(ya)
za = np.array(za)
ta = np.array(ta)


fig3d = pl.figure() # 새로운 'figure' 객체 생성, 플롯이 그려질 전체 창(캔버스)
# 3D subplot을 figure에 추가
# 111 : 1행 1열에 첫번째 서브플롯 추가
# projection : 3D plot 생성
ax3d = fig3d.add_subplot(111, projection = '3d') 

# 3D plot 초기 뷰 설정 (관찰자 위치)
ax3d.view_init(azim=105., elev=28.)

ax3d.set_xlabel('x')
ax3d.set_ylabel('y')
ax3d.set_zlabel('z')

ax3d.plot(xa, ya, za, 'b-')
ax3d.plot(xb, yb, zb, 'r--')

fig2 = pl.figure()
ax = fig2.add_subplot(111)
ax.plot(xa, ya, 'b-')
ax.plot(xb, yb, 'r+')

pl.show()
