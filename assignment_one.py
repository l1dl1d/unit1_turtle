import turtle
def octagon():
    for x in range(8):
        turtle.forward(50)
        turtle.left(45)
turtle.color("blue")
turtle.begin_fill()
octagon()
turtle.end_fill()
turtle.penup()
turtle.goto(0,-200)
turtle.pendown()
turtle.color("red")
turtle.begin_fill()
octagon()
turtle.end_fill()
turtle.penup()
turtle.goto(200,-200)
turtle.pendown()
turtle.color("pink")
turtle.begin_fill()
octagon()
turtle.end_fill()
turtle.penup()
turtle.goto(200,0)
turtle.pendown()
turtle.color("purple")
turtle.begin_fill()
octagon()
turtle.end_fill()
turtle.exitonclick()
