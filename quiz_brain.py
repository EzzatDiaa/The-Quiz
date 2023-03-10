class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    # Make a function to know when to end the questions from the question_list
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    # Make a function to know which question stopped at and show the user
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, current_question):
        if user_answer.lower() == current_question.lower():
            self.score += 1
        else:
            self.score = self.score
