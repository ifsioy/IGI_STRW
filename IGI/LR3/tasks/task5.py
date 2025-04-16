from IGI.LR3.input_handler import input_list


def decorator(func):
    def wrapper():
        numbers = input_list("Введите список чисел (разделенных пробелами): ")
        max_abs, sum_between = func(numbers)
        print(f"Максимальный по модулю элемент: {max_abs}")
        print(f"Сумма элементов между первым и вторым положительными: {sum_between}")

    return wrapper


@decorator
def process_numbers(numbers):
    if not numbers:
        print("Список пуст.")
        return

    # Находим максимальный по модулю элемент
    max_abs = max(numbers, key=lambda x: abs(x))

    # Находим индекс первого положительного элемента
    try:
        first_pos = next(i for i, x in enumerate(numbers) if x > 0) + 1
    except StopIteration:
        return max_abs, 0  # Если нет положительных элементов

    # Находим индекс второго положительного элемента после первого
    try:
        start_second = first_pos
        sum_second = sum(numbers[next(i for i, x in enumerate(numbers[start_second:], start_second) if x > 0):])
    except StopIteration:
        return max_abs, 0  # Если нет второго положительного элемента

    sum_first = sum(numbers[first_pos:])

    sum_between = sum_first - sum_second

    return max_abs, sum_between


