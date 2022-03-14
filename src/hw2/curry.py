from typing import Callable


def curry_explicit(foo: Callable, arity: int) -> Callable:
    if arity < 0:
        raise ValueError("Arity must be non-negative")

    if arity == 0:
        return foo()

    def inner_curry_explicit(first_arg=None) -> Callable:
        if arity == 1:
            return foo(first_arg)
        return curry_explicit(lambda *args: foo(first_arg, *args), arity - 1)

    return inner_curry_explicit


def uncurry_explicit(foo: Callable, arity: int) -> Callable:
    if arity < 0:
        raise ValueError("Arity must be non-negative")

    if arity == 0:
        return foo()

    def inner_uncurry_explicit(*args) -> Callable:
        if len(args) != arity:
            raise ValueError("Args count must be equal to arity")
        final = foo
        for arg in args:
            final = final(arg)
        return final

    return inner_uncurry_explicit
