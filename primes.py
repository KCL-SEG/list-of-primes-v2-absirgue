"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""


def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError("number of primes should be positive")
    list = []
    tested_number = 1
    while len(list) < number_of_primes:
        numberCanBePrime = True
        tested_number += 1
        for i in range(2, tested_number):
            if (tested_number % i == 0):
                numberCanBePrime = False
        if (numberCanBePrime):
            list.append(tested_number)
    return list
