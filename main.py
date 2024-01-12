import colorgram

list_of_colors = []
colors = colorgram.extract('image.jpg', 5)

for item in colors:
    color = item
    rgb = color.rgb
    red = rgb[0]
    green = rgb[1]
    blue = rgb[2]
    color_as_tuple = (red, green, blue)
    list_of_colors.append(color_as_tuple)
print(list_of_colors)



