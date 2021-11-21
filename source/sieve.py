"""
Python3 program for finding prime numbers
By Nathalia Bogdanova, KI21-17/1b
"""

def sieve_of_eratosphenes(n: int) -> list[int]:
    """
    Finds prime numbers <= n using the sieve of Eratosphenes algorithm.
    
    :param n: the upper limit of sorted list of primes starting with 2
    :return: sorted list of primes
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


def run() -> None:
    while (upper_limit := input("Введите верхнюю границу для решета Эратосфена (N): ")) != "stop":
        try:
            upper_limit = int(upper_limit)
            print("Простые числа в диапазоне от 0 до N:", *sieve_of_eratosphenes(upper_limit))
        except ValueError:
            print("Введено недопустимое значение.")

if __name__ == "__main__":
    run()
