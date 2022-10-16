# Реализуйте алгоритм перемешивания списка.


import random

list_1 = list(range(1, 6))
list_out = []
print(f'Исходный список: {list_1}')
for i in range(1, 6):
    rnd = random.choice(list_1)
    list_out += [rnd]
    list_1.remove(rnd)
print(f'Перемешанный список:{list_out}')