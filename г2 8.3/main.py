import random

from Question import Question
from data import questions_data
from utils import load_questions

def main():

    questions = []

    for question_data in questions_data:
        new_question = Question(
            question_data["q"],
            int(question_data["d"]),
            question_data["a"]
        )

        questions.append(new_question)
        random.shuffle(questions)

    for question in questions:
        print(question.build_question())

        user_answer = input()
        question.user_answer = user_answer

        if question.is_correct():
            print(question.build_positive_feedback())
        else:
            print(question.build_negative_feedback())
    counter = 0
    points = 0

    for question in questions:
        if question.is_correct():
            counter += 1
            points += question.get_points()

    print('Вот и все!')
    print(f"Отвечено вопросов {counter} из {len(questions)}")
    print(f"Набрано балов: {points}")


main()