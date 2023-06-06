#!/usr/bin/python3
# 12-fizzbuzz.py


def fizzbuzz():
    """Display the nos. from 1 to 100 divided by a space.

    For multiples of three, print Fizz for the number.
    For multiples of five, print Buzz for the number.
    For multiples of three and five, print FizzBuzz for the number.
    """
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz ", end="")
        elif number % 3 == 0:
            print("Fizz ", end="")
        elif number % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(number), end="")
