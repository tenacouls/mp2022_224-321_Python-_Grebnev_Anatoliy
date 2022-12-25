#Нарисовать в консоли шахматную доску

char = "██  "
for i in range(8):
    print(char * 4)
    char = char[::-1]