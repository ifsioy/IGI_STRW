
def decorator(func):
    def wrapper():
        s = input("Введите строку: ")
        print('Пробелов в строке: ', func(s))

    return wrapper

@decorator
def count_spaces(s):
    """
    Count the number of spaces in a string.

    Args:
        s (str): Input string.

    Returns:
        int: Number of spaces in the string.
    """
    return s.count(' ')