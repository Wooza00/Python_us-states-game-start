import turtle
import pandas
from pointer import Pointer

pointer = Pointer()
screen = turtle.Screen()
screen.title("U.S. States game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
data_dic = data.to_dict()
states = data_dic["state"]
x = data_dic["x"]
y = data_dic["y"]


right_ans = 0
game_on = True

while game_on:
    count = 0
    answer = screen.textinput(title=f"{right_ans}/50 States Correct", prompt="What's another state name?").title()

    for i in states:
        if answer == states[i]:
            pointer.wrt_answer(answer, x[count], y[count])
            right_ans += 1
        count += 1

    if right_ans == 50:
        print("Congrats you WIN!")
        game_on = False


screen.mainloop()
