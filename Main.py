from PIL import Image
import numpy
import os

file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Image')

img = Image.open(os.path.join(file_path, 'tester.jpg'))
pixel = img.load()
img_width, img_height = img.size

cell_size = 1

img_xrange = range(0, img_width, cell_size)
img_yrange = range(0, img_height, cell_size)

The_Matrix = numpy.zeros((len(img_xrange), len(img_yrange), 3))

def Average_Colour(pixel_x, pixel_y):
    colour_array_red = []
    colour_array_green = []
    colour_array_blue = []

    #Getting the Average Values for each Section
    for thing3 in range(pixel_x*cell_size, pixel_x*cell_size + cell_size):
        for thing4 in range(pixel_y*cell_size, pixel_y*cell_size + cell_size):
            colour = pixel[thing3, thing4]
            colour_array_red.append(colour[0])
            colour_array_green.append(colour[1])
            colour_array_blue.append(colour[2])

    avg_colour = ([sum(colour_array_red)/len(colour_array_red), sum(colour_array_green)/len(colour_array_green), sum(colour_array_blue)/len(colour_array_blue)]*[0.299, 0.587, 0.114])

    print(avg_colour)

    #Updating the Colours
    for thing3 in range(pixel_x*cell_size, pixel_x*cell_size + cell_size):
        for thing4 in range(pixel_y*cell_size, pixel_y*cell_size + cell_size):
            pixel[thing3, thing4] = avg_colour

    return avg_colour[0], avg_colour[1], avg_colour[2]


for thing1 in img_xrange:
    for thing2 in img_yrange:
        The_Matrix[thing1][thing2][0], The_Matrix[thing1][thing2][1], The_Matrix[thing1][thing2][2] = Average_Colour(thing1, thing2)

img.save(os.path.join(file_path, 'tester_update.png'))


#Note there is an error when the Image Dimensions arent a multiple of cell size
