from turtle import Turtle, Screen
import pandas as pd
import time

from pandas.core.common import not_none

data = pd.read_csv('50_states.csv')
state_list = data.state.values

# print(data.state.values)

turtle = Turtle()
screen = Screen()
screen.title("US States Game")
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

state_spot = Turtle()
state_spot.hideturtle()
state_spot.penup()

correct_answer = 0
total_states = len(state_list)


game_is_on = True

while game_is_on:
    answer_state = screen.textinput(title=f"{correct_answer}/{total_states} States Correct",
                                    prompt="What's another state's name?: ").capitalize()
    # print(data.state.tolist())
    # print(data.state.values)
    if answer_state in state_list:
        # print(answer_state,state)
        correct_answer += 1
        # target_row = (data[data.state == state])
        state_data = data[data.state == answer_state]
        # print(state_data.x.values, state_data.y.values)
        # state_spot.goto(state_data.x.values[0], state_data.y.values[0])
        n_pos = (int(state_data.iloc[0].x), int(state_data.iloc[0].y))
        state_spot.goto(n_pos)
        state_spot.write(answer_state, align='center', font=('Arial', 10, 'bold'))
        if correct_answer == total_states:
            game_is_on = False



screen.exitonclick()