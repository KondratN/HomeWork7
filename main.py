# 11.16 Дан массив целых чисел. Выяснить:
# Является ли s-ый элемент массива положительным числом
# Является ли k-ый элемент массива четным числом
# Какой элемент массива больше: k-ый или s-ый
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# someList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# someInt = int(input('Введите s-ый элемент массива\n'))
# someInt1 = int(input('Введите k-ый элемент массива\n'))
# if someInt < len(someList):
#     if someList[someInt] > 0:
#         print('Число положительное')
#     else:
#         print('Число не положительное')
# else:
#     print('Введенное вами число вышло за пределы массива')
# if someInt < len(someList):
#     if someList[someInt1] % 2 == 0:
#         print('Число четное')
#     else:
#         print('Число не четное')
# else:
#     print('Введенное вами число вышло за пределы массива')
# if someInt < len(someList) and someInt1 < len(someList):
#     if someList[someInt] > someList[someInt1]:
#         print('S-ый элемент больше K-ого')
#     else:
#         print('K-ый элемент больше S-ого')
# else:
#     print('Введенное вами число вышло за пределы массива')
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 11.18 Дан массив. Все его элементы:
# уменьшить на 20
# умножить на последний элемент
# увеличить на число B
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# someList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# someInt = int(input('Введите число B\n'))
# index = 0
# index1 = 0
# index2 = 0
# while index < len(someList):
#     someList[index] -= 20
#     index += 1
# print(someList)
# while index1 < len(someList):
#     someList[index1] += someList[-1]
#     index1 += 1
# print(someList)
# while index2 < len(someList):
#     someList[index2] += someInt
#     index2 += 1
# print(someList)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 11.21 В массиве хранятся сведения о количестве осадков, выпавших за каждый день января. Определить общее количество
# осадков за январь
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# someList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# print('Общее количество осадков за январь = ', sum(someList), 'мм')
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 11.30  В массиве хранится информация о численности учеников в каждом из 42 классов школы.
# Выяснить, верно ли, что общее число учеников в школе есть четырехзначное число.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# index = 42
# someList = []
# while 0 < index:
#     print(f'Введите количество учеников в {index} классе')
#     someList.append(int(input('Введите количество учеников\n')))
#     index -= 1
# if 9999 > sum(someList) > 999:
#     print('Общее количество учеников в школе есть четырех значное число')
# else:
#     print('Общее количество учеников в школе не есть четырех значное число')
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 11.36 Дан массив. Напечатать:
# Все неотрицательные элементы
# Все элементы, не превышающие число 100
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# someList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# index = 0
# index1 = 0
# while index < len(someList):
#     if someList[index] > 0:
#         print(someList[index])
#         index += 1
# while index1 < len(someList):
#     if someList[index1] < 100:
#         print(someList[index1])
#         index1 += 1
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 11.39 Дан массив. Напечатать:
# второй, четвертый и т.д. элементы
# третий, шестой и т.д. элементы
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# someList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# index = 1
# index1 = 2
# while index < len(someList):
#     print(someList[index])
#     index = (index + 1) * 2 - 1
# while index1 < len(someList):
#     print(someList[index1])
#     index1 = index1 * 2 + 1
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 11.52 Дан массив целых чисел.
# Все элементы, оканчивающиеся цифрой 4, уменьшить вдвое.
# Все четные элементы заменить на их квадраты, а нечетные удвоить.
# Четные элементы увеличить на a, а из элементов с четными номерами вычесть b
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# someList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# someInt = int(input('Введите число а\n'))
# someInt1 = int(input('Введите число b\n'))
# index = 0
# index1 = 0
# index2 = 0
# while index < len(someList):
#     if someList[index] % 10 == 4:
#         someList[index] /= 2
#     index += 1
# print(someList)
# while index1 < len(someList):
#     if someList[index1] // 2 == 0:
#         someList[index1] *= someList[index1]
#     else:
#         someList[index1] *= 2
#     index1 += 1
# print(someList)
# while index2 < len(someList):
#     if someList[index2] // 2 == 0:
#         someList[index2] += someInt
#     else:
#         someList[index2] -= someInt1
#     index2 += 1
# print(someList)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 11.53 Дан массив целых чисел.
# Все элементы, кратные числу 10, заменить нулем.
# Все нечетные элементы удвоить, а четные уменьшить вдвое.
# Нечетные элементы уменьшить на m, а элементы с четными номерами увеличить на n.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# someList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# someInt = int(input('Введите число m\n'))
# someInt1 = int(input('Введите число n\n'))
# index = 0
# index1 = 0
# index2 = 0
# while index < len(someList):
#     if someList[index] % 10 == 0:
#         someList[index] = 0
#     index += 1
# print(someList)
# while index1 < len(someList):
#     if someList[index1] // 2 == 0:
#         someList[index1] /= 2
#     else:
#         someList[index1] *= 2
#     index1 += 1
# print(someList)
# while index2 < len(someList):
#     if someList[index2] // 2 == 0:
#         someList[index2] += someInt1
#     else:
#         someList[index2] -= someInt
#     index2 += 1
# print(someList)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~