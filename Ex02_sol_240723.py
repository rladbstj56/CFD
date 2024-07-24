#1
#(a)

N = 100
d = 2.0 * 10 ** (-4)

def my_sum(N,d):
    result = 0.0
    for n in range(0,N+1,1):
        result += n*d
    return result

print(my_sum(N,d))


#(b)

import numpy as np
import matplotlib.pyplot as pl

def ref_sum(N,d):
    return 0.5*d*N*(N+1)
print(ref_sum(N,d))

def Test_sum():
    my = my_sum(6, 2.0e-4) # random number
    ref = ref_sum(6, 2.0e-4) # 2.0*e**(-4)
    if my == ref : print("OK")
    else : 
        print("FAIL")
        print('ref_sum = %1.16f' %ref)
        print('my_sum = %1.16f' %my)
    return

#%%


Test_sum()

#%%

result100 = my_sum(100, 2e-4)

print('result is %1.3f' %result100)

Gresult100 = ref_sum(100, 2e-4)

print('result is %1.3f' %Gresult100)

#%%

#3
#(b),(c)
def fderiv(n): # f derivative function
    if n == 0:
        return np.exp(-1)
    else: 
        return -2*fderiv(n-1)

def f(x): # f function
    f = np.exp(-2*x-1)
    return f

def fact(n):
    factresult = 0.0
    if (n == 0 or n == 1):
        factresult = 1
    else:
        factresult = fact(n-1) * n
    return factresult

def taylor(x,N):
    result = 0
    for n in range(0,N+1):
        result += ((1/fact(n))*fderiv(n)*(x+0.5)**n)
    return result

# 오차 계산 함수
def calculate_errors(x, actual, approx):
    return np.abs(actual - approx)

x = np.linspace(-1, 4, 100) # 100은 random number # it nees to be big enough
y0 = taylor(x,0)
y1 = taylor(x,1)
y2 = taylor(x,2)
y3 = taylor(x,3)
y4 = taylor(x,4)
F = f(x)

errors = calculate_errors(x,F,y4) # 오차 계산
maxerrind = np.argmax(errors) # 배열에서 가장 큰 값의 인덱스 반환
minerrind = np.argmin(errors) # 가장 작은 값
maxerror_x = x[maxerrind] # 오차가 가장 큰 지점의 x좌표
minerror_x = x[minerrind]
maxerrorvalue = errors[maxerrind] # 가장 큰 오차 값
minerrorvalue = errors[minerrind]

print(y0)
print(y1)
print(y2)
print(y3)
print(y4)

#for i in range (1,22,3):
#    pl.plot(x,taylor(x,i), label="TaylorN (N = %i)" %i)
pl.plot(x,y4, label="Taylor Series 4")
pl.plot(x,F, label="ReferenceFunction")
pl.legend() # 범례 (이름, 라벨)
pl.grid()
pl.show()


# 확대된 플롯
pl.plot(x,y4, label="Taylor Series 4")
pl.plot(x,F, label="ReferenceFunction")
pl.xlim(-1.0,1.0)
pl.legend()
pl.grid()
pl.show()

print("가장 큰 오차 : x = %f, 오차 = %f" %(maxerror_x, maxerrorvalue) )
print("가장 작은 오차 : x = %f, 오차 = %f" %(minerror_x, minerrorvalue) )


#4
