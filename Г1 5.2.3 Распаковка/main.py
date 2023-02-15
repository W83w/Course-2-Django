#поиск самого длиного слова в последовательности
def longest_word(*words):
    leader = ' ' # переменная для поиска самого длинного слова и в ней оно будет хранится
    for word in words: # проходим по циклу
        if len(word) > len(leader): # сверяем их длину
            leader = word # перезаписывается по более длинное слово

    return leader # возвращает слово


print(longest_word("Ретро", "Бэклог", "Скрам", "Достопримечательность")) # картеж слов

# поиск самого длинного списка

def longest_list(*lists):
    leader = []
    for list_ in lists:
        if len(list_)> len(leader):
            leader = list_

    return leader


print(longest_list([1], [1, 2, 3], [1, 2]))

# Удаление символа из строки
def remove_from_string(string, *symbols_to_remove):
    for symbol in symbols_to_remove:
        string = string.replace(symbol, " ")
    return string


print(remove_from_string('Слово', ',','!'))

# вычисляет среднее и возвращает его округленным до первого знака

def avg(*nums):
    count = len(nums)
    nums_sum = sum(nums)
    return round(nums_sum / count, 1)


print(avg(1, 2, 3, 4, 5, 6, 7, 8))
print(avg(1, 2, 3, 4, 5, 6))