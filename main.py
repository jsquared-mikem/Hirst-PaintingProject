# import colorgram
import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)

# list_of_colors = []
# colors = colorgram.extract('image.jpg', 88)
#
# for item in colors:
#     color = item
#     rgb = color.rgb
#     red = rgb[0]
#     green = rgb[1]
#     blue = rgb[2]
#     color_as_tuple = (red, green, blue)
#     list_of_colors.append(color_as_tuple)
# print(list_of_colors)

list_of_colors = [(252, 250, 247), (253, 247, 249), (237, 251, 245), (249, 228, 17), (213, 13, 9), (198, 12, 35),
                  (231, 228, 5), (197, 69, 20), (33, 90, 188), (43, 212, 71), (234, 148, 40), (33, 30, 152),
                  (16, 22, 55), (66, 9, 49), (240, 245, 251), (244, 39, 149), (65, 202, 229), (14, 205, 222),
                  (63, 21, 10), (224, 19, 111), (229, 165, 8), (15, 154, 22), (245, 58, 16), (98, 75, 9), (248, 11, 9),
                  (222, 140, 203), (68, 240, 161), (10, 97, 62), (5, 38, 33), (68, 219, 155), (238, 157, 212),
                  (86, 77, 208), (86, 225, 235), (250, 8, 14), (242, 166, 157), (177, 180, 224), (36, 243, 159),
                  (6, 81, 115), (11, 55, 248)]

timmy = Turtle()
timmy.hideturtle()


def starting():
    timmy.hideturtle()
    timmy.penup()
    timmy.back(250)
    timmy.showturtle()


def row_of_10():
    for _ in range(10):
        timmy.dot(20, random.choice(list_of_colors))
        timmy.penup()
        timmy.forward(50)
        timmy.pendown()


def next_row():
    timmy.hideturtle()
    timmy.penup()
    timmy.setheading(90)
    timmy.forward(50)
    timmy.setheading(0)
    timmy.back(500)
    timmy.showturtle()
    timmy.pendown()


starting()
def painting(height):
    for _ in range(height):
        row_of_10()
        next_row()
        row_of_10()

screen = Screen()
screen.exitonclick()
