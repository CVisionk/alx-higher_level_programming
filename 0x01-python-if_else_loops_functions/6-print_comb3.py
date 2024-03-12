#!/usr/bin/python3
for num in range(0, 9):
    for num2 in range(num, 10):
        if str(num) + str(num2) == '89':
            print('89')
        elif num != num2:
            print("{}, ".format(str(num)+str(num2)), end='')
