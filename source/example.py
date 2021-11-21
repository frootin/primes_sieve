"""
Python3 program for finding prime numbers
By Nathalia Bogdanova, KI21-17/1b
"""

def sieve_of_eratosphenes(n: int) -> list[int]:
    """Finds prime numbers <= n using the sieve of Eratosphenes algorithm.

    :param n: the upper limit of sorted list of primes starting with 2
    :return: sorted list of primes

    >>> sieve_of_eratosphenes(17)
    [2, 3, 5, 7, 11, 13, 17]

    >>> sieve_of_eratosphenes(16)
    [2, 3, 5, 7, 11, 13]

    >>> sieve_of_eratosphenes(2)
    [2]

    >>> sieve_of_eratosphenes(0)
    []

    >>> sieve_of_eratosphenes(-7)
    []

    >>> sieve_of_eratosphenes("m")
    Traceback (most recent call last):
        ...
    TypeError: can only concatenate str (not "int") to str

    >>> sieve_of_eratosphenes(2.3)   
    Traceback (most recent call last):
        ...
    TypeError: can't multiply sequence by non-int of type 'float'
    """
    sieve = [True] * (n+1)
    for i in range(2, n+1):
        if sieve[i] and i*i < n:
            for k in range(i*i, n+1):
                if not k%i:
                    sieve[k] = False
    prime_numbers = []
    for i in range(2, n+1):
        if sieve[i]:
            prime_numbers.append(i)
    return prime_numbers


if __name__ == "__main__":
    import doctest
    doctest.testmod(name="example", verbose=True)