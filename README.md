# Image to Ascii Art Converter

This Software converts an image into a text file of ascii art. Currently it does a 1:1 conversion between pixels and ascii characters so it is recommened not to use this on images larger than ~300x300 pixels as it becomes unpractical to view such a large text file. 

To operate simply place the image you wish to convert into the folder labeled "Image". After you have done this adjust the os file path on in the code to match the name of the image you placed in the "Image" folder. After this you'll need to run the code and export the result as a .txt document such as:

                                   python Main.py_location_here > text_files_name.txt 
                          
We have have had the best results veiwing the resultant text file in notepad and setting the font size to either with a font size of 2 or 4 depending on the size of the orignal image. One thing to be aware is that there is only a limited palette of ascii symbols used so in areas of similar colours there may not be any noteable detail. We found the best result (for faces) arer with a black background and good lighting on the face. I hope you enjoy making some wicked looking ascii art!
