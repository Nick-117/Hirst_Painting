import turtle
import random
from turtle import Turtle, Screen
t = Turtle()
t.hideturtle()
t.speed("fastest")
color_list = [(199, 175, 117), (124, 36, 24), (168, 106, 57), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203)]
turtle.colormode(255)

draw = True
counter = 0
t.penup()
t.setheading(270)
t.forward(170)
t.setheading(0)
t.left(180)
t.forward(170)
t.right(180)
while draw:

    def art_painting():
        for dot in range(10):
            t.penup()
            t.dot(20, random.choice(color_list))
            t.forward(50)
        t.left(90)
        t.forward(50)
        t.left(90)
        for space in range(10):
            t.forward(50)
        t.right(180)
    counter += 1
    if counter == 10:
        draw = False
    art_painting()




screen = Screen()
screen.exitonclick()




# Angela's random walk code below

# import turtle as turtle_module
# import random
#
# turtle_module.colormode(255)
# tim = turtle_module.Turtle()
# tim.speed("fastest")
# tim.penup()
# tim.hideturtle()
# color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
# tim.setheading(225)
# tim.forward(300)
# tim.setheading(0)
# number_of_dots = 100
#
# for dot_count in range(1, number_of_dots + 1):
#     tim.dot(20, random.choice(color_list))
#     tim.forward(50)
#
#     if dot_count % 10 == 0:
#         tim.setheading(90)
#         tim.forward(50)
#         tim.setheading(180)
#         tim.forward(500)
#         tim.setheading(0)









screen = turtle_module.Screen()
screen.exitonclick()