# Напишите программу, которая принимает на вход 
# вещественное число и показывает сумму его цифр.
# *Пример:*
# - 6782 -> 23
# - 0,56 -> 11

number = input('Введите число: ')
def sum_in_number(some_number):
    sum = 0
    for i in some_number:
        if i.isdigit():
            i = int(i)
            sum = sum + i
    print(sum)
sum_in_number(number)