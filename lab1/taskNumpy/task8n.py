# Задача 8
# Дан некоторый вектор с целочисленными метками классов, напишите функцию, которая выполняет one-hot-encoding для данного вектора
# One-hot-encoding - представление, в котором на месте метки некоторого класса стоит 1, в остальных позициях стоит 0.
# Например для вектора [0, 2, 3, 0] one-hot-encoding выглядит как: [[1, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [1, 0, 0, 0]]

import numpy as np

def one_hot_encode(labels):
    labels = np.array(labels)
    n_classes = labels.max() + 1
    result = np.zeros((len(labels), n_classes), dtype=int)
    result[np.arange(len(labels)), labels] = 1
    return result.tolist()

# Тест
assert one_hot_encode([0,2,3,0]) == [[1,0,0,0],[0,0,1,0],[0,0,0,1],[1,0,0,0]]
print('Тесты пройдены успешно!')