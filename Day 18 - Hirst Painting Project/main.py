# Used the below code to create our color_list by extracting colors from an image
#
#
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract("image.jpg", 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)


import turtle as t
import random

t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(230, 221, 208), (218, 159, 85), (41, 109, 148), (120, 163, 190), (149, 64, 87), (202, 135, 157), (211, 228, 218), (33, 130, 95), (179, 159, 36), (123, 179, 152), (160, 80, 53), (211, 88, 62), (196, 86, 112), (231, 209, 218), (206, 222, 230), (229, 199, 115), (58, 165, 134), (140, 33, 42), (9, 103, 79), (49, 158, 181), (233, 163, 180), (117, 115, 161), (33, 62, 110), (124, 38, 35), (235, 172, 158), (157, 210, 197), (32, 57, 79), (71, 41, 37), (25, 65, 54), (72, 37, 47)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
num_of_dots = 100

for dot_count in range(1, num_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()