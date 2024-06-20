from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for q_set in question_data:
    new_q = Question(q_set["text"], q_set["answer"])
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()