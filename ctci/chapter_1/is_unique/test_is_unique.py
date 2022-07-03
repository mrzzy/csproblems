#
# Cracking the Coding Interview
# Chapter 1
# 1. Is Unique
# Tests
#

from string import ascii_letters
from random import seed, sample
from is_unique import is_unique


def test_is_unique_actually_unique():
    assert is_unique("abc")
    assert is_unique("cba")
    assert is_unique("ced1#%\r\n")
    seed(0)  # make RNG deterministic
    assert is_unique("".join(sample(ascii_letters, len(ascii_letters))))


def test_is_unique_not_unique():
    assert not is_unique("aa")
    assert not is_unique("cbc")
    assert not is_unique("asdfaf")
    assert not is_unique("".join(sample(ascii_letters, len(ascii_letters))) + "A")

def test_is_unique_special_case():
    assert is_unique("")
    assert is_unique("a")
