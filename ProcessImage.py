import cv2 as cv
import numpy as np


class processClass():

    def CheckGrayscale(imageLen):
        if imageLen == 2:
            print("Image is grayscaled")
            exit(0)

    def ShowPixelValue(img):
        x = int(input("Value of x-axis: "))
        y = int(input("Value of y-axis: "))
        color = int(input("[0] - blue, [1] - green, [2] - red: "))
        print(img.item(x, y, color))

    def ModifyPixelValue(img):
        x = int(input("Value of x-axis: "))
        y = int(input("Value of y-axis: "))
        print(img[x, y])
        for i in range(0, 3, 1):
            color = int(input("[0] - blue, [1] - green, [2] - red: "))
            value = int(input("value: "))
            img.itemset((x, y, color), value)
        print(img[x, y])
        cv.imshow("test", img)
        cv.waitKey(0)

    def Dimension(img):
        x = 500
        y = 100
        print(img.shape)
        print(f"""
            Total image pixel in x-axis: {img.shape[0]}
            Total image pixel in y-axis: {img.shape[1]}
            compared value in x-axis: {x}
            compared value in y-axis: {y}
            """)
        if x <= img.shape[0] and y <= img.shape[1]:
            print("Value is on the boundaries")
        else:
            print("Value is out of the boundaries")

    def PixelCount(img):
        x = 100
        y = 100
        fixedValue = x * y
        totalNumberOfPixel = img.shape[0] * img.shape[1]

        print(f"""
           Total fixed variable: {fixedValue}
           Total image pixels: {totalNumberOfPixel}""")

        if fixedValue > totalNumberOfPixel:
            print("Higher")
        elif fixedValue < totalNumberOfPixel:
            print("Lower")
        else:
            print("Equal")

    def ImgDataType(img):
        print(img.dtype)