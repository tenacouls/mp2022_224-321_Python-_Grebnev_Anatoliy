#создать двумерный массив, заполнить случайными значениями, например, от 10 до 99, 
#распечатать его и заметем в цикле выбирать действие (повернуть в лево, в право, отразить ...) 
#и тоже распечатать

import random

def printArray(a, b, array):
    for i in range(a):
        for j in range(b):
            print(array[i][j], end=" ")
        print()
    print()

def rotateRight(h, w, arr):
    ans=[]
    for i in range(h):
        ans.append([0] * w)

    for i in range(h):
       for j in range(w):
            ans[i][j] = arr[w - j - 1][i]
    return ans

def rotateLeft(h, w, arr):
    ans=[]
    for i in range(h):
        ans.append([0] * w)

    for i in range(h):
       for j in range(w):
            ans[i][j] = arr[j][w - i - 1]
    return ans

def mirrorX(h, w, arr):
    ans=[]
    for i in range(h):
        ans.append([0] * w)

    for i in range(h):
       for j in range(w):
            ans[i][j] = arr[i][w - j - 1]
    return ans

def mirrorY(h, w, arr):
    ans=[]
    for i in range(h):
        ans.append([0] * w)

    for i in range(h):
       for j in range(w):
            ans[i][j] = arr[h - i - 1][j]
    return ans

def transpose(h, w, arr):
    ans=[]
    for i in range(h):
        ans.append([0] * w)

    for i in range(h):
       for j in range(w):
            ans[i][j] = arr[j][i]
    return ans

def matrixRotate(a, b, arr): #вызов функции
    answer = input("Повернуть по часовой стрелке? ")
    if answer.upper() == 'Y':
        if a != b:
            print('Матрицу невозможно повернуть, так как её ширина и высота различны')
        else:
            arr = rotateRight(a, b, arr)
            printArray(a, b, arr)
            return matrixRotate(a, b, arr)

    answer = input("Повернуть против часовой стрелки? ")
    if answer.upper() == 'Y':
        if a != b:
            print('Матрицу невозможно повернуть, так как её ширина и высота различны')
        else:
            arr = rotateLeft(a, b, arr)
            printArray(a, b, arr)
            return matrixRotate(a, b, arr)

    answer = input("Отразить по оси X? ")
    if answer.upper() == 'Y':
        arr = mirrorX(a, b, arr)
        printArray(a, b, arr)
        return matrixRotate(a, b, arr)
    
    answer = input("Отразить по оси Y? ")
    if answer.upper() == 'Y':
        arr = mirrorY(a, b, arr)
        printArray(a, b, arr)
        return matrixRotate(a, b, arr)

    answer = input("Транспонировать? ")
    if answer.upper() == 'Y':
        if a != b:
            print('Матрицу невозможно транспонировать, так как её ширина и высота различны')
        else:
            arr = transpose(a, b, arr)
            printArray(a, b, arr)
            return matrixRotate(a, b, arr)

    return

def main(): #заполнение массива данными
    a = int(input('Высота: '))
    b = int(input('Ширина: '))
    arr=[]
    for i in range(a):
        arr.append([0] * b)

    for i in range(a):
        for j in range(b):
            arr[i][j] = random.randint(10, 99)
    printArray(a, b, arr)
    print()
    print()

    matrixRotate(a, b, arr)
    

main()
