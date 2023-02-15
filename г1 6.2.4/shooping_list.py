# стоимость покупок
row_index = 0 # Записываю индексы
items_count = 0 # количество счетчик
items_sum = 0 # Сумма за 1

with open('shoopping_list.txt', 'r') as file:
    for item_data in file:
        row_index += 1 # с каждой итерацией увеличиваю индекс
        if item_data.count(':') < 2: # устанавливаю нужные правила что бы меньше 2 аргументов не работало
            print(f'В строке есть {row_index} ошибка ')
            continue
        item, quantity, prise = item_data.strip().split(':')
        items_count += 1 # считаю проходы и получаю количество
        items_sum += int(prise) * int(quantity)

        print(item)

print(f'В списке {items_count} позиций. Цена {items_sum}')