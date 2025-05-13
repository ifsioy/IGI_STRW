"""
LR4
variant 4
version 1
Babchanok Maksim
06.04.2025
"""
from tasks.task1 import task1
from tasks.task2 import task2
from tasks.task3 import task3
from tasks.task4 import task4
from tasks.task5 import task5


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
                task = task3()
                task.run()
            elif choice == 4:
                task4()
            elif choice == 5:
                task5()
            elif choice == 6:
                print("Завершение работы...")
                break
            else:
                print("Ошибка: Введите число от 1 до 6.")
        except ValueError:
            print("Ошибка: Введите корректное число.")

if __name__ == "__main__":
    main_menu()