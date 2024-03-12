#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = 0
if (number != 0):
    lastDigit = int(int(str(number)[-1])*(number/abs(number)))
if lastDigit == 0:
    line = "is 0"
elif lastDigit < 6:
    line = "is less than 6 and not 0"
else:
    line = "is greater than 5"
print(f"Last digit of {number} is {lastDigit} and {line}")
