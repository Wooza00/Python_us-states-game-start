from turtle import Turtle


class Pointer(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def wrt_answer(self, state, x, y):
        self.setposition(x, y)
        self.write(arg=f"{state}", align="center", font=("courier", 8, "normal"))
