import turtle as trtl 
import random as rand


# ----instructions screen-----------------
# instructions text
text = trtl.Turtle()
text.color("black")
title_font = ("Comic Sans MS", 30, "bold")
text_font = ("Comic Sans MS", 20, "normal")
text.speed(0)
text.hideturtle()

# start button
b_start = trtl.Turtle()
b_start.shape("square")
b_start.turtlesize(5)
b_start.color("green")
b_start.penup()
b_start.speed(0)
b_start.goto(0, -100)

indent = -350

def start_screen():
  text.penup()
  text.goto(-200, 300)
  text.pendown()
  text.write("Whack a... Raccoon?", font=title_font)

  text.penup()
  text.goto(indent, 200)
  text.pendown()
  text.write("> Hit raccoons to gain 10 points!", font=text_font)

  text.penup()
  text.goto(indent, 100)
  text.color("red")
  text.pendown()
  text.write("> Do not hit the bird.", font=text_font)

  text.penup()
  text.goto(indent, 0)
  text.color("red")
  text.pendown()
  text.write("> DO NOT. hit the BIRD.", font=text_font)

# After start button is pressed, change screen
def start_click(x,y):
  trtl.clearscreen()
  wn.bgcolor("darkolivegreen3")
  gamescreen()

#-----game configuration--------------
# game runtime timer
timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False

# timer to change position of turtle
pos_timer = 30
pos_timer_up = False

score = 0

turtles = ["raccoon", "bird"]
points = [10, 0]

boundary_xy = (-200, 200) # Marks the boundary coordinates the turtle can go to -- change later ts is temporary

score_writer = trtl.Turtle()

#-----initialize turtle---------------
def initial_turtle():
  raccoon = trtl.Turtle()
  raccoon.color("red")
  raccoon.penup()
  raccoon.turtlesize(5)
  raccoon.goto(50, 100)

  bird = trtl.Turtle()
  bird.penup()
  bird.turtlesize(5)


def raccoon_clicked(raccoon, x,y):
  raccoon.hideturtle()

  global timer
  if timer != 0:
    update_score()
    change_position()
    
  else:
    raccoon.hideturtle()
  raccoon.showturtle()

def score_text():
  score_writer.hideturtle()
  score_writer.speed()
  score_writer.penup()
  score_writer.goto(-480, 300)
  score_writer.write("test", font=title_font)

def counter():
  counter =  trtl.Turtle()
  counter.hideturtle()
  counter.speed(0)
  counter.penup()
  counter.goto(-200, 300)
  counter.write("test", font=title_font)

def change_position(raccoon):
  xcor = rand.randint(boundary_xy) # change coordinates later
  ycor = rand.randint(boundary_xy)
  raccoon.goto(xcor, ycor)

def random_position(raccoon):
  x_rand = rand.randint(boundary_xy)
  y_rand = rand.randint(boundary_xy)
  raccoon.goto(x_rand, y_rand)

def update_score():
  global score
  score += 1
  score_writer.write(score, font=title_font)
  score_writer.clear()
  score_writer.write(score, font=title_font)

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=title_font)
    timer_up = True

  else:
    counter.write("Timer: " + str(timer), font=title_font)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 

#-----game functions------------------
def gamescreen():
  score_text()
  counter()
  initial_turtle()
  

def raccoon_onclick(raccoon):
  raccoon.onclick(raccoon_clicked)
#-----events--------------------------
wn = trtl.Screen()
wn.title("Whack...a......Raccoon..........??????")
wn.setup(width=1000, height=900)
wn.cv._rootwindow.resizable(False, False)

# instructions screen
wn.tracer(0)
start_screen()
wn.tracer(1)
b_start.onclick(start_click)
# raccoon_onclick()
wn.ontimer(countdown, counter_interval) 
wn.ontimer(random_position, counter_interval)

# game screen

# restart game: could add a onclick to reset game OR add reset button while game runtime

wn.mainloop()