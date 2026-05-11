# Задача 7
# Дан некий временной ряд.
# Для данного ряда нужно найти его: математическое ожидание, дисперсию, СКО, найти все локальные максимумы и минимумы (локальный максимум - это точка, которая больше своих соседних точек, а локальный минимум - это точка, которая меньше своих соседей), а также вычислить для данного ряда другой ряд, получаемый методом скользящего среднего с размером окна p.
# Примечание: метод скользящего среднего подразумевает нахождение среднего из подмножетсва ряда размером p

import numpy as np

def analyze_series(series, k):
    series = np.array(series)

    mean = np.mean(series)
    var = np.var(series)
    std = np.std(series)

    local_max = [(i, series[i]) for i in range(1, len(series) - 1)
                 if series[i] > series[i - 1] and series[i] > series[i + 1]]
    local_min = [(i, series[i]) for i in range(1, len(series) - 1)
                 if series[i] < series[i - 1] and series[i] < series[i + 1]]

    moving_avg = [np.mean(series[i:i + k]) for i in range(len(series) - k + 1)]

    return {
        'mean': mean,
        'variance': var,
        'std': std,
        'local_max': local_max,
        'local_min': local_min,
        'moving_avg': moving_avg
    }

# Тест
data = [1, 3, 2, 4, 1]
res = analyze_series(data, 2)
assert res['mean'] == 2.2
assert len(res['moving_avg']) == 4
print('Тесты пройдены успешно!')