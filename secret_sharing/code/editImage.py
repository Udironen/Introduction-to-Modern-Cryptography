from PIL import Image   #PIL/PILLOW is Python's Image Library
                        # you need to insall it
from matrix import *

############################################################################
###    Converting "real" formats (.jpg/.bmp etc.) <--> .bitmap
###    .bitmap format will represent grayscale images readable
###    by Matrix class using the load method
###
###    REQUIRES INSTALLING THE PACKAGE PILLOW
###
############################################################################


def image2bitmap(path):
    ''' Given a string 'path' of image file in "real" format (.jpg/.bmp etc.)
        creates a new file in format .bitmap under the same directory
        which can then be loaded into class Matrix using Matrix.load() ''' 
    image = Image.open(path)
    image = image.convert("1")          # converts to 8 bit grayscale image
    im = image.load()                   # stores image in an array
    w,h = image.size                    # image dimensions

    new_file_name = (path.split(".")[-2]).split("/")[-1] + ".bitmap"
    new_file = open(new_file_name, 'w')

    print(h,w, file=new_file)
    for i in range(h):
        for j in range(w):
            print(int(im[j,i]), end=" ", file = new_file)
        print("", file=new_file)#newline

    new_file.close()


def bitmap2image(path):
    ''' Given a string path of image file in .bitmap format
        creates a .bmp file under the same directory '''
    mat = Matrix.load(path)
    n,m = mat.dim()
    image = Image.new('L', (m,n))
    im = image.load()
    for i in range(n):
       for j in range(m):
           im[j,i] = mat[i,j]
    image.save((path.split(".")[-2]).split("/")[-1]  + ".bmp")


#USAGE
#image2bitmap("./my_image.jpg")
#should work for other formats besides jpg as well
#Then you can use:
#mat = Matrix.load("./my_image.bitmap")
