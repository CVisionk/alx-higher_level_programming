#!/usr/bin/python3
def uppercase(s):
    for i in s:
        temp = i;
        if ord(i) >= 97 and ord(i) <= 122:
            temp  = chr(ord(i) - 32)
        print(temp, end='')
    print('')
