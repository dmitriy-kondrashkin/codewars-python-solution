class predicate:

    def __init__(self, wrapped_func): self.wrapped_func = wrapped_func

    def __call__(self, *args, **
                 kwargs): return self.wrapped_func(*args, **kwargs)

    def __invert__(self): return self.__class__(
        lambda *args, **kwargs: not self.wrapped_func(*args, **kwargs))

    def __or__(self, other): return self.__class__(
        lambda *args, **kwargs: self.wrapped_func(*args, **kwargs)
        or other(*args, **kwargs))

    def __and__(self, other): return self.__class__(
        lambda *args, **kwargs: self.wrapped_func(*args, **kwargs)
        and other(*args, **kwargs))


@predicate
def is_even(num):
    return num % 2 == 0


@predicate
def is_positive(num):
    return num > 0


print((is_even | is_positive)(4))          # True
print((is_even & is_positive)(3))          # False
print((is_even | is_positive)(3))          # True
print((~is_even & is_positive)(3))         # True
