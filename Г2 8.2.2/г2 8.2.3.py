class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def print_name(self):
        print(self.firstname, self.lastname)

    def run(self):
        print('Я не могу бежать, я человек')


class Runner(Person):
    def run(self):
        print(f'Привет, я - {self.firstname} и я бегу!')

student = Runner('Михаил', 'Альшевский')
student.print_name()
student.run()