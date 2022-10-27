from random import randint


def search(n):
    result_ok = False
    last = len(n) - 1
    first = 0
    num = int(input('Введите находимое число от 1 до 100: '))
    while True:
        if first < last:
            middle = (first + last) // 2
            print(middle)
            if num == middle:
                first = middle
                last = first
                result_ok = True
                pos = middle
            elif num > middle:
                first = middle + 1
            else:
                last = middle - 1
        else:
            if result_ok == True:
                print(f'Элемент найден: {pos}')
                break
            elif result_ok == False:
                print('Элемент не найден.')
                break


def sel_sort(array):
    for i in range(len(array) - 1):
        m = i
        j = i + 1
        while j < len(array):
            if array[j] < array[m]:
                m = j
            j = j + 1
        array[i], array[m] = array[m], array[i]


a = []
for i in range(10):
    a.append(randint(1, 99))
print(a)
sel_sort(a)
print(a)

n = []
for i in range(0, 101):
    n.append(i)
sel_sort(n)
search(n)







