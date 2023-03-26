# Задача 18:
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N.
# Выведите, ближайший к X элемент. Если есть несколько элементов, которые равноудалены от X, выведите наименьший по величине.

# Ввод: 10
# Ввод: 7
# 1 2 1 8 9 6 5 4 3 4
# Вывод: 6

from random import randrange
from input_check import IntCheckedInputLtd

arraySizeLimit = 100 # limited just for simplicity
arrayMemberLimit = 100 # limited just for simplicity

# let's ask the array size
arraySize = IntCheckedInputLtd(
    f'Enter the size of the array, not more than {arraySizeLimit}',
    arraySizeLimit + 1)

#filling the array by random ints
RandomArray = [randrange ( 1, arrayMemberLimit ) for i in range(arraySize)]

#print(RandomArray)  # it is interesting to see what the program has filled in the array

#asking the number for searching nearests
arrayMember = IntCheckedInputLtd(
    f'Enter the number to find nearests in the array, not more than {arrayMemberLimit}',
    arrayMemberLimit + 1)

nearest = RandomArray[0]
difference = arrayMember - nearest

#searching the minimal nearest in the array
for i in range(arraySize):
    if abs( arrayMember - RandomArray[i] ) <= abs( difference ):
#if we have 2 different neibours in the same distance - select smaller
        if abs( difference ) == abs( arrayMember - RandomArray[i] ): 
            nearest = min( RandomArray[i], nearest )
#usually just get a new nearest            
        else:
            nearest = RandomArray[i]
        difference = arrayMember - nearest

#how many times the nearest present in the array?        
Neibours = [i for i in RandomArray if i == nearest]

print (f'The minimal nearest to {arrayMember} member of the array is {nearest} repeated {len(Neibours)} times.')
