
def decorator(func):
    def wrapper():
        s = ('So she was considering in her own mind, as well as she could,'
             ' for the hot day made her feel very sleepy and stupid, whether'
             ' the pleasure of making a daisy-chain would be worth the trouble'
             ' of getting up and picking the daisies, when suddenly a White'
             ' Rabbit with pink eyes ran close by her.')

        a, b, c = func(s)
        print(f"Количество слов, длина которых меньше 5: {a}")
        print(f"Самое короткое слово, заканчивающееся на 'd': {b}")
        print(f"Слова в порядке убывания их длин: {c}")

    return wrapper

@decorator
def task4(s: str):
    # Split the string into words and remove punctuation
    words = [word.strip(",.") for word in s.split()]

    # a) Count words with length less than 5
    count_short_words = sum(1 for word in words if len(word) < 5)

    # b) Find the shortest word ending with 'd'
    shortest_word_ending_d = None
    for word in words:
        if word.endswith('d'):
            if shortest_word_ending_d is None or len(word) < len(shortest_word_ending_d):
                shortest_word_ending_d = word

    # c) Sort words by length in descending order
    words_sorted_by_length = sorted(words, key=len, reverse=True)

    return count_short_words, shortest_word_ending_d, words_sorted_by_length