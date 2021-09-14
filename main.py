'''

author : Soroush Jaberi

Extract color and create artwork by your program.
We can use any photo to extract color.

'''

import colorgram

rgb_colors = []
colors = colorgram.extract('painting.jpg', 50)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)


print(rgb_colors)


color_list = [(172, 45, 69), (49, 47, 133), (34, 104, 160), (10, 8, 8), (225, 40, 54), (231, 220, 71), (205, 151, 93),
              (23, 138, 88), (50, 29, 34), (143, 74, 58), (113, 182, 213), (144, 32, 72), (222, 76, 46), (15, 165, 209),
              (240, 228, 8), (24, 19, 52), (17, 39, 29), (202, 135, 147), (35, 166, 126), (127, 188, 163), (25, 92, 63),
              (126, 151, 69), (235, 166, 181), (157, 209, 178), (233, 171, 165), (115, 115, 158), (181, 182, 217),
              (104, 46, 44), (148, 208, 222), (8, 85, 110), (63, 70, 50), (243, 13, 24)]

import turtle as t
import random

t.colormode(255)
painter = t.Turtle()
painter.speed("fastest")
painter.penup()
painter.goto(-350.00, -310.00)
painter.pendown()
painter.color(random.choice(color_list))


def draw_circle():
    for _ in range(10):
        painter.color(random.choice(color_list))
        painter.begin_fill()
        painter.circle(20)
        painter.end_fill()
        painter.penup()
        painter.forward(50)
        painter.pendown()


x = -350
y = -310
for _ in range(10):
    draw_circle()
    y += 50
    painter.penup()
    painter.goto(x, y)
    painter.pendown()

painter.hideturtle()

screen = t.Screen()
screen.exitonclick()

