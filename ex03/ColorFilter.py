import numpy as np
from ImageProcessor import ImageProcessor


class ColorFilter():

    def invert(self, array):
        newArr = array - 0
        newArr[:, :, 0:3] = 1 - newArr[:, :, 0:3]
        return newArr

    def to_blue(self, array):
        newArr = np.zeros((array.shape))
        newArr[:, :, 2:4] = array[:, :, 2:4]
        return newArr

    def to_green(self, array):
        newArr = array * 1
        newArr[:, :, 0:1] = array[:, :, 0:1] * 0
        newArr[:, :, 2:3] = array[:, :, 2:3] * 0
        return newArr

    def to_red(self, array):
        newArr = array + 0
        Ab = self.to_blue(array)
        Ag = self.to_green(array)
        Ab[:, :, 3:4] = 0
        Ag[:, :, 3:4] = 0
        newArr = array - Ab - Ag
        return newArr

    def celluloid(self, array):
        color = np.linspace(0.0, 1.0, 5)
        newArray = array
        for i in range(3):
            for j in range(5):
                newArray[newArray[:, :, i] <= color[j], i] = color[j] * 100
            newArray[:, :, i] = newArray[:, :, i] / 100
        return newArray


colo = ColorFilter()
opener = ImageProcessor()
# arr = opener.load("./../ex02/tete.png")
arr = opener.load("./cc.png")
aInv = colo.invert(arr)
print("showing inverted array")
print(arr, aInv)
opener.display(aInv)
ablue = colo.to_blue(arr)
print("showing blue array")
print(arr, ablue)
opener.display(ablue)
agreen = colo.to_green(arr)
print("showing green array")
print(arr, agreen)
opener.display(agreen)
ared = colo.to_red(arr)
print("showing red array")
print(arr, ared)
opener.display(ared)
acel = colo.celluloid(arr)
print("showing celluloid array")
print(arr, acel)
opener.display(acel)
