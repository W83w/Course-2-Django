import random

def random_gift(category):
    books = ['Чистый код', 'Совершенный код', 'Паттерны ООП']
    gadgets = ['Умные часы', 'Умные Весы', 'Робот пылесос']
    games = ['Village', 'Halo Infinite', 'Far Cry 6']

    if category =='игры':
        return random.sample(games, 1)[0]
    elif category == 'книги':
        return random.sample(books, 1)[0]
    elif category == 'гаджеты':
        return random.sample(gadgets, 1)[0]
    else:
        return 'Нет подарков'

print(random_gift('игры'))
print(random_gift('книги'))
print(random_gift('гаджеты'))
