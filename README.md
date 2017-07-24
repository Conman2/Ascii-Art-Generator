# How to use:

This programm relays on the use of the Pillow libary (also known as PIL) as it uses it to acess the data of the photos. If you have not already done so you must install this libary in order for the code to work. This can be done via pip such as:
                                   
                                                pip install Pillow 

To operate simply place the image you wish to convert into the folder labeled "Image". After you have done this adjust the os file path on in the code to match the name of the image you placed in the "Image" folder. After this you'll need to run the code and export the result as a .txt document such as:

                                    python Main.py\location\here > example.txt 
                                  
# Recommendations:

We recommend that the files you convert be in the format of either .jpg or .png as these are post supported by the Pillow libary, but other photo formats are also supported. These can be found <a href="http://pillow.readthedocs.io/en/3.4.x/handbook/image-file-formats.html">Here</a>:

This Software converts an image into a text file of ascii art. Currently it does a 1:2 conversion between pixels and ascii characters so it is recommened not to use this on images much larger than ~500x500 pixels as it becomes unpractical to view such a large text file even on the smallest font settings. 

We have have had the best results veiwing the resultant text file in notepad and setting the font size to either with a font size of 4 or 5 depending on the size of the orignal image. Note we recommend that when veiwing not to use font 1 or 3 as this distorts the aspect ratio of the image, and also be aware that font 2 some of the symbols become to small to render. 

One thing to be aware is that there is only a limited palette of ascii symbols used so in areas of similar colours there may not be any noteable detail. We found the best result (for faces) arer with a black background and good lighting on the face. I hope you enjoy making some wicked looking ascii art!


# Example:

![Christopher Hitchens](http://i.imgur.com/quOV5al.png)

*Christopher Hitchens. Available in the repository as example.txt* 
