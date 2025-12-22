"""
Part 1
Requirements:
- Using Colorgram Python package - which extracts colors from imges.
- Select a Damien Hirst painting to recreate
"""

"""
Commenting out as the color extract needs to happen only once
# TODO - Extract the color informaiton from the downloaded "spot_painting.jgp" image, and save it as tuples
import colorgram

extract_colors = colorgram.extract("spot_painting.jpg", 30)
colors = []
------------------------------------------------------------------
This will not work with Turtle, as it contains r=246 in the tuple
for i in extract_colors:
    colors.append(i.rgb)
Rather use the blow
------------------------------------------------------------------
for i in extract_colors:
    r = i.rgb.r
    g = i.rgb.g
    b = i.rgb.b
    new_color = (r,g,b)
    colors.append(new_color)

print(colors)
"""
color_list=[(132, 164, 202), (225, 150, 101), (30, 43, 64), (201, 135, 147), (163, 59, 49), (236, 212, 87), (43, 101, 147), (136, 182, 161), (150, 63, 72), (51, 41, 45), (160, 32, 29), (172, 28, 32), (60, 115, 99), (59, 48, 45), (231, 162, 167), (216, 82, 72), (236, 167, 157), (36, 61, 55), (14, 96, 71), (33, 60, 107), (171, 188, 220), (197, 96, 105), (105, 126, 159), (18, 83, 105), (174, 200, 188), (34, 150, 209)]

"""
Part 2
- Create a 10 by 10 img
- The dots' size should be 20
- The gap between the dots should be 50
"""

import turtle as t
from random import choice

# Initilizing Turtle, its postion and heading
painting = t.Turtle()
t.colormode(255)
painting.teleport(-250,-250,fill_gap=False)
painting.setheading(0)

# Draw dots
for _ in range(10):
    for _ in range(10):
        painting.dot(20, choice(color_list))
        position = painting.pos()
        painting.teleport(position[0] + 50,position[1])

    painting.teleport(-250,position[1] + 50)


screen = t.Screen()
screen.exitonclick()