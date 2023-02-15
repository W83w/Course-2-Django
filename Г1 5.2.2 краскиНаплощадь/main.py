def paint_count(width, height, consumption = 0.2, layers = 2):
    total = width * height * consumption * layers

    return total

#эту функцию можно вызвать 3 разными способами 2, 3 и 4 аргументами просто если их не указывать они используются
# по умолчанию
print(paint_count(3, 4))
print(paint_count(3, 4, 0.4))
print(paint_count(3, 4, 0.4, 3))
