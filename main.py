import turtle
import pandas

screen = turtle.Screen()
my_turtle = turtle.Turtle()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

"""Get an input from the GUI by clicking on a random section"""
# def get_mousse_click_coor(x, y):
#   print(x, y) 
# turtle.onscreenclick(get_mousse_click_coor)

data = pandas.read_csv('50_states.csv')
states_list = data['state'].to_list()
x_coor = data['x'].to_list()
y_coor = data['y'].to_list()

guess_state = []
while len(guess_state) < 50:
  answer_state = screen.textinput(title=f"{len(guess_state)}/50 States Correct", prompt="What's another state name?").title()
  if answer_state == "Quit":
    missing_state= []
    for answer in states_list :
      if answer not in guess_state:
        missing_state.append(answer)
    new_data = pandas.DataFrame(missing_state)
    new_data.to_csv('missing_answers.csv')
      
    break
  else:
    for state_index, state in enumerate(states_list): 
      if state == answer_state:
        guess_state.append(state)
        my_turtle.hideturtle()
        my_turtle.penup()
        my_turtle.goto(x= x_coor[state_index], y= y_coor[state_index])
        my_turtle.write(f'{state}', align='center',font=('bold', 10, 'normal'))
    
