# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 13:22:21 2024

@author: 김윤서
"""

import numpy as np
import matplotlib.pyplot as plt

dt = 1e-3
tStart = 0
tEnd = 40
N = (tEnd - tStart)/dt + 1

x = -8.
y = -1.
z = 33.

b = 8./3.
r = 28.
s = 10.

# initialize array
xa = [x]
ya = [y]
za = [z]

xsum = x
ysum = y
zsum = z

xsqsum = x**2
ysqsum = y**2
zsqsum = z**2

t = 0

xsq = [x**2]
ysq = [y**2]
zsq = [z**2]

while t < tEnd:
    xn = x + dt*s*(y-x)
    yn = y + dt*((r-z)*x-y)
    zn = z + dt*(x*y-b*z)
    
    xa.append(xn)
    ya.append(yn)
    za.append(zn)
    
    xsq.append(xn**2)
    ysq.append(yn**2)
    zsq.append(zn**2)
    
    xsum += xn
    ysum += yn
    zsum += zn
    
    xsqsum += xn**2
    ysqsum += yn**2
    zsqsum += zn**2
    
    x = xn
    y = yn
    z = zn
    t += dt

    
# 1 
# (a), (b), (c)

x = np.array(xa[:40001])
y = np.array(ya[:40001])
z = np.array(za[:40001])

print("This is N = ", N)
print("This is length", len(xa), len(ya), len(za), len(x), len(y), len(z))

def mean(x):
    return sum(x)/len(x)

meanx = xsum/N
print("Mean of X is ", meanx, np.mean(xa), xsum/len(xa))
meany = ysum/N
print("Mean of Y is ", meany, np.mean(ya), ysum/len(ya))
meanz = zsum/N
print("Mean of Z is ", meanz, np.mean(za), zsum/len(za))

meanxsq = xsqsum/N
print(meanxsq)
meanysq = ysqsum/N
print(meanysq)
meanzsq = zsqsum/N
print(meanzsq)

plt.figure(1)

plt.subplot(2,2,1) # index from 1 to 4
plt.plot(xa, za)
plt.plot(mean(x), mean(z), 'ko')
plt.title('x vs. z') # linestyle = 'ko'

plt.subplot(2,2,2)
plt.plot(ya, za)
plt.plot(mean(y), mean(z), 'ko')
plt.title('y vs. z')

plt.subplot(2,2,3)
plt.plot(x+y, x-y)
plt.plot(meanx+meany, meanx-meany, 'ko')
plt.title('x+y vs. x-y')

plt.tight_layout() # 플롯 사이의 겹침 방지
plt.show()

# 2

devx = np.sqrt(meanxsq - meanx**2)
#print(devx)
devy = np.sqrt(meanysq - meany**2)
#print(devy)
devz = np.sqrt(meanzsq - meanz**2)
#print(devz) 

def deviation(x):
    return np.sqrt((sum((x-mean(x))**2))/len(x))
devx_ = deviation(x)
print("devx = ",devx,devx_)
devy_ = deviation(y)
print("devy = ",devy,devy_)
devz_ = deviation(z)
print("devz = ",devz,devz_)


#%%

# 3

"""
M = 200

plt.figure(2)

plt.subplot(2,2,1)
plt.hist(xa, bins = M) 
# bins 개수만큼의 구간을 나누어
# 그 구간에 해당되는 xa의 value 개수만큼 높이를 쌓아올림
plt.title('x')

plt.subplot(2,2,2)
plt.hist(ya, bins = M)
plt.title('y')

plt.subplot(2,2,3)
plt.hist(za, bins = M)
plt.title('z')

plt.show()


plt.figure(3)

plt.subplot(3,2,1)
plt.hist(xa, bins = M, density = True, alpha = 0.5, color = 'green')
plt.title('density x')

plt.subplot(3,2,2)
plt.hist(xa, bins = M, alpha = 0.5, color = 'orange')
plt.title('frequency x')

