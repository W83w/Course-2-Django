class Person():
    def eat(self):
        print('вкусно')

class Employee(Person):
    def visit_demo(self):
        print('Все сотрудники туда ходят')

class Developer(Employee):
    def review_code(self):
        print('Делаю код ревью коллеге')

class FrontendDeveloper(Developer):
    def code_frontend(self):
        print('Делаю запрос на сервер')

class BackendDeveloper(Developer):
    def code_backend(self):
        print('Ловим параметры запроса')

artur = Developer.review_code(1)