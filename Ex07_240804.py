# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 09:57:55 2024

@author: 김윤서
"""

import numpy as np
import matplotlib.pyplot as plt

b = 8./3.
r = 28.
s = 10.
x0 = -8.
y0 = -1.
z0 = 33

dt = 1.e-3
tStart = 0
tEnd = 40

N = int(tEnd / dt) + 1

x = np.zeros(N)
y = np.zeros(N)
z = np.zeros(N)

x[0] = x0
y[0] = y0
z[0] = z0

def Lorenz(x,y,z,N,dt,r,s,b):
    
    for i in range(N-1):
        x[i+1] = x[i] + dt*( s * ( y[i] - x[i] ) )
        y[i+1] = y[i] + dt*((r-z[i])*x[i]-y[i])
        z[i+1] = z[i] + dt*(x[i]*y[i] - b*z[i])
    
    return x, y, z

x, y, z = Lorenz(x,y,z,N,dt,r,s,b)


def Lorenz_mean(x):
    
    xsum = sum(x)
    
    mean = xsum/len(x)
    
    return mean

xmean, ymean, zmean = np.mean(x), np.mean(y), np.mean(z) # compute (simple)
xmean2 = Lorenz_mean(x) # encapsulate the implementation (complex)
ymean2 = Lorenz_mean(y)
zmean2 = Lorenz_mean(z)

#print(f"error of xmean : {abs(xmean - xmean2)}")
#print(f"error of ymean : {abs(ymean - ymean2)}")
#print(f"error of zmean : {abs(zmean - zmean2)}")

"""
plt.figure()

plt.subplot(3,1,1)
plt.plot(x,z)
plt.plot(xmean,zmean,'ko')
plt.xlabel('x')
plt.ylabel('z')
plt.title('x vs z')
plt.grid()

plt.subplot(3,1,2)
plt.plot(y,z)
plt.plot(ymean,zmean,'ko')
plt.xlabel('y')
plt.ylabel('z')
plt.title('y vs z')
plt.grid()

plt.subplot(3,1,3)
plt.plot(x+y,x-y)
plt.plot(xmean+ymean,xmean-ymean,'ko')
plt.xlabel('x+y')
plt.ylabel('x-y')
plt.title('x+y vs x-y')
plt.grid()

plt.tight_layout()
plt.show()

"""


#%%

def Lorenz_std(x):
    
    mean = Lorenz_mean(x)
    
    std = np.sqrt(sum((x-mean)**2)/len(x))
    
    return std


xstd, ystd, zstd = np.std(x), np.std(y), np.std(z) # compute (simple)
xstd2 = Lorenz_std(x) # encapsulate the implementation (complex)
ystd2 = Lorenz_std(y)
zstd2 = Lorenz_std(z)

#print(f"x std : {xstd}, {xstd2}")
#print(f"y std : {ystd}, {ystd2}")
#print(f"z std : {zstd}, {zstd2}")


#%%

"""
M = 200

plt.figure()

plt.subplot(3,1,1)
plt.hist(x, bins = M)
plt.title('x histogram')

plt.subplot(3,1,2)
plt.hist(y, bins = M)
plt.title('y histogram')

plt.subplot(3,1,3)
plt.hist(z, bins = M)
plt.title('z histogram')

plt.tight_layout()
plt.show()



plt.figure()

plt.subplot(3,1,1)
plt.hist(x, bins = M, density = True)
plt.title('x PDF')

plt.subplot(3,1,2)
plt.hist(y, bins = M, density = True)
plt.title('y PDF')

plt.subplot(3,1,3)
plt.hist(z, bins = M, density = True)
plt.title('z PDF')

plt.tight_layout()
plt.show()

"""


#%%

"""
M = 40

plt.figure()

plt.subplot(1,2,1)
plt.hist2d(x+y, x-y, bins = M)
plt.title('x+y vs x-y 2D histogram')

plt.subplot(1,2,2)
plt.hist2d(x+y, x-y, bins = M, density = True)
plt.title('x+y vs x-y 2D PDF')

