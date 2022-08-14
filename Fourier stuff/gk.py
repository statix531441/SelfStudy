import numpy as np
import math


def Gkernel(shape, sig):
    shape = np.array(shape)

    kernel = np.zeros(shape)

    for col in range(len(kernel)):
        for row in range(len(kernel[0])):
            r = np.array([col,row])
            u = (shape-1)/2
            kernel[col][row] = math.exp(-np.dot((r-u)/sig,(r-u)/sig)/2)/(sig*math.sqrt(2*math.pi))

    return kernel


