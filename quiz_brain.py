class Quiz_brain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        no_of_questions = len(self.question_list)
        return self.question_number < no_of_questions

    def next_question(self):
        question = self.question_list[self.question_number]
        user_answer = input(
            f"Q{self.question_number + 1}. {question.text} (True/False)?: ")

        self.check_answer(user_answer, question.answer)
        self.print_score()
        print()

    def check_answer(self, user_answer, correct_answer):
        if user_answer.strip().capitalize() == correct_answer:
            self.score += 1
            print("That's correct. You got it right.")
        else:
            print("That's wrong.")
            print(f"The correct answer was: {correct_answer}")
            print()

        self.question_number += 1

    def print_score(self):
        if self.still_has_questions():
            print(
                f"Your current score is: {self.score}/{self.question_number}")
        else:
            print("You have completed the quiz.")
            print(
                f"Your final score is: {self.score}/{len(self.question_list)}.")
