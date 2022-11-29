#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = str(number)[-1]
if number < 0:
    last_digit = int(last_digit) * -1
    print(f"Last digit of {number:d} is {last_digit} and is less than 6 and not 0")
elif number == 0:
    print(f"Last digit of {number:d} is {number}")
elif int(last_digit) > 5:
    print(f"Last digit of {number:d} is {last_digit} and is greater than 5")
else:
    print(f"Last digit of {number:d} is {last_digit} and is less than 6 and not 0")
