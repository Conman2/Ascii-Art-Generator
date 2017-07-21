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

The_Matrix = numpy.zeros((len(img_xrange), len(img_yrange)))

#Getting the Average RGB Values for each Section
def Average_Colour(pixel_x, pixel_y):
    colour_array_red = []
    colour_array_green = []
    colour_array_blue = []

    for ii in range(pixel_x*cell_size, pixel_x*cell_size + cell_size):
        for jj in range(pixel_y*cell_size, pixel_y*cell_size + cell_size):
            colour = pixel[ii, jj]
            colour_array_red.append(colour[0])
            colour_array_green.append(colour[1])
            colour_array_blue.append(colour[2])

    avg_colour = (int((sum(colour_array_red)/len(colour_array_red))*0.299) + int((sum(colour_array_green)/len(colour_array_green))*0.587) + int((sum(colour_array_blue)/len(colour_array_blue))*0.114))

    return avg_colour

#Turns the Grayscale into only five tones
def Reducing_Pallet(gray_scale):
    #Note Grayscale is a range from 0 to 255 (5 colour Pallet)
     counter = 0
     while True:
         if gray_scale < counter:
             gray_scale = counter - 50
             return gray_scale

         counter += 50

#Converts Grayscale to Ascii
def Ascii(The_Matrix, img_xrange, img_yrange):
    for ii in img_xrange:
        for jj in img_yrange:
            if The_Matrix[ii][jj] == 0:
                The_Matrix[ii][jj] = '#'
            elif The_Matrix[ii][jj] == 50:
                The_Matrix[ii][jj] = '+'
            elif The_Matrix[ii][jj] == 100:
                The_Matrix[ii][jj] = '*'
            elif The_Matrix[ii][jj] == 150:
                The_Matrix[ii][jj] = ','
            elif The_Matrix[ii][jj] == 200:
                The_Matrix[ii][jj] = '.'
            elif The_Matrix[ii][jj] == 250:
                The_Matrix[ii][jj] = ' '

    return The_Matrix

#The Loops
for ii in img_xrange:
    for jj in img_yrange:
        The_Matrix[ii][jj] = Average_Colour(ii, jj)
        The_Matrix[ii][jj] = Reducing_Pallet(The_Matrix[ii][jj])

The_Matrix = Ascii(The_Matrix, img_xrange, img_yrange)

print(The_Matrix)
#img.save(os.path.join(file_path, 'tester_update.png'))
