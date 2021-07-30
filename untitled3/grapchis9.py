import turtle as tu

my_turtle = tu.Turtle()  # create a turtle
my_turtle.screen.bgcolor('red')  # Set turtle screen color
my_turtle.left(90)  # turn turtle left by 90
my_turtle.speed(20)  # set speed of turtle
my_turtle.color('green')  # set turtle color
my_turtle.pensize(5)  # set turtle pensize i.e thickness of lines
my_turtle.screen.title("My Fractal Tree")  # set turtle title


# recursive function
def draw_fractal(blen):
    if (blen < 10):  # set limit to fractal because it repeats itself infinetly
        return
    else:
        my_turtle.forward(blen)
        my_turtle.left(30)
        draw_fractal(3 * blen / 4)
        my_turtle.right(60)
        draw_fractal(3 * blen / 4)
        my_turtle.left(30)
        my_turtle.backward(blen)


draw_fractal(80)  # call the function
my_turtle = tu.done()
