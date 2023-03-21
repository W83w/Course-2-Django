# Цепочка наследования Проверка почты и логина
class Input():
    def __init__(self, name, value = None):
        self.name = name
        self.value = value

class TextInput(Input):
    def is_empty(self):
        return  self.value == None

class EmailInput(TextInput):

    def check(self):
        has_at = self.value.count("@") == 1
        has_dot = self.value.count(".") >= 1
        if has_at and has_dot:
            return True
        return False

class PasswordInput(TextInput):
    def check(self):
        if len(self.value) < 0:
            return

usermail = EmailInput("usermail", "me@mail.ry")
print(usermail.is_empty()) # Проверка на то пустая ли строка
print(usermail.check()) # проверка на корректность заполнения
