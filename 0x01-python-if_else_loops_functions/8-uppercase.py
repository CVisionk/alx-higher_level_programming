#!/usr/bin/python3
def uppercase(s):
    if ord(s[0]) >= 97 and ord(s[0]) <= 122:
        print("{}{}".format(chr(ord(s[0]) - 32), s[1:]))
    else:
        print(s)
