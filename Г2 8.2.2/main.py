# Получение ФИО
class Employee():
    '''
    Класс Сотрудника, который описывает Фамилию, Имя и очество
    '''
    def __init__(self, f, i, o):
        self.f = f # Фамилия
        self.i = i # Имя
        self.o = o # Отчество

    def __repr__(self):
        return f'{self.f} {self.i[0]} {self.o[0]}'

employees = [
    Employee('Питерская','Анисья','Григорьевна'),
    Employee('Иванов','Иван','Иванович')
]

print(employees)
print(employees[0].__doc__)