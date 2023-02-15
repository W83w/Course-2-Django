# имя человека учит язык
with open('students.txt', 'r') as file:
    for student_data in file:
        #data = student_data.rstrip('/n').split(':') # rstrip нужен так как с право стоит !

        #name = data[0]
        #language = data[1]
        name, language = student_data.rstrip('/n').split(':') # распаковка результата на 2 переменных

        print(f"{name} учит {language}!")
