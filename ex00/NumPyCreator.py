import numpy as np
import numpy.random

# Numpy course https://www.youtube.com/watch?v=NzDQTrqsxas


class NumPyCreator:

    def from_list(self, lst):
        return (np.array(lst))

    def from_tuple(self, tpl):
        return (np.array(tpl))

    def from_iterable(self, itr):
        return (np.array(itr))

    def from_shape(self, shape, *value):
        if len(value) == 0:
            return np.zeros(shape)
        return np.full(shape, value)

    def random(self, shape):
        return np.random.random(shape)

    def identity(self, n):
        return np.eye(n)
