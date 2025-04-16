"""
LR3
variant 4
version 1
Babchanok Maksim
01.04.2025
"""
from IGI.LR3.tasks.task1 import calculate_ln_series
from IGI.LR3.tasks.task2 import count_even_numbers
from IGI.LR3.tasks.task3 import count_spaces
from IGI.LR3.tasks.task4 import task4
from IGI.LR3.tasks.task5 import process_numbers


def main_menu():
    while True:
        print("\nМеню:")
        print("1. Задание 1")
        print("2. Задание 2")
        print("3. Задание 3")
        print("4. Задание 4")
        print("5. Задание 5")
        print("6. Завершить работу")

        try:
            choice = int(input("Выберите пункт меню (1-6): "))
            if choice == 1:
                calculate_ln_series()
            elif choice == 2:
                count_even_numbers()
            elif choice == 3:
                count_spaces()
            elif choice == 4:
                task4()
            elif choice == 5:
                process_numbers()
            elif choice == 6:
                print("Завершение работы...")
                break
            else:
                print("Ошибка: Введите число от 1 до 6.")
        except ValueError:
            print("Ошибка: Введите корректное число.")

if __name__ == "__main__":
    main_menu()