import random

Character_Mood = 100 #Настроение персонажа

game_Money = 10 #Игровые деньги персонажа
Wins = 0  #Количество побед из за которых выдают злавный приз
Wins2 = 0 #Количество побед во 2 автомате
Real_money = 10 #Реальные деньги персонажа

while Character_Mood > 0: # Персонаж играет пока настроение есть
    Character_Mood -= 50 # Пока не выиграл главный приз персонаж спрашивает самого себя зачем и настроение падает
    while game_Money > 0: #Если денеги есть
        for Attempts in range(15):  #Персонаж играет 15 игр в 1 автомат
            Attempts += 1 # Игры которые хотел с играть персонаж
            game_Money -= 1  #Что стоит 1 монетку
            Slot_machine = random.randint(0, 5) #Шанс на победу Очень хороший < 5 проиграл = 5 выиграл
            if game_Money < 0: # Если игровых денег нет, всегда можно обменять их на игровые
                if Real_money >= 1: # Настоящуу на игровую
                    Real_money -= 1 #настоящая
                    game_Money += 1 #+игровая
                    print("транзакция успешно завершена", Real_money, "Игровые деньги", game_Money) #Статистика для отчета
                else: # Если денег нет то все
                    break
            if Slot_machine == 2: #Если вдруг победил
                game_Money += 2 #Награда
                Wins += 1 # + Победа
                print("транзакция успешно завершена", Real_money, "Игровые деньги", game_Money) # Статистика
            else:
                print("lose", game_Money, ' Настоящие деньги', Real_money )  # Статистика
        for Attempts2 in range(5):  # Персонаж играет 5 игр
            Attempts2 += 1 # количество игр
            game_Money -= 3  # Что стоит 3 монетки
            Slot_machine = random.randint(0, 5)  # Шанс на победу Очень хороший < 5 проиграл = 5 выиграл
            if game_Money < 0:  # Если игровых денег нет, всегда можно обменять их на игровые
                if Real_money >= 4: # Обмен
                    Real_money -= 4
                    game_Money += 3
                    print("Зачем", Real_money, game_Money)
                else:
                    break
                if Slot_machine == 5:  # Если вдруг победил
                    game_Money += 20  # Награда
                    Wins2 += 1
                    print("Win", game_Money, ' Настоящие деньги', Real_money)  # Статистика
                else:
                    print("lose", game_Money, ' Настоящие деньги', Real_money)  # Статистика
            break
        break


if Wins > 7 or Wins2 > 5: # Многго побед то Супер приз
    Character_Mood += 100
    Real_money += 10000000000
    print("Вы богаты, но почему?", "  Настоящие деньги",Real_money, "Настроение", Character_Mood)
else:
    if game_Money < 0:
        print('Это конец', Real_money, "Настроение", Character_Mood)
    else:
        print("Повезет в следующий раз, нет", '  Настоящие деньги', Real_money, "Настроение", Character_Mood)

