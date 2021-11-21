from primes_sieve.source.sieve import sieve_of_eratosphenes

def test_last_number():
    assert sieve_of_eratosphenes(17) == [2, 3, 5, 7, 11, 13, 17], "Should be list ending with 17"

def test_last_number_not_included():
    assert sieve_of_eratosphenes(16) == [2, 3, 5, 7, 11, 13], "Should be list ending with 13"

def test_negative_number():
    assert sieve_of_eratosphenes(-7) == [], "Should be empty list"

def test_null():
    assert sieve_of_eratosphenes(0) == [], "Should be empty list"

def test_lower_limit():
    assert sieve_of_eratosphenes(2) == [2], "Should be list containing 2"