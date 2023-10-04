from typing import List
from abc import ABC, abstractmethod


class Option:
    def __init__(self, text: str, is_right: bool):
        self.text = text
        self.is_right = is_right


class BaseQuestion(ABC):
    @abstractmethod
    def question_text(self, question_number: int) -> str:
        ...

    @abstractmethod
    def is_answer_correct(self, answer) -> bool:
        ...

    @abstractmethod
    def correct_answer(self):
        ...

    @abstractmethod
    def ask_answer_text(self) -> str:
        ...


class MultipleChoiceQuestion(BaseQuestion, ABC):
    def __init__(self, question: str, options: List[Option]):
        self.question = question
        self.options = options

    def question_text(self, question_number: int) -> str:
        option_texts = []
        for option in self.options:
            option_texts.append(option.text)

        return "Q%d. %s\n1. {:<50} 2. {:<10}\n3. {:<50} 4. {:<10}".format(*option_texts) % (question_number, self.question)

    def __find_option(self, option_number: int) -> Option:
        if option_number > len(self.options) or option_number < 1:
            raise AttributeError('Option number is invalid')

        return self.options[option_number - 1]

    def is_answer_correct(self, answer) -> bool:
        answer_option = self.__find_option(int(answer))

        return answer_option.is_right

    def correct_answer(self):
        for option in self.options:
            if option.is_right:
                return option.text

    def ask_answer_text(self) -> str:
        return "Choose option number: "


class TrueFalseQuestion(BaseQuestion, ABC):
    def __init__(self, question: str, answer: str):
        self.question = question
        self.answer = answer

    def question_text(self, question_number: int) -> str:
        return f"Q{question_number}. {self.question} (True or False)"

    def is_answer_correct(self, answer) -> bool:
        return answer == self.answer

    def correct_answer(self):
        return self.answer

    def ask_answer_text(self) -> str:
        return "Your answer: "
