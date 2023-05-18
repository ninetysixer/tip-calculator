import pandas
import turtle

screen = turtle.Screen()
screen.title("Turkiye Province Guessing Game by Ninetysix")
image = "turkiye_map.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("provinces.csv")
all_states = data.state.to_list()
guessed_states = []


# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()
#
# screen.exitonclick()


while len(guessed_states) < 81:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/81 States Correct",
                                    prompt=" What another state's name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        # missing_states = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        if answer_state not in guessed_states:
            guessed_states.append(answer_state)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data.state == answer_state]
            t.goto(int(state_data.x), int(state_data.y))
            t.color("dark blue")
            t.write(answer_state)
        else:
            continue
