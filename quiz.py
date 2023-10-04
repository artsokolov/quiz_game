from typing import List

from question import BaseQuestion


class Quiz:
    __questions = []
    __current_score = 0
    __current_question = 0

    def __init__(self, questions: List[BaseQuestion]):
        self.__questions = questions

    def __user_score(self):
        return f"{self.__current_score}/{self.__current_question}"

    def start(self):
        for question in self.__questions:
            print('---------------------------')

            self.__current_question += 1
            print(question.question_text(self.__current_question))
            answer = input(question.ask_answer_text())

            if question.is_answer_correct(answer):
                self.__current_score += 1
                print('You got it right!')
            else:
                print('Sorry, you are wrong!')

            print('The correct answer was:', question.correct_answer())
            print('Your current score:', self.__user_score())
        print("You've completed the quiz")
        print(f"You final score:", self.__user_score())