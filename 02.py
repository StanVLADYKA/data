# создать матрицу, транспорировать, дисперсию и детерминат вывести
# по второй - натим сумму, мин, макс, сумму и произвдвух

import numpy as np


matrix = np.random.randint(0,10, (3,3))

print(matrix)
print(matrix.transpose())
print(np.var(matrix))
print(np.linalg.det(matrix))


arr = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
  ])

print(arr.sum())
print(arr.min())
print(arr.max())
print(arr.size)
print(np.var(arr))

print(np.dot(matrix,arr))