from question import BaseQuestion, Option, MultipleChoiceQuestion, TrueFalseQuestion
import random


class QuestionFactory:
    @classmethod
    def new_question(cls, question_data) -> BaseQuestion:
        if question_data['type'] == 'multiple':
            options_texts = question_data['incorrect_answers'] + [question_data['correct_answer']]

            options = []
            for option_text in options_texts:
                options.append(Option(option_text, option_text == question_data['correct_answer']))

            random.shuffle(options)
            return MultipleChoiceQuestion(question_data['question'], options)
        else:
            return TrueFalseQuestion(question_data['question'], question_data['correct_answer'])