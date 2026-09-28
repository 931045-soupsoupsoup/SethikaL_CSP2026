# 1.1.9 python file
import turtle

# Set up screen
wn = turtle.Screen()
wn.bgcolor("burlywood3")

# Create custom turtle and register it
custom_polygon = ((0, -6), (6, -5), (8, -4), (9, 0), (0, 10), (-9, 0), (-8, -4), (-6, -5), (0, -6))
wn.register_shape("cream", custom_polygon)

# Create custom turtle and apply the shape
whip_cream = turtle.Turtle()
whip_cream.shape("cream")

'''whip_cream.color("antiquewhite3")
whip_cream.fillcolor("antiquewhite1")''' # just incase :p

# Renaming turtle variables
strawberry_top = turtle.Turtle()
strawberry_top.shape("triangle")
blueberry_top = turtle.Turtle()
blueberry_top.shape("circle")
chocolate_top = turtle.Turtle()
chocolate_top.shape("square")

# Topping shapes and corrosponding colors
topping_shapes = ["triangle", "circle", "whip_cream", "square", "circle"]
topping_color =["indianred1", "royalblue", "antiquewhite1", "saddlebrown", "gold1"]


# Keep the window open
wn.mainloop()