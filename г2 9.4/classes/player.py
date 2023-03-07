class Player:
    def __init__(self, name):
        self.name = name
        self.used_words = []

    def count_words(self):
        return 3

    def add_word(self, word):
        self.used_words += word

    def has_uses(self, word):
        return word in self.used_words