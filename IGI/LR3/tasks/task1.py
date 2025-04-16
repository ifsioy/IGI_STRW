import math

from IGI.LR3.input_handler import input_float
from IGI.LR3.validators import validate_x


def task1_decorator(func):
    def wrapper():
        try:
            x = input_float('Input x: ')
            validate_x(x)
            eps = input_float('Input eps: ')
            f_x, n = func(x, eps)
            print('x = ', x)
            print('n = ', n)
            print('f(x) = ', f_x)
            print('math f(x) = ', math.log(1 - x))
            print('eps = ', eps)

        except ValueError as e:
            print(e)
            return None

    return wrapper

@task1_decorator
def calculate_ln_series(x, eps):
    """
    Calculate ln(1-x) using power series expansion

    Args:
        x (float): Input value
        eps (float): Calculation precision

    Returns:
        tuple: (approximated value, terms used)
    """
    sum_result = 0.0
    max_iter = 500

    for n in range(1, max_iter + 1):
        term = -(x ** n) / n
        sum_result += term
        if abs(term) < eps:
            return sum_result, n
    return sum_result, max_iter