plt.tight_layout()
plt.show()
"""

#%%

fivesec = int(5 / dt)

def first(x):
    return x[:fivesec]

def last(x):
    return x[-fivesec:]

def firstmean(x,y,z):
    return Lorenz_mean(first(x)), Lorenz_mean(first(y)), Lorenz_mean(first(z))

def firststd(x,y,z):
    return Lorenz_std(first(x)), Lorenz_std(first(y)), Lorenz_std(first(z))

first_mean = firstmean(x,y,z)
first_std = firststd(x,y,z)

def lastmean(x,y,z):
    return Lorenz_mean(last(x)), Lorenz_mean(last(y)), Lorenz_mean(last(z))

def laststd(x,y,z):
    return Lorenz_std(last(x)), Lorenz_std(last(y)), Lorenz_std(last(z))

last_mean = lastmean(x,y,z)
last_std = laststd(x,y,z)

"""
print("0<=t<=40")
print(xmean, ymean, zmean)
print(xstd,ystd,zstd)
print("0<=t<=5")
print(first_mean)
print(first_std)
print("35<=t<=40")
print(last_mean)
print(last_std)
"""

#%%

x0y0z0_list = [(-8., -1., 33.), (-2., -10., 45.)]

for l in x0y0z0_list:
    x0 = l[0]
    y0 = l[1]
    z0 = l[2]
    
    x = np.zeros(N)
    y = np.zeros(N)
    z = np.zeros(N)

    x[0] = x0
    y[0] = y0
    z[0] = z0
    
    x,y,z = Lorenz(x,y,z,N,dt,r,s,b)
    
    xmean, ymean, zmean = np.mean(x), np.mean(y), np.mean(z)
    xstd, ystd, zstd = np.std(x), np.std(y), np.std(z) # compute (simple)

    plt.figure()

    plt.subplot(3,1,1)
    plt.plot(x,z)
    plt.plot(xmean,zmean,'ko')
    plt.xlabel('x')
    plt.ylabel('z')
    plt.title('x vs z')
    plt.grid()

    plt.subplot(3,1,2)
    plt.plot(y,z)
    plt.plot(ymean,zmean,'ko')
    plt.xlabel('y')
    plt.ylabel('z')
    plt.title('y vs z')
    plt.grid()

    plt.subplot(3,1,3)
    plt.plot(x+y,x-y)
    plt.plot(xmean+ymean,xmean-ymean,'ko')
    plt.xlabel('x+y')
    plt.ylabel('x-y')
    plt.title('x+y vs x-y')
    plt.grid()

    plt.tight_layout()
    plt.show()

    print(f"x std : {xstd}, {xstd2}")
    print(f"y std : {ystd}, {ystd2}")
    print(f"z std : {zstd}, {zstd2}")
    
    
#%%

rsb_list = [[28.,10.,8./3.], [10., 5., 1]]

for l in rsb_list:
    
    r = l[0]
    s = l[1]
    b = l[2]
    
    x0 = -8.
    y0 = -1.
    z0 = 33
    
    x = np.zeros(N)
    y = np.zeros(N)
    z = np.zeros(N)

    x[0] = x0
    y[0] = y0
    z[0] = z0
    
    x, y, z = Lorenz(x,y,z,N,dt,r=r,s=s,b=b)
    
    xmean, ymean, zmean = np.mean(x), np.mean(y), np.mean(z)
    xstd, ystd, zstd = np.std(x), np.std(y), np.std(z) # compute (simple)

    plt.figure()

    plt.subplot(3,1,1)
    plt.plot(x,z)
    plt.plot(xmean,zmean,'ko')
    plt.xlabel('x')
    plt.ylabel('z')
    plt.title('x vs z')
    plt.grid()

    plt.subplot(3,1,2)
    plt.plot(y,z)
    plt.plot(ymean,zmean,'ko')
    plt.xlabel('y')
    plt.ylabel('z')
    plt.title('y vs z')
    plt.grid()

    plt.subplot(3,1,3)
    plt.plot(x+y,x-y)
    plt.plot(xmean+ymean,xmean-ymean,'ko')
    plt.xlabel('x+y')
    plt.ylabel('x-y')
    plt.title('x+y vs x-y')
    plt.grid()

    plt.tight_layout()
    plt.show()

    print(f"x std : {xstd}, {xstd2}")
    print(f"y std : {ystd}, {ystd2}")
    print(f"z std : {zstd}, {zstd2}")