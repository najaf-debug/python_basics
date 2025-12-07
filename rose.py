import turtle

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
drawer = turtle.Turtle()
drawer.speed(0)
drawer.color("red")

# Draw rose curves
drawer.begin_fill()
drawer.fillcolor("red")

for i in range(150):
    drawer.circle(190 - i, 90)
    drawer.left(90)
    drawer.circle(190 - i, 90)
    drawer.left(18)

drawer.end_fill()

# Write name
drawer.up()
drawer.setposition(0, -250)
drawer.color("white")
drawer.write("For Pakeeza Ali ❤️", align="center", font=("Verdana", 20, "bold"))
drawer.hideturtle()

turtle.done()