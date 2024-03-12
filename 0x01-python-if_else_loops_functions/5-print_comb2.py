#!/usr/bin/python3
for number in range(0, 100):
    if number == 99:
        print(99)
    else:
        print("{:02}, ".format(number), end='')
