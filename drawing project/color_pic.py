import colorgram
from turtle import Turtle, Screen

rgb_colours = []
colors = colorgram.extract('img1.jpg', 100)
for col in colors:
    red = col.rgb.r
    blue = col.rgb.b
    green = col.rgb.g

    new_col = (red, blue, green)

    rgb_colours.append(new_col)
    print(len(rgb_colours))


