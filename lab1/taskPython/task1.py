# Задача 1
# Написать функцию на вход которой подается строка, состоящая из латинских букв.
# Функция должна вернуть количество гласных букв (a, e, i, o, u) в этой строке. Написать тесты для кода

def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for c in s if c in vowels)

# Тесты
assert count_vowels("hello") == 2
assert count_vowels("xyz") == 0
assert count_vowels("AEIOU") == 5
print('Тесты пройдены успешно!')