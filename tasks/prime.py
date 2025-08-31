__all__ = (
    'is_prime',
)


def is_prime(num: int) -> bool:
    """
    Функция должна вернуть True если число является простым, иначе - False
    """
    if num == 1 or num == 0:
    	return False
    
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False

    return True
