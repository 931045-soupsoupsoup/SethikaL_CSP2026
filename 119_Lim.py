import turtle as trtl

# Set up screen
wn = trtl.Screen()
wn.tracer(0)
wn.bgcolor("burlywood3")

# Turtles
# Create custom turtle and register it
custom_polygon = ((0, -6), (6, -5), (8, -4), (9, 0), (0, 10), (-9, 0), (-8, -4), (-6, -5), (0, -6))
wn.register_shape("cream", custom_polygon)

# Create whip cream as a custom turtle and rename other turtle variables
icing = trtl.Turtle() # initial turtle to draw out cake before toppings

whip_cream = trtl.Turtle()
whip_cream.shape("cream")
whip_cream.color("antiquewhite3")
whip_cream.fillcolor("antiquewhite1")
# ***
strawberry_top = trtl.Turtle()
strawberry_top.shape("triangle")
strawberry_top.color("indianred2")
strawberry_top.fillcolor("indianred1")
# ***
blueberry_top = trtl.Turtle()
blueberry_top.shape("circle")
blueberry_top.color("royalblue2")
blueberry_top.fillcolor("royalblue")
# ***
chocolate_top = trtl.Turtle()
chocolate_top.shape("square")
chocolate_top.color("saddlebrown")
chocolate_top.fillcolor("saddlebrown")
# ***
banana_top = trtl.Turtle()
banana_top.shape("circle")
banana_top.color("gold1")
banana_top.fillcolor("khaki")

# check toppings (use for debug if needed)
'''strawberry_top.goto(50, 10)
blueberry_top.goto(10, 50)
banana_top.goto(150, 50)
chocolate_top.goto(100, 15)
whip_cream.goto(30, 20)'''

# hide turtles
strawberry_top.hideturtle()
blueberry_top.hideturtle()
chocolate_top.hideturtle()
banana_top.hideturtle()
whip_cream.hideturtle()

# Definitions
def draw_icing():
  icing.showturtle()
  icing.penup()
  icing.pensize(5)
  icing.goto(-160, 150)

  icing.pendown() # covers bigger area of icing 
  icing.begin_fill()
  icing.setheading(0)
  icing.forward(380)
  icing.circle(-60, 80)
  icing.setheading(270)
  icing.forward(50)
  icing.setheading(180)
  icing.forward(490)
  icing.setheading(90)
  icing.forward(41)
  icing.circle(-60, 80)
  icing.end_fill()
  icing.penup()

  icing.goto(-150, 0) # draws the icing drips or something to make it look more detailed idk
  icing.setheading(0)
  for i in range(4):
    icing.pendown()
    icing.begin_fill()
    icing.circle(45)
    icing.end_fill()
    icing.penup()
    icing.forward(120)

def base_cake():
  icing.speed(0) # change speed if needed

  # cake platter
  icing.penup()
  icing.color("lightsalmon4")
  icing.fillcolor("lightsalmon4")
  icing.pensize(80)
  icing.goto(-250, -240)

  icing.pendown()
  icing.forward(570)


  # Base cake
  icing.penup()
  icing.color("cornsilk")
  icing.fillcolor("cornsilk")
  icing.pensize(5)
  icing.goto(-160, 150)

  icing.pendown()
  icing.begin_fill()
  icing.forward(380)
  icing.circle(-60, 80)
  icing.setheading(270)
  icing.forward(270)
  icing.circle(-60, 80)
  icing.right(10)
  icing.forward(380)
  icing.circle(-60, 80)
  icing.setheading(90)
  icing.forward(270)
  icing.circle(-60, 80)
  icing.end_fill()
  icing.penup()
  icing.hideturtle()

# update screen
wn.update()
wn.tracer(1)

# *** This section begins the program the user sees ***

# starting screen
answer = trtl.textinput("Welcome!","Type in OK to begin the Cake Maker!")
while (answer != "ok"):
  answer = trtl.textinput("bro", "JUST TYPE IN OK")
else: 
  base_cake()


# draws icing ////// work on debugging this section
icing_colors = ["lightpink", "lightskyblue", "mintcream", "chocolate4", "gold"]
icing_flavors = ["strawberry", "blueberry", "vanilla", "chocolate", "banana"]

# ask user what flavor
user_index= trtl.
answer = trtl.textinput("What flavor would you like?","OPTIONS: Strawberry, Blueberry, Vanilla, Chocolate, Banana")
for i in range(icing_colors):

if (answer == icing_flavors):


  
''' icing.color(icing_colors)
  icing.fillcolor()
draw_icing()'''

answer = trtl.textinput("We do not have that in supply. Please choose another.","OPTIONS: Strawberry, Blueberry, Vanilla, Chocolate, Banana")


# Keep the window open
wn.mainloop()