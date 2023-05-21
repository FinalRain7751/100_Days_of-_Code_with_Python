from data import question_data
from question_model import Question
from quiz_brain import Quiz_brain

question_bank = []
for question in question_data['results']:
    text = question["question"]
    answer = question["correct_answer"]
    question_bank.append(Question(text, answer))

quiz = Quiz_brain(question_bank)

while (quiz.still_has_questions()):
    quiz.next_question()
# def main():
