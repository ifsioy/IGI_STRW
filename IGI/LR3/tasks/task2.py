from IGI.LR3.input_handler import input_int


def decorator(func):
    def wrapper():
        numbers = []
        print("Вводите числа с новой строки:")
        while True:
            try:
                num = input_int()
                if num > 1000:
                    break
                numbers.append(num)
            except ValueError as e:
                print(e)

        print('Количество четных чисел:', func(numbers))

    return wrapper

@decorator
def count_even_numbers(numbers):
    """
    Count the number of even numbers in a list.

    Args:
        numbers (list): List of integers.

    Returns:
        int: Count of even numbers.
    """
    return sum(1 for num in numbers if num % 2 == 0)