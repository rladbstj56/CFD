# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 16:35:13 2024
#ex01
@author: 김윤서
"""
#(a)

import numpy as np
import matplotlib.pyplot as pl

#(b)
x = np.linspace(0,1,11)
print(x)

#(c)
#dx=0.025
#for i in range(0,1,dx):
#   x[i]=float(i*dx)
#print(x)
x = np.linspace(0,1,41)
print(x)

#(d)
pi=np.pi
print(pi)
y=1-2*x #f1(x)
g=(x-0.4)**2 #f2(x)
h=np.sin(2*pi*x) #f3(x)
pl.plot(x,y,label='y=f1(x)')
pl.plot(x,g,label='y=f2(x)')
pl.plot(x,h,label='y=f3(x)')
pl.legend()

#(e)
pl.title(f'Figure 1')
pl.xlabel('x')
pl.ylabel('y')
pl.xlim(0,1)
pl.ylim(-1.2,1.2)
pl.grid() #격자
pl.show()

#(f)
pl.plot(x,h,label='f3(x) additional task')
pl.xlim(0,0.5)
pl.ylim(-1.2,1.2)
pl.show()

