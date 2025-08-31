from typing import Optional
import re

__all__ = (
    'find_shortest_longest_word',
)


def find_shortest_longest_word(s: str) -> tuple[Optional[str], Optional[str]]:
    """
    В переданном тексте вернуть слово имеющее наименьшую и наибольшую длину.
    Если такого слова нет - вернуть None
    """
    
    ls = re.split(r'\s+', s)

    if len(ls) == 0:
        return (None, None)

    shortest = ls[0]
    longest = ls[0]


    for w in ls:
        if len(w) < len(shortest):
            shortest = w

        if len(w) > len(longest):
            longest = w
            
    if(shortest == '' and longest == ''):
        return (None, None)

    return (shortest, longest)
