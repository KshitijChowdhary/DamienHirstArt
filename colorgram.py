import colorgram

colours = colorgram.extract('image.jpg',35)
colours_rgb = []

for color in colours:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b

    new_color = (r, g, b)

    colours_rgb.append(new_color)