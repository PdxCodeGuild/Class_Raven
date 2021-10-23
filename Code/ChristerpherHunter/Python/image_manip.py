"""
Christerpher Hunter
Lab 16: Image Manipulation
Let's convert an image into greyscale using the Pillow library,
which is a fork of PIL 'python image library'.
Version 2:
Use the colorsys library to increase the saturation,
decrease the brightness, and rotate the hue.
Colorsys represents colors as floats in the range 0.0 - 1.0,
whereas pillow uses ints in the range 0 - 255.
You'll have to convert between these two representations.
Version 3:
Pillow can also be used to draw, the code below demonstrates
some functions that Pillow provides. Use these functions to
draw a stick figure. You can find more documentation here.
"""

from PIL.Image import open
from PIL.ImageEnhance import Contrast


with open("lenna.png") as img:
    width, height = img.size
    pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]

        # your code here

        pixels[i, j] = (r, g, b)


img = Contrast(img)
img.enhance(1.0).show("0% more contrast")
print(img.format, img.size, img.mode)
