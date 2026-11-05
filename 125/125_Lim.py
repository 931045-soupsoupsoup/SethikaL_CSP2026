import turtle as trtl 
import random as rand

wn = trtl.Screen()

# ----instructions screen-----------------
text = trtl.Turtle()
text.color("black")
title_font = ("Comic Sans MS", 30, "bold")
text_font = ("Comic Sans MS", 20, "normal")
sub_font = ("Comic Sans MS", 10, "normal")
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

# reset button initialize
reset = trtl.Turtle()
reset.hideturtle()
reset.shape("square")
reset.turtlesize(5)
reset.color("red")
reset.penup()
reset.speed(0)
reset.goto(0, -100)

# reset screen initialize
drawer = trtl.Turtle()
drawer.hideturtle()

indent = -400

# instructions text
def start_screen():
  text.penup()
  text.goto(-200, 300)
  text.pendown()
  text.write("Whack a... Raccoon?", font=title_font)

  text.penup()
  text.goto(-235, 280)
  text.pendown()
  text.write("(Except you have to chase them out of your yard. You'll know what I mean.)", font=sub_font)

  text.penup()
  text.goto(indent, 200)
  text.pendown()
  text.write("> Hit raccoons to gain 10 points! They might get fast... or teleport.", font=text_font)

  text.penup()
  text.goto(indent, 100)
  text.color("red")
  text.pendown()
  text.write("> Do not hit the bird. (-20)", font=text_font)

  text.penup()
  text.goto(indent, 0)
  text.color("red")
  text.pendown()
  text.write("> DO NOT. hit the bird. It's la peaceful.", font=text_font)

  text.penup()
  text.goto(-55, -200)
  text.color("black")
  text.pendown()
  text.write("^^Play!^^", font=text_font)

# After start button is pressed, change screen + Clears screen without erasing all of the turtles made (raccoon, bird): debugged
def start_click(x,y):
  text.clear()
  b_start.hideturtle()
  wn.bgcolor("darkolivegreen3")
  wn.bgpic("GitHubCSP2026/125/grassbg.png")
  gamescreen()

#-----game configuration--------------
# game runtime timer
timer = 20
counter_interval = 1500   #1000 represents 1 second
timer_up = False

trtl_counter = 2000 # counter interval to change position of turtle
score = 0

bird_counter = 1000 # yeah

points = [10, -20]

#-----initialize turtle---------------
raccoon_img = "GitHubCSP2026/125/raccoon.gif"
wn.addshape(raccoon_img)
raccoon = trtl.Turtle(shape=raccoon_img)
raccoon.hideturtle()
raccoon.color("red")
raccoon.penup()
raccoon.turtlesize(10)
raccoon.goto(50, 100)

bird_img = "GitHubCSP2026/125/bird.gif"
wn.addshape(bird_img)
bird = trtl.Turtle(shape=bird_img)
bird.hideturtle()
bird.penup()
bird.turtlesize(10)

explosion = "GitHubCSP2026/125/explode.gif"
wn.addshape(explosion)

score_writer = trtl.Turtle()
score_writer.hideturtle()

counter = trtl.Turtle()
counter.hideturtle()
counter.speed(0)
counter.penup()
counter.goto(-200, 300)

def raccoon_clicked(x,y, index):
  raccoon.hideturtle()

  global timer
  if timer != 0:
    global score 
    gained_points = points[index]
    score += gained_points
    update_score()
    change_position()
    raccoon.showturtle()
    
    
  else:
    raccoon.hideturtle()
  raccoon.showturtle()

def bird_clicked(x,y, index):
  bird.shape(explosion)
  bird.hideturtle()

  global timer
  if timer != 0:
    global score
    gained_points = points[index]
    score += gained_points
    update_score()
    bird_change_position()
    bird.showturtle()
    
  else:
    bird.shape(explosion)
    bird.hideturtle()
  bird.shape(bird_img)

def score_text():
  score_writer.hideturtle()
  score_writer.speed(0)
  score_writer.penup()
  score_writer.goto(-480, 300)
  score_writer.write("Score: " + str(score), font=title_font)

def change_position():
  xcor = rand.randint(-380, 380)
  ycor = rand.randint(-350, 200)
  raccoon.goto(xcor, ycor)
  wn.ontimer(change_position, trtl_counter)

def bird_change_position():
  xcor = rand.randint(-380, 380)
  ycor = rand.randint(-350, 200)
  bird.goto(xcor, ycor)
  wn.ontimer(bird_change_position, bird_counter)

def update_score():
  global score
  score_writer.write("Score: " + str(score), font=title_font)
  score_writer.clear()
  score_writer.write("Score: " + str(score), font=title_font)

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=title_font)
    timer_up = True
    endscreen()

     
  else:
    counter.write("Timer: " + str(timer), font=title_font)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)

# Results screen
def endscreen():

  drawer.speed(0)
  drawer.hideturtle()
  drawer.penup()
  drawer.pencolor("white")
  drawer.fillcolor("white")
  drawer.goto(-600, -400)
  drawer.pendown()
  drawer.setheading(0)
  drawer.right(45)
  drawer.begin_fill()
  drawer.circle(800, steps=4)
  drawer.end_fill()

  text.penup()
  text.goto(-175, 300)
  text.pendown()
  text.write("FINAL RESULTS:", font=title_font)

  global score
  text.penup()
  text.goto(-260, 100)
  text.pendown()
  text.write("You have gained " + str(score) + " points!", font=title_font)

  text.penup()
  text.goto(-400, 0)
  text.pendown()
  text.write("Restart? (hard reset to see instructions)", font=title_font)

  # reset button
  reset.showturtle()
  reset_click()

def reset_click(x,y): 
  wn.ontimer(countdown, counter_interval)
  wn.ontimer(change_position, trtl_counter)
  wn.ontimer(bird_change_position, bird_counter)

  text.clear()
  drawer.clear()
  reset.hideturtle()
  gamescreen()
  update_score()

#-----game functions------------------
def gamescreen():
  global score
  score = 0
  global timer
  timer = 20

  raccoon.showturtle()
  bird.showturtle()
  score_text()
  countdown()
  change_position()
  wn.ontimer(countdown, counter_interval) 

#-----events--------------------------
wn.title("Whack...a......Raccoon..........??????")
wn.setup(width=1000, height=900)
wn.cv._rootwindow.resizable(False, False)

# instructions screen
wn.tracer(0)
start_screen()
wn.tracer(1)

# game screen
b_start.onclick(start_click)
raccoon.onclick(lambda x, y: raccoon_clicked(x, y, 0))
bird.onclick(lambda x, y: bird_clicked(x, y, 1))

# restart game
reset.onclick(reset_click)

wn.mainloop()