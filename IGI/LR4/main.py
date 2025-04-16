"""
LR4
variant 4
version 1
Babchanok Maksim
06.04.2025
"""
from IGI.LR4.tasks.task1 import task1
from IGI.LR4.tasks.task2 import task2


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
                task1()
            elif choice == 2:
                task2()
            elif choice == 3:
                pass
            elif choice == 4:
                pass
            elif choice == 5:
                pass
            elif choice == 6:
                print("Завершение работы...")
                break
            else:
                print("Ошибка: Введите число от 1 до 6.")
        except ValueError:
            print("Ошибка: Введите корректное число.")

if __name__ == "__main__":
    main_menu()