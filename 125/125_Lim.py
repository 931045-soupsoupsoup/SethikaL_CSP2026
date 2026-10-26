import turtle as trtl 
import random as rand

# ----instructions screen-------
text = trtl.Turtle()
text.color("black")
title_font = ("Comic Sans MS", 30, "bold")
text_font = ("Comic Sans MS", 20, "normal")
text.speed(0)
text.hideturtle()

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


#-----events----------------
wn = trtl.Screen()
wn.setup(width=1000, height=900)
wn.cv._rootwindow.resizable(False, False)
start_screen()

wn.mainloop()