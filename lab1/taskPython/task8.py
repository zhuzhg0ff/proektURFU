# Задача 8
#Функция принимает на вход положительное число и определяет является ли оно сбалансированным, т.е. сумма цифр до средних равна сумме цифр после.
# Средними в случае нечетного числа цифр считать одну цифру, в случае четного - две средних.
# Написать тесты для кода

def is_balanced(n):
    s = str(n)
    mid = len(s) // 2
    if len(s) % 2 == 0:
        left, right = s[:mid], s[mid:]
    else:
        left, right = s[:mid], s[mid+1:]
    return sum(int(d) for d in left) == sum(int(d) for d in right)

# Тесты
assert is_balanced(12321) == True
assert is_balanced(123321) == True
assert is_balanced(123) == False
print('Тесты пройдены успешно!')