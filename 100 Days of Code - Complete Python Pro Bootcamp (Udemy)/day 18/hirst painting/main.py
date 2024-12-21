import turtle as t
import random

#import colorgram

# colors_from_image = colorgram.extract('image.jpg', 40)
# colors = []
#
# for image_color in colors_from_image:
#     r = image_color.rgb.r
#     g = image_color.rgb.g
#     b = image_color.rgb.b
#     new_color = (r, g, b)
#     colors.append(new_color)
#
# print(colors)
# print(len(colors))

colors = [(244, 235, 48), (196, 12, 35), (218, 160, 70), (43, 80, 177), (237, 40, 140), (38, 215, 76), (237, 228, 5),
          (31, 40, 154), (206, 72, 22), (21, 149, 23), (201, 34, 98), (70, 11, 27), (182, 16, 11), (213, 164, 10),
          (218, 140, 195), (56, 15, 10), (17, 20, 48), (13, 95, 62), (79, 210, 159), (73, 73, 221), (83, 191, 220),
          (237, 158, 216), (94, 232, 200), (217, 82, 51), (5, 230, 239), (14, 64, 44), (174, 176, 234), (122, 226, 233),
          (236, 173, 161), (4, 246, 230), (31, 48, 236), (252, 6, 66), (14, 84, 105), (9, 242, 246)]

# Todo: print 10x10 grid of spots. spot width 20, spaced 50 paces apart. random color.

tim = t.Turtle()
tim.hideturtle()
t.colormode(255)
tim.speed("fastest")

tim.penup()
tim.goto(-325, -325)

for _ in range (10):
    for _ in range (10):
        tim.color(random.choice(colors))
        tim.forward(50)
        tim.dot(20)
    tim.left(90)
    tim.forward(50)
    print(tim.pos())
    tim.left(90)
    tim.forward(500)
    tim.left(180)






















screen = t.Screen()
screen.exitonclick()

