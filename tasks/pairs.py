from typing import Any

__all__ = (
    'corresponding_pairs',
)


def corresponding_pairs(ls1: list[Any], ls2: list[Any]) -> list[tuple[Any, Any]]:
    """
    Функция должна возвращать соответствующие элементы двух массивов:
    corresponding_pairs([1, 2], [3, 4]) == [(1, 3), (2, 4)]
    """
    
    ls = []

    for i in range(min(len(ls1), len(ls2))):
        ls.append((ls1[i], ls2[i]))

    return ls
