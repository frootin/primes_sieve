"""
Python3 module for finding prime numbers
By Nathalia Bogdanova, KI21-17/1b
"""
import click


def sieve_of_eratosphenes(n: int) -> list[int]:
    """
    Finds prime numbers <= n using the sieve of Eratosphenes algorithm.
    
    :param n: the upper limit of sorted list of primes starting with 2
    :return: sorted list of primes

    Integers greater than 2 are considered good input that gives
    meaningful results: 

    >>> sieve_of_eratosphenes(17)
    [2, 3, 5, 7, 11, 13, 17]

    >>> sieve_of_eratosphenes(16)
    [2, 3, 5, 7, 11, 13]

    Other integers are considered relatively good input that
    results in empty list:

    >>> sieve_of_eratosphenes(0)
    []

    >>> sieve_of_eratosphenes(-7)
    []

    Other types cause TypeError and so are considered bad input:

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


@click.command()
@click.argument("upper_limit", type=int, default=0)
@click.option("-t", "--test", is_flag=True, help="Run tests")
def run(upper_limit, test) -> None:
    if test:
        import os
        import doctest, pytest
        dir_path = os.path.dirname(os.path.realpath(__file__))
        doctest.testmod(verbose=True)
        pytest.main([f"{dir_path}/tests/"])
    else:
        click.echo(sieve_of_eratosphenes(upper_limit))


if __name__ == "__main__":
    run()
