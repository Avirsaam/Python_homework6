# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: a = a + (n-1) * d.
# n 1Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15
#
# first_element = 7
# difference = 2
# number_of_elements = 5

first_element = int(input('Введите первый член прогрессии'))
difference = int(input('Введите разность между элементами'))
number_of_elements = int(input('Введите количество элементов'))

print([difference * i + first_element for i in range(number_of_elements)])