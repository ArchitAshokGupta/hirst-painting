# import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()

color_list = [(239, 230, 212), (225, 159, 67), (244, 232, 239), (234, 238, 245), (236, 245, 239), (61, 121, 170),
              (50, 96, 57), (238, 203, 71), (182, 64, 49), (179, 173, 36), (221, 172, 198), (182, 51, 56),
              (211, 87, 57), (46, 46, 95), (209, 163, 187), (133, 160, 186), (38, 39, 80), (37, 84, 45), (244, 199, 4),
              (149, 169, 152), (76, 130, 186), (195, 75, 82), (227, 175, 165), (31, 65, 39), (180, 188, 211),
              (111, 139, 113), (181, 198, 185), (75, 142, 172), (139, 38, 52), (175, 198, 204)]

tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
num_of_dots = 100

for dot_count in range(1, num_of_dots+1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()
