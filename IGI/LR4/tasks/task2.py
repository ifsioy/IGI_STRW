import re
import zipfile
from textwrap import dedent


class TextHandler:
    def __init__(self, text):
        self.text = text
        self.words = re.findall(r'\b\w+\b', text)

    def replace_spaces(self, char):
        return self.text.replace(' ', char)


class TextAnalyzer(TextHandler):
    def __init__(self, text):
        super().__init__(text)
        self.sentences = re.split(r'(?<=[.!?])\s+', text)

    def get_sentence_stats(self):
        stats = {
            'total': len(self.sentences),
            'declarative': 0,
            'interrogative': 0,
            'imperative': 0
        }
        for s in self.sentences:
            if s.endswith('.'):
                stats['declarative'] += 1
            elif s.endswith('?'):
                stats['interrogative'] += 1
            elif s.endswith('!'):
                stats['imperative'] += 1
        return stats

    def find_smileys(self):
        pattern = r'(?<!\S)([:;]-*((\(+)|(\)+)|(\[+)|(]+)))(?!\S)'
        return len(re.findall(pattern, self.text))

    def check_guid(self):
        pattern = r'\b(?:{?[0-9a-fA-F]{8}-(?:[0-9a-fA-F]{4}-){3}[0-9a-fA-F]{12}}?)\b'
        return bool(re.search(pattern, self.text))

    def get_case_stats(self):
        upper = sum(1 for c in self.text if c.isupper())
        lower = sum(1 for c in self.text if c.islower())
        return upper, lower

    def find_z_word(self):
        for i, word in enumerate(self.words):
            if 'z' in word.lower():
                return word, i + 1
        return None

    def filter_a_words(self):
        return ' '.join([w for w in self.words if not w.lower().startswith('a')])

    def calculate_averages(self):
        word_lengths = [len(w) for w in self.words]
        sentence_lengths = [len(re.findall(r'\w+', s)) for s in self.sentences]

        return {
            'word': sum(word_lengths) / len(word_lengths) if word_lengths else 0,
            'sentence': sum(sentence_lengths) / len(sentence_lengths) if sentence_lengths else 0
        }


class ReportManager:
    @staticmethod
    def save_report(data, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(data)

    @staticmethod
    def create_zip(filename):
        with zipfile.ZipFile('results.zip', 'w') as zipf:
            zipf.write(filename)
            return zipf.getinfo(filename)


def task2():
    try:
        with open('input.txt', 'r', encoding='utf-8') as f:
            text = f.read()

        analyzer = TextAnalyzer(text)

        replace_char = input("Введите символ для замены пробелов: ")[0]

        stats = {
            'sentence': analyzer.get_sentence_stats(),
            'smileys': analyzer.find_smileys(),
            'guid': analyzer.check_guid(),
            'upper': analyzer.get_case_stats()[0],
            'lower': analyzer.get_case_stats()[1],
            'z_word': analyzer.find_z_word(),
            'modified_text': analyzer.replace_spaces(replace_char),
            'filtered_text': analyzer.filter_a_words(),
            'avg': analyzer.calculate_averages()
        }

        report = dedent(f"""
        Результаты анализа:
        Всего предложений: {stats['sentence']['total']}
        Повествовательные: {stats['sentence']['declarative']}
        Вопросительные: {stats['sentence']['interrogative']}
        Побудительные: {stats['sentence']['imperative']}
        Средняя длина предложения: {stats['avg']['sentence']:.1f} слов
        Средняя длина слова: {stats['avg']['word']:.1f} символов
        Смайликов: {stats['smileys']}
        Содержит GUID: {'Да' if stats['guid'] else 'Нет'}
        Заглавных букв: {stats['upper']}
        Строчных букв: {stats['lower']}
        Первое слово с 'z': {stats['z_word'] or "Не найдено"}
        """)

        print(report)
        ReportManager.save_report(report, 'output.txt')
        zip_info = ReportManager.create_zip('output.txt')

        print(f"\nФайл заархивирован. Размер: {zip_info.file_size} байт")
        print("\nМодифицированный текст:\n", stats['modified_text'])
        print("\nТекст после фильтрации:\n", stats['filtered_text'])

    except FileNotFoundError:
        print("Ошибка: Файл input.txt не найден")
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")