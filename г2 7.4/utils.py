import json

def load_questions_from_json():
    file = open('data.json', 'r', encoding='utf-8')
    data = json.load(file)
    file.close()
    return data

def show_field(questions):
    for category_name, category_questions in questions.items():
        print(category_name.ljust(17), end='')
        for prise, questions_data in category_questions.items():
            asked = questions_data['asked']
            if not asked:
                print(prise.ljust(5), end=' ')
            else:
                print("        ".ljust(5), end=' ')
        print()
questions = load_questions_from_json()
#show_field(questions)

def parse_input(user_input):
    user_data = user_input.split(" ")

    if len(user_data) != 2:
        return False
    return {"category": user_data[0], 'prise': user_data[1]}

#print(parse_input('Еда 100'))

def print_questions(questions_text):
    print(f"Слово {questions_text} означает ")

def show_stats(points, correct, incorrect):
    print('У нас закончились вопросы')
    print('')
    print(f'Ваш счет {points}')
    print(f'Верных ответов {correct}')
    print(f'Неверных ответов {incorrect}')



def save_results_to_file(points, correct, incorrect):
    file = open('results.json', 'r')
    results = json.load(file)
    file.close()

    results.append({"points": points, "correct": correct, "incorrect": incorrect})

    file = open('results.json', 'w')
    json.dump(results, file)
    file.close()

