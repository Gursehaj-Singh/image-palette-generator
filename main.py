from colorthief import ColorThief
import matplotlib.pyplot as plt

ct = ColorThief('forest.jpg')

# dominant color
dominant_color = ct.get_color(quality=1)
plt.imshow([[dominant_color]])
plt.show()

# color palette
palette = ct.get_palette(color_count=4)
plt.imshow([[palette[i] for i in range(4)]])
plt.show()

# print palette
for color in palette:
    print(f"RGB: {color}  |  HEX: #{color[0]:02x}{color[1]:02x}{color[2]:02x}")
