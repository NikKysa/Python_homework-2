# Задайте список из N элементов, заполненных числами из 
# промежутка [-N, N]. Найдите произведение элементов на 
# указанных позициях. Позиции вводятся с клавиатуры.

number_elements = int(input("Введите количество элементов: "))
first_element = -number_elements
while True:
    try:
        pos_first_element = int(input("Введите позицию первого элемента: "))
        pos_second_element = int(input("Введите позицию второго элемента: "))
        if 0 <= pos_first_element <= number_elements * 2 + 1 and 0 <= pos_second_element <= number_elements * 2 + 1:
            break
        else:
            print('Эти цифры вне диапазона! Повторим:')
    except ValueError:
        print('Это не число! Повторим:')
list = []
for i in range(number_elements * 2 + 1):
    list += [first_element]
    first_element += 1
print(list)
print(f'Произведение заданных элементов {int(list[pos_first_element - 1]) * int(list[pos_second_element - 1])}')



# n = int(input('Введите число: '))
# list = []
# for i in range(-n, n+1):
#     list.append(i)
# print(list)
# f = open('file.txt')
# ind1 = int(f.read(1))
# ind2 = int(f.read(2))
# f.close()
# print(ind1, 'and', ind2)
# mult = list[ind1] * list[ind2]
# print(list[ind1], '*', list[ind2], '=', mult)