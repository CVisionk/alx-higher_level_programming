#!/usr/bin/python3
def uppercase(s):
    for i in s:
        temp = i;
        if ord(i) >= 97 and ord(i) <= 122:
            temp  = chr(ord(i) - 32)
        print('{}'.format(temp), end='')
    print('')
uppercase("Best School 98 Battery street")
