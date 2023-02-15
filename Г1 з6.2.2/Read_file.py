

#file = open('test.txt', 'rt') # r значит считывать t текстовый формат
# file = open('test.txt', 'rb') # r значит считывать b в бинарном формате если работаю с изображениями или аудио
#content = file.read(10) # считаю 10 байт чтобы считывать по очередно
#print(content)
#for line in file:
#    print(line)

#file.close() # закрываю чтобы не зависал в оп

#with open('test.txt', 'rt') as  file:   # для закрывания автоматически
#    for line in file:   # Не нужно закрывать файл самостоятельно
#        print(line)

guests_count = 0

with open('guets.txt', 'rt') as file:
    guests_count1 = len(file.readline())
    for line in file:
        print(line)
        guests_count += 1

print(f"Количество гостей: {guests_count}, всего символов {guests_count1}")