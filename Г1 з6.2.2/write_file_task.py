user_language = input("Какой язык программирования вы учете")
user_time = input("Как давно?")
user_institution = input('Где?')

with open('answer.txt', 'w') as file:  # здесь записываю ответы пользователь t опустил так как по умолчанию текст
    file.write(f"{user_language}\n")
    file.write(f"{user_time}\n")
    file.write(f"{user_institution}\n")

print('Ответы записаны')

# ����� ���-�� ���������� ��������� � ������
print("� �����!!!!!")
