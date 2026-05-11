# Задача 3
# Напишите функцию, которая возвращает уникальные элементы из каждой строки матрицы.
# Напишите такую же функцию, но для столбцов.
# Напишите тесты для кода

import numpy as np

def unique_rows(mat):
    return [np.unique(row) for row in mat]

def unique_columns(mat):
    return [np.unique(mat[:, j]) for j in range(mat.shape[1])]

# Тесты
mat = np.array([[1,2,2],[3,3,4]])
result_rows = unique_rows(mat)
assert len(result_rows) == 2
assert list(result_rows[0]) == [1, 2]
assert list(result_rows[1]) == [3, 4]

result_cols = unique_columns(mat)
assert len(result_cols) == 3
assert list(result_cols[0]) == [1, 3]
assert list(result_cols[1]) == [2, 3]
assert list(result_cols[2]) == [2, 4]
print('Тесты пройдены успешно!')