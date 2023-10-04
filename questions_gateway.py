from typing import List, Dict

import requests
from question_factory import QuestionFactory
from question import BaseQuestion


class QuestionsGateway:
    __api_domain = 'https://opentdb.com/'

    def list_categories(self) -> Dict:
        request_url = self.__api_domain + 'api_category.php'
        response = requests.get(request_url).json()
        if 'trivia_categories' not in response:
            raise RuntimeError('API response is not valid')

        categories = {}
        for category in response['trivia_categories']:
            categories[category['id']] = category['name']

        return categories

    def list_questions(self, number_of_questions: int, category_id: int) -> List[BaseQuestion]:
        request_url = self.__api_domain + 'api.php?amount=' + str(number_of_questions) + '&category=' + str(category_id)
        response = requests.get(request_url).json()
        if 'results' not in response:
            raise RuntimeError('API response is invalid')

        questions = []
        for question_response in response['results']:
            questions.append(QuestionFactory.new_question(question_response))

        return questions
