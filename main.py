import cv2 as cv
import numpy as np
import ProcessImage as func

img = cv.imread("goku.jpg")

print("""
1.  Check if the image is grayscale
2.  Show pixel value
3.  Modify pixel value
4.  Set the image dimension
5.  Set the image total pixel count
6.  Show image data type""")

num = int(input("select: "))

if num == 1:
    imageLen = len(img.shape)
    func.processClass.checkGrayscale(imageLen)
    cv.imshow("test", img)
    cv.waitKey(0)

elif num == 2:
    func.processClass.ShowPixelValue(img)

elif num == 3:
    func.processClass.ModifyPixelValue(img)

elif num == 4:
    func.processClass.Dimension(img)

elif num == 5:
    func.processClass.PixelCount(img)

elif num == 6:
    func.processClass.ImgDataType(img)