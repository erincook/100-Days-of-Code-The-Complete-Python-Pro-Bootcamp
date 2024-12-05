from turtle import Turtle, Screen, colormode

import random

tim = Turtle()
tim.shape("turtle")
colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_tuple = (r, g, b)
    return random_tuple

# colors = ["brown", "SeaGreen1", "DeepPink1", "chartreuse2", "coral2", "DarkGoldenrod1",
#           "cyan3", "maroon3", "purple", "PaleVioletRed"]

# for side_number in range(3, 11):
#     ext_angle = 360 / side_number
#     tim.color(random.choice(colors))
#     for _ in range (side_number):
#         tim.forward(100)
#         tim.right(ext_angle)
## think more modularly!!

# Todo: randomwalk
# Todo: 1) move a set distance in random direction (multiples of 90, including 0)
# Todo: 2) make the pen line thicker
# Todo: 3) change color every step of the set distance.
# Todo: 4) get the cursor to move faster.

# tim.pensize(10)
tim.speed("fastest")


# def random_walk(step_num):
#     angles = [0, 90, 180, 270]
#     for _ in range(step_num+1):
#         tim.color(random_color())
#         turn = random.choice(angles)
#         tim.right(turn)
#         tim.forward(20)
#
#
# random_walk(100)
# # could have used "tim.setheading()" instead of "turn"

for _ in range(72):
    tim.color(random_color())
    tim.circle(100)
    tim.setheading(tim.heading() + 5)













screen = Screen()
screen.exitonclick()
