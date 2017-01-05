import turtle


def draw_square(brad):
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)


def draw_circle():
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)


def draw_triangle():
    andrew = turtle.Turtle()
    andrew.shape("square")
    andrew.color("green")

    andrew.right(180)
    andrew.forward(100)
    andrew.right(-120)
    andrew.forward(100)
    andrew.right(-120)
    andrew.forward(100)
    andrew.right(-120)


def draw():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)
    for i in range(1, 37):
        draw_square(brad)
        brad.right(10)

    draw_circle()
    draw_triangle()

    window.exitonclick()


draw()
