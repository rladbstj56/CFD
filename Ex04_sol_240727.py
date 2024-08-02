# Ex4

#%%

# 1
# (a)

import numpy as np
import matplotlib.pyplot as pl

def g(x, mu = 0.3, sigma = 1.2):
    return 1/np.sqrt(2*np.pi*(sigma)**2)*np.exp(-(x-mu)**2/(2*(sigma)**2))

N = 100 # random
x = np.linspace(-5,5,N+1)
dx = x[1] - x[0]

y = g(x)

pl.figure(1)
pl.plot(x, y, 'b', label = 'g(x)')

def g1(y, dx):
    tmp = np.zeros_like(y)
    tmp[1:-1] = (y[2:] - y[0:-2]) / (2*dx)
    return tmp

y1 = g1(y,dx)
pl.plot(x, y1, color = 'coral', label = 'g1(x)')

def g2(y, dx):
    tmp = np.zeros_like(y)
    tmp[1:-1] = (y[2:]-2*y[1:-1]+y[0:-2])/(dx**2)
    return tmp

y2 = g2(y,dx)
pl.plot(x, y2, 'r-', label = 'g2(x)')

def g1_cal(x, mu = 0.3, sigma = 1.2):
    return -(x-mu)/sigma**2*g(x)

#pl.figure(1)
y1cal = g1_cal(x)
pl.plot(x, y1cal, color = 'mediumslateblue', linestyle = '--', label = 'g1_cal(x)')
#pl.legend()
#pl.grid()

def g2_cal(x, mu = 0.3, sigma = 1.2):
    return - (1./sigma**2 - (x-mu)**2/sigma**4) * g(x)

y2cal = g2_cal(x)
pl.plot(x, y2cal, 'g--' , label = 'g2_cal(x)')

pl.legend()
pl.grid()
pl.show()

err1 = np.abs(y1cal - y1)
err2 = np.abs(y2cal - y2)

pl.figure(2)
#pl.subplot(1,2,1) # row, column, index(1부터 시작)
pl.plot(x,err1,label = 'err1')
pl.plot(x,err2,label = 'err2')
pl.title('Linear')
pl.legend()
pl.grid()
pl.show()

pl.figure(3)
#pl.subplot(1,2,2)
pl.semilogy(x,err1,label = 'err1')
pl.semilogy(x,err2,label = 'err2')
pl.title('Semi-log')
pl.legend()
pl.grid()

pl.show()