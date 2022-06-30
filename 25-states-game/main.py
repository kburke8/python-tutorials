import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
correct_states = []

while len(correct_states) < 50:
    answer_state = screen.textinput(title=f"{len(correct_states)}/50 Guess The State",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in states:
            if state not in correct_states:
                missing_states.append(state)
        new_data = pandas   .DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
        
    if answer_state in states and answer_state not in correct_states:
        correct_states.append(answer_state)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state = data[data.state == answer_state]
        t.goto(float(state.x), float(state.y))
        t.write(answer_state)
