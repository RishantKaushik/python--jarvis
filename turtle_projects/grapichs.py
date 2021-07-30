import turtle
a= turtle.Turtle()
a.getscreen().bgcolor("black")


a.penup()
a.goto(-200,100)
a.pendown()
a.color("yellow")
a.speed(1000)
def star(turtle,size):
     if size<=10:
         return

     else:
         turtle.begin_fill()
         for i in range(5):
             turtle.forward(size)
             star(turtle,size/3)
             turtle.left(216)
             turtle.end_fill()
star(a,360)
turtle.delay(60)

turtle.pensize(2)
turtle.speed(15)
turtle.bgcolor("black")


for i in range(10):
    for colours in ["yellow","blue","white","green","red","pink"]:
        turtle.color(colours)
        turtle.circle(200)
        turtle.left(10)
turtle.hideturtle()
turtle.done()