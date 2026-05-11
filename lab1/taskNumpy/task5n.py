# Задача 5
#Напишите функцию, которая заполняет матрицу (m,n) в шахматном порядке заданными числами a и b.
# Напишите тесты для кода

import numpy as np

def chess(m, n, a, b):
    result = np.zeros((m, n))
    result[::2, ::2] = a
    result[1::2, 1::2] = a
    result[::2, 1::2] = b
    result[1::2, ::2] = b
    return result

# Тесты
assert np.array_equal(chess(3,3,1,0), [[1,0,1],[0,1,0],[1,0,1]])
assert np.array_equal(chess(2,4,5,9), [[5,9,5,9],[9,5,9,5]])
print('Тесты пройдены успешно!')