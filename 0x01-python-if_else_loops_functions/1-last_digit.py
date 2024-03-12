#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number = str(number)
if number[-1]  == '0':
    line = "is zero"
elif int(number[-1]) < 6:
    line = "is less than 6 and not 0"
else: 
    line = "is greater than 5"
print(f"Last digit of {number} is {int(int(number[-1])*int(number)/abs(int(number)))} and {line}")
