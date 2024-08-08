from math import sqrt
from typing import Optional


def add_numbers(xo: int, yo: int) -> int:
    return xo + yo


def calculate_square_root(number: float) -> float:
    return sqrt(number)


def calc(your_number: float) -> Optional[str]:
    if your_number <= 0:
        return None
    root_result 
    return (f'Мы вычислили квадратный корень из введённого вами числа.'
            f'Это будет: {root_result}')



xo = 10
yo = 5

print('Сумма чисел: ', add_numbers(xo, yo))

print(calc(25.5))
