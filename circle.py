import turtle
turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(0)
color = ["red","yellow","orange","green","blue", "white"]
for i in range(6):
    for colors in color:
        turtle.color(colors)
        turtle.circle(100)
        turtle.left(10)
turtle.hideturtle()
turtle.done()



