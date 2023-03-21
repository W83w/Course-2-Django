#тема обязательные аргументы
def with_tax(value, tax_parcanage):
    total = value + value * tax_parcanage / 100
    return total
print(with_tax(10000, 5))


def with_tax(value, tax_parcenage):
    total = value + value * tax_parcenage/ 100
    return total
salary = 10000
income_tax = 6
total = with_tax(salary, income_tax)
print(total)


def calc(numbers):
    i = 0
    for number in numbers:
        i += int(number)
    return i

def main():
    numbers = input("Введите числа через пробел") # числа через пробел
    list_number = numbers.split(' ')
    result = calc(list_number)
    print(result)

main()