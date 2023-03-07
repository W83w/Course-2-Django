from config import WORDS_ON_JSON_KEEPER
from  classes.basic_word import BasicWord

def load_random_word():
    path = WORDS_ON_JSON_KEEPER

    data = {
        "word": "набор",
        "sub_words": ["бар", "бан", "бор", "раб", "бра", "нора", "роба", "боа"],
    }



    word = BasicWord(data["word"], data["sub_words"])
    print(path)
    return word

