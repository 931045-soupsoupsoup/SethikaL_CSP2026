import turtle as trtl

# Set up screen
wn = trtl.Screen()
wn.tracer(0)
wn.bgcolor("burlywood3")

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

# update screen
wn.update()
wn.tracer(1)

# Cake platter
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

# Keep the window open
wn.mainloop()