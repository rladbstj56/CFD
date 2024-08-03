# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 11:11:08 2024

@author: 김윤서
"""

# Ex 06

import numpy as np
import matplotlib.pyplot as pl
from mpl_toolkits.mplot3d import Axes3D

b = 8/3
r = 28
s = 10

x0 = -8
y0 = -1
z0 = 33

dt = 1e-3
tStart = 0
tEnd = 40

N = int((tEnd - tStart) / dt)
x = np.zeros(N)
x[0] = x0
y = np.zeros(N)
y[0] = y0
z = np.zeros(N)
z[0] = z0

for i in range(N-1):
    x[i+1] = x[i] + dt*s*(y[i]-x[i])
    y[i+1] = y[i] + dt*((r-z[i])*x[i]-y[i])
    z[i+1] = z[i] + dt*(x[i]*y[i]-b*z[i])
    
print(len(x))

fig, pl2D = pl.subplots(3)

pl2D[0].plot(x,z,label='x vs. z')
pl2D[1].plot(y,z,label='y vs. z')
pl2D[2].plot(x+y,x-y,label='x+y vs. x-y')
#pl.legend()
pl.show()

fig = pl.figure()
pl3D = fig.add_subplot(111, projection = '3d')
pl3D.set_xlabel('x+y')
pl3D.set_ylabel('x-y')
pl3D.set_zlabel('z')
pl3D.plot(x+y,x-y,z,'r-', linewidth = 1)
pl.show()


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

ax3d.plot(x, y, z, 'b-')
ax3d.plot(x, y, z, 'r--')

fig2 = pl.figure()
ax = fig2.add_subplot(111)
ax.plot(x, y, 'b-')
ax.plot(x, y, 'r+')

pl.show()


