from tkinter import *

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: 0", background=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            font=("Arial", 20, "italic"),
            text="Question",
            fill=THEME_COLOR,
            width=280,
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        true_button_image = PhotoImage(file="images/true.png")
        self.true_button = Button(
            image=true_button_image,
            highlightthickness=0,
            command=lambda: self.check_answer("True"),
        )
        self.true_button.grid(row=2, column=0)

        false_button_image = PhotoImage(file="images/false.png")
        self.false_button = Button(
            image=false_button_image,
            highlightthickness=0,
            command=lambda: self.check_answer("False"),
        )
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_tex = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_tex)
        else:
            self.canvas.itemconfig(
                self.question_text, text="You've reached the end of the quiz."
            )
            self.true_button.config(state=DISABLED)
            self.false_button.config(state=DISABLED)

    def check_answer(self, answer):
        is_right = self.quiz.check_answer(answer)
        self.score_label.config(text=f"Score : {self.quiz.score}")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
