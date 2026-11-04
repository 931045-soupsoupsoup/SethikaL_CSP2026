import turtle as trtl 
import random as rand
wn = trtl.Screen()

# ----instructions screen-----------------
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

# instructions text
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

  text.penup()
  text.goto(-70, -200)
  text.color("black")
  text.pendown()
  text.write("^^Play!^^", font=text_font)

# After start button is pressed, change screen + Clears screen without erasing all of the turtles made (raccoon, bird): debugged
def start_click(x,y):
  text.clear()
  b_start.hideturtle()
  wn.bgcolor("darkolivegreen3")
  gamescreen()

#-----game configuration--------------
# game runtime timer
timer = 45
counter_interval = 1500   #1000 represents 1 second
timer_up = False

trtl_counter = 3000 # counter interval to change position of turtle
score = 0

turtles = []
points = [10, -5]

#-----initialize turtle---------------
'''for i in range(len(points)):
  t = trtl.Turtle()
  t.penup()
  turtles.append(t)'''

raccoon = trtl.Turtle()
raccoon.hideturtle()
raccoon.color("red")
raccoon.penup()
raccoon.turtlesize(10)
raccoon.goto(50, 100)

bird = trtl.Turtle()
bird.hideturtle()
bird.penup()
bird.turtlesize(10)

score_writer = trtl.Turtle()
score_writer.hideturtle()

counter = trtl.Turtle()
counter.hideturtle()
counter.speed(0)
counter.penup()
counter.goto(-200, 300)

'''def t_clicked(x,y):
  t.hideturtle()
  
  global timer
  if timer != 0:
    update_score()
    change_position()
    t.showturtle()
    
  else:
    t.hideturtle()
  t.showturtle()'''

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
    bird.hideturtle()
  bird.showturtle()

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
  wn.ontimer(change_position, trtl_counter)

def update_score():
  global score
  '''for i in range(len(points)):
    if (turtles[i] == points[0]):
      score += (points[0])

    else: 
      score += (points[1])'''
  score_writer.write("Score: " + str(score), font=title_font)
  score_writer.clear()
  score_writer.write("Score: " + str(score), font=title_font)

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
  raccoon.showturtle()
  bird.showturtle()
  score_text()
  countdown()
  change_position()
  wn.ontimer(countdown, counter_interval) 

  # wn.ontimer(add_raccoon, pos_count)
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


# restart game: could add a onclick to reset game OR add reset button while game runtime

wn.mainloop()