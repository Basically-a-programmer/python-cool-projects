
class QuizBrain:

    def __init__(self,q_list):
        self.question_no = 0
        self.question_list = q_list
        self.score = 0;

    def next_question(self):
        current_question = self.question_list[self.question_no]
        self.question_no +=1;
        user_ans = input(f"Q.{self.question_no}:{current_question.q_text} (True/False): ")
        self.check_ans(user_ans,current_question.q_ans)
    def still_has_question(self):
        return self.question_no < len(self.question_list)

    def check_ans(self,user_ans,correct_ans):
        if user_ans.lower() == correct_ans.lower():
            print("You got it correct ans")
            self.score+=1
        else:
            print("You got it wrong ans")
            print(f"The correct answer is {correct_ans}")

        print(f"Your score is {self.score} out of {self.question_no}" )
        print("\n")

    def print_score(self):
        print(f"Your final score is {self.score}/{self.question_no}")
