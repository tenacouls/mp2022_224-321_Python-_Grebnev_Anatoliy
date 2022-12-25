def drawRectangle():

    b = int(input("Высота фигуры: "))

    a = int(input("Ширина фигуры: "))

    simbol = input("Символ фигуры: ")
    print(simbol * a)

    for i in range(b - 2):
        print(simbol * a)
    print(simbol * a)
    answer = input("Повторить? Y or N: ")
    if answer == 'Y':
        drawRectangle()
    elif answer == 'N':
        return
drawRectangle()
