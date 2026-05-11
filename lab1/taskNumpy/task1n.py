# Задача 1
# Дан набор из p матриц размерностью (n,n) и p векторов размерностью (n,1).
# Найти сумму произведений матриц на векторы.
# Написать тесты для кода

import numpy as np

def sum_prod(X, V):
    result = np.zeros(X[0].shape[0])
    for matrix, vector in zip(X, V):
        result += matrix @ vector.flatten()
    return result

# Тесты
X = [np.eye(3), np.ones((3,3))]
V = [np.array([1,2,3]).reshape(-1,1), np.array([1,0,1]).reshape(-1,1)]
result = sum_prod(X, V)
assert np.array_equal(sum_prod(X, V), [3, 4, 5])
print('Тесты пройдены успешно!')