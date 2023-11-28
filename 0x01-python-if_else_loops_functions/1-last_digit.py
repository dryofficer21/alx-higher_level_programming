#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
div = -(-number % 10) if number < 0 else (number % 10)
if div > 5:
    print(f"Last digit of {number} is {div} and is greater than 5")
elif div == 0:
    print(f"Last digit of {number} is {div} and is 0")
else:
    print(f"Last digit of {number} is {div} and is less than 6 and not 0")
