import random

import numpy as np

array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(type(array))
print(array.shape)

matrix = np.zeros((5, 5), dtype=int)
matrix1 = np.random.randint((10, 10))
print(matrix)
print(matrix1)

first = np.array([1, 2, 3])
second = np.array([1, 2, 3])

print((first + second) * random.randint(1, 1000))
