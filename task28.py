# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.
# return sum(a,b-1) + 1 - Так делать нельзя
# *Пример:*
# Input: 2 2
# Output: 4 

def sum_nums(number_1: int, number_2: int) -> int:
    min_num = min(number_1, number_2)
    max_num = max(number_1, number_2)
    if min_num == 0:
        return max_num
    return sum_nums(max_num, min_num - 1) + 1

num_1 = int(input('Введите первое слагаемое: '))
num_2 = int(input('Введите второе слагаемое: '))

print(sum_nums(num_1, num_2))