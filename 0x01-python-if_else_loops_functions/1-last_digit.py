#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number = str(number)
lastDigit = int(int(number[-1])*int(number)/abs(int(number)))
if lastDigit  == 0:
    line = "is zero"
elif lastDigit < 6:
    line = "is less than 6 and not 0"
else: 
    line = "is greater than 5"
print(f"Last digit of {number} is {lastDigit} and {line}")
