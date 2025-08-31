__all__ = (
    'even_odd',
)


def even_odd(ls: list[int]) -> float:
    """
    Функция возвращает отношение суммы четных элементов массив к сумме нечетных
    Пример:
    even_odd([1, 2, 3, 4, 5]) == 0.8889
    """
    evens = 0
    odds = 0

    for i in ls:
        if i % 2 == 0:
            evens += i
        else:
            odds += i
            
    if(odds == 0):
    	return 0

    return evens / odds
