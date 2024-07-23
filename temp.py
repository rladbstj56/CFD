# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print('Hello')

i=5
pi=3.14159265358979323844

print(pi, i)
print("pi = %1.6f \t i = %i" %(pi,i,))

a = 3; b = 2
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a/float(b))
print(a//b) #몫만을 반환
print(a%b)


def myFunc(x, a=1, b=0) :
    y = a*x + b
    return y

z=myFunc(1,b=-1) #a=1(default)
print(z)

a=(1+2+3
   +4+5+6)
print(a)

if round(pi) == 3:
    print('OK')
else :
    print("rounding_error!")
    exit()
    
for i in 1,2,3,4 :
    x = 0.25*i
    print(x)
    #%%
    
import numpy as np
import matplotlib.pyplot as pl

pi=np.pi
y=np.sin(pi/2)
print(y)
a=np.zeros(10) # create a NumPy array of length 10 and initialize with zeros
print(a)
for i in range(0, len(a), 1) :
    a[i]=i*0.5
print(a)
#%%

#numpy.linspace(start,stop,num=50,endpoint=True,retstep=False,dtype=None,axis=0)
#시작점과 끝점 사이를 균등하게 나눈 값을 포함하는 배열을 만듦
#num: 생성할 샘플 수
#endpoint: True면 마지막 값을 포함하고, False면 마지막 값을 포함하지 않음
#retstep: True면 샘플 간의 간격도 반환
#dtype: 반환할 배열의 데이터 타입
x,dx = np.linspace(-1.,3.,7,retstep=True) # i=1,...,7 vertices -1<xi<3
print('여기가 linspace')
#%%
print(x)
#dx=x[1]-x[0]
print('dx는 샘플간의 간격')
print(dx)

#%%
y=np.zeros_like(x) #array of zeros with the same shape as x
z=np.zeros_like(x)
for i in range(0,len(x),1) :
    y[i]=x[i]**3 - 5
print(y)
z=x**3-5
print(z)
z[::2]=0*x[::2]
print(z)
#%%

pl.plot(x,y,'o-',label='my data')
pl.legend()
pl.savefig('myPlot.png')
pl.savefig('myPlot.pdf')













