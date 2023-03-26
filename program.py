# Задача 16:
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N/2.
# Выведите, сколько раз X встречается в массиве.

# Ввод: 5
# Ввод: 1

# 1 2 1 2 2
# Вывод: 2

from random import randrange
from input_check import IntCheckedInputLtd

arraySizeLimit = 101 # limited just for simplicity
arraySize = IntCheckedInputLtd(
    f'Enter the size of the array, not more than {arraySizeLimit-1}',
    arraySizeLimit)

RandomArray = [randrange ( 1, arraySize // 2 ) for i in range(arraySize)]
print(RandomArray)  # it is interesting to see what the progam has added in into the array

arrayMenber = IntCheckedInputLtd(
    f'Enter the number to be found in the array, not more than {arraySizeLimit // 2}',
    arraySizeLimit // 2 + 1)

print(f'Count of {arrayMenber} in the array founded bu function "array.count" is:  {RandomArray.count(arrayMenber)}')

memberCount = 0
for i in RandomArray:
    if i == arrayMenber:
        memberCount += 1

print(f'Count of {arrayMenber} in the array founded by iteration is: {memberCount}')

memberCount = 0
for i in range(arraySize):
    if RandomArray [i] == arrayMenber:
        memberCount += 1

print(f'Count of {arrayMenber} in the array founded by index cycle is: {memberCount}')
