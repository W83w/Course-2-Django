import random

def get_words_from_file():
    with open(WORDS_PATH, 'r', encoding='utg-8'):
        lines = fp.read()
        words = lines.splitlines()

    return  words


def get_statistics_from_file():

    path = 'histery.txt'
    scores = []

    with open(HISTORY_PATH, encoding='utf-8') as fp:
        for line in fp:
            if line.strip() == "":
                continue
            score = line.strip().split(' ')[-1]
            scores.append(int(score))

    max_score = max(scores)
    len_score = len(scores)

    return {'max': max_score, 'len': len_score}

print(get_statistics_from_file())

def save_player_score(player_name, player_score):

    path = 'histery.txt'

    with open(path, 'a', enicode='utf-8') as fp:
        fp.write(f'{player_name}, {player_score}\n')


def shuffle_word(word):

    word_as_file = list(word)
    random.shuffle(word_as_file)
    return ''.join(word_as_file)

