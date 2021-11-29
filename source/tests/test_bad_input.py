"""
Tests on bad input for main function with pytest
"""


import pytest
from primes_sieve.source.sieve import sieve_of_eratosphenes


def test_str():
    with pytest.raises(TypeError):
        sieve_of_eratosphenes("m")

def test_float():
    with pytest.raises(TypeError):
        sieve_of_eratosphenes(1.23)
