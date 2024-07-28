# Ex5

# 1
# (a)

import numpy as np
import matplotlib.pyplot as pl

I = np.log(2)

# (b)

def f(x):
    return 1/(1 + x)

def lowersum(N):
    result = 0.0
    h = 1./(N+1)
    
    for n in range(N):
        result += f(n*h)*h
        
    epsilon = np.abs(result - I)
    
    rel = epsilon/I
    
    print("epsilon = ", epsilon)
    
    return h, rel


# (c)


def uppersum(N):
    result = 0.0
    h = 1./(N+1)
    
    for n in range(N):
        result += f((n+1)*h)*h
        
    epsilon = np.abs(result - I)
    
    rel = epsilon/I
    
    print("epsilon = ", epsilon)
    
    return h, rel

def trapezoidal(N):
    result = 0.0
    x, h = np.linspace(0., 1., N+1, retstep = True)
    
    y = f(x)
    
    for n in range(N):
        result += (y[n]+y[n+1])*h/2
        
    epsilon = np.abs(result - I)
    
    rel = epsilon/I
    
    print("epsilon = ", epsilon)
    
    return h, rel

h, rel = lowersum(102)

N = 100
h, rel = trapezoidal(N)
pl.plot(h, rel, 'bo')

N = 10000
h, rel = trapezoidal(N)
pl.plot(h, rel, 'rs')

N = 1000000
h, rel = trapezoidal(N)
pl.plot(h, rel, 'gd')

#pl.show()

# (d)

hmin = 1.e-8
hmax = 1.e-1
N = 100
x = np.linspace(hmin, hmax, N)


eps1 = 0.35*x
pl.loglog(x,eps1,'k--')

eps2 = 0.1*x**2
pl.loglog(x,eps2,'k:')
    
pl.show()


