from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface(object):
    _instance = None

    def __new__(cls, quiz_brain: QuizBrain):

        if not cls._instance:
            
            # set up class instance
            cls._instance = super(QuizInterface, cls).__new__(cls) 

            # set up quiz
            cls._instance.quiz = quiz_brain

            # set up window
            cls._instance.window = Tk()

            # set up window title
            cls._instance.window.title("Quizzler")
            # set up window size
            cls._instance.window.config(padx=20, pady=20, bg=THEME_COLOR)

            # set up score label's text and background color
            cls._instance.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
            # set up score label's position
            cls._instance.score_label.grid(row=0, column=1)

            # set up canvas background and color
            cls._instance.canvas = Canvas(width=300, height=250, bg="white")
            # set up question text
            cls._instance.question_text = cls._instance.canvas.create_text(
                150,
                125,
                width=280,
                text="Some Question Text",
                fill=THEME_COLOR,
                font=("Arial", 20, "italic")
            )

            # set up canvas position
            cls._instance.canvas.grid(row=1, column=0, columnspan=2, pady=50)

            # set up true image and true button
            true_image = PhotoImage(file="Python Bootcamp\Tkiner\GUI_Quiz_Project\images\\true.png")
            cls._instance.true_button = Button(image=true_image, highlightthickness=0, command= cls._instance.true_pressed)
            cls._instance.true_button.grid(row=2, column=0)

            # set up false image and false button
            false_image = PhotoImage(file="Python Bootcamp\Tkiner\GUI_Quiz_Project\images\\false.png")
            cls._instance.false_button = Button(image=false_image, highlightthickness=0, command= cls._instance.false_pressed)
            cls._instance.false_button.grid(row=2, column=1)

            cls._instance.get_next_question()

            cls._instance.window.mainloop()

        return cls._instance

    def get_next_question(self):

        self.canvas.config(bg="white")

        # there are still questions in the quizlet
        if self.quiz.still_has_questions():
            # configure scores
            self.score_label.config(text=f"Score: {self.quiz.score}")
            # go to the next question
            q_text = self.quiz.next_question()
            # configure question text on the canvas
            self.canvas.itemconfig(self.question_text, text=q_text)
        # no more question left
        else:
            # reach the end of the quiz
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            # disable true button
            self.true_button.config(state="disabled")
            # disable false button
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        # user clicks the right answer
        # give green feedback
        if is_right:
            self.canvas.config(bg="green")
        # user clicks the wrong answer
        # give red feedback
        else:
            self.canvas.config(bg="red")

        # after one second, go to the next question
        self.window.after(1000, self.get_next_question)








