# Ex4

#%%

# 1
# (a)
# 여기서 i를 linspace로 정의해서 h와 x까지 생성해서 plot 만드는게 안되고
# x를 직접 linspace로 해서 plot만드는 이유 질문
import numpy as np
import matplotlib.pyplot as pl

def g(x, mu = 0.3, sigma = 1.2):
    return 1/np.sqrt(2*np.pi*(sigma)**2)*np.exp(-(x-mu)**2/(2*(sigma)**2))

N = 100 # random
#i = np.linspace(0,N,N)
h = 10**(-2)
#x = i*h
x = np.linspace(-5,5,N)

pl.plot(x, g(x), 'b', label = 'g(x)')
#pl.xlim(-5,5)
#pl.legend()
#pl.grid()
#pl.show()

#%%

import numpy as np
import matplotlib.pyplot as pl

# (b)

def g1_cal(x, mu = 0.3, sigma = 1.2):
    return -(x-mu)/sigma**2*g(x)
#pl.figure(1)
pl.plot(x, g1_cal(x), 'r-', label = 'g1_cal(x)')
#pl.legend()
#pl.grid()

# (c)

def g1(x):
    dx = x[1] - x[0]
    return (g(x+dx)-g(x-dx))/(2*dx)
#pl.figure(2)
x_ghost = x[1:N-1]
pl.plot(x_ghost, g1(x_ghost), 'g--', label = 'g1(x)')
#pl.legend()
#pl.grid()

#pl.show()

#%%

# (d)

def g2_cal(x, mu = 0.3, sigma = 1.2):
    return -g(x)/sigma**2-(x-mu)/sigma**2*g1(x)

pl.plot(x, g2_cal(x), color = 'coral', label = 'g2_cal(x)')

# (e)

def g2(x):
    return (g1(x+h)-g1(x-h)) / (2*h)

x_2ghost = x[2:N-2]
pl.plot(x_2ghost, g2(x_2ghost), color = 'mediumslateblue', linestyle = '--', label = 'g2(x)')

pl.legend()
pl.grid()
pl.show()

#%%

# (f)

err1 = np.abs(g1_cal(x) - g1(x))
err2 = np.abs(g2_cal(x) - g2(x))

pl.subplot(1,2,1) # row, column, index(1부터 시작)
pl.plot(x,err1,label = 'err1')
pl.plot(x,err2,label = 'err2')
pl.title('Linear')
pl.legend()
pl.grid()

pl.subplot(1,2,2)
pl.semilogy(x,err1,label = 'err1')
pl.semilogy(x,err2,label = 'err2')
pl.title('Semi-log')
pl.legend()
pl.grid()

pl.show()


#%%

# (g)

maxind = np.argmax[g2(x)]
h = 10**(-3)*2/g2(x)[maxind]
print(h)