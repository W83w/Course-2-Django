virus_code = "Я вирус"

with open('write_file_task.py') as file: # вирус будет дописывать
    content = file.read()

    if virus_code in content:
        print('Вирус обнаружен!') # ищет по сообщению я вирус
    else:
        print('Все хорошо')