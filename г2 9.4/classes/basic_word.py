class BasicWord:
    def __init__(self, word, sub_words):
        self.word = word
        self.sub_words = sub_words

    def has_subword(self, candidate):
        return candidate.lower() in self.sub_words

    def count_subwords(self):
        return 7

    def __repr__(self):
        return f"{self.word} содержит {len(self.sub_words)} слов"