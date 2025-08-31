from typing import Any

__all__ = (
    'cartesian_product',
)


def cartesian_product(ls1: list[Any], ls2: list[Any]) -> list:
    """
    Должна возвращать все пары элементы двух массивов:
    cartesian_product([1, 2], [3, 4]) == [(1, 3), (1, 4), (2, 3), (2, 4)]
    """
    ls = []

    for i in ls1:
        for j in ls2:
            ls.append((i, j))

    return ls
