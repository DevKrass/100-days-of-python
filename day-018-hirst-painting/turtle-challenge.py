import random
import turtle as t

timmy = t.Turtle()
t.colormode(255)


timmy.shape("classic")
timmy.width(1)
timmy.speed(0)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r, g, b)


def draw_shapes(n_shapes):
    n_sides = 3
    angle = 360 / n_sides
    for _ in range(n_shapes):
        for _ in range(n_sides):
            timmy.forward(100)
            timmy.right(angle)
        timmy.color(random.choice(random_color()))
        n_sides += 1


def random_walk(n_steps):
    angles = [0, 90, 180, 270]
    for _ in range(n_steps):
        timmy.forward(20)
        timmy.color(random_color())
        timmy.right(random.choice(angles))


def draw_spirograph(gap):
    for _ in range(int(360 / gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + gap)


draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()
