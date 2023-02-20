# задание 2 количество правильных ответов
def print_statistic(answer):
    answer_total = len(answer)
    answers_ = sum(answer)
    answers_incorect = answer_total - answers_
    print(f"Всего ответов : {answer_total}",
          f'верных: {answers_}',
          f'неверно: {answers_incorect}')

print_statistic([True, False, True, True])