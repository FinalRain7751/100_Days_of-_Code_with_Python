from data import Question_bank
from question_model import Question
from quiz_brain import Quiz_brain

while True:
    try:
        number_of_questions = int(
            input("How many questions do you want?: "))  # Max 50
        if number_of_questions > 50 or number_of_questions <= 0:
            continue
        break
    except ValueError:
        print("Enter a valid integer between 1 and 50.")


question_data = Question_bank(10).question_data
question_bank = []
for question in question_data:
    text = question["question"]
    answer = question["correct_answer"]
    question_bank.append(Question(text, answer))

quiz = Quiz_brain(question_bank)

while (quiz.still_has_questions()):
    print()
    quiz.next_question()
