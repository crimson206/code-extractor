from typing import Dict


class A:
    pass


def example_func(arg1: int = 1, arg2: Dict[str, A] = {"hi": A()}) -> int:
    more_line = 1
    return more_line
