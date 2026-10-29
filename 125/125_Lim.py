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
timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False

score = 0

turtles = ["raccoon", "bird"]
points = [10, 0]



#-----initialize turtle---------------
def initial_turtle():
  raccoon = trtl.Turtle()
  raccoon.penup()
  raccoon.turtlesize(5)
  raccoon.goto(50, 100)

  bird = trtl.Turtle()
  bird.penup()
  bird.turtlesize(5)

def score_text():
  score_writer = trtl.Turtle()
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

def change_position():
  xcor = rand.randint(-250, 250)
  ycor = rand.randint(-200, 200)

#-----game functions------------------
def gamescreen():
  score_text()
  counter()
  initial_turtle()
#-----events--------------------------
wn = trtl.Screen()
wn.setup(width=1000, height=900)
wn.cv._rootwindow.resizable(False, False)

# instructions screen
wn.tracer(0)
start_screen()
wn.tracer(1)
b_start.onclick(start_click)

# game screen

# restart game: could add a onclick to reset game OR add reset button while game runtime

wn.mainloop()