from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()
screen.title("US States Game")
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name?: ")
print(answer_state)



screen.exitonclick()