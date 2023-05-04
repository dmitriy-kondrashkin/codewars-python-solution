# Solution 1
class CustomInt(int):
    def __call__(self, n):
        return CustomInt(self + n)


def add_1(n):
    return CustomInt(n)


# Solution 2
def add_2(v): return type("", (int,), {
    "__call__": lambda self, v: self.__class__(self + v)})(v)


# add(1)(2)(3) # 6
# add(1)(2)(3)(4); # 10
# add(1)(2)(3)(4)(5) # 15


print(add_2(1)(2)(3))
