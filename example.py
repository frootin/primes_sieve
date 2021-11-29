"""
Example program
"""

import sieve


# storing function output
primes = sieve.sieve_of_eratosphenes(10)

# print primes with their number by order
for i, num in enumerate(primes, start=1):
    print(f"{i}-е простое число: {num}")