plt.subplot(3,2,3)
plt.hist(ya, bins = M, density = True, alpha = 0.5, color = 'green')
plt.title('density y')

plt.subplot(3,2,4)
plt.hist(ya, bins = M, alpha = 0.5, color = 'orange')
plt.title('density y')

plt.subplot(3,2,5)
plt.hist(za, bins = M, density = True, alpha = 0.5, color = 'green')
plt.title('density z')

plt.subplot(3,2,6)
plt.hist(za, bins = M, alpha = 0.5, color = 'orange')
plt.title('frequency z')

plt.show()

"""

#%%

# 4

plt.figure(4)
plt.subplot(1,2,1)
plt.hist2d(x+y, x-y, bins = 40)
plt.title('frequency : x+y vs. x-y')

plt.subplot(1,2,2)
plt.hist2d(x+y, x-y, bins = 40, density = True)
plt.title('density : x+y vs. x-y')

plt.show()


# 5

firstrange = int(5 / dt + 1)

def first(x):
    return x[0:firstrange]

def last(x):
    return x[-firstrange:]

t = np.arange(tStart, tEnd + dt, dt) # pdf에 적힌 방법

print("mean : ", meanx, mean(first(x)), mean(x[t<5]), mean(last(x)), mean(x[t>35]))
print("mean : ", meany, mean(first(y)), mean(y[t<5]), mean(last(y)), mean(x[t>35]))
print("mean : ", meanz, mean(first(z)), mean(z[t<5]), mean(last(z)), mean(x[t>35]))


print("dev : ", deviation(x), deviation(first(x)), deviation(last(x)))
print(deviation(x[t<5]), deviation(x[t>35]))
print("dev : ", deviation(y), deviation(first(y)), deviation(last(y)))
print("dev : ", deviation(z), deviation(first(z)), deviation(last(z)))


# 6

boundary_list = [(-8., -1., 33.), (-2., -10., 45.)]

for l in boundary_list:
    x0 = l[0]
    y0 = l[1]
    z0 = l[2]
    
    xa = [x0]
    ya = [y0]
    za = [z0]
    
    t = tStart
    
    x = x0
    y = y0
    z = z0
    
    while t < tEnd:
        xn = x + dt*s*(y-x)
        yn = y + dt*((r-z)*x-y)
        zn = z + dt*(x*y-b*z)
        
        xa.append(xn)
        ya.append(yn)
        za.append(zn)
        
        x = xn
        y = yn
        z = zn
        t += dt

    x = np.array(xa)
    y = np.array(ya)
    z = np.array(za)
    
    print(l)
    print("mean x : ", mean(x))
    print("mean y : ", mean(y))
    print("mean z : ", mean(z))
    print("\n")
    print("std x : ", deviation(x))
    print("std y : ", deviation(y))
    print("std z : ", deviation(z))
    print("\n")
    
    
# 7

boundary_list = [(8./3., 28., 10.), (5., 15., 15.)]

for l in boundary_list:
    b = l[0]
    r = l[1]
    s = l[2]
    
    xa = [x0]
    ya = [y0]
    za = [z0]
    
    t = tStart
    
    x = x0
    y = y0
    z = z0
    
    while t < tEnd:
        xn = x + dt*s*(y-x)
        yn = y + dt*((r-z)*x-y)
        zn = z + dt*(x*y-b*z)
        
        xa.append(xn)
        ya.append(yn)
        za.append(zn)
        
        x = xn
        y = yn
        z = zn
        t += dt

    x = np.array(xa)
    y = np.array(ya)
    z = np.array(za)
    
    print(l)
    print("mean x : ", mean(x))
    print("mean y : ", mean(y))
    print("mean z : ", mean(z))
    print("\n")
    print("std x : ", deviation(x))
    print("std y : ", deviation(y))
    print("std z : ", deviation(z))
    print("\n")
