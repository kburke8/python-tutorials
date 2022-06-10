class QuizBrain:

    def __init__(self, questions_list):
        self.questions_list = questions_list
        self.question_number = 0
        self.score = 0

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number }: {current_question.text} (True/False): ")
        self.check_answer(answer, current_question.answer)

    def still_has_questions(self):
        return self.question_number < len(self.questions_list) - 1

    def check_answer(self, answer, correct_answer):
        if answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")

        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}.")
        print("\n")

    def complete_quiz(self):
        print("You've completed the quiz.")
        print(f"Your final score was: {self.score}/{len(self.questions_list)}.")