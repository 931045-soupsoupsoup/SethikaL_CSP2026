import turtle as trtl

# Set up screen
wn = trtl.Screen()
wn.tracer(0)
wn.bgcolor("burlywood3")

# Turtles
# Create custom turtle and register it
custom_polygon = ((0, -6), (6, -5), (8, -4), (9, 0), (0, 10), (-9, 0), (-8, -4), (-6, -5), (0, -6))
wn.register_shape("cream", custom_polygon)

# Create whip cream as a custom turtle
icing = trtl.Turtle() # initial turtle to draw out cake before toppings
whip_cream = trtl.Turtle()
whip_cream.shape("cream")
whip_cream.color("antiquewhite3")
whip_cream.fillcolor("antiquewhite1")
whip_cream.hideturtle()

# *** Definitions ***
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

  icing.hideturtle()
  icing.penup()

def base_cake():
  icing.speed(5)

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


# draws icing + list
icing.speed(50)
icing_colors = ["lightpink", "lightskyblue", "mintcream", "chocolate4", "gold"]
icing_flavors = ["strawberry", "blueberry", "vanilla", "chocolate", "banana"]

# ask user what flavor
answer = trtl.textinput("What flavor would you like?","OPTIONS: Strawberry, Blueberry, Vanilla, Chocolate, Banana (we don't have anything else in supply... so if you ask for something else we wont put it.)")
for i in range(len(icing_colors)):
  if (answer == icing_flavors[i] and icing_colors[i]):
    icing.color(icing_colors[i])
    icing.fillcolor(icing_colors[i])
    draw_icing()

# draws toppings
# list of toppings
icing.speed(5)
topping_shapes = ["triangle", "circle", "cream", "square", "circle"]
topping_colors = ["indianred1", "royalblue", "antiquewhite1", "saddlebrown", "khaki"]
topping_name = ["strawberry", "blueberry", "cream", "chocolate", "banana"]

# ask user for toppings
# topping layer 1
icing.goto(-182, -205)
icing.shapesize(5)
icing.tilt(90) # keeps the turtle facing north the entire time

answer = trtl.textinput("Time for toppings!!!","OPTIONS: Strawberry, Blueberry, Cream, Chocolate, Banana (we don't have anything else in supply... so if you ask for something else we wont put it.)")
for i in range(len(topping_shapes)):
  if (answer == topping_name[i] and topping_shapes[i] and topping_colors[i]):
    for tops in range(8):
      icing.shape(topping_shapes[i])
      icing.color(topping_colors[i])
      icing.stamp()
      icing.forward(60)

# topping layer 2
icing.goto(-180, 80)
icing.shapesize(3)

answer = trtl.textinput("Why dont you pick another topping?","OPTIONS: Strawberry, Blueberry, Cream, Chocolate, Banana")
for i in range(len(topping_shapes)):
  if (answer == topping_name[i] and topping_shapes[i] and topping_colors[i]):
    for tops in range(8):
      icing.shape(topping_shapes[i])
      icing.color(topping_colors[i])
      icing.stamp()
      icing.forward(60)

# topping layer 3
icing.goto(-90, 130)
icing.shapesize(2)

answer = trtl.textinput("One more wouldn't hurt... right?","OPTIONS: Strawberry, Blueberry, Cream, Chocolate, Banana")
for i in range(len(topping_shapes)):
  if (answer == topping_name[i] and topping_shapes[i] and topping_colors[i]):
    for tops in range(5):
      icing.shape(topping_shapes[i])
      icing.color(topping_colors[i])
      icing.stamp()
      icing.forward(60)

# yay
answer = trtl.textinput("Congrats! You have made your cake!","Though uh.. um. it looks kinda ugly. sorry. Just replay the program at this point. or leave it for the next person to see.. yup.")

# Keep the window open
wn.mainloop()