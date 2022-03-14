import pytest
from src.hw2.curry import *


def test_curry_explicit_negative():
    with pytest.raises(ValueError):
        curry_explicit((lambda x, y, z: f"<{x},{y},{z}>"), -1)


def test_curry_explicit_zero():
    foo = curry_explicit((lambda: 10), 0)
    assert foo == 10


def test_curry_explicit_1():
    foo = curry_explicit((lambda x, y, z: f"<{x},{y},{z}>"), 3)
    assert foo(123)(456)(562) == "<123,456,562>"


def test_curry_explicit_2():
    foo = curry_explicit((lambda a, b, c, d: a * b + c * d), 4)
    assert foo(1)(2)(3)(4) == 14


def test_uncurry_explicit_negative():
    foo = curry_explicit((lambda x, y, z: f"<{x},{y},{z}>"), 3)
    with pytest.raises(ValueError, match="Arity must be non-negative"):
        uncurry_explicit(foo, -1)


def test_uncurry_explicit_unmatch():
    foo = curry_explicit((lambda a, b, c, d: a * b + c * d), 4)
    with pytest.raises(ValueError, match="Args count must be equal to arity"):
        uncurry_explicit(foo, 4)(1)


def test_uncurry_explicit_1():
    foo = curry_explicit((lambda x, y, z: f"<{x},{y},{z}>"), 3)
    uncurry_foo = uncurry_explicit(foo, 3)
    assert uncurry_foo(123, 456, 562) == "<123,456,562>"


def test_uncurry_explicit_2():
    foo = curry_explicit((lambda a, b, c, d: a * b + c * d), 4)
    uncurry_foo = uncurry_explicit(foo, 4)
    assert uncurry_foo(1, 2, 3, 4) == 14
