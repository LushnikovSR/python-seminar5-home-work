# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

# Описание работы рекурсии:
# 1   2   3   4 - изменение степени числа в ходе работы программы, при движении со дна рекурсии
# 3   9  27  81 - результат возврата из из рекурсии в ходе работы программы, при движении со дна рекурсии, последнее значение возврщается из функции
#   * 3 * 3 * 3 - умножаем полученный из рекурсии возврат на 3 для получение последующего возврата

def raise_power(base: int, power: int) -> int:
    """Возведение числа в степень через рекурсию"""
    if power == 1:
        return base
    return raise_power(base, power - 1) * base

number_base = int(input('Введите основание числа: '))
number_power = int(input('Введите степень числа: '))

print(raise_power(number_base, number_power))