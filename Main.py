from PIL import Image
import os

file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Image')
img = Image.open(os.path.join(file_path, 'tester1.jpg')).convert('L')
pixel = img.load()

(img_width, img_height) = img.size

if img_width > 700 or img_height > 700:
    print('This image is too large, for your own good it will not be converted')
    quit()

img_xrange = range(0, img_width,  1)
img_yrange = range(0, img_height - 1, 2)

The_Matrix = [[0 for i in img_xrange] for j in img_yrange]

def Average_Colour(pixel_x, pixel_y):
    ''' Takes the average grayscale value between two vertical pixels '''
    pixel_1 = pixel[pixel_x, pixel_y]
    pixel_2 = pixel[pixel_x, pixel_y +1]
    avg_colour = (pixel_1 + pixel_2)/2
    return(avg_colour)

# Converts Grayscale to Ascii
def Ascii(The_Matrix, img_xrange, img_yrange):
    ''' Converts a Matrix of grayscale values into a Matrix of Ascii characters, standerdizing the colour range in the process '''
    lowest  = max(max(The_Matrix))
    highest = min(min(The_Matrix))
    difference = lowest - highest

    for i in img_xrange:
        for j in img_yrange:
            if The_Matrix[int(j/2)][i] <= 1*difference/11:
                The_Matrix[int(j/2)][i] = ord('@')
            elif The_Matrix[int(j/2)][i] <= 2*difference/11:
                The_Matrix[int(j/2)][i] = ord('%')
            elif The_Matrix[int(j/2)][i] <= 3*difference/11:
                The_Matrix[int(j/2)][i] = ord('#')
            elif The_Matrix[int(j/2)][i] <= 4*difference/11:
                The_Matrix[int(j/2)][i] = ord('+')
            elif The_Matrix[int(j/2)][i] <= 5*difference/11:
                The_Matrix[int(j/2)][i] = ord('=')
            elif The_Matrix[int(j/2)][i] <= 6*difference/11:
                The_Matrix[int(j/2)][i] = ord('~')
            elif The_Matrix[int(j/2)][i] <= 7*difference/11:
                The_Matrix[int(j/2)][i] = ord(':')
            elif The_Matrix[int(j/2)][i] <= 8*difference/11:
                The_Matrix[int(j/2)][i] = ord('-')
            elif The_Matrix[int(j/2)][i] <= 9*difference/11:
                The_Matrix[int(j/2)][i] = ord(',')
            elif The_Matrix[int(j/2)][i] <= 10*difference/11:
                The_Matrix[int(j/2)][i] = ord('.')
            else:
                The_Matrix[int(j/2)][i] = ord(' ')
    return The_Matrix

def print_ascii_image(matrix):
    """Takes a 2D matrix of ASCII values as input and prints out an image of ASCII characters based on matrix values."""
    for row in matrix:
        for i in range(len(row)):
            if (i != len(row)-1):
                print(chr(row[i]), end='')
            else:
                print(chr(row[i]))

#The Loops
for i in img_xrange:
    for j in img_yrange:
        The_Matrix[int(j/2)][i] = Average_Colour(i, j)

The_Matrix = Ascii(The_Matrix, img_xrange, img_yrange)
print_ascii_image(The_Matrix)
