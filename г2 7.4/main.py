'''
 предлагается категория, а потом задается вопрос по этой категории
 Для начала надо в вести категорию с большой буквы и количество очков например
 Еда 200
 После чего будет вопрос на который нужно ответить с маленькой буквы например
 Слово carrot означает
 морковь
'''
from pprint import pprint as pp
import utils

questions = utils.load_questions_from_json()
some_questions_left = True
points, correct, incorrect = 0, 0, 0
questions_total = 9


while correct + incorrect < questions_total:

    utils.show_field(questions)

    user_input = input()
    user_data = utils.parse_input(user_input)

    if not user_data:
        print('Нет такой категории или вопроса')
        continue
    category, price = user_data['category'], user_data['prise']

    question = questions[category][price]

    if question['asked']:
        print('Вы уже это спрашивали')
        continue

    # Здесь проверка

    utils.print_questions(question['question'])
    user_answer = input().lower()

    if user_answer == question['answer']:
        print('Ответ верный ')
        points += int(price)
        correct += 1
    else:
        print('Ответ не верный')
        points -= int(price)
        incorrect += 1


    question['asked'] = True

utils.show_stats(points, correct, incorrect)
utils.save_results_to_file(points, correct, incorrect)