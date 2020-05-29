import numpy as np
from ImageProcessor import ImageProcessor


class ScrapBooker():

    def crop(self, array, dimensions, position=(0, 0)):
        if array.shape[0] - position[0] < dimensions[0] or\
                array.shape[1] - position[1] < dimensions[1]:
            print("ERROR\nGiven dimensions greater than array's\nCan't crop")
            return array
        return array[position[0]:position[0]+dimensions[0],
                     position[1]:position[1]+dimensions[1]]

    def thin(self, array, n, axis):
        """deletes every n-th pixel row along the specified axis \
(0 vertical, 1 horizontal)"""
        if axis == 0:
            return array[: array.shape[0] - n, :]
        else:
            return array[:, : array.shape[1] - n]

    def juxtapose(self, array, n, axis):
        """juxtaposes n copies of the image along \
the specified axis (0 vertical, 1 horizontal)."""
        newArray = array
        for i in range(n):
            newArray = np.concatenate((newArray, array), axis)
        return newArray

    def mosaic(self, array, dimensions):
        """makes a grid with multiple copies of the array. \
The dimensions argument specifies the dimensions \
(meaning the height and width) of the grid (e.g. 2x3)"""
        newArr = self.juxtapose(array, dimensions[0], 0)
        newArr = self.juxtapose(newArr, dimensions[1], 1)
        return newArr


scrap = ScrapBooker()
opener = ImageProcessor()
arr = opener.load("./tete.png")
arrcrop = scrap.crop(arr, (300, 700), (200, 100))
print("showing cropped array")
opener.display(arrcrop)
print("showing thin'ed array")
aThin = scrap.thin(arr, 500, 0)
opener.display(aThin)
print("showing juxtaposed arrays")
aJuxt = scrap.juxtapose(arr, 3, 0)
opener.display(aJuxt)
print("showing mosaic'ed arrays B)")
aMos = scrap.mosaic(arrcrop, (6, 6))
opener.display(aMos)
