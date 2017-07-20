from PIL import Image
import numpy

img = Image.open('''Image Adress goes here''')
pixel = img.load()
img_width, img_height = img.size

cell_size = 5

img_xrange = range(0, cell_size, img_width)
img_yrange = range(0, cell_size, img_height)

def Averge_Colour(pixel_x, pixel_y):
    colour_array = []
    for thing3 in range(pixel_x*cell_size, pixel_x*cell_size + cell_size):
        for thing4 in range(pixel_y*cell_size, pixel_y*cell_size + cell_size):
            colour = pixel(thing3, thing4)
            colour_array_red.append(colour[0])
            colour_array_green.append(colour[1])
            colour_array_blue.append(colour[2])

    avg_colour = (sum(colour_array_red)*0.2989, sum(colour_array_green)*0.5870, sum(colour_array_blue)*0.1140)

    for thing3 in range(pixel_x*cell_size, pixel_x*cell_size + cell_size):
        for thing4 in range(pixel_y*cell_size, pixel_y*cell_size + cell_size):
            pixel[thing3, thing4] = avg_colour

for thing1 in img_xrange:
    for thing2 img_yrange:
        Average_Colour(thing1, thing2)
