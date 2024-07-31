# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 09:25:06 2024

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

x = np.array(xa)
y = np.array(ya)
z = np.array(za)

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

"""
# 3

M = 200

fig, axs = plt.subplots(2,2)

axs[0,0].hist(xa, bins = M)
axs[0,1].hist(ya, bins = M)
axs[1,0].hist(za, bins = M)

plt.show()

fig, pdf = plt.subplots(2,2)

pdf[0,0].hist(xa, bins = M, density = True)
pdf[0,1].hist(ya, bins = M, density = True)
pdf[1,0].hist(za, bins = M, density = True)

plt.show()
"""

"""
# 4

fig = plt.figure()
plt.hist2d(x+y, x-y, bins = 40)
plt.show()
print("it's well done")

fig = plt.figure()
plt.hist2d(x+y, x-y, bins = 40, density = True)
plt.show()
"""

# 5

firstrange = int(5 / dt + 1)

def first(x):
    return x[0:firstrange]

def last(x):
    return x[-firstrange:]

print("mean : ", meanx, mean(first(x)), mean(last(x)))
print("mean : ", meany, mean(first(y)), mean(last(y)))
print("mean : ", meanz, mean(first(z)), mean(last(z)))


print("dev : ", deviation(x), deviation(first(x)), deviation(last(x)))
print("dev : ", deviation(y), deviation(first(y)), deviation(last(y)))
print("dev : ", deviation(z), deviation(first(z)), deviation(last(z)))



