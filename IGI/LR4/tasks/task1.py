import csv
import pickle

from IGI.LR4.input_handler import input_int


class HistoricalEvent:
    def __init__(self, year, description):
        self.year = year
        self.description = description

class DataManager:
    @staticmethod
    def save_to_csv(data, filename):
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Year', 'Event'])
            for event in data:
                writer.writerow([event.year, event.description])

    @staticmethod
    def load_from_csv(filename):
        events = []
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                events.append(HistoricalEvent(int(row['Year']), row['Event']))
        return events

    @staticmethod
    def save_to_pickle(data, filename):
        with open(filename, 'wb') as file:
            pickle.dump(data, file)

    @staticmethod
    def load_from_pickle(filename):
        with open(filename, 'rb') as file:
            return pickle.load(file)


def handle_century_search(events):
    century = input_int("Введите век для поиска (например 20): ")
    start_year = (century - 1) * 100 + 1
    end_year = century * 100

    filtered = [e for e in events if start_year <= e.year <= end_year]
    sorted_events = sorted(filtered, key=lambda x: x.year)

    print(f"\nСобытия {century} века:")
    for event in sorted_events:
        print(f"{event.year} - {event.description}")

def task1():
    # Исходные данные
    events_data = [
        HistoricalEvent(862, "Первое упоминание о Полоцке"),
        HistoricalEvent(1240, "Битва на Немиге"),
        HistoricalEvent(1569, "Люблинская уния"),
        HistoricalEvent(1918, "Провозглашение БНР"),
        HistoricalEvent(1991, "Независимость Беларуси"),
        HistoricalEvent(2020, "Президентские выборы")
    ]

    # Сохраняем в оба формата
    DataManager.save_to_csv(events_data, 'history.csv')
    DataManager.save_to_pickle(events_data, 'history.pkl')

    # Загрузка данных (можно выбрать любой формат)
    try:
        loaded_events = DataManager.load_from_csv('history.csv')  # Или load_from_pickle
        handle_century_search(loaded_events)
    except FileNotFoundError:
        print("Ошибка: Файлы данных не найдены")