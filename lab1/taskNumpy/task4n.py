# Задача 4
# Напишите функцию, которая заполняет матрицу с размерами (m,n) случайными числами, распределенными по нормальному закону.
# Затем считает мат. ожидание и дисперсию для каждого из столбцов и строк, а также строит для каждой строки и столбца гистограмму значений (использовать функцию hist из модуля matplotlib.plot).

import numpy as np
import matplotlib.pyplot as plt

def analyze_matrix(m, n, seed=None):
    rng = np.random.default_rng(seed)
    mat = rng.normal(size=(m, n))

    print("Мат. ожидание по строкам:", mat.mean(axis=1))
    print("Дисперсия по строкам:", mat.var(axis=1))
    print("Мат. ожидание по столбцам:", mat.mean(axis=0))
    print("Дисперсия по столбцам:", mat.var(axis=0))

    for i in range(m):
        plt.figure();
        plt.hist(mat[i]);
        plt.title(f'Row {i}');
        plt.show()
    for j in range(n):
        plt.figure();
        plt.hist(mat[:, j]);
        plt.title(f'Col {j}');
        plt.show()

    return mat

# Результаты
analyze_matrix(3, 4, seed=42)
