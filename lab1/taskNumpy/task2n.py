# Задача 2
# Дана матрица M, напишите функцию, которая бинаризует матрицу по некоторому threshold (то есть, все значения большие threshold становятся равными 1, иначе 0).
# Напишите тесты для кода

import numpy as np

def binarize(M, threshold=0.5):
    return (M > threshold).astype(int)

# Тесты
M = np.array([[0.3, 0.7], [0.5, 0.9]])
assert np.array_equal(binarize(M), [[0,1],[0,1]])
assert np.array_equal(binarize(M, 0.6), [[0,1],[0,1]])
print('Тесты пройдены успешно!')