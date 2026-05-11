# Задача 7
# Написать функцию, принимающая целое число n, задающее количество кубиков.
# Функция должна определить, можно ли из данного кол-ва кубиков построить пирамиду, то есть можно ли представить число n как 1^2+2^2+3^2+…+k^2.
# Если можно, то функция должна вернуть k, иначе строку “It is impossible”.
# Написать тесты для кода

def pyramid(number):
    k, total = 1, 0
    while total < number:
        total += k**2
        if total == number:
            return k
        k += 1
    return "It is impossible"

# Тесты
assert pyramid(14) == 3  # 1+4+9
assert pyramid(15) == "It is impossible"
print('Тесты пройдены успешно!')