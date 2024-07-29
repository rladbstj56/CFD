#(a)

import numpy as np
import matplotlib.pyplot as pl

#(b)
N = 11
x = np.linspace(0,1,N)
print(x)

#%%

#(c)
delta_x = 0.025
N = int(1/delta_x)+1 # 1:total length(L)
x = np.linspace(0,1,N) # 양쪽 0과 1까지 카운트하므로 N
print(x)

#(d)

def f_1(x):
    return 1 - 2*x
def f_2(x):
    return (x-0.4)**2
def f_3(x):
    return np.sin(2*np.pi*x)

y1 = f_1(x)
y2 = f_2(x)
y3 = f_3(x)

print('여기까지가 print 되기 전')
print(y1)
print(y2)
print(y3)
print('여기까지가 print')
pl.figure()
pl.plot(x,y1,label='y=f1(x)')
pl.plot(x,y2,label='y=f2(x)')
pl.plot(x,y3,label='y=f3(x)')
pl.legend()

#(e)
pl.title('Figure 1')
pl.xlabel('x')
pl.ylabel('y')
pl.xlim(0,1)
pl.ylim(-1.2,1.2)
pl.grid() #격자
pl.show()



#(f)
pl.figure()
pl.plot(x,y3,label='f3(x) additional task')
pl.xlim(0,0.5)
pl.ylim(-1.2,1.2)
pl.show()







# %%
