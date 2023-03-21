class Word():
    def __init__(self, value, subwoeds):
        self.value = value
        self.subwords = subwoeds

    def has_subwoed(self, word):
        if word.lower() in self.subwords:
            return True

        return False

word = Word("прокрастинация", ['рок', 'кор', 'карп'])

for round in range(3):

    print("Введите слово")
    user_input = input()
    if word.has_subwoed(user_input):
        print("Слово есть ")
    else:
        print("Слова нет")