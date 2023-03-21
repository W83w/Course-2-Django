if 5 > 3:
    print('True')

x = 5
y = 2
if x < 6:
  print('сработало первое условие')
elif x % y == 1:
  print('сработало второе условие')
elif x % y > 2 or x >= 6:
  print('остался else')



every2ndElement = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
for i in every2ndElement:
    if i % 2 == 0:
        print()



fromForToWhile = []
i = 0
while len(fromForToWhile) < 10:
    i = i + 1
    fromForToWhile.append(i)
print(fromForToWhile, '4')

someList = [8, 15, 6, 67, 0, 13, 1, 34]
for i in someList:
    try:
        print(1/i)
    except:
        print('ошибка')
