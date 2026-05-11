# Задача 6
# Напишите функцию, которая отрисовывает прямоугольник с заданными размерами (a, b) на изображении размера (m, n), цвет фона задайте в схеме RGB, как и цвет прямоугольника.
# Цвета также должны быть параметрами функции.
# Напишите аналогичную функцию но для овала с полуосями a и b.
# Напишите тесты для кода.
# Примечание: уравнение эллипса (границы овала) можно записать как: ((x-x0)^2/a^2)+((y-y0)^2/b^2)=1

import numpy as np

def draw_rectangle(a, b, m, n, rectangle_color, background_color):
    img = np.full((m, n, 3), background_color, dtype=np.uint8)
    start_row, start_col = (m - a) // 2, (n - b) // 2
    img[start_row:start_row+a, start_col:start_col+b] = rectangle_color
    return img

def draw_ellipse(a, b, m, n, ellipse_color, background_color):
    img = np.full((m, n, 3), background_color, dtype=np.uint8)
    center_y, center_x = m // 2, n // 2
    y, x = np.ogrid[:m, :n]
    mask = ((x - center_x) / b) ** 2 + ((y - center_y) / a) ** 2 <= 1
    img[mask] = ellipse_color
    return img

# Тесты (проверка размеров и наличия цвета)
rect = draw_rectangle(10, 20, 50, 60, [255,0,0], [0,0,0])
assert rect.shape == (50, 60, 3)
assert np.any(rect == 255)  # есть красный пиксель

ellipse = draw_ellipse(5, 10, 30, 40, [0,255,0], [255,255,255])
assert ellipse.shape == (30, 40, 3)
print('Тесты пройдены успешно!')