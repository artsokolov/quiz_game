from quiz import Quiz
from questions_gateway import QuestionsGateway

api = QuestionsGateway()
categories = api.list_categories()

for category_id, category_name in categories.items():
    print(f"{category_id}. {category_name}")

chosen_id = int(input('Choose category id: '))
if chosen_id not in categories:
    raise ValueError('Chosen id is not valid')

questions_number = int(input('How many questions? Write number: '))

questions = api.list_questions(questions_number, chosen_id)

quiz = Quiz(questions)
quiz.start()