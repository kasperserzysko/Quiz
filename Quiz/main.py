import turtle
import pandas

def get_x(state):
    states = states_data[states_data.state == state]
    states_x = states['x'].tolist()
    return states_x[0]
def get_y(state):
    states = states_data[states_data.state == state]
    states_y = states['y'].tolist()
    return states_y[0]



states_data = pandas.read_csv('50_states.csv')
states_names = states_data['state'].to_list()



states_answered = 0
screen = turtle.Screen()
screen.title('U.S. QUIZ GAME')
states_map = 'blank_states_img.gif'
screen.addshape(states_map)
turtle.shape(states_map)


while True:
    answer_state = screen.textinput(title=f"{states_answered}/50 States Correct", prompt='Give a state name')
    if answer_state in states_names:
        text = turtle.Turtle()
        text.hideturtle()
        text.penup()
        text.setposition(get_x(answer_state),get_y(answer_state))
        text.write(answer_state, align='left')
        states_answered += 1
        states_names.remove(answer_state)
    if states_answered == 50:
        quit()

turtle.mainloop()
screen.exitonclick()





