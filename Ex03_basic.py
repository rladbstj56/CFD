import numpy as np
import matplotlib.pyplot as pl

#%%

N1 = 5
N2 = 3
N3 = 2
matrix1 = np.zeros((N1,N2))
matrix = np.zeros((N1,N2,N3)) # np.ones는 모든 요소가 1인 행렬 생성

full_matrix = np.full((2, 3), 7) # (shape, fill_value) 7로 채운 행렬 생성
print(full_matrix)

random_matrix = np.random.random((3, 3, 3)) # random 0~1 value 로 채워진 행렬 생성
print(random_matrix)
print(random_matrix[:,0,0])

element = matrix[1,2,0]

print(element)

matrix[1,2,0] = 99.
element = matrix[1,2,0]

print(matrix)
print(element)

xslice = matrix[0:N1+1:1,0,0] # start index : end index + 1 : step

matrix[:,0,0] = np.linspace(-np.pi,np.pi,N1)
print(matrix)

# 0 ~ 10 까지의 숫자 생성 (10은 포함 X)
array = np.arange(10)

# 2 ~ 10 까지 2씩 증가하는 숫자 생성 (10은 포함 X)
array = np.arange(2, 10, 2)

# 원본 배열 생성
original_array = np.array([1, 2, 3, 4, 5])

# 배열 복사
copied_array = original_array.copy()

# 원본 배열 수정
original_array[0] = 99

print("원본 배열 :", original_array)
print("복사된 배열 : ", copied_array)

#%%

import numpy as np
import matplotlib.pyplot as pl

# 2-D Equidistant Grid
x = np.linspace(0, 1, 5)
y = np.linspace(0, 1, 5)

X, Y = np.meshgrid(x, y)
print("X:\n", X)
print("Y:\n", Y)

pl.scatter(X, Y, color='b')

pl.show()

# 2-D Stretched Grid
x = np.linspace(0, 1, 5)**2
y = np.linspace(0, 1, 5)**2

X, Y = np.meshgrid(x, y)
print("X:\n", X)
print("Y:\n", Y)

# 공백자는 ,로 표시
np.savetxt('grid_x.csv', X, delimiter=',')
np.savetxt('grid_y.csv', Y, delimiter=',')

pl.scatter(X, Y, color='b')

pl.show()



# %%
