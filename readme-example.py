from bpgfx import Canvas, Rectangle
from math import sin, radians

# Create a 80 x 60 canvas of virtual dot-pixels.
#
# Virtual dot-pixels are mapped onto a grid of braille characters when the
# canvas is rendered via its __str__ method.
canvas = Canvas(80, 60)

# Draw a rectangle around the border of the canvas.
# The Rectangle class implements the "drawable" interface with the method:
#
#   def draw(self, canvas: Canvas) -> None:
#       ...
#
# Library-defined drawable classes include Point, Line, Rectangle, and Sprite.
rectangle = Rectangle(0, 0, canvas.width, canvas.height)
canvas.draw(rectangle)

# Draw a pretty sine wave across the canvas.
for x in range(canvas.width):
    # The canvas' set method will set a virtual dot-pixel to raised or not
    # raised (on or off).
    #
    # canvas.set(x, y, True)   # raised
    # canvas.set(x, y, False)  # not raised
    # canvas.set(x, y)         # default = raised
    canvas.set(x, canvas.height // 2 - int(sin(radians(x * 4)) * 15))

# Write the rendered contents of the canvas to the terminal.
print(canvas, end="")
