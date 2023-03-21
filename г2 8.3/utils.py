import random

from data import questions_data
from Question import Question

def load_questions():
    questions = []

    for question_data in questions_data:
        new_question = Question(
            question_data["q"],
            int(question_data["d"]),
            question_data["a"]
        )

        questions.append(new_question)
        random.shuffle(questions)

print(load_questions())