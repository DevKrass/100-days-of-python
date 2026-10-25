import turtle

import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()


def place_state_on_map(answer_state):
    state = data[data.state == answer_state]
    text = turtle.Turtle()
    text.hideturtle()
    text.penup()
    text.goto(state.x.item(), state.y.item())
    text.write(answer_state)


guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="What's another state's name?",
    ).title()
    if answer_state in all_states and answer_state not in guessed_states:
        place_state_on_map(answer_state)
        guessed_states.append(answer_state)

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        states_to_learn = pandas.DataFrame(missing_states)
        states_to_learn.to_csv("states_to_learn.csv")
        break
